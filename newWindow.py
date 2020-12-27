"""新窗口页"""
import requests, sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QToolTip, QDesktopWidget, QMessageBox, QTextEdit, QLabel, QPushButton, QApplication, QMainWindow, QAction, qApp, QHBoxLayout, QVBoxLayout, QGridLayout, QLineEdit
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import QCoreApplication
from custom import titleBar,scrollBox

class Ui_MainWindow(QtWidgets.QMainWindow):
    #创建新窗口

    def __init__(self):
        super().__init__()
        self.setUI()
        self.pageList = ['home','synopsis']
        self.creatPage(self.pageList)

    def setUI(self):

        MainWindow = self
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)  # 隐藏窗口边框
        MainWindow.resize(1025, 670)
        #MainWindow.resize(1200, 670)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName('centralwidget')
        MainWindow.setCentralWidget(self.centralwidget)
        self.setMinimumHeight(600)
        self.setMinimumWidth(400)

        # 添加标题栏
        self.TopLab = titleBar(self.centralwidget)
        self.TopLab.window = self  # 传入父组件对象
        self.TopLab.setGeometry(0, 0, self.width(), 60)

        self.TopLabP = self.TopLab.height() + self.y()

    def creatPage(self, list):
        #按照self.pagelist中项+Box创建两个scrollBox（scrollBox在custom.py中定义继承自groupBox）
        for i in list:
            exec('self.%sBox = scrollBox(self.centralwidget)' % i)
            #exec('self.%sBox.move(0,60)' % i)
            exec('self.%sBox.window = self' % i)

        self.pageTage = list[0]