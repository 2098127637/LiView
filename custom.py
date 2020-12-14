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

    def load(self,listpoint):
        #data = self.data
        a = int((self.width() - 20) / 3)    #宽
        b = 0   #x方向距离
        c = listpoint#self.Lab.y() + self.Lab.height() + 10   #y方向上的距离
        d = 1   #所在行数
        i = 0   #生成组件的编号
        for img in self.data:
            if d <= 3:
                pass
            else:
                c = c + int(a * 0.2) + 5
                d = 1
                b = 0
            exec('self.sourceG%s = QGroupBox(self)' % i)
            exec('self.sourceG%s.setGeometry(%s,%s,%s,%s)' % (i, b, c, a, int(a * 0.2)))
            exec('self.sourceG%s.setFixedHeight(52)' % i)
            b = b + a + 10
            d = d + 1
            exec('''if self.sourceG%s.y() + self.sourceG%s.height()>= self.height():
                                        self.resize(self.width(),self.height()+52)''' % (i, i))
            '''p = QPixmap()
            p.loadFromData(img)
            exec('self.tp%s = QLabel(self.sourceG%s)' % (i, i))
            exec('self.tp%s.setGeometry(0,0,self.sourceG%s.width(),self.sourceG%s.height())' % (i, i, i))
            exec('self.tp%s.setPixmap(p)' % i)
            exec('self.tp%s.setScaledContents(True)' % i)'''
            i = i + 1
    moveDown = 0

    def wheelEvent(self, event):
        UnitLength = 40  # 每次滚动的像素
        angle = event.angleDelta() / 8  # 返回QPoint对象，为滚轮转过的数值，单位为1/8度
        angleY = angle.y()  # 竖直滚过的距离
        if angleY > 0:
            if self.y() <= 60:#
                if self.y() + UnitLength <= 60:
                    self.move(0, self.y() + UnitLength)
                    self.moveDown = self.moveDown - 40
                else:
                    self.move(0, 60)
                    self.moveDown - 40
                    #有一点小瑕疵，可能多减那么一点点
            else:
                pass
        else:  # 向下滚
            if self.height() + self.y() > self.window.height() - 10 and self.moveDown < self.lenth:
                self.move(0, self.y() - UnitLength)
                self.moveDown = self.moveDown + 40
                #print(self.moveDown)
            else:
                pass
                # print('到底了！')
            # print("鼠标滚轮下滚")

class sourceListBox(QGroupBox):
    '''
    资源列表框
    '''
    def __init__(self, parent=None):
        super(sourceListBox, self).__init__(parent)
        self.window = QtWidgets

    def UI(self):
        pass

    def load(self,data,colorPicture,authorLogo,openLogo):
        self.columnsNum = 4
        self.boxHeight = 150
        a = int((self.window.width() - 20) / self.columnsNum)  # 宽
        b = 0  # x方向距离
        c = 0  # self.Lab.y() + self.Lab.height() + 10   #y方向上的距离
        d = 1  # 所在行数
        i = 0  # 生成组件的编号
        for img in data:
            if d <= self.columnsNum:
                pass
            else:
                c = c + self.boxHeight
                d = 1
                b = 0
            exec('self.sourceG%s = QGroupBox(self)'%i)  #为每一个来源创建box
            exec('self.a= self.sourceG%s'%i)
            #self.a.setStyleSheet('background-color:#FF6666')

            self.a.setGeometry(b,c,a,self.boxHeight)
            self.a.setFixedHeight(self.boxHeight)
            exec('self.lab_logo%s = clickLabel(self.a)'%i)   #来源网站的logo图标
            exec('self.replace_logo = self.lab_logo%s'%i)
            self.replace_logo.setGeometry(int(self.a.height()*0.7),int(self.a.height() * 0.7),int(self.a.width()-self.a.height()*0.7),int(self.a.height()*0.3))
            replace_logoP = QPixmap()
            replace_logoP.loadFromData(img[0])
            self.replace_logo.setPixmap(replace_logoP)
            self.replace_logo.setScaledContents(True)


            exec('self.lab_color%s = clickLabel(self.a)' % i)    #来源网站彩图
            exec('self.replace_color = self.lab_color%s' % i)
            self.replace_color.setGeometry(0,5,int(self.a.height()*0.7),self.a.height())
            replace_colorP = QPixmap()
            replace_colorP.loadFromData(colorPicture[i][0])
            self.replace_color.setPixmap(replace_colorP)
            self.replace_color.setScaledContents(True)


            exec('self.lab_authorlogo%s = clickLabel(self.a)' % i)    #来源作者图标
            exec('self.replace_authorlogo = self.lab_authorlogo%s' % i)
            self.replace_authorlogo.setGeometry(int(self.a.height()*0.7),0, int(self.a.height() * 0.4),int(self.a.height() * 0.4))
            replace_authorlogoP = QPixmap()
            replace_authorlogoP.loadFromData(authorLogo[i][0])
            self.replace_authorlogo.setPixmap(replace_authorlogoP)
            self.replace_authorlogo.setScaledContents(True)

            exec('self.lab_openlogo%s = clickLabel(self.a)' % i)  # 打开图标
            exec('self.replace_openlogo = self.lab_openlogo%s' % i)
            self.replace_openlogo.setGeometry(int(self.a.width()*0.85), int(self.a.height()*0.1), int(self.a.height() * 0.2),
                                                int(self.a.height() * 0.6))
            replace_openlogoP = QPixmap()
            replace_openlogoP.loadFromData(openLogo[0][0])
            self.replace_openlogo.setPixmap(replace_openlogoP)
            self.replace_openlogo.setScaledContents(True)
            ''' p = QPixmap()
            print(img)
            p.loadFromData(img)
            self.b.setPixmap(p)
            self.b.setScaledContents(True)'''


            b = b + a + 10
            d = d + 1
            i = i+1
            self.resize(self.window.width(), self.boxHeight * (i + 2))
        if i <= self.columnsNum:
            self.lastHight = 200
        elif i <= self.columnsNum * 2:
            self.lastHight = 2 * self.boxHeight
        else:
            self.lastHight = c + self.boxHeight



