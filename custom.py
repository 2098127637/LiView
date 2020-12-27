'''自定义一些组件'''

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

#标题栏组件，继承自QGroupBox
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
        res.ParentComponent = self      #绑定本身为res父组件，
        res.titleBarRes()       #获取标题栏所需的ui元素

    def UI(self):

        #添加一个label作为标题栏的背景将其充满
        self.backLab = QtWidgets.QLabel(self)
        self.backLab.setGeometry(0, 0, self.width(), self.height())
        self.backLab.setStyleSheet('background-color:#FF6666')

        #添加logo，组件继承QLabel
        self.LogoLab = QLabel(self)
        self.LogoLab.setGeometry(15, 0, 120, self.height())
        LogoLab_p = QPixmap()
        LogoLab_p.loadFromData(self.logo[0])
        self.LogoLab.setPixmap(LogoLab_p)
        self.LogoLab.setScaledContents(True)

        # 添加搜索按钮，组件继承自定义可点击的clickLabel
        self.searchButton = clickLabel(self)
        self.searchButton.function = self.closeEvent
        self.searchButton.setGeometry(int(3 * self.height()), int(self.height() * 0.2), int(self.height() * 0.6),int(self.height() * 0.6))
        #加载图片
        searchButton_p = QPixmap()
        searchButton_p.loadFromData(self.search[0])
        self.searchButton.setPixmap(searchButton_p)
        self.searchButton.setScaledContents(True)

        # 添加搜索框背景label，组件继承自定义可点击的clickLabel
        self.searchBackLab = clickLabel(self)
        # self.searchBackLab.function = self.closeEvent
        self.searchBackLab.setGeometry(int(3 * self.height()), int(self.height() * 0.2), int(self.height() * 0.6),int(self.height() * 0.6))
        #加载图片
        searchBackLab_p = QPixmap()
        searchBackLab_p.loadFromData(self.searchBackground[0])
        self.searchBackLab.setPixmap(searchBackLab_p)
        self.searchBackLab.setScaledContents(True)

        # 添加设置按钮，组件继承自定义可点击的clickLabel
        self.settingButton = clickLabel(self)
        self.settingButton.function = self.closeEvent
        self.settingButton.setGeometry(int(self.width() - 4 * self.height() * 0.5), int(self.height() * 0.25),int(self.height() * 0.5), int(self.height() * 0.5))
        #加载图片
        settingButton_p = QPixmap()
        settingButton_p.loadFromData(self.setting[0])
        self.settingButton.setPixmap(settingButton_p)
        self.settingButton.setScaledContents(True)

        # 添加窗口最小化按钮，组件继承自定义可点击的clickLabel
        self.minimizeWindow = clickLabel(self)
        self.minimizeWindow.function = self.closeEvent
        self.minimizeWindow.setGeometry(int(self.width() - 3 * self.height() * 0.5), int(self.height() * 0.25),int(self.height() * 0.5), int(self.height() * 0.5))
        #加载图片
        minimizeWindow_p = QPixmap()
        minimizeWindow_p.loadFromData(self.minimizeApp[0])
        self.minimizeWindow.setPixmap(minimizeWindow_p)
        self.minimizeWindow.setScaledContents(True)


        # 添加窗口最大化按钮，组件继承自定义可点击的clickLabel
        self.setMaxWindow = clickLabel(self)
        self.setMaxWindow.function = self.windowMax()
        self.setMaxWindow.setGeometry(int(self.width()-2*self.height()*0.5), int(self.height()*0.25), int(self.height()*0.5), int(self.height()*0.5))
        # 加载图片
        setMaxWindow_p = QPixmap()
        setMaxWindow_p.loadFromData(self.FullScreen[0])
        self.setMaxWindow.setPixmap(setMaxWindow_p)
        self.setMaxWindow.setScaledContents(True)

        # 添加窗口关闭按钮，组件继承自定义可点击的clickLabel
        self.closeWindow = clickLabel(self)
        self.closeWindow.function = self.closeEvent
        self.closeWindow.setGeometry(int(self.width()-self.height()*0.5), int(self.height()*0.25), int(self.height()*0.5), int(self.height()*0.5))
        # 加载图片
        closeWindow_p = QPixmap()
        closeWindow_p.loadFromData(self.closeApp[0])
        self.closeWindow.setPixmap(closeWindow_p)
        self.closeWindow.setScaledContents(True)
        #self.arg = QCloseEvent
        self.function = self.closeEvent

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
            #event.accept()
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


