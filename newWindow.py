"""新窗口页"""
import requests, sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QToolTip, QDesktopWidget, QMessageBox, QTextEdit, QLabel, QPushButton, QApplication, QMainWindow, QAction, qApp, QHBoxLayout, QVBoxLayout, QGridLayout, QLineEdit
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import QCoreApplication

class Ui_MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.setUI()
        self.pageList = ['home','synopsis']
        self.creatPage(self.pageList)

    def setUI(self):

        MainWindow = self
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)  # 隐藏窗口边框
        MainWindow.resize(1025, 670)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName('centralwidget')
        MainWindow.setCentralWidget(self.centralwidget)
        self.setWindowTitle('LiView')
        self.setWindowIcon(QIcon('img\\icon.png'))
        self.setMinimumHeight(600)
        self.setMinimumWidth(400)

    def creatPage(self, list):
        for i in list:
            exec('self.%sBox = QGroupBox(self.centralwidget)' % i)

        self.pageTage = list[0]
        ''' def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QtCore.Qt.SizeAllCursor)  # 更改鼠标图标

    def mouseMoveEvent(self, QMouseEvent):
        if QtCore.Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QtCore.Qt.ArrowCursor)'''