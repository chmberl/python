# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanmovieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    mid = scrapy.Field()
    name = scrapy.Field()
    year = scrapy.Field()
    drc = scrapy.Field()
    scw = scrapy.Field()
    act = scrapy.Field()
    genre = scrapy.Field()
    ct_area = scrapy.Field()
    language = scrapy.Field()
    release_dt = scrapy.Field()
    runtime = scrapy.Field()
    alias = scrapy.Field()
    rating = scrapy.Field()
    votes = scrapy.Field()

class DoubancelebrityItem(scrapy.Item):
    cid = scrapy.Field()
    role = scrapy.Field()
    name = scrapy.Field()
    gender = scrapy.Field()
    cons = scrapy.Field()
    birthday = scrapy.Field()
    birthplace = scrapy.Field()
    job = scrapy.Field()
    family = scrapy.Field()
    nickname = scrapy.Field()

