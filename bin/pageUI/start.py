'''
self（窗口）的属性注册
'''

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
from PyQt5.QtGui import QPixmap, QImage, QPalette,QMovie
from PyQt5.QtCore import QCoreApplication,Qt
import time
from mainWindow import Ui_MainWindow

#获取数据库数据（子线程）
#获取云端数据（子线程）
#显示页面UI实例化窗口（mainWindow）(主线程)

class mainStart(Ui_MainWindow):
    '''
    继承并调用页面，控制它们的显示与影藏
    '''
    def __init__(self):
        super().__init__()
        self.logging.debug("### mainStart,程序开始")
        self.logging.debug("* 初始化页面显示")
        self.PageSwitching()#初始化页面显示

class SplashScreen(QSplashScreen):
    def __init__(self):
        super(SplashScreen, self).__init__()  #启动程序的图片
        pix = QPixmap('../../img/start.png')
        self.setPixmap(pix)
        self.resize(300,217)

    #效果 fade =1 淡入   fade= 2  淡出，  t sleep 时间 毫秒
    def fadeIut(self):
        #淡出
        self.setWindowOpacity(0)
        t = 0
        while t <= 100:
            newOpacity = self.windowOpacity() + 0.1    #设置淡入
            if newOpacity > 1:
                break
            self.setWindowOpacity(newOpacity)
            self.show()
            t -= 1
            time.sleep(0.04)

        time.sleep(1)
    def fadeOut(self):
        #淡入
        t = 0
        while t <= 100:
            newOpacity = self.windowOpacity() - 0.1        #设置淡出
            if newOpacity < 0:
                break

            self.setWindowOpacity(newOpacity)
            t += 1
            time.sleep(0.04)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    LiView = mainStart()
    LiView.logging.debug("### 程序启动图开始")
    splash = SplashScreen()
    splash.fadeIut()
    app.processEvents()
    LiView.show()
    LiView.logging.debug("### 程序启动图关闭")
    splash.fadeOut()
    splash.finish(LiView)
    LiView.logging.debug("### 删除程序启动图")
    splash.deleteLater()
    LiView.logging.debug("### 关闭程序启动图资源")
    sys.exit(app.exec_())
