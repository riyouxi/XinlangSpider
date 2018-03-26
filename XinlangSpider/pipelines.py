# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class XinlangspiderPipeline(object):

    def process_item(self, item, spider):
        sonurls = item['sonUrls']
        filename = sonurls[7:-6].replace('/','_')
        filename+='.txt'

        fp = open(item['subFileName']+"/"+filename,'w')
        fp.write(item['sonContent'])
        fp.close()
        return item
