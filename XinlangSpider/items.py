# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class XinlangspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    parentTitle = scrapy.Field()
    parentUrls = scrapy.Field()

    subTitle = scrapy.Field()
    subUrls = scrapy.Field()

    subFileName = scrapy.Field()

    sonUrls = scrapy.Field()
    sonTitle = scrapy.Field()
    sonContent = scrapy.Field()


