# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddAuthorForm.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_add_author(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(370, 283)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.FullName_inp = QtWidgets.QLineEdit(self.centralwidget)
        self.FullName_inp.setGeometry(QtCore.QRect(10, 50, 331, 20))
        self.FullName_inp.setObjectName("FullName_inp")
        self.Years_inp = QtWidgets.QLineEdit(self.centralwidget)
        self.Years_inp.setGeometry(QtCore.QRect(10, 110, 331, 20))
        self.Years_inp.setObjectName("Years_inp")
        self.Country_inp = QtWidgets.QLineEdit(self.centralwidget)
        self.Country_inp.setGeometry(QtCore.QRect(10, 170, 331, 20))
        self.Country_inp.setObjectName("Country_inp")
        self.Add_author_button = QtWidgets.QPushButton(self.centralwidget)
        self.Add_author_button.setGeometry(QtCore.QRect(110, 210, 131, 51))
        self.Add_author_button.setObjectName("Add_author_button")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 13, 81, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 81, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 140, 81, 20))
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Add Author"))
        self.Add_author_button.setText(_translate("MainWindow", "Add"))
        self.label.setText(_translate("MainWindow", "Full name"))
        self.label_2.setText(_translate("MainWindow", "Years of life"))
        self.label_3.setText(_translate("MainWindow", "Country"))
