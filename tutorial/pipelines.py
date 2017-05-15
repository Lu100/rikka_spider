# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import tutorial.persistence


class TutorialPipeline(object):
    def process_item(self, item, spider):
        return item


class AcfunPipeline(object):
    def __init__(self):
        self.file = open("E:/article.json", "w", encoding="UTF-8")

    def open_spider(self, spider):
        pass

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item


class SQLitePipeLine(object):
    def process_item(self, item, spider):
        tutorial.persistence.insert_acfun_item(item)
