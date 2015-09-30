# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

# import MySQLdb
import psycopg2
# 数据库连接参数
conn = psycopg2.connect(database="basedb", user="postdb", password="postdb", host="127.0.0.1", port="5432")


class DoubanmoviePipeline(object):

    def process_item(self, item, spider):
        self._save(item)
        return item

    def open_spider(self, spider):
        ## self.conn = MySQLdb.connect(
        ##         host="localhost",
        ##         port=3306,
        ##         db="movie",
        ##         user="root",
        ##         passwd="myroot",
        ##         charset="utf8"
        ##         )
        self.conn = conn = psycopg2.connect(database="basedb",
                                            user="postdb",
                                            password="postdb",
                                            host="127.0.0.1",
                                            port="5432")
        self.cur = self.conn.cursor()

    def close_spider(self, spider):
        self.cur.close()
        self.conn.commit()
        self.conn.close()

    def _save(self, item):
        sqlv = "select 1 from t_movie where m_id='%s'" % item["mid"]
        self.cur.execute(sqlv)
        result = self.cur.fetchone()
        if not result:
            act = self._gen(item['act'])
            drc = self._gen(item['drc'])
            scw = self._gen(item['scw'])

            sqli = "insert into t_movie values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"
            sqli = sqli % (item['mid'],item['name'][0].replace("'"," "),item['year'][0],drc.replace("'"," "),
                    scw.replace("'"," "),act.replace("'",""),item['genre'],item['ct_area'].replace("'"," "),
                    item['language'],item['release_dt'],item['runtime'].replace("'",""),item['alias'].replace("'"," "),item['rating'][0],item['votes'][0])
            self.cur.execute(sqli)
            self.conn.commit()


    def _gen(self, ads_list):
        ads = ''
        len_ads = len(ads_list)
        for i in xrange(len_ads):
            ads+=ads_list[i]
            if i < len_ads-1:
                ads+='/'
        return ads
