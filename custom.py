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
        res.name='logo'
        res.table = 'sys'
        res.initialization()
        self.logo = res.result
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

    def resizeEvent(self, event):
        self.backLab.resize(self.width(), self.height())
        self.LogoLab.resize(120, self.height())

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