#coding:utf-8
import sys
from scrapy import cmdline
reload(sys)
sys.setdefaultencoding("utf-8")

cmdline.execute(['scrapy','crawl','wangzhe'])
