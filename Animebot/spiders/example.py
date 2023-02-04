import scrapy


class GamerSpider(scrapy.Spider):
    name = "gamer"
    allowed_domains = ["ani.gamer.com.tw"]
    start_urls = ["https://ani.gamer.com.tw/"]

    def parse(self, response):
        title = response.xpath("//p[@class='theme-name']/text()").getall()
        print(title)