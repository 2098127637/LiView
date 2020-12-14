"""大纲页面"""
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget
import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QToolTip, QDesktopWidget, QMessageBox, QTextEdit, QLabel, QPushButton, QApplication, QMainWindow, QAction, qApp, QHBoxLayout, QVBoxLayout, QGridLayout, QLineEdit
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtGui import QPixmap, QImage, QPalette
from PyQt5.QtCore import QCoreApplication
from newWindow import Ui_MainWindow

class synopsisPage(Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.synopsisBox = self.synopsisBox
        self.synopsisUI()

    def synopsisUI(self):
        self.homeBox.setGeometry(0,60,QApplication.desktop().width(), QApplication.desktop().height())
        self.synopsisBox.setStyleSheet('background-color:#FF6666')

    def synopsisInitialization(self,SourceID):
        print(SourceID)