#自定义可点击的label组件
#标签被点击时触发 self.function 事件
class clickLabel(QtWidgets.QLabel):
    '''
    自定义可点击的label组件
    标签被点击时触发 self.function 事件
    '''

    def __init__(self,parent=None):
        super(clickLabel, self).__init__(parent)
        self.arg = ''

    def mousePressEvent(self, event):
        '''
        重写标签的被点击事件
        :param event:
        :return:
        '''
        try:
            if event.buttons() == QtCore.Qt.LeftButton:  # 左键按下
                if self.arg == '':
                    self.function()
                else:
                    self.function(self.arg)
        except Exception as e:
            print(e)

#自定义滚动组件框
class scrollBox(QGroupBox):
    '''自定义滚动组件框'''
    def __init__(self, parent=None):
        super(scrollBox, self).__init__(parent)
        self.window = QtWidgets


    moveDown = 0

    def wheelEvent(self, event):
        UnitLength = 40  # 每次滚动的像素
        angle = event.angleDelta() / 8  # 返回QPoint对象，为滚轮转过的数值，单位为1/8度
        angleY = angle.y()  # 竖直滚过的距离
        if self.window.pageTage == 'home':
            #homeBox显示时滚动条件
            if angleY > 0:
                if self.y() <= 60:  #
                    if self.y() + UnitLength <= 60:
                        self.move(0, self.y() + UnitLength)
                        self.moveDown = self.moveDown - 40
                    else:
                        self.move(0, 60)
                        self.moveDown - 40
                        # 有一点小瑕疵，可能多减那么一点点
                else:
                    pass
            else:  # 向下滚
                if self.height() + self.y() > self.window.height() - 10 and self.moveDown < self.lenth:
                    self.move(0, self.y() - UnitLength)
                    self.moveDown = self.moveDown + 40
                    # print(self.moveDown)
                else:
                    pass
        elif self.window.pageTage == 'synopsis':
            #synopsis显示时滚动条件
            if angleY > 0:
                if self.y() <= 60:  #
                    if self.y() + UnitLength <= 60:
                        self.move(0, self.y() + UnitLength)
                        self.moveDown = self.moveDown - 40
                    else:
                        self.move(0, 60)
                        self.moveDown - 40
                        # 有一点小瑕疵，可能多减那么一点点
                else:
                    pass
            else:  # 向下滚
                if self.height() + self.y() > self.window.height() - 10 and self.moveDown < self.lenth:
                    self.move(0, self.y() - UnitLength)
                    self.moveDown = self.moveDown + 40
                    # print(self.moveDown)
                else:
                    pass

