#coding:utf-8

doc=[":",":",":",u"类型:",u"爱情","/",u"动作",u"制片国家/地区:",u"中国大陆"]

a=[]
b=[]
import re
for i in doc:
    p=re.compile(r'(.*)(:)')
    r=p.search(i)
    if r is None:
        a[0]=a[0] + i
    elif r.group(1) and r.group(2):
        b.append(a)
        a=[i]

b.append(a)
for i in b:
    for j in i:
        print j.encode("utf-8")
