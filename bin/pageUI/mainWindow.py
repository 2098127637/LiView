'''自定义窗口'''
import requests, sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QIcon

#从commponent目录下加载自定义组件
import sys
sys.path.append('..\component')

from titleBar import titleBar
from home import home
from synopsis import synopsis

class Ui_MainWindow(QtWidgets.QMainWindow):
    #创建新窗口

    def __init__(self):
        super().__init__()
        self.log()
        self._setUI()
        self.pageList = ['home','synopsis']
        self._creatPage(self.pageList)

    def log(self):
        # 日志初始化
        import logging
        self.logging = logging
        LOG_FORMAT = "###### %(asctime)s - %(levelname)s \n%(message)s"
        self.logging.basicConfig(filename='../../log/log.md',level=logging.DEBUG, format=LOG_FORMAT)
        self.logging.debug("> 日志初始化完成开始输出日志.")

    def _setUI(self):

        self.logging.debug("> mainWindow 开始")
        self.logging.debug("### mainWindow UI开始初始化")
        self.logging.debug("* 创建窗口")
        #固有属性定义

        MainWindow = self
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)  # 隐藏窗口边框
        MainWindow.resize(1025, 670)#更改窗口大小
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName('centralwidget')
        MainWindow.setCentralWidget(self.centralwidget)

        #最小宽高
        self.setMinimumHeight(600)
        self.setMinimumWidth(400)

        self.logging.debug("* 设置图标")
        #设置图标
        self.setWindowIcon(QIcon('logo.ico'))
        import ctypes
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")#任务栏图标修改

        self.logging.debug("* 实例化属于窗口本身的组件")
        self.logging.debug("* 实例化创建标题栏")
        #实例化属于窗口本身的组件
        #标题栏、

        # 添加标题栏
        self.TopLab = titleBar(self.centralwidget)
        self.TopLab.ParentComponent = self  # 传入父组件对象
        self.TopLab.__ini__()
        self.TopLab.setGeometry(0, 0, self.width(), 60)

    def _creatPage(self, list):

        self.logging.debug("* 创建页面")

        #按照self.pagelist中项+Box创建两个scrollBox（scrollBox在custom.py中定义继承自groupBox）
        self.homePage = home(self)
        self.homePage.ParentComponent = self
        self.homePage.move(0,60)
        self.homePage.__int__()
        self.pageTage = list[0]

        self.synopsisPage = synopsis(self)
        self.synopsisPage.ParentComponent = self
        self.synopsisPage.move(0, 60)
        self.synopsisPage.__int__()

        self.logging.debug("* 完成！~~创建页面")

    #页面切换函数
    def PageSwitching(self):
        '''
        切换页面
        :return:
        '''
        try:
            for i in self.pageList:
                if i != self.pageTage:
                    print('i',i)
                    print('pageTage',self.pageTage)
                    # 页面不是正在显示的页面
                    exec('self.hiddenPage = self.%sPage' % i)
                    self.hiddenPage.setVisible(False)
                    print('hiddenPage', self.hiddenPage)
                    self.hiddenPage.lower()
                else:
                    # 要显示页面
                    exec('self.displayedPage = self.%sPage' % self.pageTage)
                    print('self.displayedPage', self.displayedPage)
                    self.displayedPage.setVisible(True)
                    self.displayedPage.raise_()
                    self.TopLab.raise_()
            self.TopLab.raise_()# 标题栏永远是最上层
            QApplication.processEvents()
        except Exception as e:
            print(e)