#资源列表框
class sourceListBox(QGroupBox):
    '''
    资源列表框
    '''

    def __init__(self, parent=None):
        super(sourceListBox, self).__init__(parent)
        self.window = QtWidgets
        self.get_res()

    def UI(self):
        pass

    def get_res(self):
        res = rescource()
        res.ParentComponent = self  # 绑定本身为res父组件
        res.sourceListBoxRes()  # 获取标题栏所需的ui元素


    def load(self):
        self.columnsNum = 4
        self.boxHeight = 150
        a = int((self.window.width() - 20) / self.columnsNum)  # 宽
        b = 0  # x方向距离
        c = 0  # self.Lab.y() + self.Lab.height() + 10   #y方向上的距离
        d = 1  # 所在行数
        i = 0  # 生成组件的编号
        for img in self.spiderLogo:
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
            replace_colorP.loadFromData(self.spiderPicture[i][0])
            self.replace_color.setPixmap(replace_colorP)
            self.replace_color.setScaledContents(True)


            exec('self.lab_authorlogo%s = clickLabel(self.a)' % i)    #来源作者图标
            exec('self.replace_authorlogo = self.lab_authorlogo%s' % i)
            self.replace_authorlogo.setGeometry(int(self.a.height()*0.7),0, int(self.a.height() * 0.4),int(self.a.height() * 0.4))
            replace_authorlogoP = QPixmap()
            replace_authorlogoP.loadFromData(self.authorLogo[i][0])
            self.replace_authorlogo.setPixmap(replace_authorlogoP)
            self.replace_authorlogo.setScaledContents(True)

            exec('self.lab_openlogo%s = clickLabel(self.a)' % i)  # 打开图标
            exec('self.replace_openlogo = self.lab_openlogo%s' % i)
            self.replace_openlogo.setGeometry(int(self.a.width()*0.85), int(self.a.height()*0.1), int(self.a.height() * 0.2),
                                                int(self.a.height() * 0.6))
            self.replace_openlogo.function = self.openSource  #绑定事件
            self.replace_openlogo.arg = i+1   #绑定参数,即所点击来源在数据库中的id，使synopis页面能够进行初始化加载
            replace_openlogoP = QPixmap()
            replace_openlogoP.loadFromData(self.openLogo[0][0])
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


    def openSource(self,id):
        #小说ID
        self.window.novelId = 0

        self.window.synopsisInitialization(id)
        self.window.pageTage = 'synopsis'
        self.window.PageSwitching()
        self.dataThread = myThread()
        #self.a.breakSignal.connect(self.updateInterface)

        self.dataThread.breakSignal.connect(self.updateInterface)
        self.dataThread.arg = id
        self.dataThread.start()
        #self.a.function = self.qiehuan

    def updateInterface(self):
        #更新界面
        print('更新界面')
        try:
            if len(self.dataThread.novelName) >= 49:
                try:
                    # 删除loading.png
                    import sip
                    sip.delete(self.window.novelListBox.loadingLab)
                    sip.delete(self.window.novelListBox.loadingBackgroundLab)
                    # print('传入总数:')
                    # print(len(self.dataThread.novelName))
                except:
                    pass
            print(self.window.novelId)
            print(self.dataThread.novelId[-1][0])
            for i in range(self.window.novelId,self.dataThread.novelId[-1][0]):
                # 小说封面更新
                exec('self.novelPLab= self.window.novelListBox.novelPLab%s' % i)
                novelP = QPixmap()
                novelP.loadFromData(self.dataThread.novelImg[i][0])
                self.novelPLab.setPixmap(novelP)
                # 小说名称更新
                exec('self.novelNLab = self.window.novelListBox.novelNLab%s' % i)
                if len(self.dataThread.novelName[i][0]) <= 8:  # 判断是否可以完全显示，是直接加载文字
                    self.novelNLab.setText(self.dataThread.novelName[i][0])  # 更新文字
                else:  # 否记载前七字符后加……并设置提示为完整名称
                    self.novelNLab.setText(self.dataThread.novelName[i][0][0:7] + '…')  # 更新文字
                    self.novelNLab.setAlignment(QtCore.Qt.AlignLeft)  # 设置文字居中
                    self.novelNLab.setToolTip(self.dataThread.novelName[i][0])  # 设置鼠标悬停提示
            self.window.novelId = self.dataThread.novelId[-1][0]
        except Exception as e:
            print(e)

class myThread(QThread):

    breakSignal = pyqtSignal(int)

    def __init__(self, parent=None):
        super(myThread, self).__init__(parent)
        self.arg = ''
    def run(self):
        #加载数量
        self.loadNum = 50
        a=0 #上次数据库数据数据
        num = 0 #已加载的数目
        for i in range(self.loadNum):
            res = rescource()
            res.ParentComponent = self  # 绑定本身为res父组件
            res.novelListBoxRes()  # 获取标题栏所需的ui元素
            import time
            time.sleep(2)
            if self.novelName != []:
                num = num + self.novelId[-1][0] - a
                if num < self.loadNum or num - (self.novelId[-1][0]-a) < self.loadNum:
                    self.breakSignal.emit(i)
                    # print('发送')
                    print('已加载数目' + str(num))
                    print('数目' + str(self.novelId[-1][0] - a))

                    a = self.novelId[-1][0]
                else:
                    break
            ''' if self.novelName != []:
                if self.novelId[-1][0] <= self.loadNum:
                    self.breakSignal.emit(i)
                    #print('发送')'''
            if i == self.loadNum+50:
                print('加载超时！')


#遮罩标签 主要是增加灰色背景并设置透明度为0.8，覆盖父组件鼠标滚动，点击事件
class maskLabel(QLabel):
    def __init__(self,parent=None):
        super(maskLabel, self).__init__(parent)
        # 添加灰色背景色，透明度0.8
        self.setStyleSheet('border-width: 1px;border-style: solid;border-color: rgb(255, 170, 0);background-color: rgb(105,105,105,0.8);')

    #忽略鼠标点击事件
    def mousePressEvent(self, event):
        pass
    #重写滚轮滚动事件，将其忽略
    def wheelEvent(self, event):
        if event.type() == QEvent.Wheel:
            event.ignore()


