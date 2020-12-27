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
from home import homePage
from synopsis import synopsisPage

class CallPage(homePage,synopsisPage):
    '''
    继承并调用页面，控制它们的显示与影藏
    '''
    def __init__(self):
        super().__init__()
        self.PageSwitching()#初始化页面显示

    def PageSwitching(self):
        '''
        切换页面
        :return:
        '''
        for i in self.pageList:
            if i != self.pageTage:
                #页面不是正在显示的页面
                exec('self.hiddenPage = self.%sBox'%i)
                self.hiddenPage.setVisible(False)
                self.hiddenPage.lower()
            else:
                #要显示页面
                exec('self.displayedPage = self.%sBox' % self.pageTage)
                self.displayedPage.setVisible(True)
                self.displayedPage.raise_()
        self.TopLab.raise_() #标题栏永远是最上层


if __name__ == "__main__":
    app = QApplication(sys.argv)
    LiView = CallPage()
    LiView.show()
    sys.exit(app.exec_())


