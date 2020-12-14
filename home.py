'''首页'''
from PyQt5.Qt import *
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget
import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QWidget, QToolTip, QDesktopWidget, QMessageBox, QTextEdit, QLabel, QPushButton, QApplication, QMainWindow, QAction, qApp, QHBoxLayout, QVBoxLayout, QGridLayout, QLineEdit
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtGui import QPixmap, QImage, QPalette
from PyQt5.QtCore import QCoreApplication
from custom import titleBar,sourceListBox
from newWindow import Ui_MainWindow

class homePage(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.homeBox = self.homeBox
        self.homeUI()

    def homeUI(self):
        import sqlite3
        conn = sqlite3.connect('I:\\amadeus\\LiView\\userData\\sql\\spider.db')
        c = conn.cursor()
        #c.execute('SELECT logo FROM spider')
        c.execute('SELECT logo FROM spider;')
        self.spiderLogo = c.fetchall()
        c.execute('SELECT colorPicture FROM spider;')
        self.spiderPicture = c.fetchall()
        c.execute('SELECT logo FROM sys ')
        self.logo = c.fetchone()
        c.execute('SELECT TopPoster FROM sys ')
        self.TopPoster = c.fetchone()
        c.close()
        conn.close()
        #self.homeBox.resize()
        self.homeBox.setGeometry(0,60,QApplication.desktop().width(), QApplication.desktop().height())


        self.advertisementLab = QLabel(self.homeBox)
        self.advertisementLab.setGeometry(0, 0, self.width(), int(self.width() * 0.45))
        advertisementLab_p = QPixmap()
        advertisementLab_p.loadFromData(self.TopPoster[0])
        self.advertisementLab.setPixmap(advertisementLab_p)
        self.advertisementLab.setScaledContents(True)

        #来源框
        self.source = sourceListBox(self.homeBox)
        self.source.move(0,self.advertisementLab.height() +self.advertisementLab.y())
        self.source.window =self
        self.source.load(self.spiderLogo,self.spiderPicture)
        self.homeBox.lenth = self.source.lastHight + self.advertisementLab.height() + 60-self.height()
        self.homeBox.resize(self.width(),self.source.height())

    def resizeEvent(self, event):

        self.TopLab.resize(self.width(), 60)
        self.advertisementLab.resize(self.width(), int(self.width() * 0.45))