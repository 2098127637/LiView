class homePage():
    def __init__(self):
        '''
        :param kwargs: {'url':'',coding:'utf-8'}
        '''

        '''
        获取源码    crawling(self,url,coding)
            依赖函数    无
            获取参数 url,coding(链接，编码)
            返回参数 self.htmlText
        '''
        self.htmlText = '' #获取的网页源码

        '''
        解析源码
                    解析获取首页推荐所有小说名称及章节目录详情页面链接   recommend(self)
                    依赖函数    crawling(self,url,coding)
                    获取参数 self.htmlText
                    返回参数 self.novelData  self.novelName'''
        self.novelName=''       #所下载的小说的名称
        self.novelData = {}     #获取到的小说字典{名称：链接}
        '''
                    解析小说章节页面源码返回所有章节名称与其正文链接   chapter(self)
                    依赖函数    recommend(self)  crawling(self,url,coding)
                    获取参数 self.novelName  self.htmlText  self.novelData
                    返回参数 self.totalTasks self.chapterData
        '''
        self.totalTasks = 0  # 下载任务的总数
        self.chapterData = {}  # 获取到的章节字典{章节名称：链接}
        '''
                    获取小说每一章的正文      content(self,url)
                    依赖函数 crawling(self,url,coding) recommend(self) chapter(self)
                    获取参数 self.htmlText
                    返回参数 self.wrongChapterUrl  self.wrongChapterNum  self.result
        '''
        self.wrongChapterNum = 0  # 下载时错误的总个数
        self.wrongChapterUrl = []  # 下载时错误章节的链接列表
        self.result = ''  # 返回的章节内容
        '''
                    循环爬取一本小说所有章节的正文，支持单线程或多线程选择，并执行打印或缓存操作   download(self,partList)
                    依赖函数    
                    获取参数 self.threadsNum time.sleep(self.sleepTime)
        '''

        self.threadsNum=50    #下载时所用的线程数，值为None时不开启多线程
        self.threadsName = [] #所有线程的名称
        self.completedTasks=0       #所下载完成的任务数目

    def _crawling(self,url,coding):
        '''

        :param url:
        :param coding:
        :return: self.htmlText
        '''
        import requests
        import re
        import sys
        print('获取网页('+ url +')的源码~')
        '''  url = kwargs.get('url')
        coding = kwargs.get('coding')'''

        hea = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36'}
        html = requests.get(url, headers=hea)
        html.encoding= coding
        html.encoding = 'utf-8'  # 这一行是将编码转为utf-8否则中文会显示乱码。
        #print(html.text)
        print('---成功！')

        self.htmlText=html.text

        #self.recommend()
    def _recommend(self,url,coding):
        '获取推荐'
        from bs4 import BeautifulSoup

        self.crawling(url,coding)

        novelNamelist = []
        novelUrl = []
        print('即将获取推荐内容')
        print('正在解析网页~')
        text = self.htmlText
        data= BeautifulSoup(text,features="html.parser")
        #print(data)
        m = 0
        n=1
        '''
        示例函数，主要要求返回novelData 与 novelUrl 且二者相互对应
        
        def XXX ()
        information1 = data.find_all('div',class_='xname')
        for a in information1:
            information2 = a.find_all('a')
            for i in information2:
                novelNamelist.append(i.get_text())
                novelUrl.append('https://www.xuanshu.com'+i.get('href'))
                print('第'+ str(n) +'本')
                print(i.get_text())
                print(i.get('href'))
                print('-----------------')
                m=m+1
                n=n+1
        print('共找到'+str(m)+'本书')
        
        
        '''

        #print(novelUrl)
        #print(novelName)
        self.novelData= dict(zip(novelNamelist,novelUrl))
        return self.novelData
    def _chapter(self):
        '''

        :param name:
        :return:
        '''
        '获取章节'

        self.crawling(self.novelData[self.novelName], 'utf-8')
        from bs4 import BeautifulSoup

        chapterName=[]
        chapterUrl=[]
        print('即将获取章节')
        text = self.htmlText
        data = BeautifulSoup(text, features="html.parser")

        '''
        示例函数 主要返回  chapterName , chapterUrl
        
        def XXX()
        information1 = data.find('div',class_='pc_list').find('ul')
        information2 = information1.find_all('li')
        for i in information2:
            i=i.find('a')
            chapterUrl.append(self.novelData[self.novelName]+i.get('href'))
            chapterName.append(i.get_text())
        m=0
        n=1
        for i in chapterName:
            print('第'+str(n)+'章')
            print(i)
            m=m+1
            n=n+1
        print('共'+str(m)+'章')
        self.totalTasks = m
            
            
        '''

        self.chapterData = dict(zip(chapterName,chapterUrl))

        return self.chapterData

    def _content(self,url):
        '获取内容'
        self.crawling(url, 'utf-8')
        from bs4 import BeautifulSoup
        import time

        text = self.htmlText
        data = BeautifulSoup(text, features="html.parser")

       ''' 
       示例函数  主要返回 result
       
       information1 = data.find('div',id="content1")
        if information1 == None:
            print("无数据，原网页："+url)
            self.wrongChapterUrl.append(url)
            self.wrongChapterNum = self.wrongChapterNum+1
        else:
            a=information1.get_text()
            self.result= self.result + a
            print('获取到此章大小为：'+ str(len(a))+'kb')
            print(self.result)'''

        return self.result


    def theBehavior(self,partDict,sleepTime):
        import random
        a = random.randint(0, 1000)
        exec('xuanshuwang%s = homePage()' % a)
        for i in list(partDict.values()):
            print('即将获取的章节名称：' + list(partDict.keys())[list(partDict.values()).index(i)])
            # 获取锁，用于线程同步
            #self.threadLock.acquire()
            threadLock.acquire()
            exec('xuanshuwang%s.content(i)' % a)
            # 释放锁，开启下一个线程
            #self.threadLock.release()
            threadLock.release()
            eval("%s" % a)
            # xuanshuwang.content('https://www.xuanshu.com' + self.novelData[self.novelName] + i)
            self.completedTasks = self.completedTasks + 1
            print("当前总进度：" + str('{:.20%}'.format(self.completedTasks / self.totalTasks)))
            time.sleep(sleepTime)

    def _download(self,downloadDict,sleepTime):
        sleepTime = sleepTime       #下载时等待时间
        if self.threadsNum == None:
            print('多线程下载已关闭')
            for i in list(downloadDict.values()):
                print('即将获取的章节名称：' + list(downloadDict.keys())[self.completedTasks])
                self.content('https://www.xuanshu.com' + self.novelData[self.novelName] + i)
                self.completedTasks = self.completedTasks + 1
                print("当前总进度：" + str('{:.20%}'.format(self.completedTasks / self.totalTasks)))
        else:
            import _thread

            a = list(downloadDict.values())
            childNum_a = len(a) // self.threadsNum
            list_of_groups = zip(*(iter(a),) * childNum_a)
            end_list_a = [list(i) for i in list_of_groups]
            if len(a) != 0:
                count = len(a) % childNum_a
            else:
                print(a)
                print('erro:章节链接列表为空')
                exit()
            end_list_a.append(a[-count:]) if count != 0 else end_list_a

            b = list(downloadDict.keys())
            childNum_b = len(b) // self.threadsNum
            list_of_groups = zip(*(iter(b),) * childNum_b)
            end_list_b = [list(i) for i in list_of_groups]
            if len(b) != 0:
                count = len(b) % childNum_b
            else:
                print(b)
                print('erro:章节名称列表为空')
                exit()
            end_list_b.append(b[-count:]) if count != 0 else end_list_b

            m=0
            partList = []
            for i in end_list_b:
                print(end_list_b[m])
                print(end_list_a[m])
                partDict = dict(zip(end_list_b[m],end_list_a[m]))
                partList.append(partDict)
                m=m+1

            print('即将开始多线程下载，线程数：' + str(len(end_list_a)))

            try:
                for i in range(self.threadsNum):
                    exec(
                        'thread%s=myThread(%s,"Thread-%s", %s,partList[%s],sleepTime)' % (i, i, i, i, i)
                    )
                    exec(  # 开启新线程
                        'thread%s . start()' % i
                    )
                    exec(  # 添加线程到线程列表
                        'self.threadsName.append(thread%s)' % i
                    )
                    eval("%s" % i)
            except Exception as e:
                import traceback
                print("Error: 无法启动线程")
                print(e)
                # 这个是输出错误类别的，如果捕捉的是通用错误，其实这个看不出来什么
                print('str(Exception):\t', str(Exception))
                # 这个是输出错误的具体原因
                print('str(e):\t\t', str(e))
                print('repr(e):\t', repr(e)) # 输出 repr(e):
                #输出位置
                print('traceback.print_exc():')
                print(traceback.print_exc())
                print('traceback.format_exc():\n%s' %traceback.format_exc())

                # 等待所有线程完成
            for t in self.threadsName:
                t.join()
            print("退出主线程")


import threading
import time

threadLock = threading.Lock()

class myThread (threading.Thread):
    def __init__(self, threadID, name, counter,partDict,sleepTime):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.partDict = partDict
        self.sleepTime = sleepTime

    def run(self):
        import random
        print("开启线程： " + self.name)
        xuanshuwang._theBehavior(self.partDict,self.sleepTime)

if __name__ == '__main__':
    xuanshuwang = homePage()
    xuanshuwang.recommend('https://www.xuanshu.com/sort1/1.html','utf-8')
