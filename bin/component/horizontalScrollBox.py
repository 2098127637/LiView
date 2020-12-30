from PyQt5.Qt import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QGroupBox
from PyQt5.QtWidgets import QWidget,QLabel,  QApplication
#水平滚动框
class horizontalScrollBox(QGroupBox):
    '''
    水平滚动框
    '''
    def __init__(self,parent=None):
        super(horizontalScrollBox, self).__init__(parent)
        self.selfMove = 0
        self.UI()

    def UI(self):


        #添加网页logo
        i = 0 #名称编号
        x = 0 #坐标x信息
        width = 80
        height= 40
        self.resize(QApplication.desktop().width(),10)
        self.setStyleSheet('background-color:#FF6666')
        for name in range(50):#['玄幻魔法', '武侠修真', '都市言情', '历史军事', '网游动漫', '科幻小说', '恐怖灵异', '综合其他','玄幻魔法', '武侠修真', '都市言情', '历史军事', '网游动漫', '科幻小说', '恐怖灵异', '综合其他']:
            exec('self.typeLab%s = horizontalScrollLabel(self)'%i)
            exec('self.typeLab = self.typeLab%s'%i)
            self.typeLab.horizontalScrollBox = self
            #self.typeLab.setText(name)
            self.typeLab.setGeometry(x,0,width,height)
            self.typeLab.setStyleSheet('background-color:#FF6666')
            self.typeLab.setAlignment(Qt.AlignCenter)
            self.typeLab.mousePressEvent = self.mousePressEvent
            #self.typeLab.arg = name
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
            if QtCore.Qt.LeftButton and self.m_flag and self.x() <= 0 and self.leftMax > self.ParentComponent.width() and -(self.selfMove) < self.leftMax:
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