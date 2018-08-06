import os
import sys

from scrapy.cmdline import execute


# 调试的一个写法
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(['scrapy', 'crawl', 'stock'])
