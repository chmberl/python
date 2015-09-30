#coding:utf-8

import scrapy
from scrapy.selector import Selector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor as sgml
from doubanmovie.items import DoubanmovieItem
import re

class MovieSpider(CrawlSpider):
    name = "doubanmovie"
    allowed_domains = ["movie.douban.com"]

    start_urls = ["http://movie.douban.com/top250"]

    rules = [
            Rule(sgml(allow=(r'http://movie.douban.com/top250\?start=\d+.*'))),
            Rule(sgml(allow=(r'http://movie.douban.com/subject/\d+/'),
                      deny=r'http://movie.douban.com/subject/\d+/\w+'),callback="parse_item", follow=True),
            Rule(sgml(allow=(r'http://movie.douban.com/subject/\d+/\?from.*')),callback="parse_item", follow=True),
    ]

    def parse_item(self, response):
        sel = Selector(response)
        itemMovie = DoubanmovieItem()
        url = response.url.split("?",2)[0]
        print response.url
        pattern = re.compile(r'(?<=com/subject/)(\d+)')
        num = pattern.search(url)
        if num is not None:
            itemMovie['mid']= num.group()
        itemMovie['name']=sel.xpath('//*[@id="content"]/h1/span[1]/text()').extract()
        itemMovie['year']=sel.xpath('//*[@id="content"]/h1/span[2]/text()').re(r'\((\d+)\)')
        itemMovie['drc']=sel.xpath('//a[@rel="v:directedBy"]/text()').extract()
        itemMovie['scw']=sel.xpath('//*[@id="info"]/span[2]/span[2]/a/text()').extract()
        itemMovie['act']=sel.xpath('//a[@rel="v:starring"]/text()').extract()
        #itemMovie['genre']=sel.xpath('//span[@property="v:genre"]/text()').extract()
        item_info = sel.xpath('//*[@id="info"]/text()[normalize-space()] | //*[@id="info"]/span/text()').extract()
        item_info = self._gen(item_info)
        try:
            itemMovie['genre'] = item_info[0][0].split(':',2)[1]
            itemMovie['ct_area']=item_info[1][0].split(':',2)[1]
            itemMovie['language'] = item_info[2][0].split(':',2)[1]
            itemMovie["release_dt"]=item_info[3][0].split(':',2)[1]
            itemMovie["runtime"] = item_info[4][0].split(':',2)[1]
        except:
            if itemMovie['genre'] is None:
                itemMovie['genre'] = ""
            if itemMovie['ct_area'] is None:
                itemMovie['ct_area'] = ""
            if itemMovie['language'] is None:
                itemMovie['language'] = ""
            if itemMovie["release_dt"] is None:
                itemMovie["release_dt"] = ""
            if itemMovie["runtime"] is None:
                itemMovie["runtime"] = ""

        if len(item_info) > 5:
            itemMovie["alias"] = item_info[5][0].split(':',2)[1]
        else:
            itemMovie["alias"]= ""
        itemMovie["rating"] = sel.xpath('//*[@id="interest_sectl"]/div/p[1]/strong/text()').extract()
        itemMovie["votes"] = sel.xpath('//*[@id="interest_sectl"]/div/p[2]/a/span/text()').extract()
        return itemMovie

    def _gen(self, doc_list):
        a=[]
        b=[]
        for i in doc_list:
            p=re.compile(r'(.*)(:)')
            r=p.search(i)
            if r is None:
                a[0]=a[0] + i.replace(" ","")
            elif r.group(1) and r.group(2):
                b.append(a)
                a=[i]
        b.append(a)
        p = re.compile(r'.+:.+')
        c=[]
        for j in b:
            for i in j:
                if p.match(i):
                    c.append([i])
        return c


class MovieDoubanSpider(CrawlSpider):
    name = "moviedouban"
    allowed_domains = ["movie.douban.com", "www.douban.com"]

    start_urls = ["http://www.douban.com/tag/2014/?focus=movie"]

    rules = [
            Rule(sgml(allow=(r'http://movie.douban.com/\?start=\d+.*'))),
            Rule(sgml(allow=(r'http://movie.douban.com/tag/\w+'))),
            Rule(sgml(allow=(r'http://www.douban.com/tag/\w+'))),
            Rule(sgml(allow=(r'http://movie.douban.com/subject/\d+/'),
                      deny=r'http://movie.douban.com/subject/\d+/\w+'),callback="parse_item", follow=True),
            Rule(sgml(allow=(r'http://movie.douban.com/subject/\d+/\?from.*')),callback="parse_item", follow=True),
    ]

    def parse_item(self, response):
        sel = Selector(response)
        itemMovie = DoubanmovieItem()
        url = response.url.split("?",2)[0]
        print response.url
        pattern = re.compile(r'(?<=com/subject/)(\d+)')
        num = pattern.search(url)
        if num is not None:
            itemMovie['mid']= num.group()
        itemMovie['name']=sel.xpath('//*[@id="content"]/h1/span[1]/text()').extract()
        itemMovie['year']=sel.xpath('//*[@id="content"]/h1/span[2]/text()').re(r'\((\d+)\)')
        itemMovie['drc']=sel.xpath('//a[@rel="v:directedBy"]/text()').extract()
        itemMovie['scw']=sel.xpath('//*[@id="info"]/span[2]/span[2]/a/text()').extract()
        itemMovie['act']=sel.xpath('//a[@rel="v:starring"]/text()').extract()
        #itemMovie['genre']=sel.xpath('//span[@property="v:genre"]/text()').extract()
        item_info = sel.xpath('//*[@id="info"]/text()[normalize-space()] | //*[@id="info"]/span/text()').extract()
        item_info = self._gen(item_info)
        itemMovie['genre'] = item_info[0][0].split(':',2)[1]
        itemMovie['ct_area']=item_info[1][0].split(':',2)[1]
        try:
            itemMovie['language'] = item_info[2][0].split(':',2)[1]
            itemMovie["release_dt"]=item_info[3][0].split(':',2)[1]
            itemMovie["runtime"] = item_info[4][0].split(':',2)[1]
        except:
            itemMovie['language'] = ""
            itemMovie["release_dt"] = ""
            itemMovie["runtime"] = ""

        if len(item_info) > 5:
            itemMovie["alias"] = item_info[5][0].split(':',2)[1]
        else:
            itemMovie["alias"]= ""
        itemMovie["rating"] = sel.xpath('//*[@id="interest_sectl"]/div/p[1]/strong/text()').extract()
        itemMovie["votes"] = sel.xpath('//*[@id="interest_sectl"]/div/p[2]/a/span/text()').extract()
        return itemMovie

    def _gen(self, doc_list):
        a=[]
        b=[]
        for i in doc_list:
            p=re.compile(r'(.*)(:)')
            r=p.search(i)
            if r is None:
                a[0]=a[0] + i.replace(" ","")
            elif r.group(1) and r.group(2):
                b.append(a)
                a=[i]
        b.append(a)
        p = re.compile(r'.+:.+')
        c=[]
        for j in b:
            for i in j:
                if p.match(i):
                    c.append([i])
        return c

