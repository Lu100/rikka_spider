# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import AcfunArticleItem
from bs4 import BeautifulSoup


class AcfunSpiderSpider(scrapy.Spider):
    name = "acfun_spider"
    allowed_domains = ["http://www.acfun.cn/"]
    base_url = "http://www.acfun.cn"

    # url = "http://www.acfun.cn/v/list110/index.htm"

    def start_requests(self):
        start_index = 1
        end_index = 16
        url_format = 'http://www.acfun.cn/v/list110/index_{0}.htm'
        for index in range(start_index, end_index):
            # 在获取评论时，需要使用其他的解释方法，或者新开一只爬虫
            yield scrapy.Request(url_format.format(index), self.parse)

    def parse(self, response):
        bs = BeautifulSoup(response.body, features="lxml")
        for div in bs.find(id="block-content-article").find_all("div", class_="item"):
            item = AcfunArticleItem()
            # 想要获取时间
            item["publish_date"] = div.find("a", class_="title").get("title")
            item["hint_comment"] = div.find("a", class_="hint-comm-article").get("title")
            item["title"] = div.find("a", class_="title").string
            item["author"] = div.find(class_="article-info").find(class_="name").string
            item["introduction"] = div.find("div", class_="desc").string
            item["link"] = self.base_url + div.find("a", class_="title").get("href")
            item["article_id"] = item["link"].split("/")[-1]
            yield item
