import scrapy


class SearchSpider(scrapy.Spider):
    name = 'search'
    allowed_domains = []
    start_urls = ['https://www.xuanshu.com/search.php']
    def __init__(self):
        data = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
                'Cache-Control': 'max-age=0',
                'Connection': 'keep-alive', 'Content-Length': 37,
                'Content-Type': 'application/x-www-form-urlencoded',
                'Cookie': 'obj=1',
                'Host': 'www.xuanshu.com',
                'Origin': 'https://www.xuanshu.com',
                'Referer': 'https://www.xuanshu.com/',
                'Upgrade-Insecure-Requests': 1,
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0',
                'searchkey': "我"}
        import requests
        url = "https://www.xuanshu.com/search.php"
        res = requests.post(url=url, data=data)
        html = res.content.decode(encoding='UTF-8', errors='strict')
        selector = scrapy.Selector(text=html)
        for result in selector.xpath('//table[@class = "grid"]/tr/td[@class="even"]/a/@href').getall():
            yield scrapy.Request(result, callback=self.parse)

    def parse(self, response):
        pass
