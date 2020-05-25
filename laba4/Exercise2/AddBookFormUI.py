# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddBookForm.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_add_book(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(369, 280)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 12, 61, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 61, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 120, 71, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(210, 10, 91, 20))
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(210, 70, 91, 20))
        self.label_6.setObjectName("label_6")
        self.Add_book_button = QtWidgets.QPushButton(self.centralwidget)
        self.Add_book_button.setGeometry(QtCore.QRect(120, 202, 121, 51))
        self.Add_book_button.setObjectName("Add_book_button")
        self.authorID_inp = QtWidgets.QLineEdit(self.centralwidget)
        self.authorID_inp.setGeometry(QtCore.QRect(10, 40, 141, 20))
        self.authorID_inp.setObjectName("authorID_inp")
        self.BookName_inp = QtWidgets.QLineEdit(self.centralwidget)
        self.BookName_inp.setGeometry(QtCore.QRect(10, 90, 141, 20))
        self.BookName_inp.setObjectName("BookName_inp")
        self.Pages_count_inp = QtWidgets.QLineEdit(self.centralwidget)
        self.Pages_count_inp.setGeometry(QtCore.QRect(10, 150, 141, 20))
        self.Pages_count_inp.setObjectName("Pages_count_inp")
        self.publish_house_inp = QtWidgets.QLineEdit(self.centralwidget)
        self.publish_house_inp.setGeometry(QtCore.QRect(210, 40, 141, 20))
        self.publish_house_inp.setObjectName("publish_house_inp")
        self.Year_publishing_inp = QtWidgets.QLineEdit(self.centralwidget)
        self.Year_publishing_inp.setGeometry(QtCore.QRect(210, 90, 141, 20))
        self.Year_publishing_inp.setObjectName("Year_publishing_inp")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Author ID"))
        self.label_2.setText(_translate("MainWindow", "Book Name"))
        self.label_3.setText(_translate("MainWindow", "Pages count"))
        self.label_4.setText(_translate("MainWindow", "Рublishing house"))
        self.label_6.setText(_translate("MainWindow", "Year of publication"))
        self.Add_book_button.setText(_translate("MainWindow", "Add"))
