# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

#负责爬取的信息
import sqlite3

class XuanShuSpiderPipeline:
    def __init__(self):

        #self.conn = sqlite3.connect('..//..//..//sql//novel.db')
        self.conn = sqlite3.connect('I:\\amadeus\\LiView\\userData\\sql\\novel.db')
        self.cu = self.conn.cursor()

    #重写close_spider回调,用于关闭数据库资源
    def close_spider(self,spider):
        self.cu.close()
        self.conn.close()
    def process_item(self, item, spider):
        if item['name'] != '':
            print('名称：', item['name'])
        else:
            print('名称为空')
        if item['url'] != '':
            print('详细页链接：', item['url'])
        else:
            print('详细页链接为空')
        if item['picture'] != '':
            print('图片链接：', item['picture'])
        else:
            print('图片链接链接为空')
        if item['name'] != '' and item['name'] != None and item['url'] != '' and item['url'] != None:    #名称和详情链接不能为空
            if item['picture'] == '':
                picture = None
                img = None
            else:
                picture = item['picture']
                img = item['imgdata']
            source = item['source']
            name= item['name']
            url = item['url']

            #存入数据库
            self.cu.execute("INSERT INTO novelIndex VALUES (?,?,?,?,?,?)",(None,name,source,url,picture,img))
            self.conn.commit()

