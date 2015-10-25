#!/usr/bin/python
# coding:utf-8

import requests
from bs4 import BeautifulSoup


host = 'http://www.hunantv.com'
_url = 'http://list.hunantv.com/album/18.html'
query = ""


def get_href_list(url):
    r = requests.get(url)
    if str(r.status_code).startswith('2'):
        soup = BeautifulSoup(r.text, "lxml")
        ul = soup.find('ul', class_='clearfix ullist-ele')
        li = ul.find_all('li', limit=10)
        items = []
        for l in li:
            item = {}
            item['title'] = l.find('span',
                                   class_='a-pic-t2').text.encode("utf-8")
            item['time'] = l.find('span',
                                  class_='a-pic-t1').text.encode('utf-8')
            a = l.find('a', class_='a-pic-play')
            item['href'] = a.attrs['href']
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

