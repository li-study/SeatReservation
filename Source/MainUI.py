# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainUI.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(569, 292)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.inputCourseButton = QtWidgets.QPushButton(self.centralwidget)
        self.inputCourseButton.setGeometry(QtCore.QRect(330, 40, 93, 28))
        self.inputCourseButton.setObjectName("inputCourseButton")
        self.inputTextFileButton = QtWidgets.QPushButton(self.centralwidget)
        self.inputTextFileButton.setGeometry(QtCore.QRect(450, 40, 93, 28))
        self.inputTextFileButton.setObjectName("inputTextFileButton")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(20, 20, 296, 236))
        self.calendarWidget.setObjectName("calendarWidget")
        self.timeEdit = QtWidgets.QTimeEdit(self.centralwidget)
        self.timeEdit.setGeometry(QtCore.QRect(430, 90, 118, 31))
        self.timeEdit.setObjectName("timeEdit")
        self.searchButton = QtWidgets.QPushButton(self.centralwidget)
        self.searchButton.setGeometry(QtCore.QRect(400, 180, 141, 61))
        self.searchButton.setObjectName("searchButton")
        self.timeLabel = QtWidgets.QLabel(self.centralwidget)
        self.timeLabel.setGeometry(QtCore.QRect(380, 100, 72, 15))
        self.timeLabel.setObjectName("timeLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.inputCourseButton.setText(_translate("MainWindow", "课程表文件"))
        self.inputTextFileButton.setText(_translate("MainWindow", "测试文件"))
        self.searchButton.setText(_translate("MainWindow", "查询"))
        self.timeLabel.setText(_translate("MainWindow", "时间:"))


