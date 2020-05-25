# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ShowAuthorInfoFormUI.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Info_author(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(438, 196)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ID_label = QtWidgets.QLabel(self.centralwidget)
        self.ID_label.setGeometry(QtCore.QRect(20, 12, 391, 21))
        self.ID_label.setObjectName("ID_label")
        self.Full_name_label = QtWidgets.QLabel(self.centralwidget)
        self.Full_name_label.setGeometry(QtCore.QRect(20, 42, 391, 21))
        self.Full_name_label.setObjectName("Full_name_label")
        self.Country_label = QtWidgets.QLabel(self.centralwidget)
        self.Country_label.setGeometry(QtCore.QRect(20, 70, 391, 21))
        self.Country_label.setObjectName("Country_label")
        self.Years_label = QtWidgets.QLabel(self.centralwidget)
        self.Years_label.setGeometry(QtCore.QRect(20, 100, 391, 21))
        self.Years_label.setObjectName("Years_label")
        self.save_to_file_btn = QtWidgets.QPushButton(self.centralwidget)
        self.save_to_file_btn.setGeometry(QtCore.QRect(30, 130, 141, 51))
        self.save_to_file_btn.setObjectName("save_to_file_btn")
        self.save_to_file_btn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.save_to_file_btn_2.setGeometry(QtCore.QRect(240, 130, 141, 51))
        self.save_to_file_btn_2.setObjectName("save_to_file_btn_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Информация"))
        self.ID_label.setText(_translate("MainWindow", "TextLabel"))
        self.Full_name_label.setText(_translate("MainWindow", "TextLabel"))
        self.Country_label.setText(_translate("MainWindow", "TextLabel"))
        self.Years_label.setText(_translate("MainWindow", "TextLabel"))
        self.save_to_file_btn.setText(_translate("MainWindow", "Сохранить в XML"))
        self.save_to_file_btn_2.setText(_translate("MainWindow", "Сохранить в Json"))
