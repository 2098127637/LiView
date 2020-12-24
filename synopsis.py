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
from custom import titleBar,sourceListBox,horizontalScrollBox
from resources import rescource

class synopsisPage(Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.synopsisBox = self.synopsisBox
        self.get_res()
        self.synopsisUI()
        res = rescource()
        res.ParentComponent = self  # 绑定本身为res父组件
        res.synopsisPageRes()

    def synopsisUI(self):
        self.synopsisBox.setGeometry(0,60,QApplication.desktop().width(), QApplication.desktop().height())
        #self.synopsisBox.setStyleSheet('background-color:#FF6666')

    def synopsisInitialization(self,ID):
        self.sourceID = ID
        self.typeColumn = horizontalScrollBox(self.synopsisBox)
        self.typeColumn.window = self
        self.typeColumn.move(0,3)

        # 处理json信息
        import json
        # 利用json模块的loads函数将json字符串转为python对象
        typeNameList = json.loads(str(self.novelType[self.sourceID - 1][0]))
        self.typeNmae = typeNameList[0]['typeName']
        self.spiderName = typeNameList[1]['spiderName']

        #获取安装目录
        from configparser import ConfigParser
        cf = ConfigParser()
        f = open('INIT.INI')
        cf.read_file(f)
        InstallationDirectory = cf.get('InstallationDirectory', 'InstallationDirectory')
        self.callSpider(InstallationDirectory + 'userData\\spider\\%s\\call\\%s'%(self.path[self.sourceID-1][0],self.spiderName[self.sourceID-1]+'.py'))

        #添加信息


    def callSpider(self,callName):
        from configparser import ConfigParser
        import win32api
        import sqlite3

        #获取novel.db的位置
        from configparser import ConfigParser
        cf = ConfigParser()
        f = open('INIT.INI')
        cf.read_file(f)
        novelPath = cf.get('db', 'novel')

        #清空表
        conn = sqlite3.connect(novelPath)
        c = conn.cursor()
        c.execute('delete from novelindex;')#清空
        c.execute('update sqlite_sequence SET seq = 0;')#自增索引为零
        conn.commit()#提交更改
        c.close()
        conn.close()

        #调用相应爬虫
        cf = ConfigParser()
        f = open('INIT.INI')
        cf.read_file(f)
        python = cf.get('python', 'python')
        win32api.ShellExecute(0, "open", python,callName, '', 1)



