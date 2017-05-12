# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from scrapy.exceptions import DropItem


class TutorialPipeline(object):
    def process_item(self, item, spider):
        return item


class AcfunPipeline(object):
    def __init__(self):
        self.file = open("E:/article.json", "w", encoding="UTF-8")
        self.id_seed = set()

    def open_spider(self, spider):
        pass

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        if item["author"] in self.id_seed:
            raise DropItem("duplicate article_id %s" % item["author"])
        else:
            line = json.dumps(dict(item), ensure_ascii=False) + "\n"
            self.file.write(line)
            self.id_seed.add(item["author"])
        return item
