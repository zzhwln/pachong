# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb

class FirstPipeline(object):
    def __init__(self):
        self.conn= MySQLdb.connect(
    host='localhost',    # mysql所在主机的ip
    port=3306, 		    # mysql的端口号
    user="root",         # mysql 用户名
    password="000000",   # mysql 的密码
    db="pachong",          # 要使用的库名
    charset="utf8"      # 连接中使用的字符集
)
        self.cursor=self.conn.cursor()
    def process_item(self, item, spider):
        sql = "insert into app01_pac(zhize,url,guimo,zhuying,zhiweidian,xueli,jinyan,gdidian,zhiwei,money,gonshi) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        # sql = "insert into app01_pac(url,guimo,zhuying,zhiweidian,xueli,jinyan,gdidian,money,gonshi) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"


        print('202020')
        # self.cursor.execute(sql,[item['url'],item['guimo'],item['zhuying'],item['zhiweidian'],item['xueli'],item['jinyan'],item['gdidian'],item['money'],item['zhize'],item['gonshi']])
        self.cursor.execute(sql,[item['zhize'],item['url'],item['guimo'],item['zhuying'],item['zhiweidian'],item['xueli'],item['jinyan'],item['gdidian'],item['zhiwei'],item['money'],item['gonshi']])


        self.conn.commit()
        return item
