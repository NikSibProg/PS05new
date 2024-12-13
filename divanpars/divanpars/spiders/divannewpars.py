import scrapy


class DivannewparsSpider(scrapy.Spider):
    name = "divannewpars"
    allowed_domains = ["https://divan.ru"]
    start_urls = ["https://https://www.divan.ru/sankt-peterburg/category/divany-i-kresla"]

    def parse(self, response):
        pass
