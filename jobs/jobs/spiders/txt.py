import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'https://english.thesaigontimes.vn/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        title = response.xpath("//h3[@class='entry-title td-module-title']/a/text()").get()
        date = response.xpath("//time[@class='entry-date updated td-module-date']/text()").get()
        content = response.xpath("//div[@class='td-module-meta-info td-module-meta-info-bottom']/div[@class='td-excerpt']/text()").get()
        print("Title"+title)
        print("Date"+date)
        print("Content"+content)
        