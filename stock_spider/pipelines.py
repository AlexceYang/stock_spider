# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os


class StockSpiderPipeline(object):
    def process_item(self, item, spider):
        return item


class StockPipeline(object):

    def __init__(self):
        # 类被加载时自动创建一个文件
        self.file = open("executive_prep.csv", 'a+')
        # a+ 拿到文件的读写权限，如果没有在追加写

    def process_item(self, item, spider):
        # 判断文件是否为空，为空写：高管姓名，性别，年龄，股票代码，职位
        # 不为空就追加文件
        if os.path.getsize("executive_prep.csv"):
            self.write_content(item)
        else:
            self.file.write("高管姓名,性别,年龄,股票代码,职位\n")

        self.file.flush()
        return item

    def write_content(self, item):
        names = item["names"]
        sexes = item["sexes"]
        ages = item["ages"]
        codes = item["codes"]
        leaders = item["leaders"]

        for i in range(len(names)):
            result = names[i] + ',' + sexes[i] + ',' + ages[i] + ',' + \
                     codes[i] + ','
            if ',' in leaders[i]:
                self.file.write(result + "\"" + leaders[i] + "\"" + '\n')
            else:
                self.file.write(result + leaders[i] + '\n')



