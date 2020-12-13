'''自定义组件'''

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
    '''
    标题栏组件，继承自QGroupBox

    :arg
    window 父组件对象，实例化后需要传入
    '''
    def __init__(self, parent=None):
        super(titleBar, self).__init__(parent)

        self.window = QtWidgets #父组件对象，实例化后需要传入
        self.get_res() #获取图片资源
        self.UI()#绘制标题栏

    def get_res(self):
        '''
        :arg
        information=[[数据名称],[所在数据库],]

        :return:
        result = []
        '''
        res = rescource()
        res.information = [['logo', 'search', 'searchBackground', 'setting', 'minimize', 'FullScreen', 'close'],['sys', 'sys', 'sys', 'sys', 'sys', 'sys', 'sys']]
        res.initialization()
        self.logo = res.result[0]
        self.search = res.result[1]
        self.searchBackground = res.result[2]
        self.setting = res.result[3]
        self.minimizeApp = res.result[4]
        self.FullScreen = res.result[5]
        self.closeApp = res.result[6]
        res.close()


    def UI(self):

        #添加一个label作为标题栏的背景将其充满
        self.backLab = QtWidgets.QLabel(self)
        self.backLab.setGeometry(0, 0, self.width(), self.height())
        self.backLab.setStyleSheet('background-color:#FF6666')

        #添加logo，组件继承QLabel
        self.LogoLab = QLabel(self)
        self.LogoLab.setGeometry(15, 0, 120, self.height())
        LogoLab_p = QPixmap()
        LogoLab_p.loadFromData(self.logo)
        self.LogoLab.setPixmap(LogoLab_p)
        self.LogoLab.setScaledContents(True)

        # 添加搜索按钮，组件继承自定义可点击的clickLabel
        self.searchButton = clickLabel(self)
        self.searchButton.function = self.closeEvent
        self.searchButton.setGeometry(int(3 * self.height()), int(self.height() * 0.2), int(self.height() * 0.6),int(self.height() * 0.6))
        #加载图片
        searchButton_p = QPixmap()
        searchButton_p.loadFromData(self.search)
        self.searchButton.setPixmap(searchButton_p)
        self.searchButton.setScaledContents(True)

        # 添加搜索框背景label，组件继承自定义可点击的clickLabel
        self.searchBackLab = clickLabel(self)
        # self.searchBackLab.function = self.closeEvent
        self.searchBackLab.setGeometry(int(3 * self.height()), int(self.height() * 0.2), int(self.height() * 0.6),int(self.height() * 0.6))
        #加载图片
        searchBackLab_p = QPixmap()
        searchBackLab_p.loadFromData(self.searchBackground)
        self.searchBackLab.setPixmap(searchBackLab_p)
        self.searchBackLab.setScaledContents(True)

        # 添加设置按钮，组件继承自定义可点击的clickLabel
        self.settingButton = clickLabel(self)
        self.settingButton.function = self.closeEvent
        self.settingButton.setGeometry(int(self.width() - 4 * self.height() * 0.5), int(self.height() * 0.25),int(self.height() * 0.5), int(self.height() * 0.5))
        #加载图片
        settingButton_p = QPixmap()
        settingButton_p.loadFromData(self.setting)
        self.settingButton.setPixmap(settingButton_p)
        self.settingButton.setScaledContents(True)

        # 添加窗口最小化按钮，组件继承自定义可点击的clickLabel
        self.minimizeWindow = clickLabel(self)
        self.minimizeWindow.function = self.closeEvent
        self.minimizeWindow.setGeometry(int(self.width() - 3 * self.height() * 0.5), int(self.height() * 0.25),int(self.height() * 0.5), int(self.height() * 0.5))
        #加载图片
        minimizeWindow_p = QPixmap()
        minimizeWindow_p.loadFromData(self.minimizeApp)
        self.minimizeWindow.setPixmap(minimizeWindow_p)
        self.minimizeWindow.setScaledContents(True)


        # 添加窗口最大化按钮，组件继承自定义可点击的clickLabel
        self.setMaxWindow = clickLabel(self)
        self.setMaxWindow.function = self.windowMax()
        self.setMaxWindow.setGeometry(int(self.width()-2*self.height()*0.5), int(self.height()*0.25), int(self.height()*0.5), int(self.height()*0.5))
        # 加载图片
        setMaxWindow_p = QPixmap()
        setMaxWindow_p.loadFromData(self.FullScreen)
        self.setMaxWindow.setPixmap(setMaxWindow_p)
        self.setMaxWindow.setScaledContents(True)

        # 添加窗口关闭按钮，组件继承自定义可点击的clickLabel
        self.closeWindow = clickLabel(self)
        self.closeWindow.function = self.closeEvent
        self.closeWindow.setGeometry(int(self.width()-self.height()*0.5), int(self.height()*0.25), int(self.height()*0.5), int(self.height()*0.5))
        # 加载图片
        closeWindow_p = QPixmap()
        closeWindow_p.loadFromData(self.closeApp)
        self.closeWindow.setPixmap(closeWindow_p)
        self.closeWindow.setScaledContents(True)



    def resizeEvent(self, event):
        '''
        重写大小改变事件，在标题栏大小变化时同步其中子组件大小
        :param event:
        :return:
        '''
        self.backLab.resize(self.width(), self.height())
        self.LogoLab.resize(120, self.height())
        self.setMaxWindow.setGeometry(int(self.width()-2*self.height()*0.5), int(self.height()*0.25), int(self.height()*0.5), int(self.height()*0.5))
        self.closeWindow.setGeometry(int(self.width()-self.height()*0.5), int(self.height()*0.25), int(self.height()*0.5), int(self.height()*0.5))
        self.minimizeWindow.setGeometry(int(self.width() - 3 * self.height() * 0.5), int(self.height() * 0.25),int(self.height() * 0.5), int(self.height() * 0.5))
        self.searchButton.setGeometry(int(3 * self.height()),int(self.height()*0.2), int(self.height()*0.6),int(self.height()*0.6))
        self.searchBackLab.setGeometry(int(3.3 * self.height()), int(self.height() * 0.2), int(self.height() * 4),int(self.height() * 0.6))
        self.settingButton.setGeometry(int(self.width() - 4 * self.height() * 0.5), int(self.height() * 0.25),
                                       int(self.height() * 0.5), int(self.height() * 0.5))


    '''
    实现长按拖动标题栏移动窗口功能
    
    '''

    def mousePressEvent(self, event):
        '''
        重写鼠标左键按下事件
        :param event:
        m_flag = boolean 为True 时窗口随鼠标移动
        windows 窗口对象
        :return:
        '''
        try:
            if event.buttons() == QtCore.Qt.LeftButton:  # 左键按下
                self.m_flag = True
                self.m_Position = event.globalPos() - self.window.pos()  # 获取鼠标相对窗口的位置
                event.accept()
                self.setCursor(QtCore.Qt.SizeAllCursor)  # 更改鼠标图标
        except Exception as e:
            print(e)

    def mouseMoveEvent(self, QMouseEvent):
        '''
        重写鼠标移动事件
        :param QMouseEvent:
        :return:
        '''
        if QtCore.Qt.LeftButton and self.m_flag:
            self.window.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        '''
        重写鼠标左键弹起事件
        :param QMouseEvent:
        :return:
        '''
        self.m_flag = False
        self.setCursor(QtCore.Qt.ArrowCursor)

    def windowMax(self):
        pass
        #setWindowState(state)
        #self.window

