import re
import json
from urlparse import urlparse
import urllib


from scrapy.selector import Selector
try:
    from scrapy.spider import Spider
except:
    from scrapy.spider import BaseSpider as Spider
from scrapy.utils.response import get_base_url
from scrapy.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor as sle


from test01.items import *

class spider01(Spider):
    name = "test01"
    allowed_domains = ["itjuzi.com"]
    start_urls = ["http://www.itjuzi.com/investor/%d" %i for i in range(10)]
    
    def parse(self, response):
        sel = Selector(response)
        filename = response.url.split("/")[-1] + '.html'
        print filename
	item = Test01Item()
	item['title'] = sel.css('div.public-info.pull-left p a::text').extract()[0]
	print item['title']
	with open(filename, 'wb') as f:
            f.write(response.body)

