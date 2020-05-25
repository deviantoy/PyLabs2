"""
Напишите скрипт для информационной системы библиотеки. База
данных библиотеки включает таблицы «Авторы» с полями «id»,
«имя», «страна», «годы жизни», и «Книги» с полями «id автора»,
«название», «количество страниц», «издательство», «год издания»).
Необходимо производить авторизацию пользователей, логины и
пароли которых хранятся в отдельной таблице. Пароли должны
храниться в зашифрованном виде (например, хэш SHA-1 или MD5).
В программе должны быть окна для отображения информации о
всех книгах и авторах, окно добавления книги/автора. Реализуйте
также возможность сохранения информации о выделенном авторе в
файле в формате json или XML (по выбору пользователя). При
добавлении нового автора в базу допускается не заполнять поля в
соответствующем окне, а распарсить файл, указанный
пользователем (файл необходимо заранее создать и заполнить
информацией вручную, в текстовом редакторе). Для преобразования
в формат XML и json напишите собственный код; парсинг можно
делать с помощью сторонних библиотек. Форматы файлов:
JSON:
{
 "name": "L.N.Tolstoi",
 "country": "Russia",
 "years": [1828, 1910]
}
XML:
<author>
 <name>L.N.Tolstoi</Name>
 <country>Russia</Country>
 <years born=”1828” died=”1910”/>
</author>
"""
import sqlite3
import hashlib
import sys
import wx
import threading

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from autorizationFormUI import *
from MainWindowUI import *
from ShowAuthorInfoFormUI import *
from ShowBookInfoFormUI import *
from AddAuthorFormUI import *
from AddBookFormUI import *

from FileManager import FileManager


