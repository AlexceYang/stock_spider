# -*- coding: utf-8 -*-
import scrapy


class TonghuashunSpider(scrapy.Spider):
    name = 'tonghuashun'
    #  http://basic.10jqka.com.cn/600004/company.html
    allowed_domains = ['stockpage.10jqka.com.cn/600004/company/#detail']
    start_urls = ['http://basic.10jqka.com.cn/600004/company.html']

    def parse(self, response):
        #  //*[@id="ml_001"]/table/tbody/tr[1]/td[1]/a
        #  //*[@id="ml_001"]/table/tbody/tr[1]/td[1]/a
        res_selector = response.xpath("//*[@id=\"ml_001\"]/table/tbody/tr[1]/td[1]/a/text()")
        name = res_selector.extract()
        # print(name)

        tc_names = response.xpath("//*[@class=\"tl\"]/text()").extract()
        for tc_name in tc_names:
            print(tc_name)




"""
动态页面：我的页面数据是从数据库或者其他地方得到的，然后渲染的页面

静态页面：所见即所得
"""
