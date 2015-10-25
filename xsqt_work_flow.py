#!/usr/bin/python
# coding:utf-8

import requests
from bs4 import BeautifulSoup


_url = 'http://www.iqiyi.com/a_19rrgifngp.html'

query = ""


def get_href_list(url):
    r = requests.get(url)
    if str(r.status_code).startswith('2'):
        soup = BeautifulSoup(r.text, "lxml")
        ul = soup.find(id='albumpic-showall-wrap')
        a_list = ul.find_all('a', class_='site-piclist_pic_link', limit=10)
        items = []
        for href in a_list:
            item = {}
            item['href'] = href.attrs['href']
            img = href.find('img')
            item['title'] = img.attrs['title'].encode('utf-8')
            item['time'] = href.find('span',
                                     class_='mod-listTitle_right').text.encode('utf-8')
            items.append(item)
        return items
    else:
        return None


def to_wf_xml(items):
    print "<?xml version=\"1.0\"?>\n<items>"
    for item in items:
        print " <item uid=\"" + item['title'] + "\" arg=\"" + item['href'] + "\">"
        print " <title>" + item['title'] + "</title>"
        print " <subtitle>" + item['time'] + "</subtitle>"
        print " <icon>icon.png</icon>"
        print " </item>"
    if not items:
        print "<item uid=\"Not Found\" arg=\"\" >"
        print "   <title>No Match!</title>"
        print "   <subtitle>Connot find " + query + "</subtitle>"
        print "</item>"
    print "</items>"

items = get_href_list(_url)
to_wf_xml(items)
