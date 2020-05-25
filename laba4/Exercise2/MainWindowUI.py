# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(418, 211)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.search_author_button = QtWidgets.QPushButton(self.centralwidget)
        self.search_author_button.setGeometry(QtCore.QRect(20, 90, 75, 23))
        self.search_author_button.setObjectName("search_author_button")
        self.search_book_button = QtWidgets.QPushButton(self.centralwidget)
        self.search_book_button.setGeometry(QtCore.QRect(220, 90, 75, 23))
        self.search_book_button.setObjectName("search_book_button")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 32, 71, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(250, 32, 81, 21))
        self.label_2.setObjectName("label_2")
        self.AuthorID_inp = QtWidgets.QLineEdit(self.centralwidget)
        self.AuthorID_inp.setGeometry(QtCore.QRect(20, 60, 181, 21))
        self.AuthorID_inp.setObjectName("AuthorID_inp")
        self.BookName_inp = QtWidgets.QLineEdit(self.centralwidget)
        self.BookName_inp.setGeometry(QtCore.QRect(220, 60, 181, 21))
        self.BookName_inp.setObjectName("BookName_inp")
        self.add_book_button = QtWidgets.QPushButton(self.centralwidget)
        self.add_book_button.setGeometry(QtCore.QRect(220, 160, 181, 31))
        self.add_book_button.setObjectName("add_book_button")
        self.add_author_button = QtWidgets.QPushButton(self.centralwidget)
        self.add_author_button.setGeometry(QtCore.QRect(20, 160, 181, 31))
        self.add_author_button.setObjectName("add_author_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.search_author_button.setText(_translate("MainWindow", "Find"))
        self.search_book_button.setText(_translate("MainWindow", "Find"))
        self.label.setText(_translate("MainWindow", "Author ID"))
        self.label_2.setText(_translate("MainWindow", "Book Name"))
        self.add_book_button.setText(_translate("MainWindow", "Add book"))
        self.add_author_button.setText(_translate("MainWindow", "Add author"))
