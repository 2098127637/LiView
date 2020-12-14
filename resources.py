class rescource:
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
        db = 'I:\\amadeus\\LiView\\userData\\sql\\spider.db'
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
        db = 'I:\\amadeus\\LiView\\userData\\sql\\spider.db'
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

    def close(self):
        self.c.close()
        self.conn.close()