#小说列表框
class novelListBox(QGroupBox):
    '''
    小说列表框
    '''

    def __init__(self, parent=None):
        super(novelListBox, self).__init__(parent)
        self.window = QtWidgets


    def loading(self):
        #显示等待Git图片
        self.loadingBackgroundLab = maskLabel(self)    #背景遮罩，继承自maskLabel
        self.loadingBackgroundLab.setGeometry(0,0, self.width(),self.height())#设置大小


        self.loadingLab=QLabel(self)
        self.loadingLabSize = 50
        self.loadingLab.setGeometry(int((self.window.width()-self.loadingLabSize)/2),int((self.window.height()-self.loadingLabSize)/2),self.loadingLabSize,self.loadingLabSize)
        self.loadingLab.setScaledContents(True)
        self.gif = QMovie('loading.gif')
        self.loadingLab.setMovie(self.gif)
        self.gif.start()

    def load(self):
        #加载UI
        self.columnsNum = 7#列数
        self.boxHeight = 200#高度
        a = int((self.window.width()-(self.columnsNum-1)*10) / self.columnsNum)  # 宽
        b = 0  # x方向距离
        c = 0  # self.Lab.y() + self.Lab.height() + 10   #y方向上的距离
        d = 1  # 所在列数
        i = 0  # 生成组件的编号
        pix = QPixmap('ui/break_img.jpg')   #图片资源--图片损坏(占位)
        for img in range(49):
            if d <= self.columnsNum:    #所在列数小于等于最大列数，无操作
                pass
            else:   #列数归为一重新计数，跳到下一行
                c = c + self.boxHeight
                d = 1
                b = 0
            if d ==1:#判断是否为第一列，是则前空5
                b =b+5
            elif d==self.columnsNum:#判断是否为最后一列，是后空5
                b=b+5
            else:#其余中间都空10
                b=b+10
            exec('self.novelBox%s = QGroupBox(self)'%i)  #为每一个来源创建box
            exec('self.novelBox= self.novelBox%s'%i)
            self.novelBox.setStyleSheet('background-color:#CCCCCC')
            #self.a.setStyleSheet('background-color:#FF6666')
            self.novelBox.setGeometry(b, c, a, self.boxHeight)

            #显示图片
            exec('self.novelPLab%s = clickLabel(self.novelBox)' % i)  # 显示图片的标签
            exec('self.novelPLab= self.novelPLab%s' % i)
            self.novelPLab.setGeometry(0,0,self.novelBox.width(),int(self.novelBox.height()*0.9))
            self.novelPLab.setPixmap(pix)
            self.novelPLab.setScaledContents(True)

            #显示名称
            exec('self.novelNLab%s = clickLabel(self.novelBox)' % i)  # 显示名称的标签
            exec('self.novelNLab= self.novelNLab%s' % i)
            self.novelNLab.setGeometry(0,int(self.novelBox.height()*0.9), self.novelBox.width(), int(self.novelBox.height() * 0.1))
            self.novelNLab.setText('正在载入……')#设置文字
            self.novelNLab.setAlignment(Qt.AlignCenter)#设置文字居中
            self.novelNLab.setAutoFillBackground(True)  # 设置背景充满，为设置背景颜色的必要条件
            pe = QPalette()
            pe.setColor(QPalette.Window,Qt.blue)  # 设置背景颜色
            self.novelNLab.setPalette(pe)  # 设置背景颜色

            #加载字体
            fontId = QFontDatabase.addApplicationFont('方正宋刻本秀楷简.TTF')
            fontName = QFontDatabase.applicationFontFamilies(fontId)[0]
            self.font = QFont(fontName,13)
            self.novelNLab.setFont(self.font)#设置字体

            b = b + a# + 10
            d = d + 1
            i = i + 1
            self.resize(self.window.width(), self.boxHeight * (i + 2))

        if i <= self.columnsNum:
            self.lastHight = 200
        elif i <= self.columnsNum * 2:
            self.lastHight = 2 * self.boxHeight
        else:
            self.lastHight = c + self.boxHeight


    def openSource(self,id):
        self.window.synopsisInitialization(id)
        self.window.pageTage = 'synopsis'
        self.window.PageSwitching()