class Autorization(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_autorization()
        self.ui.setupUi(self)

        self.login = ''
        self.password = ''

        self.ui.pushButton.clicked.connect(self.sing_in)

    def sing_in(self):
        try:
            self.login = self.ui.lineEdit.text()
            self.password = self.ui.lineEdit_2.text()
        except Exception as e:
            print('Error with getting data from textLines: ', e.args)
        db = None
        try:
            db = sqlite3.connect('Library.db')
        except Exception as e:
            print('Error with connecting to DB: ', e.args)
        try:
            with db:
                cursor = db.cursor()
                hash_log = hashlib.md5(self.login.encode()).hexdigest()
                hash_pass = hashlib.md5(self.password.encode()).hexdigest()
                try:
                    cursor.execute('SELECT * FROM Пользователи')
                except Exception as e:
                    print('Error with taking info about users: ', e.args)
                users = cursor.fetchall()
                for user in users:
                    log, passw = user
                    if hash_log == log and hash_pass == passw:
                        try:
                            self.show_form()
                        except Exception as e:
                            print('Error with Openning new Window: ', e.args)
                    else:
                        print('here')
        except Exception as e:
            print('Error with openning DB: ', e.args)

    @pyqtSlot()
    def show_form(self):
        self.mainW = MainTask()
        self.mainW.show()
        self.close()


class MainTask(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        # QtWidgets.QWidget.__init__(self, parent)
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.show_author_infoF = None
        self.show_book_infoF = None
        self.add_authorF = None
        self.add_bookF = None

        self.ui.add_author_button.clicked.connect(self.add_author)
        self.ui.add_book_button.clicked.connect(self.add_book)
        self.ui.search_author_button.clicked.connect(self.show_author_info)
        self.ui.search_book_button.clicked.connect(self.show_book_info)

    def show_author_info(self):
        try:
            author_id = self.ui.AuthorID_inp.text()
            db = sqlite3.connect('Library.db')
        except Exception as ex:
            print(ex.args)
        with db:
            cursor = db.cursor()
            request = u'SELECT * FROM Авторы WHERE id = ' + author_id
            try:
                cursor.execute(request)
            except Exception as e:
                print('Error with getting data from DB: ', e.args)
            try:
                found_authors = cursor.fetchall()
                if len(found_authors) == 0:
                    raise Exception('Автора с таким ID нет в базе данных')
                try:
                    author = found_authors[0]
                    self.show_author_info_form(author)
                except Exception as e:
                    print('error with openning next form: ', e.args)
            except Exception as e:
                print(e)

    @pyqtSlot()
    def show_author_info_form(self, dat):
        self.show_author_infoF = ShowAuthorInfoForm(data=dat)
        self.show_author_infoF.show()

    def show_book_info(self, dat):
        book_title = self.ui.BookName_inp.text()
        db = sqlite3.connect('Library.db')
        with db:
            cursor = db.cursor()
            request = request = u'SELECT * FROM Книги WHERE Название = "' + book_title + u'"'
            cursor.execute(request)
            try:
                found_books = cursor.fetchall()
                if len(found_books) == 0:
                    raise Exception('Книги с таким названием нет')
                book = found_books[0]
                self.show_book_info_form(book)
            except Exception as e:
                print(e)

    def show_book_info_form(self, dat):
        self.show_book_infoF = ShowBookInfoForm(data=dat)
        self.show_book_infoF.show()

    @pyqtSlot()
    def add_author(self):
        self.add_authorF = Add_author()
        self.add_authorF.show()

    @pyqtSlot()
    def add_book(self):
        self.add_bookF = Add_book()
        self.add_bookF.show()


class ShowAuthorInfoForm(QtWidgets.QMainWindow, Ui_Info_author):
    def __init__(self, data, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Info_author()
        self.ui.setupUi(self)

        self._info = data
        ID, name, country, years = data
        try:
            self.ui.ID_label.setText('ID: ' + str(ID))
            self.ui.Full_name_label.setText('Full Name: ' + str(name))
            self.ui.Country_label.setText('Country: ' + str(country))
            self.ui.Years_label.setText('Years: ' + str(years))
        except Exception as e:
            print('Some error with put data to labels: ', e.args)
        self.ui.save_to_file_btn.clicked.connect(self.save_xml)
        self.ui.save_to_file_btn_2.clicked.connect(self.save_json)

    def save_xml(self):
        try:
            threading.Thread(target=FileManager.save_author_info_XML(self._info)).start()
            print('Saved into XML!')
        except Exception as e:
            print(e)

    def save_json(self):
        try:
            threading.Thread(target=FileManager.save_author_info_json(self._info)).start()
            print('Saved into Json!')
        except Exception as e:
            print(e)


class ShowBookInfoForm(QtWidgets.QMainWindow, Ui_showBook):
    def __init__(self, data, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_showBook()
        self.ui.setupUi(self)

        self._info = data
        authors_id, title, sheets, publisher, year = data
        self.ui.label.setText('Author\'s ID: ' + str(authors_id))
        self.ui.label_2.setText('Title: ' + str(title))
        self.ui.label_3.setText('Sheets: ' + str(sheets))
        self.ui.label_4.setText('Publisher: ' + str(publisher))
        self.ui.label_5.setText('Year: ' + str(year))

        self.ui.pushButton.clicked.connect(self.save_book_xml)
        self.ui.pushButton_2.clicked.connect(self.save_book_json)

    def save_book_xml(self):
        try:
            threading.Thread(target=FileManager.save_book_info_xml(self._info)).start()
        except Exception as e:
            print(e.args)

    def save_book_json(self):
        try:
            threading.Thread(target=FileManager.save_book_info_json(self._info)).start()
        except Exception as e:
            print(e.args)


class Add_author(QtWidgets.QMainWindow, Ui_add_author):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_add_author()
        self.ui.setupUi(self)

        self.name = ''
        self.country = ''
        self.years = ''

        self.ui.Add_author_button.clicked.connect(self.push_author)

    def push_author(self):
        self.name = self.ui.FullName_inp.text()
        self.country = self.ui.Country_inp.text()
        self.years = self.ui.Years_inp.text()
        db = sqlite3.connect('Library.db')
        try:
            with db:
                cursor = db.cursor()
                cursor.execute('INSERT INTO Авторы  VALUES(NULL, ?,?,?)', (self.name, self.country, self.years))
                db.commit()
        except Exception as e:
            print(e.args)
        QtWidgets.QMessageBox.question(self,
                                       'Done.',
                                       'Данные успешно загружены!',
                                       QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Ok)


class Add_book(QtWidgets.QMainWindow, Ui_add_book):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_add_book()
        self.ui.setupUi(self)

        self.author_id = None
        self.title = ''
        self.sheets = None
        self.publisher = ''
        self.year = None

        self.ui.Add_book_button.clicked.connect(self.push_book)

    def push_book(self):
        self.author_id = int(self.ui.authorID_inp.text())
        self.title = self.ui.BookName_inp.text()
        self.sheets = int(self.ui.Pages_count_inp.text())
        self.publisher = self.ui.publish_house_inp.text()
        self.year = int(self.ui.Year_publishing_inp.text())

        db = sqlite3.connect('Library.db')
        with db:
            cursor = db.cursor()
            try:
                cursor.execute('INSERT INTO Книги VALUES(?,?,?,?,?)', (self.author_id, self.title, self.sheets,
                                                                       self.publisher, self.year))
                db.commit()
            except Exception as e:
                print(e.args)
        QtWidgets.QMessageBox.question(self,
                                       'Done.',
                                       'Данные успешно загружены!',
                                       QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Ok)


def main():
    app = QtWidgets.QApplication(sys.argv)
    my_app = Autorization()
    my_app.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
