from PyQt5.QtCore import QThread,pyqtSignal

class dataOperation(QThread):
    threadEnd = pyqtSignal()
    def __init__(self,parent = None):
        super(dataOperation, self).__init__(parent)

        from configparser import ConfigParser
        cf = ConfigParser()
        f = open('../../INIT.INI')
        cf.read_file(f)
        self.spiderDB = cf.get('db', 'spider')
        self.novelDB = cf.get('db', 'novel')
        f.close()

    def run(self):
        try:
            self.ParentComponent.ParentComponent.logging.debug("* 数据库操作线程--执行查询")
            exec('self.%s()'%self.call_Label)
            self.ParentComponent.ParentComponent.logging.debug("* 结束！~~数据库操作线程")
            self.threadEnd.emit()
        except Exception as e:
            print(e)

    def initialization(self):
        try:
            import sqlite3
            self.conn = sqlite3.connect(self.information[0])
            self.c = self.conn.cursor()
            self.result=[]
            a=0
            for i in self.information[1]:
                exec("self.c.execute('SELECT %s FROM %s ')" % (i, self.information[2][a]))
                #self.result.append(self.c.fetchone()[0])
                self.result.append(self.c.fetchall())
                a=a+1
        except Exception as e:
            print(e)

    def titleBarRes(self):
        '''
                :arg
                information=[[数据名称],[所在数据库],]

                :return:
                result = []
                '''
        db = self.spiderDB
        nameList = ['logo', 'search', 'searchBackground', 'setting', 'minimize', 'FullScreen', 'close']
        tabeList = []
        for i in nameList:
            tabeList.append('PictureUI')
        self.information = [db,nameList,tabeList]
        #self.ParentComponent =
        self.initialization()

        #返回的对象
        self.returnObject = ['logo', 'search', 'searchBackground','setting','minimizeApp','FullScreen','closeApp']
        num = 0
        for i in self.result:
            exec('self.ParentComponent.%s = i[0]' % (self.returnObject[num]))
            #print('logo',self.ParentComponent.logo)
            num = num + 1

        self.close()

    def horizontalScrollBoxRes(self):
        db = self.spiderDB
        nameList = ['type']
        tabeList = []
        for i in nameList:
            tabeList.append('spider')
        self.information = [db, nameList, tabeList]

        self.initialization()

        # 返回的对象
        self.returnObject = ['novelType']  # 网站logo  显示的彩图  作者logo
        num = 0
        for i in self.result:
            exec('self.ParentComponent.%s = i' % (self.returnObject[num]))
            num = num + 1
    def synopsisPageRes(self):
        db = self.spiderDB
        nameList = ['path','type']
        tabeList = []
        for i in nameList:
            tabeList.append('spider')
        self.information = [db, nameList, tabeList]

        self.initialization()

        # 返回的对象
        self.returnObject = ['path','novelType']  # 网站logo  显示的彩图  作者logo
        num = 0
        for i in self.result:
            exec('self.ParentComponent.%s = i' % (self.returnObject[num]))
            num = num + 1
    def homeBoxRes(self):
        #第一页彩图要用到的信息
        db = self.spiderDB
        nameList = ['TopPoster']#彩图海报
        tabeList = []
        for i in nameList:
            tabeList.append('sys')
        self.information = [db, nameList, tabeList]

        self.initialization()

        # 返回的对象
        self.returnObject = ['TopPoster']
        num = 0
        for i in self.result:
            exec('self.ParentComponent.%s = i' % (self.returnObject[num]))
            num = num + 1

        #显示来源所用到的信息
        nameList = ['logo', 'colorPicture', 'authorLogo']# 网站logo  显示的彩图  作者logo
        tabeList = []
        for i in nameList:
            tabeList.append('spider')
        self.information = [db, nameList, tabeList]

        self.initialization()

        # 返回的对象
        self.returnObject = ['spiderLogo', 'spiderPicture', 'authorLogo']  # 网站logo  显示的彩图  作者logo
        num = 0
        for i in self.result:
            exec('self.ParentComponent.%s = i' % (self.returnObject[num]))
            num = num + 1

        nameList = ['openLogo']
        tabeList = ['PictureUI']
        self.information = [db, nameList, tabeList]
        self.initialization()
        self.ParentComponent.openLogo = self.result[0]


    def novelListBoxRes(self):
        db = self.novelDB
        nameList = ['name', 'img','id']
        tabeList = []
        for i in nameList:
            tabeList.append('novelindex')
        self.information = [db, nameList, tabeList]

        self.initialization()

        # 返回的对象
        self.returnObject = ['novelName', 'novelImg','novelId']  # 小说名称 小说图片 小说ID
        num = 0
        for i in self.result:
            exec('self.ParentComponent.%s = i' % (self.returnObject[num]))
            num = num + 1
    def close(self):
        self.c.close()
        self.conn.close()
