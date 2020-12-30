#标题栏组件

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

from dataOperation import dataOperation
from clickLabel import clickLabel


class titleBar(QGroupBox):
    '''
    标题栏组件，继承自QGroupBox

    :arg
    window 父组件对象，实例化后需要传入
    '''

    def __init__(self, parent=None):
        super(titleBar, self).__init__(parent)
        self.ParentComponent = QtWidgets
    def __ini__(self):
        self.ParentComponent.logging.debug("> 标题栏开始")
        try:
            self.get_res()  # 获取图片资源
            self.UI()  # 绘制标题栏
        except Exception as e:
            print(e)
            self.ParentComponent.logging.critical('# 标题栏初始化失败！'+str(e))

    def get_res(self):
        '''
        :arg
        information=[[数据名称],[所在数据库],]

        :return:
        result = []
        '''
        self.ParentComponent.logging.debug("* 从数据库获取信息")
        try :
            # 获取标题栏所需的ui元素
            self.res = dataOperation()
            self.res.ParentComponent = self  # 绑定本身为res父组件，
            self.res.call_Label = 'titleBarRes'  # 调用标签

            self.res.threadEnd.connect(self.updateInterface)

            self.ParentComponent.logging.debug("* 开启数据库操作线程")

            self.res.start()
            #import time
            #time.sleep(10)

            self.ParentComponent.logging.debug("* 完成！~~从数据库获取信息")
        except Exception as e:
            print(e)
            self.ParentComponent.logging.critical('# 标题栏从数据库获取信息失败！'+str(e))

    def UI(self):
        #哈，UI线程，更新页面还需要等数据库操作线程返回信号时调用

        self.ParentComponent.logging.debug("* 添加一个label作为标题栏的背景将其充满")
        # 添加一个label作为标题栏的背景将其充满
        self.backLab = QtWidgets.QLabel(self)
        self.backLab.setGeometry(0, 0, self.width(), self.height())
        self.backLab.setStyleSheet('background-color:#FF6666')

        self.ParentComponent.logging.debug("* 添加logo，组件继承QLabel")
        # 添加logo，组件继承QLabel
        self.LogoLab = QLabel(self)
        self.LogoLab.setGeometry(15, 0, 120, self.height())


        self.ParentComponent.logging.debug("* 添加搜索按钮，组件继承自定义可点击的clickLabel")
        # 添加搜索按钮，组件继承自定义可点击的clickLabel
        self.searchButton = clickLabel(self)
        self.searchButton.function = self.closeEvent
        self.searchButton.setGeometry(int(3 * self.height()), int(self.height() * 0.2), int(self.height() * 0.6),
                                      int(self.height() * 0.6))
        # 加载图片



        self.ParentComponent.logging.debug("* 添加搜索框背景label，组件继承自定义可点击的clickLabel")
        # 添加搜索框背景label，组件继承自定义可点击的clickLabel
        self.searchBackLab = clickLabel(self)
        # self.searchBackLab.function = self.closeEvent
        self.searchBackLab.setGeometry(int(3 * self.height()), int(self.height() * 0.2), int(self.height() * 0.6),
                                       int(self.height() * 0.6))
        # 加载图片



        self.ParentComponent.logging.debug("* 添加设置按钮，组件继承自定义可点击的clickLabel")
        # 添加设置按钮，组件继承自定义可点击的clickLabel
        self.settingButton = clickLabel(self)
        self.settingButton.function = self.closeEvent
        self.settingButton.setGeometry(int(self.width() - 4 * self.height() * 0.5), int(self.height() * 0.25),
                                       int(self.height() * 0.5), int(self.height() * 0.5))
        # 加载图片



        self.ParentComponent.logging.debug("* 添加窗口最小化按钮，组件继承自定义可点击的clickLabel")
        # 添加窗口最小化按钮，组件继承自定义可点击的clickLabel
        self.minimizeWindow = clickLabel(self)
        self.minimizeWindow.function = self.closeEvent
        self.minimizeWindow.setGeometry(int(self.width() - 3 * self.height() * 0.5), int(self.height() * 0.25),
                                        int(self.height() * 0.5), int(self.height() * 0.5))
        # 加载图片


        self.ParentComponent.logging.debug("* 添加窗口最大化按钮，组件继承自定义可点击的clickLabel")
        # 添加窗口最大化按钮，组件继承自定义可点击的clickLabel
        self.setMaxWindow = clickLabel(self)
        self.setMaxWindow.setGeometry(int(self.width() - 2 * self.height() * 0.5), int(self.height() * 0.25),
                                      int(self.height() * 0.5), int(self.height() * 0.5))
        # 加载图片




        self.ParentComponent.logging.debug("* 添加窗口关闭按钮，组件继承自定义可点击的clickLabel")
        # 添加窗口关闭按钮，组件继承自定义可点击的clickLabel
        self.closeWindow = clickLabel(self)
        self.closeWindow.function = self.closeEvent
        self.closeWindow.setGeometry(int(self.width() - self.height() * 0.5), int(self.height() * 0.25),
                                     int(self.height() * 0.5), int(self.height() * 0.5))
        # 加载图片

        # self.arg = QCloseEvent
        self.function = self.closeEvent
    def updateInterface(self):
        self.ParentComponent.logging.debug("* 标题栏UI更新--加载图片")

        #页面更新，加载图片

        LogoLab_p = QPixmap()
        LogoLab_p.loadFromData(self.logo[0])
        self.LogoLab.setPixmap(LogoLab_p)
        self.LogoLab.setScaledContents(True)

        searchButton_p = QPixmap()
        searchButton_p.loadFromData(self.search[0])
        self.searchButton.setPixmap(searchButton_p)
        self.searchButton.setScaledContents(True)

        searchBackLab_p = QPixmap()
        searchBackLab_p.loadFromData(self.searchBackground[0])
        self.searchBackLab.setPixmap(searchBackLab_p)
        self.searchBackLab.setScaledContents(True)

        settingButton_p = QPixmap()
        settingButton_p.loadFromData(self.setting[0])
        self.settingButton.setPixmap(settingButton_p)
        self.settingButton.setScaledContents(True)

        minimizeWindow_p = QPixmap()
        minimizeWindow_p.loadFromData(self.minimizeApp[0])
        self.minimizeWindow.setPixmap(minimizeWindow_p)
        self.minimizeWindow.setScaledContents(True)

        setMaxWindow_p = QPixmap()
        setMaxWindow_p.loadFromData(self.FullScreen[0])
        self.setMaxWindow.setPixmap(setMaxWindow_p)
        self.setMaxWindow.setScaledContents(True)

        closeWindow_p = QPixmap()
        closeWindow_p.loadFromData(self.closeApp[0])
        self.closeWindow.setPixmap(closeWindow_p)
        self.closeWindow.setScaledContents(True)




    def closeEvent(self):
        """
        重写closeEvent方法，实现dialog窗体关闭时执行一些代码
        :param event: close()触发的事件
        :return: None
        """
        # 创建一个消息盒子（提示框）
        quitMsgBox = QMessageBox()
        # 设置提示框的标题
        quitMsgBox.setWindowTitle('LiView')
        # 设置提示框的内容
        quitMsgBox.setText('是否退出程序？')
        # 创建两个点击的按钮，修改文本显示内容
        buttonY = QPushButton('退出')
        buttonN = QPushButton('取消')
        # 将两个按钮加到这个消息盒子中去，并指定yes和no的功能
        quitMsgBox.addButton(buttonY, QMessageBox.YesRole)
        quitMsgBox.addButton(buttonN, QMessageBox.NoRole)
        quitMsgBox.exec_()
        # 判断返回值，如果点击的是Yes按钮，我们就关闭组件和应用，否则就忽略关闭事件
        if quitMsgBox.clickedButton() == buttonY:
            QCoreApplication.instance().quit()
            # event.accept()
        else:
            pass

    def resizeEvent(self, event):
        '''
        重写大小改变事件，在标题栏大小变化时同步其中子组件大小
        :param event:
        :return:
        '''
        self.backLab.resize(self.width(), self.height())
        self.LogoLab.resize(120, self.height())
        self.setMaxWindow.setGeometry(int(self.width() - 2 * self.height() * 0.5), int(self.height() * 0.25),
                                      int(self.height() * 0.5), int(self.height() * 0.5))
        self.closeWindow.setGeometry(int(self.width() - self.height() * 0.5), int(self.height() * 0.25),
                                     int(self.height() * 0.5), int(self.height() * 0.5))
        self.minimizeWindow.setGeometry(int(self.width() - 3 * self.height() * 0.5), int(self.height() * 0.25),
                                        int(self.height() * 0.5), int(self.height() * 0.5))
        self.searchButton.setGeometry(int(3 * self.height()), int(self.height() * 0.2), int(self.height() * 0.6),
                                      int(self.height() * 0.6))
        self.searchBackLab.setGeometry(int(3.3 * self.height()), int(self.height() * 0.2), int(self.height() * 4),
                                       int(self.height() * 0.6))
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
                self.m_Position = event.globalPos() - self.ParentComponent.pos()  # 获取鼠标相对窗口的位置
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
            self.ParentComponent.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        '''
        重写鼠标左键弹起事件
        :param QMouseEvent:
        :return:
        '''
        self.m_flag = False
        self.setCursor(QtCore.Qt.ArrowCursor)