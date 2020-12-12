import scrapy
from XuanShuSpider.items import XuanShuSpiderItem
from urllib.request import*
import urllib
import requests
import random
class RecommendSpider(scrapy.Spider):
    # 定义spider的名字
    name = 'recommend'
    # 定义允许爬取的域名
    allowed_domains = ['xuanshu.com']
    # 定义爬取的首页列表
    start_urls = ['https://www.xuanshu.com/']

    # 该方法负责爬取response所包含的信息
    def parse(self, response):
        for xiatui in response.xpath('//div[@class="xiatui"]/ul/li/a[1]'):
            item = XuanShuSpiderItem()
            item['source'] = '选书网首页推荐'
            item['name'] = xiatui.xpath('./text()').get()
            item['url'] = 'https://www.xuanshu.com'+ xiatui.xpath('./@href').get()
            a= xiatui.xpath('./@href').get()
            item['picture'] ='http://www.xuanshu.com/tupian/' + a[6:-4] + '/' + a[6:-1] + '/' + a[6:-1] + 's.jpg'
            try:
                header = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) \
                                    AppleWebKit/537.36 (KHTML, like Gecko) \
                                        Chrome/35.0.1916.114 Safari/537.36',
                    'Cookie': 'AspxAutoDetectCookieSupport=1'
                }
                '''
                request = urllib.Request(item['picture'], None, header)
                response = urllib.urlopen(request)'''
                item['imgdata'] = requests.get(item['picture'], headers=header, stream=True).content
                '''with open('I:\\amadeus\LiView\img\\' + str(random.randint(0, 100000)) + '.jpg', 'wb') as f:
                    f.write(item['imgdata'])
                    f.close()'''
            except Exception as e:
                print('下载图片出现错误' % item['picture'])
                print(e)
                item['imgdata'] = None
            yield item

        for zuixin  in  response.xpath('//div[@class="zuixin"]/ul/li/div[@class="xname"]/a[1]'):
            item = XuanShuSpiderItem()
            item['source'] = '选书网首页推荐'
            item['name'] = zuixin.xpath('./text()').get()
            item['url'] = zuixin.xpath('./@href').get()
            a = zuixin.xpath('./@href').get()
            item['picture'] = 'http://www.xuanshu.com/tupian/' + a[28:-4] + '/' + a[28:-1] + '/' + a[28:-1] + 's.jpg'
            try:
                header = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) \
                                    AppleWebKit/537.36 (KHTML, like Gecko) \
                                        Chrome/35.0.1916.114 Safari/537.36',
                    'Cookie': 'AspxAutoDetectCookieSupport=1'
                }
                '''
                request = urllib.Request(item['picture'], None, header)
                response = urllib.urlopen(request)'''
                item['imgdata'] = requests.get(item['picture'], headers=header, stream=True).content
                '''with open('I:\\amadeus\LiView\img\\' + str(random.randint(0, 100000)) + '.jpg', 'wb') as f:
                    f.write(item['imgdata'])
                    f.close()'''
            except Exception as e:
                print('下载图片出现错误' % item['picture'])
                print(e)
                item['imgdata'] = None
            yield item

        for paihang  in  response.xpath('//div[@class="paihang"]/ul[@class="ultop"]/li/a[1]'):
            item = XuanShuSpiderItem()
            item['source'] = '选书网首页推荐'
            item['name'] = paihang.xpath('./text()').get()
            item['url'] = paihang.xpath('./@href').get()
            a = paihang.xpath('./@href').get()
            item['picture'] = 'http://www.xuanshu.com/tupian/' + a[28:-4] + '/' + a[28:-1] + '/' + a[28:-1] + 's.jpg'
            try:
                header = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) \
                    AppleWebKit/537.36 (KHTML, like Gecko) \
                        Chrome/35.0.1916.114 Safari/537.36',
                    'Cookie': 'AspxAutoDetectCookieSupport=1'
                }
                '''
                request = urllib.Request(item['picture'], None, header)
                response = urllib.urlopen(request)'''
                item['imgdata'] = requests.get(item['picture'], headers=header, stream=True).content
                '''with open('I:\\amadeus\LiView\img\\'+ str(random.randint(0,100000)) +'.jpg', 'wb') as f:
                    f.write(item['imgdata'])
                    f.close()'''
            except Exception as e:
                print('下载图片出现错误' % item['picture'])
                print(e)
                item['imgdata'] = None

            yield item



