# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding("utf-8")
import scrapy
import urlparse,json,urllib
from ..items import WangzhespiderItem



class WangzheSpider(scrapy.Spider):
    name = 'wangzhe'
    allowed_domains = ['pvp.qq.com']
    start_urls = ['http://apps.game.qq.com/cgi-bin/ams/module/ishow/V1.0/query/workList_inc.cgi?activityId=2735&sVerifyCode=ABCD&sDataType=JSON&iListNum=20&totalpage=0&page=1&iOrder=0&iSortNumClose=1&jsoncallback=jQuery17105366497514242182_1522197218777&iAMSActivityId=51991&_everyRead=true&iTypeId=2&iFlowId=267733&iActId=2735&iModuleId=2735&_=1522199360298']

    def start_requests(self):
        for x in xrange(1,14):
            url = "http://apps.game.qq.com/cgi-bin/ams/module/ishow/V1.0/query/workList_inc.cgi?activityId=2735&sVerifyCode=ABCD&sDataType=JSON&iListNum=20&totalpage=0&page={0}&iOrder=0&iSortNumClose=1&jsoncallback=jQuery17105366497514242182_1522197218777&iAMSActivityId=51991&_everyRead=true&iTypeId=2&iFlowId=267733&iActId=2735&iModuleId=2735&_=1522199360298".format(str(x))
            yield scrapy.Request(url=url,callback=self.parse,dont_filter=True)
    def parse(self, response):
        s = response.body.split("(")
        a = s[1].split(")")
        js = json.loads(a[0])
        for ob in js["List"]:
            jsRet = ob["sProdImgNo_3"]
            new_url = urlparse.unquote(jsRet)
            new_url = new_url.replace("/200","/0")
            heros_name = ob["sProdName"]
            heros_name = str(heros_name)
            heros_name = urlparse.unquote(heros_name)
            print heros_name
            yield scrapy.Request(url=new_url,callback=self.picture,dont_filter=True,meta={"heros_name":heros_name})
    def picture(self,response):
        img_url = response.url
        heros_name = response.meta["heros_name"]
        item = WangzhespiderItem()
        item["img_url"] = [img_url]
        item["heros_name"] = heros_name
        return item




