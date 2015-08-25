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

class spider01(CrawlSpider):
    name = "test01"
    allowed_domains = ["itjuzi.com"]
    start_urls = [
        "http://www.itjuzi.com",
	#"http://www.itjuzi.com/investor"
    ]
    rules = [
        Rule(sle(allow=("/investor/[0-9]*$")), callback='parse'),
        #Rule(sle(allow=("/topsites/category/Top$", )), callback='parse_category_top', follow=True),
        #Rule(sle(allow=("/people/[^/]+$", )), callback='parse_people', follow=True),
    ]

    def parse(self, response):
        filename = response.url.split("/")[-1] + '.html'
        print filename
	with open(filename, 'wb') as f:
            f.write(response.body)