#自定义配合水平滚动框使用的标签，可点击长按拖动父组件水平滚动
#标签被点击时触发 self.function 事件
class horizontalScrollLabel(QLabel):
    '''
        自定义配合水平滚动框使用的标签，可点击长按拖动父组件水平滚动
        标签被点击时触发 self.function 事件
        '''

    def __init__(self, parent=None):
        super(horizontalScrollLabel, self).__init__(parent)
        self.arg = ''
        self.horizontalScrollBox = QWidget
        self.horizontalScrollBox.m_flag = False
        self.horizontalScrollBox.start_time = False

    def mousePressEvent(self, event):
        '''
        重写标签的被点击事件
        :param event:
        :return:
        '''
        try:
            if event.buttons() == QtCore.Qt.LeftButton:  # 左键按下
                if self.arg == '':
                    self.function()
                else:
                    self.function(self.arg)
        except Exception as e:
            print(e)

    def mouseReleaseEvent(self, QMouseEvent):
        '''
        重写鼠标左键弹起事件
        :param QMouseEvent:
        :return:
        '''
        import traceback
        try:
            import time
            self.end_time = time.time()
            if self.end_time - self.horizontalScrollBox.start_time <= 0.2:
                if self.arg == '':
                    pass
                else:
                    self.function(self.arg)
            self.horizontalScrollBox.m_flag = False
        except Exception as e:
            print(e)
            traceback.print_exc()

#水平滚动框
class horizontalScrollBox(QGroupBox):
    '''
    水平滚动框
    '''
    def __init__(self,parent=None):
        super(horizontalScrollBox, self).__init__(parent)
        self.window = QtWidgets
        self.selfMove = 0
        self.get_res()
        self.UI()


    def get_res(self):
        res = rescource()
        res.ParentComponent = self  # 绑定本身为res父组件
        res.horizontalScrollBoxRes()  # 获取水平滚动框所需的json信息

        #处理json信息

        import json
        # 利用json模块的loads函数将json字符串转为python对象
        typeNameList = json.loads(str(self.novelType[0][0]))

        self.typeNmae = typeNameList[0]['typeName']
        self.spiderName = typeNameList[1]['spiderName']

    def UI(self):


        #添加网页logo
        logo = QLabel(self)
        logo.setGeometry(0,0,60,40)
        i = 0 #名称编号
        x = 0 #坐标x信息
        width = 80
        height= 40
        self.resize(QApplication.desktop().width(),10)
        self.setStyleSheet('background-color:#FF6666')
        for name in self.typeNmae:#['玄幻魔法', '武侠修真', '都市言情', '历史军事', '网游动漫', '科幻小说', '恐怖灵异', '综合其他','玄幻魔法', '武侠修真', '都市言情', '历史军事', '网游动漫', '科幻小说', '恐怖灵异', '综合其他']:
            exec('self.typeLab%s = horizontalScrollLabel(self)'%i)
            exec('self.typeLab = self.typeLab%s'%i)
            self.typeLab.horizontalScrollBox = self
            self.typeLab.setText(name)
            self.typeLab.setGeometry(x,0,width,height)
            self.typeLab.setStyleSheet('background-color:#FF6666')
            self.typeLab.setAlignment(Qt.AlignCenter)
            self.typeLab.mousePressEvent = self.mousePressEvent
            self.typeLab.arg = name
            self.typeLab.function = self.test
            i += 1
            x += width

            self.resize(self.width()+width,height)

        self.leftMax = 80*i+80
    def test(self,a):
        print(a)

    def mousePressEvent(self, event):
        '''
        重写鼠标左键按下事件
        :param event:
        m_flag = boolean 为True 时窗口随鼠标移动
        windows 窗口对象
        :return:
        '''
        import time
        self.start_time = time.time()
        import traceback
        try:
            if event.buttons() == QtCore.Qt.LeftButton:  # 左键按下
                self.m_flag = True
                self.m_Position = QCursor.pos().x()  # 获取鼠标相对窗口的位置
                event.accept()
        except Exception as e:
            print(e)
            traceback.print_exc()

    def mouseMoveEvent(self, QMouseEvent):
        '''
        重写鼠标移动事件
        :param QMouseEvent:
        :return:
        '''
        import traceback
        try:
            if QtCore.Qt.LeftButton and self.m_flag and self.x() <= 0 and self.leftMax > self.window.width() and -(self.selfMove) < self.leftMax:
                # self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
                # print(QCursor.pos().x()-self.m_Position)
                a = int(self.x() + int(0.009 * (QCursor.pos().x() - self.m_Position)))
                #print(a)
                if a >= 0:
                    if self.x() == 0:
                        self.selfMove = 0
                    else:
                        self.selfMove = self.selfMove + a
                    print('x',self.x())
                    self.move(0, self.y())
                    print('a',a)
                    print('selfMove',self.selfMove)
                else:
                    self.move(self.x() + int(0.009 * (QCursor.pos().x() - self.m_Position)),self.y())
                    self.selfMove = self.selfMove + int(0.009 * (QCursor.pos().x() - self.m_Position))
                    print('selfMove',self.selfMove)
                QMouseEvent.accept()

        except Exception as e:
            print(e)
            traceback.print_exc()















