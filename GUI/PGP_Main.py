# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pgp.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QSystemTrayIcon, QMenu, QAction


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 650)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(182, 0, 618, 620))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_1 = QtWidgets.QWidget()
        self.page_1.setObjectName("page_1")
        self.title_label_1 = QtWidgets.QLabel(self.page_1)
        self.title_label_1.setGeometry(QtCore.QRect(0, 0, 250, 50))
        font = QtGui.QFont()
        font.setFamily(".萍方-简")
        font.setPointSize(18)
        self.title_label_1.setFont(font)
        self.title_label_1.setAlignment(QtCore.Qt.AlignCenter)
        self.title_label_1.setObjectName("title_label_1")
        self.key_label_1 = QtWidgets.QLabel(self.page_1)
        self.key_label_1.setGeometry(QtCore.QRect(0, 60, 100, 32))
        self.key_label_1.setAlignment(QtCore.Qt.AlignCenter)
        self.key_label_1.setObjectName("key_label_1")
        self.key_label_2 = QtWidgets.QLabel(self.page_1)
        self.key_label_2.setGeometry(QtCore.QRect(0, 100, 100, 32))
        self.key_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.key_label_2.setObjectName("key_label_2")
        self.key_label_3 = QtWidgets.QLabel(self.page_1)
        self.key_label_3.setGeometry(QtCore.QRect(0, 140, 100, 32))
        self.key_label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.key_label_3.setObjectName("key_label_3")
        self.key_label_4 = QtWidgets.QLabel(self.page_1)
        self.key_label_4.setGeometry(QtCore.QRect(300, 60, 100, 32))
        self.key_label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.key_label_4.setObjectName("key_label_4")
        self.key_label_5 = QtWidgets.QLabel(self.page_1)
        self.key_label_5.setGeometry(QtCore.QRect(300, 100, 100, 32))
        self.key_label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.key_label_5.setObjectName("key_label_5")
        self.key_tf_1 = QtWidgets.QTextEdit(self.page_1)
        self.key_tf_1.setGeometry(QtCore.QRect(100, 60, 200, 32))
        self.key_tf_1.setObjectName("key_tf_1")
        self.key_tf_2 = QtWidgets.QTextEdit(self.page_1)
        self.key_tf_2.setGeometry(QtCore.QRect(100, 100, 200, 32))
        self.key_tf_2.setObjectName("key_tf_2")
        self.key_tf_3 = QtWidgets.QTextEdit(self.page_1)
        self.key_tf_3.setGeometry(QtCore.QRect(100, 140, 200, 32))
        self.key_tf_3.setObjectName("key_tf_3")
        self.key_tf_4 = QtWidgets.QTextEdit(self.page_1)
        self.key_tf_4.setEnabled(False)
        self.key_tf_4.setGeometry(QtCore.QRect(400, 60, 200, 32))
        self.key_tf_4.setObjectName("key_tf_4")
        self.key_tf_5 = QtWidgets.QTextEdit(self.page_1)
        self.key_tf_5.setEnabled(False)
        self.key_tf_5.setGeometry(QtCore.QRect(400, 100, 200, 32))
        self.key_tf_5.setObjectName("key_tf_5")
        self.key_push_1 = QtWidgets.QPushButton(self.page_1)
        self.key_push_1.setGeometry(QtCore.QRect(430, 140, 180, 45))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.key_push_1.setFont(font)
        self.key_push_1.setObjectName("key_push_1")
        self.key_display = QtWidgets.QTextEdit(self.page_1)
        self.key_display.setEnabled(False)
        self.key_display.setGeometry(QtCore.QRect(5, 200, 610, 200))
        self.key_display.setObjectName("key_display")
        self.key_label_6 = QtWidgets.QLabel(self.page_1)
        self.key_label_6.setGeometry(QtCore.QRect(0, 410, 100, 32))
        self.key_label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.key_label_6.setObjectName("key_label_6")
        self.key_tf_6 = QtWidgets.QTextEdit(self.page_1)
        self.key_tf_6.setEnabled(False)
        self.key_tf_6.setGeometry(QtCore.QRect(100, 410, 400, 32))
        self.key_tf_6.setObjectName("key_tf_6")
        self.key_push_2 = QtWidgets.QPushButton(self.page_1)
        self.key_push_2.setGeometry(QtCore.QRect(510, 410, 100, 32))
        self.key_push_2.setObjectName("key_push_2")
        self.key_push_3 = QtWidgets.QPushButton(self.page_1)
        self.key_push_3.setGeometry(QtCore.QRect(240, 450, 180, 45))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.key_push_3.setFont(font)
        self.key_push_3.setObjectName("key_push_3")
        self.key_push_4 = QtWidgets.QPushButton(self.page_1)
        self.key_push_4.setGeometry(QtCore.QRect(430, 450, 180, 45))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.key_push_4.setFont(font)
        self.key_push_4.setObjectName("key_push_4")
        self.key_push_5 = QtWidgets.QPushButton(self.page_1)
        self.key_push_5.setGeometry(QtCore.QRect(430, 510, 180, 45))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.key_push_5.setFont(font)
        self.key_push_5.setObjectName("key_push_5")
        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.title_label_2 = QtWidgets.QLabel(self.page_2)
        self.title_label_2.setGeometry(QtCore.QRect(0, 0, 250, 50))
        font = QtGui.QFont()
        font.setFamily(".萍方-简")
        font.setPointSize(18)
        self.title_label_2.setFont(font)
        self.title_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.title_label_2.setObjectName("title_label_2")
        self.file_push_1 = QtWidgets.QPushButton(self.page_2)
        self.file_push_1.setGeometry(QtCore.QRect(510, 60, 100, 32))
        self.file_push_1.setObjectName("file_push_1")
        self.file_tf_1 = QtWidgets.QTextEdit(self.page_2)
        self.file_tf_1.setEnabled(False)
        self.file_tf_1.setGeometry(QtCore.QRect(100, 60, 400, 32))
        self.file_tf_1.setObjectName("file_tf_1")
        self.file_label_1 = QtWidgets.QLabel(self.page_2)
        self.file_label_1.setGeometry(QtCore.QRect(0, 60, 100, 32))
        self.file_label_1.setAlignment(QtCore.Qt.AlignCenter)
        self.file_label_1.setObjectName("file_label_1")
        self.file_tf_2 = QtWidgets.QTextEdit(self.page_2)
        self.file_tf_2.setEnabled(False)
        self.file_tf_2.setGeometry(QtCore.QRect(100, 100, 400, 32))
        self.file_tf_2.setObjectName("file_tf_2")
        self.file_label_2 = QtWidgets.QLabel(self.page_2)
        self.file_label_2.setGeometry(QtCore.QRect(0, 100, 100, 32))
        self.file_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.file_label_2.setObjectName("file_label_2")
        self.file_push_2 = QtWidgets.QPushButton(self.page_2)
        self.file_push_2.setGeometry(QtCore.QRect(510, 100, 100, 32))
        self.file_push_2.setObjectName("file_push_2")
        self.file_label_4 = QtWidgets.QLabel(self.page_2)
        self.file_label_4.setGeometry(QtCore.QRect(0, 360, 100, 32))
        self.file_label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.file_label_4.setObjectName("file_label_4")
        self.file_push_7 = QtWidgets.QPushButton(self.page_2)
        self.file_push_7.setGeometry(QtCore.QRect(240, 400, 180, 45))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.file_push_7.setFont(font)
        self.file_push_7.setObjectName("file_push_7")
        self.file_push_6 = QtWidgets.QPushButton(self.page_2)
        self.file_push_6.setGeometry(QtCore.QRect(510, 360, 100, 32))
        self.file_push_6.setObjectName("file_push_6")
        self.file_tf_3 = QtWidgets.QTextEdit(self.page_2)
        self.file_tf_3.setEnabled(False)
        self.file_tf_3.setGeometry(QtCore.QRect(100, 320, 400, 32))
        self.file_tf_3.setObjectName("file_tf_3")
        self.file_push_8 = QtWidgets.QPushButton(self.page_2)
        self.file_push_8.setGeometry(QtCore.QRect(430, 400, 180, 45))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.file_push_8.setFont(font)
        self.file_push_8.setObjectName("file_push_8")
        self.file_label_3 = QtWidgets.QLabel(self.page_2)
        self.file_label_3.setGeometry(QtCore.QRect(0, 320, 100, 32))
        self.file_label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.file_label_3.setObjectName("file_label_3")
        self.file_tf_4 = QtWidgets.QTextEdit(self.page_2)
        self.file_tf_4.setEnabled(False)
        self.file_tf_4.setGeometry(QtCore.QRect(100, 360, 400, 32))
        self.file_tf_4.setObjectName("file_tf_4")
        self.file_push_5 = QtWidgets.QPushButton(self.page_2)
        self.file_push_5.setGeometry(QtCore.QRect(510, 320, 100, 32))
        self.file_push_5.setObjectName("file_push_5")
        self.file_label_title_2 = QtWidgets.QLabel(self.page_2)
        self.file_label_title_2.setGeometry(QtCore.QRect(0, 200, 250, 50))
        font = QtGui.QFont()
        font.setFamily(".萍方-简")
        font.setPointSize(18)
        self.file_label_title_2.setFont(font)
        self.file_label_title_2.setAlignment(QtCore.Qt.AlignCenter)
        self.file_label_title_2.setObjectName("file_label_title_2")
        self.file_push_4 = QtWidgets.QPushButton(self.page_2)
        self.file_push_4.setGeometry(QtCore.QRect(430, 140, 180, 45))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.file_push_4.setFont(font)
        self.file_push_4.setObjectName("file_push_4")
        self.file_push_3 = QtWidgets.QPushButton(self.page_2)
        self.file_push_3.setGeometry(QtCore.QRect(240, 140, 180, 45))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.file_push_3.setFont(font)
        self.file_push_3.setObjectName("file_push_3")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.title_label_3 = QtWidgets.QLabel(self.page_3)
        self.title_label_3.setGeometry(QtCore.QRect(0, 0, 250, 50))
        font = QtGui.QFont()
        font.setFamily(".萍方-简")
        font.setPointSize(18)
        self.title_label_3.setFont(font)
        self.title_label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.title_label_3.setObjectName("title_label_3")
        self.clip_tf = QtWidgets.QTextEdit(self.page_3)
        self.clip_tf.setEnabled(False)
        self.clip_tf.setGeometry(QtCore.QRect(0, 60, 610, 400))
        self.clip_tf.setObjectName("clip_tf")
        self.clip_push_1 = QtWidgets.QPushButton(self.page_3)
        self.clip_push_1.setGeometry(QtCore.QRect(240, 480, 180, 45))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.clip_push_1.setFont(font)
        self.clip_push_1.setObjectName("clip_push_1")
        self.clip_push_2 = QtWidgets.QPushButton(self.page_3)
        self.clip_push_2.setGeometry(QtCore.QRect(430, 480, 180, 45))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.clip_push_2.setFont(font)
        self.clip_push_2.setObjectName("clip_push_2")
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.title_label_4 = QtWidgets.QLabel(self.page_4)
        self.title_label_4.setGeometry(QtCore.QRect(0, 0, 250, 50))
        font = QtGui.QFont()
        font.setFamily(".萍方-简")
        font.setPointSize(18)
        self.title_label_4.setFont(font)
        self.title_label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.title_label_4.setObjectName("title_label_4")
        self.zip_label_2 = QtWidgets.QLabel(self.page_4)
        self.zip_label_2.setGeometry(QtCore.QRect(0, 90, 100, 32))
        self.zip_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.zip_label_2.setObjectName("zip_label_2")
        self.zip_label_1 = QtWidgets.QLabel(self.page_4)
        self.zip_label_1.setGeometry(QtCore.QRect(0, 50, 100, 32))
        self.zip_label_1.setAlignment(QtCore.Qt.AlignCenter)
        self.zip_label_1.setObjectName("zip_label_1")
        self.zip_push_1 = QtWidgets.QPushButton(self.page_4)
        self.zip_push_1.setGeometry(QtCore.QRect(510, 50, 100, 32))
        self.zip_push_1.setObjectName("zip_push_1")
        self.zip_push_2 = QtWidgets.QPushButton(self.page_4)
        self.zip_push_2.setGeometry(QtCore.QRect(510, 90, 100, 32))
        self.zip_push_2.setObjectName("zip_push_2")
        self.zip_push_3 = QtWidgets.QPushButton(self.page_4)
        self.zip_push_3.setGeometry(QtCore.QRect(240, 130, 180, 45))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.zip_push_3.setFont(font)
        self.zip_push_3.setObjectName("zip_push_3")
        self.zip_tf_2 = QtWidgets.QTextEdit(self.page_4)
        self.zip_tf_2.setEnabled(False)
        self.zip_tf_2.setGeometry(QtCore.QRect(100, 90, 400, 32))
        self.zip_tf_2.setObjectName("zip_tf_2")
        self.zip_tf_1 = QtWidgets.QTextEdit(self.page_4)
        self.zip_tf_1.setEnabled(False)
        self.zip_tf_1.setGeometry(QtCore.QRect(100, 50, 400, 32))
        self.zip_tf_1.setObjectName("zip_tf_1")
        self.zip_push_4 = QtWidgets.QPushButton(self.page_4)
        self.zip_push_4.setGeometry(QtCore.QRect(430, 130, 180, 45))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.zip_push_4.setFont(font)
        self.zip_push_4.setObjectName("zip_push_4")
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.title_label_5 = QtWidgets.QLabel(self.page_5)
        self.title_label_5.setGeometry(QtCore.QRect(0, 0, 250, 50))
        font = QtGui.QFont()
        font.setFamily(".萍方-简")
        font.setPointSize(18)
        self.title_label_5.setFont(font)
        self.title_label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.title_label_5.setObjectName("title_label_5")
        self.sig_tf_1 = QtWidgets.QTextEdit(self.page_5)
        self.sig_tf_1.setEnabled(False)
        self.sig_tf_1.setGeometry(QtCore.QRect(100, 60, 400, 32))
        self.sig_tf_1.setObjectName("sig_tf_1")
        self.sig_label_1 = QtWidgets.QLabel(self.page_5)
        self.sig_label_1.setGeometry(QtCore.QRect(0, 60, 100, 32))
        self.sig_label_1.setAlignment(QtCore.Qt.AlignCenter)
        self.sig_label_1.setObjectName("sig_label_1")
        self.sig_push_1 = QtWidgets.QPushButton(self.page_5)
        self.sig_push_1.setGeometry(QtCore.QRect(510, 60, 100, 32))
        self.sig_push_1.setObjectName("sig_push_1")
        self.sig_push_3 = QtWidgets.QPushButton(self.page_5)
        self.sig_push_3.setGeometry(QtCore.QRect(430, 100, 180, 45))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.sig_push_3.setFont(font)
        self.sig_push_3.setObjectName("sig_push_3")
        self.sig_push_2 = QtWidgets.QPushButton(self.page_5)
        self.sig_push_2.setGeometry(QtCore.QRect(240, 100, 180, 45))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.sig_push_2.setFont(font)
        self.sig_push_2.setObjectName("sig_push_2")
        self.sig_tf_2 = QtWidgets.QTextEdit(self.page_5)
        self.sig_tf_2.setEnabled(True)
        self.sig_tf_2.setGeometry(QtCore.QRect(0, 150, 610, 400))
        self.sig_tf_2.setObjectName("sig_tf_2")
        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.layoutWidget = QtWidgets.QWidget(self.page_6)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 60, 611, 557))
        self.layoutWidget.setObjectName("layoutWidget")
        self.smtp_layout_1 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.smtp_layout_1.setContentsMargins(0, 0, 0, 0)
        self.smtp_layout_1.setObjectName("smtp_layout_1")
        self.smtp_layout_2 = QtWidgets.QVBoxLayout()
        self.smtp_layout_2.setObjectName("smtp_layout_2")
        self.smtp_layout_3 = QtWidgets.QHBoxLayout()
        self.smtp_layout_3.setObjectName("smtp_layout_3")
        self.smtp_label_1 = QtWidgets.QLabel(self.layoutWidget)
        self.smtp_label_1.setMaximumSize(QtCore.QSize(16777215, 32))
        self.smtp_label_1.setObjectName("smtp_label_1")
        self.smtp_layout_3.addWidget(self.smtp_label_1)
        self.smtp_tf_1 = QtWidgets.QTextEdit(self.layoutWidget)
        self.smtp_tf_1.setMaximumSize(QtCore.QSize(16777215, 32))
        self.smtp_tf_1.setObjectName("smtp_tf_1")
        self.smtp_layout_3.addWidget(self.smtp_tf_1)
        self.smtp_layout_2.addLayout(self.smtp_layout_3)
        self.smtp_layout_4 = QtWidgets.QHBoxLayout()
        self.smtp_layout_4.setObjectName("smtp_layout_4")
        self.smtp_label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.smtp_label_2.setMaximumSize(QtCore.QSize(16777215, 32))
        self.smtp_label_2.setObjectName("smtp_label_2")
        self.smtp_layout_4.addWidget(self.smtp_label_2)
        self.smtp_tf_2 = QtWidgets.QTextEdit(self.layoutWidget)
        self.smtp_tf_2.setMaximumSize(QtCore.QSize(16777215, 32))
        self.smtp_tf_2.setObjectName("smtp_tf_2")
        self.smtp_layout_4.addWidget(self.smtp_tf_2)
        self.smtp_layout_2.addLayout(self.smtp_layout_4)
        self.smtp_layout_5 = QtWidgets.QHBoxLayout()
        self.smtp_layout_5.setObjectName("smtp_layout_5")
        self.smtp_label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.smtp_label_3.setMaximumSize(QtCore.QSize(16777215, 32))
        self.smtp_label_3.setObjectName("smtp_label_3")
        self.smtp_layout_5.addWidget(self.smtp_label_3)
        self.smtp_tf_3 = QtWidgets.QTextEdit(self.layoutWidget)
        self.smtp_tf_3.setMaximumSize(QtCore.QSize(16777215, 32))
        self.smtp_tf_3.setObjectName("smtp_tf_3")
        self.smtp_layout_5.addWidget(self.smtp_tf_3)
        self.smtp_layout_2.addLayout(self.smtp_layout_5)
        self.smtp_layout_6 = QtWidgets.QHBoxLayout()
        self.smtp_layout_6.setObjectName("smtp_layout_6")
        self.smtp_label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.smtp_label_4.setMaximumSize(QtCore.QSize(16777215, 32))
        self.smtp_label_4.setObjectName("smtp_label_4")
        self.smtp_layout_6.addWidget(self.smtp_label_4)
        self.smtp_tf_4 = QtWidgets.QTextEdit(self.layoutWidget)
        self.smtp_tf_4.setMaximumSize(QtCore.QSize(16777215, 32))
        self.smtp_tf_4.setObjectName("smtp_tf_4")
        self.smtp_layout_6.addWidget(self.smtp_tf_4)
        self.smtp_layout_2.addLayout(self.smtp_layout_6)
        self.smtp_layout_7 = QtWidgets.QHBoxLayout()
        self.smtp_layout_7.setObjectName("smtp_layout_7")
        self.smtp_label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.smtp_label_5.setMaximumSize(QtCore.QSize(16777215, 32))
        self.smtp_label_5.setObjectName("smtp_label_5")
        self.smtp_layout_7.addWidget(self.smtp_label_5)
        self.smtp_tf_5 = QtWidgets.QTextEdit(self.layoutWidget)
        self.smtp_tf_5.setMaximumSize(QtCore.QSize(16777215, 32))
        self.smtp_tf_5.setObjectName("smtp_tf_5")
        self.smtp_layout_7.addWidget(self.smtp_tf_5)
        self.smtp_layout_2.addLayout(self.smtp_layout_7)
        self.smtp_layout_8 = QtWidgets.QHBoxLayout()
        self.smtp_layout_8.setObjectName("smtp_layout_8")
        self.smtp_label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.smtp_label_6.setMaximumSize(QtCore.QSize(16777215, 32))
        self.smtp_label_6.setObjectName("smtp_label_6")
        self.smtp_layout_8.addWidget(self.smtp_label_6)
        self.smtp_tf_6 = QtWidgets.QTextEdit(self.layoutWidget)
        self.smtp_tf_6.setMaximumSize(QtCore.QSize(16777215, 32))
        self.smtp_tf_6.setObjectName("smtp_tf_6")
        self.smtp_layout_8.addWidget(self.smtp_tf_6)
        self.smtp_layout_2.addLayout(self.smtp_layout_8)
        self.smtp_layout_1.addLayout(self.smtp_layout_2)
        self.smtp_layout_9 = QtWidgets.QHBoxLayout()
        self.smtp_layout_9.setObjectName("smtp_layout_9")
        self.smtp_label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.smtp_label_7.setMinimumSize(QtCore.QSize(480, 0))
        self.smtp_label_7.setText("")
        self.smtp_label_7.setObjectName("smtp_label_7")
        self.smtp_layout_9.addWidget(self.smtp_label_7)
        self.smtp_push = QtWidgets.QPushButton(self.layoutWidget)
        self.smtp_push.setObjectName("smtp_push")
        self.smtp_layout_9.addWidget(self.smtp_push)
        self.smtp_layout_1.addLayout(self.smtp_layout_9)
        self.smtp_layout_10 = QtWidgets.QHBoxLayout()
        self.smtp_layout_10.setObjectName("smtp_layout_10")
        self.smtp_label_8 = QtWidgets.QLabel(self.layoutWidget)
        self.smtp_label_8.setObjectName("smtp_label_8")
        self.smtp_layout_10.addWidget(self.smtp_label_8)
        self.smtp_tf_7 = QtWidgets.QTextEdit(self.layoutWidget)
        self.smtp_tf_7.setMaximumSize(QtCore.QSize(16777215, 32))
        self.smtp_tf_7.setObjectName("smtp_tf_7")
        self.smtp_layout_10.addWidget(self.smtp_tf_7)
        self.smtp_layout_1.addLayout(self.smtp_layout_10)
        self.smtp_layout_11 = QtWidgets.QVBoxLayout()
        self.smtp_layout_11.setObjectName("smtp_layout_11")
        self.smtp_label_9 = QtWidgets.QLabel(self.layoutWidget)
        self.smtp_label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.smtp_label_9.setObjectName("smtp_label_9")
        self.smtp_layout_11.addWidget(self.smtp_label_9)
        self.smtp_tf_8 = QtWidgets.QTextEdit(self.layoutWidget)
        self.smtp_tf_8.setObjectName("smtp_tf_8")
        self.smtp_layout_11.addWidget(self.smtp_tf_8)
        self.smtp_layout_1.addLayout(self.smtp_layout_11)
        self.title_label_6 = QtWidgets.QLabel(self.page_6)
        self.title_label_6.setGeometry(QtCore.QRect(0, 0, 250, 50))
        font = QtGui.QFont()
        font.setFamily(".萍方-简")
        font.setPointSize(18)
        self.title_label_6.setFont(font)
        self.title_label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.title_label_6.setObjectName("title_label_6")
        self.stackedWidget.addWidget(self.page_6)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(0, 0, 182, 337))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.button_left_1 = QtWidgets.QPushButton(self.layoutWidget1)
        self.button_left_1.setMinimumSize(QtCore.QSize(180, 50))
        self.button_left_1.setObjectName("button_left_1")
        self.verticalLayout.addWidget(self.button_left_1)
        self.button_left_2 = QtWidgets.QPushButton(self.layoutWidget1)
        self.button_left_2.setMinimumSize(QtCore.QSize(180, 50))
        self.button_left_2.setObjectName("button_left_2")
        self.verticalLayout.addWidget(self.button_left_2)
        self.button_left_3 = QtWidgets.QPushButton(self.layoutWidget1)
        self.button_left_3.setMinimumSize(QtCore.QSize(180, 50))
        self.button_left_3.setObjectName("button_left_3")
        self.verticalLayout.addWidget(self.button_left_3)
        self.button_left_4 = QtWidgets.QPushButton(self.layoutWidget1)
        self.button_left_4.setMinimumSize(QtCore.QSize(180, 50))
        self.button_left_4.setObjectName("button_left_4")
        self.verticalLayout.addWidget(self.button_left_4)
        self.button_left_5 = QtWidgets.QPushButton(self.layoutWidget1)
        self.button_left_5.setMinimumSize(QtCore.QSize(180, 50))
        self.button_left_5.setObjectName("button_left_5")
        self.verticalLayout.addWidget(self.button_left_5)
        self.button_left_6 = QtWidgets.QPushButton(self.layoutWidget1)
        self.button_left_6.setMinimumSize(QtCore.QSize(180, 50))
        self.button_left_6.setObjectName("button_left_6")
        self.verticalLayout.addWidget(self.button_left_6)
        self.pix_label_1 = QtWidgets.QLabel(self.centralwidget)
        self.pix_label_1.setGeometry(QtCore.QRect(10, 360, 150, 150))
        self.pix_label_1.setText("")
        self.pix_label_1.setPixmap(QtGui.QPixmap("Assets/auth.jpg"))
        self.pix_label_1.setScaledContents(True)
        self.pix_label_1.setObjectName("pix_label_1")
        self.pix_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.pix_label_2.setGeometry(QtCore.QRect(10, 520, 150, 32))
        self.pix_label_2.setScaledContents(False)
        self.pix_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.pix_label_2.setObjectName("pix_label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 28))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        self.menu_4 = QtWidgets.QMenu(self.menubar)
        self.menu_4.setObjectName("menu_4")
        MainWindow.setMenuBar(self.menubar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.action_4 = QtWidgets.QAction(MainWindow)
        self.action_4.setObjectName("action_4")
        self.action_5 = QtWidgets.QAction(MainWindow)
        self.action_5.setObjectName("action_5")
        self.action_6 = QtWidgets.QAction(MainWindow)
        self.action_6.setObjectName("action_6")
        self.action_7 = QtWidgets.QAction(MainWindow)
        self.action_7.setObjectName("action_7")
        self.action_8 = QtWidgets.QAction(MainWindow)
        self.action_8.setObjectName("action_8")
        self.action_9 = QtWidgets.QAction(MainWindow)
        self.action_9.setObjectName("action_9")
        self.action_10 = QtWidgets.QAction(MainWindow)
        self.action_10.setObjectName("action_10")
        self.action_11 = QtWidgets.QAction(MainWindow)
        self.action_11.setObjectName("action_11")
        self.action_12 = QtWidgets.QAction(MainWindow)
        self.action_12.setObjectName("action_12")
        self.action_13 = QtWidgets.QAction(MainWindow)
        self.action_13.setObjectName("action_13")
        self.action_14 = QtWidgets.QAction(MainWindow)
        self.action_14.setObjectName("action_14")
        self.action_15 = QtWidgets.QAction(MainWindow)
        self.action_15.setObjectName("action_15")
        self.menu.addAction(self.action_2)
        self.menu.addAction(self.action_3)
        self.menu.addAction(self.action_4)
        self.menu.addAction(self.action_5)
        self.menu_2.addAction(self.action_10)
        self.menu_2.addAction(self.action_11)
        self.menu_2.addAction(self.action_12)
        self.menu_2.addAction(self.action_13)
        self.menu_2.addAction(self.action_14)
        self.menu_2.addAction(self.action_15)
        self.menu_3.addAction(self.action_6)
        self.menu_3.addAction(self.action_7)
        self.menu_3.addAction(self.action_8)
        self.menu_3.addAction(self.action_9)
        self.menu_4.addAction(self.action)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PGP客户端（Based on Qt5） Version 0.9"))
        MainWindow.setWindowIcon((QIcon("Assets/tray.ico")))
        self.title_label_1.setText(_translate("MainWindow", "密钥管理"))
        self.key_label_1.setText(_translate("MainWindow", "姓名"))
        self.key_label_2.setText(_translate("MainWindow", "电子邮件"))
        self.key_label_3.setText(_translate("MainWindow", "密码"))
        self.key_label_4.setText(_translate("MainWindow", "RSA密钥长度"))
        self.key_label_5.setText(_translate("MainWindow", "期限"))
        self.key_tf_4.setHtml(_translate("MainWindow",
                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'.蘋方-簡\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">4096</p></body></html>"))
        self.key_tf_5.setHtml(_translate("MainWindow",
                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'.蘋方-簡\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0</p></body></html>"))
        self.key_push_1.setText(_translate("MainWindow", "生成PGP密钥"))
        self.key_label_6.setText(_translate("MainWindow", "目标文件"))
        self.key_push_2.setText(_translate("MainWindow", "浏览"))
        self.key_push_3.setText(_translate("MainWindow", "导入PGP密钥"))
        self.key_push_4.setText(_translate("MainWindow", "导出PGP密钥"))
        self.key_push_5.setText(_translate("MainWindow", "备份PGP密钥"))
        self.title_label_2.setText(_translate("MainWindow", "文件加密/解密"))
        self.file_push_1.setText(_translate("MainWindow", "浏览"))
        self.file_label_1.setText(_translate("MainWindow", "源文件"))
        self.file_label_2.setText(_translate("MainWindow", "目标文件"))
        self.file_push_2.setText(_translate("MainWindow", "浏览"))
        self.file_label_4.setText(_translate("MainWindow", "目标文件"))
        self.file_push_7.setText(_translate("MainWindow", "加密"))
        self.file_push_6.setText(_translate("MainWindow", "浏览"))
        self.file_push_8.setText(_translate("MainWindow", "解密"))
        self.file_label_3.setText(_translate("MainWindow", "源文件"))
        self.file_push_5.setText(_translate("MainWindow", "浏览"))
        self.file_label_title_2.setText(_translate("MainWindow", "文本加密/解密"))
        self.file_push_4.setText(_translate("MainWindow", "解密"))
        self.file_push_3.setText(_translate("MainWindow", "加密"))
        self.title_label_3.setText(_translate("MainWindow", "剪贴板"))
        self.clip_push_1.setText(_translate("MainWindow", "加密"))
        self.clip_push_2.setText(_translate("MainWindow", "解密"))
        self.title_label_4.setText(_translate("MainWindow", "压缩/解压缩"))
        self.zip_label_2.setText(_translate("MainWindow", "目标文件"))
        self.zip_label_1.setText(_translate("MainWindow", "源文件"))
        self.zip_push_1.setText(_translate("MainWindow", "浏览"))
        self.zip_push_2.setText(_translate("MainWindow", "浏览"))
        self.zip_push_3.setText(_translate("MainWindow", "加密"))
        self.zip_push_4.setText(_translate("MainWindow", "解密"))
        self.title_label_5.setText(_translate("MainWindow", "数字签名"))
        self.sig_label_1.setText(_translate("MainWindow", "源文件"))
        self.sig_push_1.setText(_translate("MainWindow", "浏览"))
        self.sig_push_3.setText(_translate("MainWindow", "验证"))
        self.sig_push_2.setText(_translate("MainWindow", "签名"))
        self.sig_tf_2.setHtml(_translate("MainWindow",
                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'.蘋方-簡\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">私钥</p></body></html>"))
        self.smtp_label_1.setText(_translate("MainWindow", "Your Email"))
        self.smtp_label_2.setText(_translate("MainWindow", "Your Name"))
        self.smtp_label_3.setText(_translate("MainWindow", "Receiver\'s Email"))
        self.smtp_label_4.setText(_translate("MainWindow", "Receiver\'s Name"))
        self.smtp_label_5.setText(_translate("MainWindow", "Password"))
        self.smtp_label_6.setText(_translate("MainWindow", "SMTP"))
        self.smtp_push.setText(_translate("MainWindow", "Send"))
        self.smtp_label_8.setText(_translate("MainWindow", "Subject"))
        self.smtp_label_9.setText(_translate("MainWindow", "Text"))
        self.title_label_6.setText(_translate("MainWindow", "SMTP电子邮件"))
        self.button_left_1.setText(_translate("MainWindow", "密钥管理"))
        self.button_left_2.setText(_translate("MainWindow", "文件加密/解密"))
        self.button_left_3.setText(_translate("MainWindow", "剪贴板"))
        self.button_left_4.setText(_translate("MainWindow", "压缩/解压缩"))
        self.button_left_5.setText(_translate("MainWindow", "数字签名"))
        self.button_left_6.setText(_translate("MainWindow", "SMTP电子邮件"))
        self.pix_label_2.setText(_translate("MainWindow", "Y.Wang"))
        self.menu.setTitle(_translate("MainWindow", "文件"))
        self.menu_2.setTitle(_translate("MainWindow", "工具"))
        self.menu_3.setTitle(_translate("MainWindow", "密钥"))
        self.menu_4.setTitle(_translate("MainWindow", "帮助"))
        self.action.setText(_translate("MainWindow", "关于"))
        self.action_2.setText(_translate("MainWindow", "新建"))
        self.action_3.setText(_translate("MainWindow", "打开"))
        self.action_4.setText(_translate("MainWindow", "保存"))
        self.action_5.setText(_translate("MainWindow", "退出"))
        self.action_6.setText(_translate("MainWindow", "生成"))
        self.action_7.setText(_translate("MainWindow", "导入"))
        self.action_8.setText(_translate("MainWindow", "导出"))
        self.action_9.setText(_translate("MainWindow", "备份"))
        self.action_10.setText(_translate("MainWindow", "文件加密"))
        self.action_11.setText(_translate("MainWindow", "文件解密"))
        self.action_12.setText(_translate("MainWindow", "剪贴板"))
        self.action_13.setText(_translate("MainWindow", "压缩/解压缩"))
        self.action_14.setText(_translate("MainWindow", "数字签名"))
        self.action_15.setText(_translate("MainWindow", "电子邮件"))

    def addSystemTray(self):
        Action1 = QAction("PGP客户端 -- Qt5 Version 0.9")
        Action2 = QAction("打开主界面")
        Action3 = QAction("退出")
        self.trayIconMenu = QMenu()
        self.trayIconMenu.addAction(Action1)
        self.trayIconMenu.addSeparator()
        self.trayIconMenu.addAction(Action2)
        self.trayIconMenu.addAction(Action3)
        self.trayIcon = QSystemTrayIcon()
        self.trayIcon.setContextMenu(self.trayIconMenu)
        self.trayIcon.setIcon(QIcon("Assets/tray.ico"))
        self.trayIcon.show()
        self.trayIconMenu.show()

    def closeEvent(self, event):
        if self.trayIcon.isVisible():
            self.trayIcon.hide()