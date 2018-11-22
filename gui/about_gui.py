# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(600, 400)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(0, 360, 600, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.pix_label_2 = QtWidgets.QLabel(Dialog)
        self.pix_label_2.setGeometry(QtCore.QRect(0, 160, 150, 32))
        self.pix_label_2.setScaledContents(False)
        self.pix_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.pix_label_2.setObjectName("pix_label_2")
        self.pix_label_1 = QtWidgets.QLabel(Dialog)
        self.pix_label_1.setGeometry(QtCore.QRect(0, 0, 150, 150))
        self.pix_label_1.setText("")
        self.pix_label_1.setPixmap(QtGui.QPixmap("gui/auth.jpg"))
        self.pix_label_1.setScaledContents(True)
        self.pix_label_1.setObjectName("pix_label_1")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(160, 10, 430, 50))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(160, 70, 430, 70))
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(160, 150, 430, 120))
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "关于"))
        self.pix_label_2.setText(_translate("Dialog", "Y.Wang"))
        self.label.setText(_translate("Dialog", "PGP客户端（Based on Qt5）"))
        self.label_2.setText(_translate("Dialog", "PGP（英语：Pretty Good Privacy，中文翻译“优良保密协议”）是一套用于消息加密、验证的应用程序，采用IDEA的散列算法作为加密与验证之用。"))
        self.label_3.setText(_translate("Dialog", "Qt 是一个著名的 C++ 应用程序框架。你并不能说它只是一个 GUI 库，因为 Qt 十分庞大，并不仅仅是 GUI 组件。使用 Qt，在一定程度上你获得的是一个“一站式”的解决方案：不再需要研究 STL，不再需要 C++ 的<string>，不再需要到处去找解析 XML、连接数据库、访问网络的各种第三方库，因为 Qt 自己内置了这些技术。"))

