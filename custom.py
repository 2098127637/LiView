'''自定义的标题栏类继承自QLabel'''

from PyQt5.Qt import *
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget
import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QGroupBox
from PyQt5.QtWidgets import QFrame
from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QWidget, QToolTip, QDesktopWidget, QMessageBox, QTextEdit, QLabel, QPushButton, \
    QApplication, QMainWindow, QAction, qApp, QHBoxLayout, QVBoxLayout, QGridLayout, QLineEdit
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtGui import QPixmap, QImage, QPalette
from PyQt5.QtCore import QCoreApplication
from resources import rescource


class titleBar(QGroupBox):
    def __init__(self, parent=None):
        super(titleBar, self).__init__(parent)

        self.window = QtWidgets
        res= rescource()
        res.information = [['logo','search','searchBackground','setting','minimize','FullScreen','close'],['sys','sys','sys','sys','sys','sys','sys']]
        res.initialization()
        self.logo = res.result[0]
        self.search = res.result[1]
        self.searchBackground = res.result[2]
        self.setting = res.result[3]
        self.minimizeApp = res.result[4]
        self.FullScreen = res.result[5]
        self.closeApp = res.result[6]
        res.close()


        self.UI()


    def UI(self):
        self.backLab = QtWidgets.QLabel(self)
        self.backLab.setGeometry(0, 0, self.width(), self.height())
        self.backLab.setStyleSheet('background-color:#FF6666')

        self.LogoLab = QLabel(self)
        self.LogoLab.setGeometry(15, 0, 120, self.height())
        LogoLab_p = QPixmap()
        LogoLab_p.loadFromData(self.logo)
        self.LogoLab.setPixmap(LogoLab_p)
        self.LogoLab.setScaledContents(True)

        self.searchButton = clickLabel(self)
        self.searchButton.function = self.closeEvent
        self.searchButton.setGeometry(int(3 * self.height()), int(self.height() * 0.2), int(self.height() * 0.6),
                                      int(self.height() * 0.6))
        searchButton_p = QPixmap()
        searchButton_p.loadFromData(self.search)
        self.searchButton.setPixmap(searchButton_p)
        self.searchButton.setScaledContents(True)

        self.searchBackLab = clickLabel(self)
        # self.searchBackLab.function = self.closeEvent
        self.searchBackLab.setGeometry(int(3 * self.height()), int(self.height() * 0.2), int(self.height() * 0.6),
                                       int(self.height() * 0.6))
        searchBackLab_p = QPixmap()
        searchBackLab_p.loadFromData(self.searchBackground)
        self.searchBackLab.setPixmap(searchBackLab_p)
        self.searchBackLab.setScaledContents(True)

        self.settingButton = clickLabel(self)
        self.settingButton.function = self.closeEvent
        self.settingButton.setGeometry(int(self.width() - 4 * self.height() * 0.5), int(self.height() * 0.25),
                                       int(self.height() * 0.5), int(self.height() * 0.5))
        settingButton_p = QPixmap()
        settingButton_p.loadFromData(self.setting)
        self.settingButton.setPixmap(settingButton_p)
        self.settingButton.setScaledContents(True)

        self.minimizeWindow = clickLabel(self)
        self.minimizeWindow.function = self.closeEvent
        self.minimizeWindow.setGeometry(int(self.width() - 3 * self.height() * 0.5), int(self.height() * 0.25),
                                        int(self.height() * 0.5), int(self.height() * 0.5))
        minimizeWindow_p = QPixmap()
        minimizeWindow_p.loadFromData(self.minimizeApp)
        self.minimizeWindow.setPixmap(minimizeWindow_p)
        self.minimizeWindow.setScaledContents(True)


        self.setMaxWindow = clickLabel(self)
        self.setMaxWindow.function = self.windowMax()
        self.setMaxWindow.setGeometry(int(self.width()-2*self.height()*0.5), int(self.height()*0.25), int(self.height()*0.5), int(self.height()*0.5))
        setMaxWindow_p = QPixmap()
        setMaxWindow_p.loadFromData(self.FullScreen)
        self.setMaxWindow.setPixmap(setMaxWindow_p)
        self.setMaxWindow.setScaledContents(True)

        self.closeWindow = clickLabel(self)
        self.closeWindow.function = self.closeEvent
        self.closeWindow.setGeometry(int(self.width()-self.height()*0.5), int(self.height()*0.25), int(self.height()*0.5), int(self.height()*0.5))
        closeWindow_p = QPixmap()
        closeWindow_p.loadFromData(self.closeApp)
        self.closeWindow.setPixmap(closeWindow_p)
        self.closeWindow.setScaledContents(True)



    def resizeEvent(self, event):
        self.backLab.resize(self.width(), self.height())
        self.LogoLab.resize(120, self.height())
        self.setMaxWindow.setGeometry(int(self.width()-2*self.height()*0.5), int(self.height()*0.25), int(self.height()*0.5), int(self.height()*0.5))
        self.closeWindow.setGeometry(int(self.width()-self.height()*0.5), int(self.height()*0.25), int(self.height()*0.5), int(self.height()*0.5))
        self.minimizeWindow.setGeometry(int(self.width() - 3 * self.height() * 0.5), int(self.height() * 0.25),int(self.height() * 0.5), int(self.height() * 0.5))
        self.searchButton.setGeometry(int(3 * self.height()),int(self.height()*0.2), int(self.height()*0.6),int(self.height()*0.6))
        self.searchBackLab.setGeometry(int(3.3 * self.height()), int(self.height() * 0.2), int(self.height() * 4),int(self.height() * 0.6))
        self.settingButton.setGeometry(int(self.width() - 4 * self.height() * 0.5), int(self.height() * 0.25),
                                       int(self.height() * 0.5), int(self.height() * 0.5))

    def mousePressEvent(self, event):
        try:
            if event.buttons() == QtCore.Qt.LeftButton:  # 左键按下
                self.m_flag = True
                self.m_Position = event.globalPos() - self.window.pos()  # 获取鼠标相对窗口的位置
                event.accept()
                self.setCursor(QtCore.Qt.SizeAllCursor)  # 更改鼠标图标
        except Exception as e:
            print(e)

    def mouseMoveEvent(self, QMouseEvent):
        if QtCore.Qt.LeftButton and self.m_flag:
            self.window.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QtCore.Qt.ArrowCursor)

    def windowMax(self):
        pass
        #setWindowState(state)
        #self.window

class clickLabel(QtWidgets.QLabel):

    def __init__(self, parent=None):
        super(clickLabel, self).__init__(parent)

    def mousePressEvent(self, event):
        try:
            if event.buttons() == QtCore.Qt.LeftButton:  # 左键按下
                pass
                self.function()
        except Exception as e:
            print(e)