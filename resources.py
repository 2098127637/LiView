class rescource:
    def __init__(self):
        from configparser import ConfigParser
        cf = ConfigParser()
        f = open('INIT.INI')
        cf.read_file(f)
        self.spiderDB = cf.get('db', 'spider')
        self.novelDB = cf.get('db', 'novel')
        f.close()
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
            num = num + 1

        self.close()

    def sourceListBoxRes(self):
        db = self.spiderDB
        nameList = ['logo', 'colorPicture', 'authorLogo']
        tabeList = []
        for i in nameList:
            tabeList.append('spider')
        self.information = [db, nameList, tabeList]

        self.initialization()

        #返回的对象
        self.returnObject = ['spiderLogo','spiderPicture','authorLogo']# 网站logo  显示的彩图  作者logo
        num = 0
        for i in self.result:
            exec('self.ParentComponent.%s = i'%(self.returnObject[num]))
            num = num + 1

        nameList = ['openLogo']
        tabeList = ['PictureUI']
        self.information = [db, nameList, tabeList]
        self.initialization()
        self.ParentComponent.openLogo = self.result[0]

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
        db = self.spiderDB
        nameList = ['openLogo','TopPoster']
        tabeList = []
        for i in nameList:
            tabeList.append('sys')
        self.information = [db, nameList, tabeList]

        self.initialization()

        # 返回的对象
        self.returnObject = ['openLogo','TopPoster']  # 网站logo  显示的彩图  作者logo
        num = 0
        for i in self.result:
            exec('self.ParentComponent.%s = i' % (self.returnObject[num]))
            num = num + 1

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

if __name__ == '__main__':
    a= rescource()