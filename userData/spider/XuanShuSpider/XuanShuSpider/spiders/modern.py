import scrapy
from XuanShuSpider.items import XuanShuSpiderItem
import requests

class ModernSpider(scrapy.Spider):
    name = 'modern'
    allowed_domains = []
    start_urls = ['https://www.xuanshu.com/soft/sort04/']

    def __init__(self):
        self.num = 2

    def parse(self, response):
        for listBox in response.xpath('//div[@class="listBox"]/ul/li/a[1]'):
            item = XuanShuSpiderItem()
            item['source'] = '选书网现代都市'
            item['name'] = listBox.xpath('./text()').get()
            item['url'] = 'https://www.xuanshu.com' + listBox.xpath('./@href').get()
            item['picture'] = 'https://www.xuanshu.com' + listBox.xpath('./img/@src').get()
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

        next_page = 'https://www.xuanshu.com/soft/sort04/index_' + str(self.num) + '.html'
        self.num = self.num + 1
        if next_page is not None:
            print(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
