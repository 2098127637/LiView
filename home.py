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
from resources import rescource

class homePage(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.homeBox = self.homeBox
        self.homeUI()

    def get_res(self):
        res = rescource()
        res.ParentComponent = self  # 绑定本身为res父组件
        res.homeBoxRes() # 获取水平滚动框所需的json信息

    def homeUI(self):
        '''import sqlite3
        conn = sqlite3.connect('I:\\amadeus\\LiView\\userData\\sql\\spider.db')
        c = conn.cursor()
        #c.execute('SELECT logo FROM spider')

        c.execute('SELECT openLogo FROM sys;')  # 打开图标
        self.openLogo = c.fetchall()
        c.execute('SELECT TopPoster FROM sys ')     #顶层海报背景图
        self.TopPoster = c.fetchone()
        c.close()
        conn.close()'''
        #self.homeBox.resize()
        self.homeBox.setGeometry(0,60,QApplication.desktop().width(), QApplication.desktop().height())

        self.advertisementLab = QLabel(self.homeBox)
        self.advertisementLab.setGeometry(0, 0, self.width(), int(self.width() * 0.45))
        advertisementLab_p = QPixmap()
        advertisementLab_p.loadFromData(self.TopPoster[0][0])
        self.advertisementLab.setPixmap(advertisementLab_p)
        self.advertisementLab.setScaledContents(True)

        #来源框
        self.source = sourceListBox(self.homeBox)
        self.source.move(0,self.advertisementLab.height() +self.advertisementLab.y())
        self.source.window =self
        self.source.load()    #加载来源信息
        self.homeBox.lenth = self.source.lastHight + self.advertisementLab.height() + 60-self.height()      #限制homeBox能向下滚动的最大距离
        self.homeBox.resize(self.width(),self.source.height())      #增加homeBox的高度

    def resizeEvent(self, event):

        self.TopLab.resize(self.width(), 60)
        self.advertisementLab.resize(self.width(), int(self.width() * 0.45))