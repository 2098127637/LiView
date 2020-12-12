# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
#用于定义项目

import scrapy


class XuanShuSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    '''爬取首页内容爬虫需要的属性'''
    # 书名
    name = scrapy.Field()
    #书籍章节目录链接
    url = scrapy.Field()
    # 书籍封面图片链接
    picture = scrapy.Field()
    # 书籍封面数据
    imgdata = scrapy.Field()

    # 书籍类型
    bookType = scrapy.Field()
    # 书籍作者
    author = scrapy.Field()
    # 书籍介绍
    introduce = scrapy.Field()
    # 书籍评分
    score = scrapy.Field()
    # 书籍评价
    evaluate = scrapy.Field()
    # 书籍来源
    source = scrapy.Field()
    '''爬取单一书籍爬虫所需要的属性'''
    #书籍章节名称
    chapterName = scrapy.Field()
    #书籍章节链接
    chapterUrl = scrapy.Field()




