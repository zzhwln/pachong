# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FirstItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    print('141414')
    zhiwei = scrapy.Field()  # 职位
    money = scrapy.Field()  # 工资
    zhize = scrapy.Field()  # 职责
    gonshi = scrapy.Field()  # 公司
    gdidian = scrapy.Field()  # 工作地点
    jinyan = scrapy.Field()  # 经验
    xueli = scrapy.Field()  # 学历
    zhiweidian = scrapy.Field()  # 职位亮点
    zhuying = scrapy.Field()  # 主营
    guimo = scrapy.Field()  # 规模
    url = scrapy.Field()  # ip
