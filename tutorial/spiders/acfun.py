# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import TutorialItem


class AcfunSpider(scrapy.Spider):
    name = "acfun"
    allowed_domains = ["www.acfun.tv"]
    start_urls = ['http://www.acfun.cn/v/list110/index.htm']

    def parse(self, response):
        aTags = response.css("a.title")
        for a in aTags:
            item = TutorialItem()
            item["title"] = a.css("::text").extract()
            item["link"] = a.css("::attr(href)").extract()
            yield item
