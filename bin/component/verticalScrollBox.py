#自定义页面要用的垂直滚动组件框
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QGroupBox,QSplitter
from PyQt5.QtCore import pyqtSignal,Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget,QMainWindow

class verticalScrollBox(QGroupBox):
    gxSignal = pyqtSignal(int)
    '''自定义滚动组件框'''
    def __init__(self, parent=None):
        super(verticalScrollBox, self).__init__(parent)
        #self.setWindowFlags(Qt.FramelessWindowHint)#设置窗体无边框
        self.ParentComponent = QtWidgets
        self.gxSignal.connect(self.a)


    moveDown = 0

    def wheelEvent(self, event):
        UnitLength = 40  # 每次滚动的像素
        angle = event.angleDelta() / 8  # 返回QPoint对象，为滚轮转过的数值，单位为1/8度
        angleY = angle.y()  # 竖直滚过的距离
        if self.ParentComponent.pageTage == 'home':
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
                if self.height() + self.y() > self.ParentComponent.height() - 10 and self.moveDown < self.lenth:
                    self.move(0, self.y() - UnitLength)
                    self.moveDown = self.moveDown + 40
                    # print(self.moveDown)
                else:
                    pass
        elif self.ParentComponent.pageTage == 'synopsis':
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
                if self.height() + self.y() > self.ParentComponent.height() - 10 and self.moveDown < self.lenth:
                    self.move(0, self.y() - UnitLength)
                    self.moveDown = self.moveDown + 40
                    # print(self.moveDown)
                else:
                    print('到底了！')
                    try:
                        #注意scrollBox实例化后，此处self为synopsisBox本身
                        self.gxSignal.emit(1)
                        self.resize(self.width(), self.ParentComponent.novelListBox.height())  # 增加synopsisBox的高度
                    except Exception as e:
                        print(e)
    def a(self):
        try:
            self.ParentComponent.novelListBox.loading(True)
            #print('novelName:len', str(len(self.dataThread.novelName)))
            self.ParentComponent.novelId = 0
            self.ParentComponent.source.updateInterface()
            self.ParentComponent.source.dataThread.start()
            self.showPage = self.showPage + 1
            # self.resize(self.width(), self.height() + 30)
            self.lenth = 200 * 7 * self.showPage + self.ParentComponent.typeColumn.height() + 50 - self.ParentComponent.height()  # 限制synopsisBox能向下滚动的最大距离
        except Exception as e:
            print(e)

    def updateInterface(self):
        #更新界面
        print('更新界面')
        try:
            if len(self.dataThread.novelName) >= 49:
                try:
                    # 删除loading.png
                    import sip
                    sip.delete(self.ParentComponent.novelListBox.loadingLab)
                    sip.delete(self.ParentComponent.novelListBox.loadingBackgroundLab)
                    # print('传入总数:')
                    # print(len(self.dataThread.novelName))
                except:
                    pass
            print(self.ParentComponent.novelId)
            print(self.dataThread.novelId[-1][0])
            for i in range(self.ParentComponent.novelId,self.dataThread.novelId[-1][0]):
                # 小说封面更新
                exec('self.novelPLab= self.ParentComponent.novelListBox.novelPLab%s' % i)
                novelP = QPixmap()
                novelP.loadFromData(self.dataThread.novelImg[i][0])
                self.novelPLab.setPixmap(novelP)
                # 小说名称更新
                exec('self.novelNLab = self.ParentComponent.novelListBox.novelNLab%s' % i)
                if len(self.dataThread.novelName[i][0]) <= 8:  # 判断是否可以完全显示，是直接加载文字
                    self.novelNLab.setText(self.dataThread.novelName[i][0])  # 更新文字
                else:  # 否记载前七字符后加……并设置提示为完整名称
                    self.novelNLab.setText(self.dataThread.novelName[i][0][0:7] + '…')  # 更新文字
                    self.novelNLab.setAlignment(QtCore.Qt.AlignLeft)  # 设置文字居中
                    self.novelNLab.setToolTip(self.dataThread.novelName[i][0])  # 设置鼠标悬停提示
            self.ParentComponent.novelId = self.dataThread.novelId[-1][0]
        except Exception as e:
            print(e)