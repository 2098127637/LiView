'''首页'''

from PyQt5.QtWidgets import  QLabel, QApplication,QGroupBox
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore

import traceback
#从commponent目录下加载自定义组件
import sys,time
sys.path.append('..\component')

from verticalScrollBox import verticalScrollBox
from dataOperation import dataOperation
from clickLabel import clickLabel

class home(verticalScrollBox):
    def __init__(self,parent = None):
        super(home, self).__init__(parent)
        self.resize(QApplication.desktop().width(), QApplication.desktop().height())
    def __int__(self):

        self.get_res()
        self.homeUI()

    def get_res(self):
        self.ParentComponent.logging.debug("> homePage开始")
        self.ParentComponent.logging.debug("* 从数据库获取信息")
        try:
            # 获取homePage所需的ui元素
            self.res = dataOperation()
            self.res.ParentComponent = self  # 绑定本身为res父组件，
            self.res.call_Label = 'homeBoxRes'  # 调用标签

            self.res.threadEnd.connect(self.updateInterface)

            self.ParentComponent.logging.debug("* 开启数据库操作线程")

            self.res.start()
            # import time
            # time.sleep(10)

            self.ParentComponent.logging.debug("* 完成！~~从数据库获取信息")
        except Exception as e:
            print(e)
            self.ParentComponent.logging.critical('# homePage从数据库获取信息失败！' + str(e))

    def homeUI(self):
        self.ParentComponent.logging.debug("* homePageUI初始化开始")


        self.advertisementLab = QLabel(self)
        self.advertisementLab.setGeometry(0, 0, self.ParentComponent.width(), int(self.ParentComponent.width() * 0.45))

        self.ParentComponent.logging.debug("* homePageUI初始化完成")

        self.columnsNum = 4  #
        self.boxHeight = 150
        self.wide = int((self.ParentComponent.width() - 20) / self.columnsNum)  # 宽
        self.Xdirection= 0  # x方向距离
        self.Ydirection = self.advertisementLab.height() + self.advertisementLab.y()  # y方向上的距离
        self.row = 1  # 所在行数
        self.componentNum = 0  # 生成组件的编号

    def updateInterface(self):
        self.ParentComponent.logging.debug("* homePageUI更新--加载图片")
        advertisementLab_p = QPixmap()
        advertisementLab_p.loadFromData(self.TopPoster[0][0])
        advertisementLab_p = advertisementLab_p.scaled(self.advertisementLab.width(),self.advertisementLab.height(), QtCore.Qt.KeepAspectRatio)
        self.advertisementLab.setScaledContents(True)
        self.advertisementLab.setPixmap(advertisementLab_p)

        # 页面更新，加载图片
        self.load()

    def load(self):
        i = 0
        self.ParentComponent.logging.debug("* 开始加载来源")
        try:
            for img in self.spiderLogo:
                if self.row <= self.columnsNum:
                    pass
                else:
                    self.Ydirection = self.Ydirection + self.boxHeight
                    self.row = 1
                    self.Xdirection = 0
                exec('self.sourceG%s = QGroupBox(self)' % self.componentNum)  # 为每一个来源创建box
                exec('self.a= self.sourceG%s' % self.componentNum)
                #self.a.setStyleSheet('background-color:#FF6666')
                self.a.setGeometry(self.Xdirection,self.Ydirection, self.wide, self.boxHeight)
                self.a.setFixedHeight(self.boxHeight)
                exec('self.lab_logo%s = clickLabel(self.a)' % self.componentNum)  # 来源网站的logo图标
                exec('self.replace_logo = self.lab_logo%s' % self.componentNum)
                self.replace_logo.setGeometry(int(self.a.height() * 0.7), int(self.a.height() * 0.7),
                                              int(self.a.width() - self.a.height() * 0.7), int(self.a.height() * 0.3))
                replace_logoP = QPixmap()
                replace_logoP.loadFromData(img[0])
                self.replace_logo.setPixmap(replace_logoP)
                self.replace_logo.setScaledContents(True)

                exec('self.lab_color%s = clickLabel(self.a)' % self.componentNum)  # 来源网站彩图
                exec('self.replace_color = self.lab_color%s' % self.componentNum)
                self.replace_color.setGeometry(0, 5, int(self.a.height() * 0.7), self.a.height())
                replace_colorP = QPixmap()
                replace_colorP.loadFromData(self.spiderPicture[i][0])
                self.replace_color.setPixmap(replace_colorP)
                self.replace_color.setScaledContents(True)

                exec('self.lab_authorlogo%s = clickLabel(self.a)' % self.componentNum)  # 来源作者图标
                exec('self.replace_authorlogo = self.lab_authorlogo%s' % self.componentNum)
                self.replace_authorlogo.setGeometry(int(self.a.height() * 0.7), 0, int(self.a.height() * 0.4),
                                                    int(self.a.height() * 0.4))
                replace_authorlogoP = QPixmap()
                replace_authorlogoP.loadFromData(self.authorLogo[i][0])
                self.replace_authorlogo.setPixmap(replace_authorlogoP)
                self.replace_authorlogo.setScaledContents(True)

                exec('self.lab_openlogo%s = clickLabel(self.a)' % self.componentNum)  # 打开图标
                exec('self.replace_openlogo = self.lab_openlogo%s' % self.componentNum)
                self.replace_openlogo.setGeometry(int(self.a.width() * 0.85), int(self.a.height() * 0.1),
                                                  int(self.a.height() * 0.2),
                                                  int(self.a.height() * 0.6))
                self.replace_openlogo.function = self.openSource  # 绑定事件
                self.replace_openlogo.arg = i + 1  # 绑定参数,即所点击来源在数据库中的id，使synopis页面能够进行初始化加载
                replace_openlogoP = QPixmap()
                replace_openlogoP.loadFromData(self.openLogo[0][0])
                self.replace_openlogo.setPixmap(replace_openlogoP)
                self.replace_openlogo.setScaledContents(True)
                ''' p = QPixmap()
                print(img)
                p.loadFromData(img)
                self.b.setPixmap(p)
                self.b.setScaledContents(True)'''

                self.Xdirection = self.Xdirection + self.wide + 10
                self.row = self.row + 1
                self.componentNum = self.componentNum+1
                i = i+1
                self.resize(self.ParentComponent.width(), self.boxHeight * (self.componentNum + 2))

        except Exception as e:
            print(e)
        self.ParentComponent.logging.debug("* 完成！~~加载来源")
        self.ParentComponent.logging.debug("* homePage最终大小计算更改")
        self.end = True
        try:
            if self.componentNum <= self.columnsNum:
                self.lastHight = 200
            elif self.componentNum <= self.columnsNum * 2:
                self.lastHight = 2 * self.boxHeight
            else:
                self.lastHight = self.Ydirection + self.boxHeight

            self.lenth = self.lastHight + self.advertisementLab.height() + 60 - self.ParentComponent.height()  # 限制homeBox能向下滚动的最大距离
            self.resize(self.width(),self.boxHeight*self.row + self.advertisementLab.height() +60)  # 增加homeBox的高度
        except:
            print(traceback.print_exc())
            print('traceback.format_exc():\n%s' % traceback.format_exc())

    def openSource(self,id):
        self.ParentComponent.synopsisPage.sourceSelection.emit(id)
