import scrapy


class GamerSpider(scrapy.Spider):
    name = "gamer"
    allowed_domains = ["ani.gamer.com.tw"]
    start_urls = ["https://ani.gamer.com.tw/"]

    def parse(self, response):
        name = response.css('div.theme-info-block p::text').get()
        print(name)