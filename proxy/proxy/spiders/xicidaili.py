# -*- coding: utf-8 -*-
import scrapy
from proxy.items import ProxyItem
from scrapy.http import Request


class XicidailiSpider(scrapy.Spider):
    name = 'xicidaili'
    allowed_domains = ['xicidaili.com']
    start_urls = ['https://www.xicidaili.com']

    def parse(self, response):
        # pass
        res_main = response.xpath('//table[@id="ip_list"]')
        # res_page = response.xpath('//div[@id="listnav"]/ul/li[last()-1]/a/text()').extract()[0]
        # print(res_page)
        data = ProxyItem()
        data['name'] = '西刺代理'
        data['ip'] = res_main.xpath('./tr/td[2]/text()').extract()
        data['port'] = res_main.xpath('./tr/td[3]/text()').extract()
        data['protocol'] = res_main.xpath('./tr/td[6]/text()').extract()
        data['anonymity'] = res_main.xpath('./tr/td[5]/text()').extract()
        data['area'] = res_main.xpath('./tr/td[4]/text()').extract()
        yield data
        # print(data['name'], data['ip'], data['port'], data['protocol'], data['anonymity'], data['area'])

        # for i in range(2,int(res_page_result)+1):
        #     url='http://www.ip3366.net/?stype=1&page={}'.format(i)
        #     # print(url)
        #     yield  Request(url,callback=self.parse)


