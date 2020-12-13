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
from custom import titleBar
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
        c.execute('SELECT logo FROM spider WHERE name = ?', ('选书网', ))
        self.spiderLogo = c.fetchone()
        c.execute('SELECT logo FROM sys ')
        self.logo = c.fetchone()
        c.execute('SELECT TopPoster FROM sys ')
        self.TopPoster = c.fetchone()
        c.close()
        conn.close()
        self.homeBox.resize(QApplication.desktop().width(), QApplication.desktop().height())


        self.TopLab =titleBar(self.homeBox)
        self.TopLab.window =self
        #self.TopLab.backcolor =self.logo[0]
        self.TopLab.setGeometry(0, 0, self.width(), 60)
        #self.TopLab.initialization()
        #self.TopLab.setStyleSheet('background-color:#FF6666')
        #self.TopLab.setMaximumHeight(60)
        #self.TopLab.setMinimumHeight(20)

        '''
        self.LogoLab = QLabel('图片', self.homeBox)
        self.LogoLab.setGeometry(15, 0, 120, 60)
        LogoLab_p = QPixmap()
        LogoLab_p.loadFromData(self.logo[0])
        self.LogoLab.setPixmap(LogoLab_p)
        self.LogoLab.setScaledContents(True)
        #self.LogoLab.setMaximumHeight(40)
        #self.LogoLab.setMinimumHeight(20)'''
        self.TopLabP = self.TopLab.height() + self.y()


        self.advertisementLab = QLabel(self.homeBox)
        self.advertisementLab.setGeometry(0, self.TopLab.height(), self.width(), int(self.width() * 0.45))
        advertisementLab_p = QPixmap()
        advertisementLab_p.loadFromData(self.TopPoster[0])
        self.advertisementLab.setPixmap(advertisementLab_p)
        self.advertisementLab.setScaledContents(True)
        self.data = 30
        self.load(self.data)

    def resizeEvent(self, event):
        data = self.data

        self.TopLab.resize(self.width(), 60)
        #self.LogoLab.resize(140,60)

        '''self.TopLab.resize(self.width(), int(self.height() * 0.08))
        self.LogoLab.resize(int(self.height() * 0.08), int(self.height() * 0.08))'''
        self.advertisementLab.resize(self.width(), int(self.width() * 0.45))
        self.advertisementLab.move(0, self.TopLabP - self.TopLab.height() + self.TopLab.height())


        self.Lab.move(0, self.advertisementLab.height() + self.advertisementLab.y() - self.Lab.height() + 28)
        self.Lab.resize(self.width(), 30)
        self.TopLabP = self.TopLab.height()

        if self.width() >= 600:
            a = int((self.width() - 20) / 3)
            b = 0
            c = self.Lab.y() + self.Lab.height()
            d = 1
            i = 0
            for img in self.spiderLogo:
                if d <= 3:
                    pass
                elif int(a * 0.2) >= 52:
                    c = c + int(a * 0.2) + 2
                    print('c:' + str(c))
                    d = 1
                    b = 0
                else:
                    c = c + 55
                    print('c:' + str(c))
                    d = 1
                    b = 0
                exec('self.sourceG%s.move(%s,%s+3)' % (i, b, c))
                exec('self.sourceG%s.resize(%s,%s)' % (i, a, int(a * 0.2)))
                exec('self.sourceG%s.setFixedHeight(52)' % i)
                b = b + a + 10
                d = d + 1
                exec('self.sourceG = self.sourceG%s' % i)
                if self.sourceG.y() + self.sourceG.height() >= self.homeBox.height():
                    self.homeBox.resize(self.homeBox.width(), self.homeBox.height() + 52)
                exec('self.tp%s.setGeometry(0,0,self.sourceG%s.width(),self.sourceG%s.height())' % (i, i, i))
                exec('self.tp%s.setScaledContents(True)' % i)
                i = i + 1

        elif self.width() >= 550:
                a = int((self.width() - 20) / 2)
                b = 0
                c = self.Lab.y() + self.Lab.height() + 10
                d = 1
                i = 0
                for img in self.spiderLogo:
                    if d <= 2:
                        pass
                    elif int(a * 0.2) >= 52:
                        c = c + int(a * 0.2) + 5
                        d = 1
                        b = 0
                    else:
                        c = c + 57
                        d = 1
                        b = 0
                    exec('self.sourceG%s.move(%s,%s)' % (i, b, c))
                    exec('self.sourceG%s.resize(%s,%s)' % (i, a, int(a * 0.2)))
                    b = b + a + 10
                    d = d + 1
                    exec('self.sourceG = self.sourceG%s'%i)
                    if self.sourceG.y() + self.sourceG.height()>= self.homeBox.height():
                        self.homeBox.resize(self.homeBox.width(),self.homeBox.height()+52)
                    exec('self.tp%s.setGeometry(0,0,self.sourceG%s.width(),self.sourceG%s.height())' % (i, i, i))
                    exec('self.tp%s.setScaledContents(True)' % i)
                    i = i + 1
        else:
            a = self.width()
            b = 0
            c = self.Lab.y() + self.Lab.height() + 10
            i = 0
            for img in self.spiderLogo:
                if int(a * 0.2) >= 52:
                    b = 0
                else:
                    b = 0
                exec('self.sourceG%s.move(%s,%s)' % (i, b, c))
                exec('self.sourceG%s.resize(%s,%s)' % (i, a, int(a * 0.2)))
                c = c + 57
                exec('self.sourceG = self.sourceG%s' % i)
                if self.sourceG.y() + self.sourceG.height()>= self.homeBox.height():
                    self.homeBox.resize(self.homeBox.width(),self.homeBox.height()+52)
                exec('self.tp%s.setGeometry(0,0,self.sourceG%s.width(),self.sourceG%s.height())' % (i, i, i))
                exec('self.tp%s.setScaledContents(True)' % i)

    def load(self, data):
        import sqlite3
        self.Lab = QLabel(self.homeBox)
        self.Lab.setGeometry(0, self.advertisementLab.height() + self.advertisementLab.y(), self.width(), 30)
        self.Lab.setText('来源')
        if self.width() >= 600:
            a = int((self.width() - 20) / 3)
            b = 0
            c = self.Lab.y() + self.Lab.height() + 10
            d = 1
            i = 0
            for img in self.spiderLogo:
                if d <= 3:
                    pass
                else:
                    c = c + int(a * 0.2) + 5
                    d = 1
                    b = 0
                exec('self.sourceG%s = QGroupBox(self.homeBox)' % i)
                exec('self.sourceG%s.setGeometry(%s,%s,%s,%s)' % (i, b, c, a, int(a * 0.2)))
                exec('self.sourceG%s.setFixedHeight(52)' % i)
                b = b + a + 10
                d = d + 1
                exec('if self.sourceG%s.y() + self.sourceG%s.height()>= self.homeBox.height():\n                            self.homeBox.resize(self.homeBox.width(),self.homeBox.height()+52)\n                            print(self.homeBox.height())' % (i, i))
                p = QPixmap()
                p.loadFromData(img)
                exec('self.tp%s = QLabel(self.sourceG%s)' % (i, i))
                exec('self.tp%s.setGeometry(0,0,self.sourceG%s.width(),self.sourceG%s.height())' % (i, i, i))
                exec('self.tp%s.setPixmap(p)' % i)
                exec('self.tp%s.setScaledContents(True)' % i)
                i = i + 1
