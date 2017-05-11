# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import TutorialItem


class AcfunSpiderSpider(scrapy.Spider):
    name = "acfun_spider"
    allowed_domains = ["http://www.acfun.cn/"]

    # url = "http://www.acfun.cn/v/list110/index.htm"

    def start_requests(self):
        start_index = 1
        end_index = 2
        url_format = 'http://www.acfun.cn/v/list110/index_{0}.htm'
        for index in range(start_index, end_index):
            yield scrapy.Request(url_format.format(index), self.parse)

    def parse(self, response):
        base_url = "http://www.acfun.tv/{0}"
        for a in response.css("a.title"):
            item = TutorialItem()
            item["title"] = a.css("::text").extract_first()
            item["link"] = base_url.format(a.css("::attr('href')").extract_first())
            yield item
