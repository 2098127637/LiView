from PyQt5.QtWidgets import QApplication

from PyQt5.QtCore import pyqtSignal

import traceback
#从commponent目录下加载自定义组件
import sys,time
sys.path.append('../component')

from verticalScrollBox import verticalScrollBox
from dataOperation import dataOperation
from clickLabel import clickLabel
from horizontalScrollBox import horizontalScrollBox

class synopsis(verticalScrollBox):
    sourceSelection= pyqtSignal(int)
    def __init__(self,parent = None):
        super(synopsis, self).__init__(parent)
        self.resize(QApplication.desktop().width(), QApplication.desktop().height())


    def __int__(self):
        self.synopsisUI()
        self.sourceSelection.connect(self.synopsisInitialization)

    def get_res(self):
        self.ParentComponent.logging.debug("> synopsis开始")
        self.ParentComponent.logging.debug("* 从数据库获取信息")
        try:
            # 获取homePage所需的ui元素
            self.res = dataOperation()
            self.res.ParentComponent = self  # 绑定本身为res父组件，
            self.res.call_Label = 'synopsisPageRes'  # 调用标签

            self.res.threadEnd.connect(self.updateInterface)

            self.ParentComponent.logging.debug("* 开启数据库操作线程")

            self.res.start()
            # import time
            # time.sleep(10)

            self.ParentComponent.logging.debug("* 完成！~~从数据库获取信息")
        except Exception as e:
            print(e)
            self.ParentComponent.logging.critical('# synopsis从数据库获取信息失败！' + str(e))

    def synopsisUI(self):
        self.resize(QApplication.desktop().width(),4500)

        #self.sourceID = ID
        self.typeColumn = horizontalScrollBox(self)  # 实例化水平类型展示框
        self.typeColumn.ParentComponent = self
        self.typeColumn.move(0, 3)

    def updateInterface(self):
        # 处理json信息
        import json
        # 利用json模块的loads函数将json字符串转为python对象
        typeNameList = json.loads(str(self.novelType[self.sourceID - 1][0]))
        self.typeNmae = typeNameList[0]['typeName']
        self.spiderName = typeNameList[1]['spiderName']
        i = 0
        for name in self.typeNmae:
            exec('self.typeLab = self.typeLab%s' % i)
            self.typeColumn.typeLab.setText(name)

            self.typeColumn.typeLab.arg = name
            i=i+1

    def synopsisInitialization(self,ID):
        self.ParentComponent.pageTage = 'synopsis'
        self.ParentComponent.PageSwitching()
        time.sleep(10)
        self.get_res()
        #获取安装目录
        print(ID)
        from configparser import ConfigParser
        cf = ConfigParser()
        f = open('INIT.INI')
        cf.read_file(f)
        InstallationDirectory = cf.get('InstallationDirectory', 'InstallationDirectory')
        #self.callSpider(InstallationDirectory + 'userData\\spider\\%s\\call\\%s'%(self.path[self.sourceID-1][0],self.spiderName[self.sourceID-1]+'.py'))

    def novelListBoxInit(self):
        self.typeColumn_height = 10
        self.typeColumn_y = 60

        #添加信息
        self.novelListBox = NovelListBox(self.synopsisBox)#实例化小说列表框
        self.novelListBox.window = self
        self.novelListBox.setGeometry(0,self.typeColumn_height+self.typeColumn_y+3,self.width(),self.height())

        # 加载UI
        self.novelListBox.columnsNum = 7  # 列数
        self.novelListBox.boxHeight = 200  # 高度
        self.novelListBox.a = int((self.width() - (self.novelListBox.columnsNum - 1) * 10) / self.novelListBox.columnsNum)  # 宽
        self.novelListBox.b = 0  # x方向距离
        self.novelListBox.c = 0  # self.Lab.y() + self.Lab.height() + 10   #y方向上的距离
        self.novelListBox.d = 1  # 所在列数
        self.novelListBox.i = 0  # 生成组件的编号
        self.novelListBox.load() # 先加载UI后更新数据
        self.novelListBox.loading(True)

        self.synopsisBox.showPage = 1
        #self.synopsisBox.lenth = self.novelListBox.lastHight + self.typeColumn.height() + 50 - self.height()  # 限制synopsisBox能向下滚动的最大距离
        self.synopsisBox.lenth = 200*7*self.synopsisBox.showPage + self.typeColumn_height + 50 - self.height()  # 限制synopsisBox能向下滚动的最大距离
        self.synopsisBox.resize(self.width(), self.novelListBox.height())  # 增加synopsisBox的高度

    def callSpider(self,callName):
        #爬虫调用
        from configparser import ConfigParser
        import win32api
        import sqlite3

        #获取novel.db的位置
        from configparser import ConfigParser
        cf = ConfigParser()
        f = open('INIT.INI')
        cf.read_file(f)
        novelPath = cf.get('db', 'novel')

        '''#清空表
        conn = sqlite3.connect(novelPath)
        c = conn.cursor()
        c.execute('delete from novelindex;')#清空
        c.execute('update sqlite_sequence SET seq = 0;')#自增索引为零
        conn.commit()#提交更改
        c.close()
        conn.close()'''

        '''#调用相应爬虫
        cf = ConfigParser()
        f = open('INIT.INI')
        cf.read_file(f)
        python = cf.get('python', 'python')
        win32api.ShellExecute(0, "open", python,callName, '', 1)'''