class clickLabel(QtWidgets.QLabel):
    '''
    自定义可点击的label组件
    标签被点击时触发 self.function 事件
    '''

    def __init__(self, parent=None):
        super(clickLabel, self).__init__(parent)

    def mousePressEvent(self, event):
        '''
        重写标签的被点击事件
        :param event:
        :return:
        '''
        try:
            if event.buttons() == QtCore.Qt.LeftButton:  # 左键按下
                pass
                self.function()
        except Exception as e:
            print(e)

class scrollBox(QGroupBox):
    '''自定义滚动组件框'''
    def __init__(self, parent=None):
        super(scrollBox, self).__init__(parent)
        self.window = QtWidgets

    def wheelEvent(self, event):
        UnitLength = 40  # 每次滚动的像素
        angle = event.angleDelta() / 8  # 返回QPoint对象，为滚轮转过的数值，单位为1/8度
        angleY = angle.y()  # 竖直滚过的距离
        if angleY > 0:
            if self.y() <= 60:#
                if self.y() + UnitLength <= 60:
                    self.move(0, self.y() + UnitLength)
                else:
                    self.move(0, 60)
            else:
                pass
        else:  # 向下滚
            if self.height() + self.y() > self.window.height() - 10:
                self.move(0, self.y() - UnitLength)
            else:
                pass
                # print('到底了！')
            # print("鼠标滚轮下滚")

class sourceListBox(QGroupBox):
    def __init__(self, parent=None):
        super(scrollBox, self).__init__(parent)
        self.window = QtWidgets

    def UI(self):
        pass

    def load(self):
        data = self.data
