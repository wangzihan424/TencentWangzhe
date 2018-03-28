# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


# class WangzhespiderPipeline(object):
#     def process_item(self, item, spider):
#         return item
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy import Request
import json
import codecs

class JsonWithEncodingPipeline(object):

    def __init__(self):
        self.file = codecs.open('wangzhe.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item

    def spider_closed(self, spider):
        self.file.close()

class DownloadImagesPipeline(ImagesPipeline):
    def get_media_requests(self,item,info): #下载图片
        for image_url in item['img_url']:
            yield Request(image_url,meta={'item':item}) #添加meta是为了下面重命名文件名使用

    def file_path(self,request,response=None,info=None):
        item=request.meta['item'] #通过上面的meta传递过来item
        image_guid = item['heros_name']+'.'+"jpg"
        filename = u'full/{0}'.format(image_guid)
        return filename