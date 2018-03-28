#coding:utf-8
import sys

reload(sys)
sys.setdefaultencoding("utf-8")
import urlparse

name = "%E8%BE%89%E5%85%89%E4%B9%8B%E8%BE%B0%2D%E5%90%8E%E7%BE%BF"
s = urlparse.unquote(name)
print s