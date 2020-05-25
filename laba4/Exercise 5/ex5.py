"""
Напишите приложение для загрузки файлов из интернета. В главном
окне должно быть три текстовых поля, в которые можно вводить
URL файла на закачку; под каждым из текстовых полей должны
быть индикаторы загрузки и рядом поля с процентом загрузки
каждого файла. Необходимо организовать возможность качать от
одного до трех файлов параллельно (использовать потоки
обязательно, файлы загружать фрагментами по 4 Кб). Загрузка
должна инициироваться нажатием кнопки «Start downloading!». По
окончанию загрузки последнего файла должно появиться окно со
столбчатой диаграммой со значениями времени загрузки каждого
файла в формате «2s 322ms» и размерами файлов (используйте
библиотеку matplotlib).
"""

import sys
from PyQt5 import QtWidgets,QtGui,QtCore
import download_window_UI
from threading import Thread
import os
import requests
import time
import urllib.request
import matplotlib.pyplot as plt
dict_time = dict()
dict_size = dict()

class DownloadThread(Thread):
    def __init__(self, url,directory, update_progressBar):
        """Инициализация потока"""
        Thread.__init__(self)
        self.url = url
        self.directory = directory
        self.update = update_progressBar
        self.percent =0
    def run(self):
        try:
            handle = requests.get(self.url)
            filename = self.directory+"//"+os.path.basename(self.url)
            print(filename)
            d = urllib.request.urlopen(self.url)
            file_size = int(d.getheader('Content-Length'))
            print(file_size)
            with open(filename, "wb") as file:
                time_start = time.time()
                for chunk in handle.iter_content(4096):
                    file.write(chunk)
                    time.sleep(0.05)
                    self.percent = int((os.path.getsize(filename)/file_size)*100)
                    self.update(self.percent)
            if os.path.getsize(filename) == file_size:
                self.update(100)
            time_finish = time.time()
            delta_time = time_finish-time_start
            #dict_time[os.path.basename(filename)] = str(delta_time).split(".")[0] + "s " +str(delta_time).split(".")[1][:3] + "ms"
            dict_time[os.path.basename(filename)+"\n"+str(delta_time).split(".")[0] + "s " +str(delta_time).split(".")[1][:3] + "ms"] = delta_time
            #dict_size[os.path.basename(filename)] = str(os.path.getsize(filename)/1048576.0)[:4] + " mb"
            dict_size[os.path.basename(filename)+"\n "+str(os.path.getsize(filename)/1048576.0)[:4] + " mb"]=  os.path.getsize(filename)
        except Exception:
            e = sys.exc_info()[1]
            print(e.args[0])
#-------------------------------
class Example(QtWidgets.QMainWindow, download_window_UI.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.pushButton.clicked.connect(self.download)
    def download(self):
        self.update_progress_bar1(0)
        self.update_progress_bar2(0)
        self.update_progress_bar3(0)
        dict_time.clear()
        dict_size.clear()
        if self.lineEdit.text() is not "" or self.lineEdit_2.text() is not "" or self.lineEdit_3.text() is not "":
            self.directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Выберите папку для загрузки файлов")
            thread1 = DownloadThread(self.lineEdit.text(), self.directory, self.update_progress_bar1)
            thread2 = DownloadThread(self.lineEdit_2.text(), self.directory, self.update_progress_bar2)
            thread3 = DownloadThread(self.lineEdit_3.text(), self.directory, self.update_progress_bar3)
            if self.lineEdit.text() is not "":
                thread1.start()
            if self.lineEdit_2.text() is not "":
                thread2.start()
            if self.lineEdit_3.text() is not "":
                thread3.start()
            if thread1.isAlive() is True:
                thread1.join()
            if thread2.isAlive() is True:
                thread2.join()
            if thread3.isAlive() is True:
                thread3.join()
            print("Все потоки завершили работу!")
            try:
                fig, axes = plt.subplots(1,2)
                axes[0].bar(dict_time.keys(),dict_time.values(), color = 'red')
                axes[0].set_ylabel("Download time")
                axes[0].set_title("Download time plot")
                axes[1].pie(dict_size.values(), labels=dict_size.keys())
                axes[1].set_title("File size")
                fig.set_figwidth(14)  # ширина Figure
                fig.set_figheight(5)  # высота Figure
                plt.subplots_adjust(wspace=0.3)
                plt.show()
                #--------------------------------------------
            except Exception:
                e = sys.exc_info()[1]
                print(e.args[0])
            #--------------------------- диаграмма
        else:
            print("Не введена ни одна ссылка!")
    def update_progress_bar1(self,percent):
        self.progressBar.setValue(percent)
    def update_progress_bar2(self,percent):
        self.progressBar_2.setValue(percent)
    def update_progress_bar3(self,percent):
        self.progressBar_3.setValue(percent)

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = Example()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    sys.exit(app.exec_())  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()