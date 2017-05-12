# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    pass


class AcfunArticleItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    author = scrapy.Field()
    article_id = scrapy.Field()
    publish_date = scrapy.Field()
    introduction = scrapy.Field()
    hint_comment = scrapy.Field()
