import scrapy
import json
from ..items import FirstItem

class Zhilians(scrapy.Spider):
    name = 'zl'
    def __init__(self):
        self.cookie={'at':'214c58f1403b4bac8b0231cf95ee35af'}
    #发送请求
    def start_requests(self):
        for citys in ['489','530', '538', '765', '763', '531', '801', '653', '736', '600', '613', '635', '702', '703', '639',
                 '599', '854', '719', '749', '551', '622', '636', '654', '681', '682', '565', '664', '773']:
            for kws in ['实习','林','其它','农','跨领域经营','政府','学术','水电','能源','化工','环保','仓库','运输','自动化','加工','设备','办公','休闲','媒体','娱乐','保健','卫生','护理','医疗','酒店','翻译','度假','旅游','培训','教育','消费','贸易','批发','外包','中介','广告','设计','家具','建筑','房地产','基金','银行','保险','网络','通信','计算机软件','网络游戏','互联网','电子','计算机硬件','IT服务','AI', '爬虫', 'python', 'web开发', '大数据', '数据挖掘与数']:
                url = 'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=' + citys+ '&salary=0,1000000&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=' + kws + '&kt=3&=6001&at=5bcda904de17419c8561921a75da0d97&rt=03087525a03f428ba58a849e4b52d32b&_v=0.24289770&userCode=1014714762&x-zp-page-request-id=28ede8da1850485b94d7250ac57ed262-1560159198492-879556&x-zp-client-id=f95b1816-0c10-4c79-afad-d17d8e985e7e&start=0'

#任何一个带有yield语句的函数都是生成器，当你直接调用这个函数时，内部的代码是不会被执行的，只有调用yield里面的next函数才会去执行代码，for循环也就是会自动去调用这个next函数来输出值。
                #第一次用next()唤醒生成器时，从函数的开头开始运行，遇到yield a，返回a，然后暂停函数，并记住函数是运行到这个位置的。

# 第二次唤醒生成器，从yield a断点处开始，然后a,b开始赋值，while True循环又遇见yield a，返回a，然后暂停函数，并记住函数是运行到这个位置的。
                yield scrapy.Request(url,cookies=self.cookie,dont_filter=True)# 可以return 返回，也可以使用yield将方法变成生成器，由引擎交给调度器
#回调函数（解析列表页响应），接收请求对应的响应
    def parse(self, response):
        data = json.loads(response.text)['data']
        # data=json.loads(response.text)['data']
        datas=data['results']
        count=data['count']
        for ip in datas:
            yield scrapy.Request(url=ip['positionURL'],callback=self.pares1,cookies=self.cookie,dont_filter=True)
        #翻页  发送下一页请求
        dd=response.url.split('&start=')#切割对应的页数
        if int(dd[1])+90<count:
            new_url=dd[0]+'&start='+str(int(dd)+90)
            yield scrapy.Request(new_url,cookies=self.cookie,dont_filter=True)

        # 详情页解析规则
    def pares1(self, resp):
        item = FirstItem()
        print('37')
        title = resp.xpath('//title/text()').extract()[0]
        print(title,'38')
        zhiwei = resp.xpath('//h3[@class="summary-plane__title"]//text()').extract()[0]
        print(zhiwei,'39')
        money = resp.xpath('//span[@class="summary-plane__salary"]/text()').extract()[0]
        zhize = resp.xpath('//div[@class="describtion__detail-content"]//text()').extract()[1]
        gonshi = resp.xpath('//a[@class="company__title"]//text()').extract()[0]
        gdidian = resp.xpath('//span[@class="job-address__content-text"]//text()').extract()[0]
        jinyan = resp.xpath('//ul[@class="summary-plane__info"]//text()').extract()[1]
        xueli = resp.xpath('//ul[@class="summary-plane__info"]//text()').extract()[2]
        print(xueli,'49')
        zhiweidian = resp.xpath('//div[@class="highlights__content"]//text()').extract()[0]
        print(zhiweidian,'51')
        zhuying = resp.xpath('//button[@class="company__industry"]//text()').extract()[0]
        print(zhuying,'52')
        guimo = resp.xpath('//button[@class="company__size"]//text()').extract()[0]
        print(guimo,'53')
        url = resp.xpath('//div[@class="company"]/a/@href').extract()[0]
        print(url,'55')
        item['zhiwei'] = zhiwei
        item['money'] = money
        item['zhize'] = zhize
        item['gonshi'] = gonshi
        print(gonshi,'57')
        item['gdidian'] = gdidian
        item['jinyan'] = jinyan
        item['xueli'] = xueli
        print(zhiweidian,'57')
        item['zhiweidian'] = zhiweidian
        item['zhuying'] = zhuying
        item['guimo'] = guimo
        item['url'] = url

        # return item
        yield item  # 由引擎将item交给pipeline
