
import scrapy
import os
from scrapy.spiders import Spider
from  XinlangSpider.items import XinlangspiderItem

class XinlangSpider(Spider):

    name = "xinlang"
    allow_domains=['news.sina.com.cn/']

    start_urls = ['http://news.sina.com.cn/guide/']

    def parse(self, response):

        items=[]
        parentUrls = response.xpath('//div[@id="tab01"]//h3/a/@href').extract()
        parentTitle = response.xpath('//div[@id="tab01"]//h3/a/text()').extract()

        subUrls = response.xpath('//div[@id="tab01"]//ul[@class="list01"]//a/@href').extract()
        subTitle = response.xpath('//div[@id="tab01"]//ul[@class="list01"]//a/text()').extract()

        for i in range(0,len(parentTitle)):
            parentFileName = "Data/"+parentTitle[i]
            print(parentFileName)
            if(not os.path.exists(parentFileName)):
                os.makedirs(parentFileName)

            for j in range(0,len(subTitle)):

                item = XinlangspiderItem()
                item['parentUrls'] = parentUrls[i]
                item['parentTitle'] = parentTitle[i]

                if_belong = subUrls[j].startswith(item['parentUrls'])
                if(if_belong):
                    subFileName = parentFileName+"/"+subTitle[j]
                    if(not os.path.exists(subFileName)):
                        os.makedirs(subFileName)

                    item['subTitle'] = subTitle[j]
                    item['subUrls'] = subUrls[j]
                    item['subFileName'] = subFileName

                    items.append(item)

        for item in items:
            yield scrapy.Request(url=item['subUrls'],meta={'meta_1':item},callback=self.second_parse)


    def second_parse(self,response):
        meta_1 = response.meta['meta_1']
        sonUrls = response.xpath('//a/@href').extract()
        items =[]
        for i in range(0,len(sonUrls)):
            if_belong = sonUrls[i].endswith('.shtml') and sonUrls[i].startswith(meta_1['parentUrls'])
            if(if_belong):
                item = XinlangspiderItem()
                item['parentTitle'] = meta_1['parentTitle']
                item['parentUrls'] = meta_1['parentUrls']
                item['subTitle'] = meta_1['subTitle']
                item['subFileName'] = meta_1['subFileName']
                item['subUrls'] = meta_1['subUrls']
                item['sonUrls'] = sonUrls[i]
                items.append(item)


        for item in items:
            yield scrapy.Request(url=item['sonUrls'],meta={'meta_2':item},callback=self.detail_parse)

    def detail_parse(self,response):

        item = response.meta['meta_2']
        content = ""
        head = response.xpath('//h1[@class="main-title"]/text()').extract()
        content_list = response.xpath('//div[@class="article"]/p/text()').extract()

        for content_one in content_list:
            content+=content_one

        item['sonTitle'] = head
        item['sonContent'] = content
        yield item




