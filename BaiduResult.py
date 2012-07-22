#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
百度关键词排名
By Jibo He @ ueseo.org
hejibo@ueseo.org
26 Oct, 2011
'''
import sys
import urllib ,urllib2
import re
urllib2.socket.setdefaulttimeout(30)
def getNakedDomain(url):
    '''
    return the naked domain based on url
    '''
    if url.startswith('http://'):
        url=url[7:]
    if url.startswith('www.'):
        url=url[4:]
    if "/" in url:
        url =url[0:url.find('/')]

    return url

def baidu100(w):
    url= "http://www.baidu.com/s?"
    values = {
    "w":w.encode('gbk','ignore')
    }
    data = urllib.urlencode(values)
    newurl = url + data+"&rn=100"
    response = urllib2.urlopen(newurl)
    the_page = response.read().decode('gbk','ignore')
    return the_page

def baidu30(w):
    url= "http://www.baidu.com/s?"
    values = {
        "w":w.encode('gbk','ignore')
    }
    data = urllib.urlencode(values)
    newurl = url + data+"&rn=30"
    response = urllib2.urlopen(newurl)
    the_page = response.read().decode('gbk','ignore')
    return the_page

def baidu10(w):
    url= "http://www.baidu.com/s?"
    values = {
    "w":w.encode('gbk','ignore')
    }
    data = urllib.urlencode(values)
    newurl = url + data
    response = urllib2.urlopen(newurl)
    the_page = response.read().decode('gbk','ignore')
    return the_page

def ResultLinksFilter(data,mysite):
    o = re.compile('''href="(.+?)"''')
    f = o.findall(data)
    time=0
    #line = 1
    isInFirst100 = False
    websitelist=[]
    for ff in f:
        if not re.search("baidu",ff) and not re.search("bing",ff) and ff.startswith('http://'):

            if getNakedDomain(mysite) in ff:
                time+=1
                websitelist.append(ff)
            if time>2:
                isInFirst100=True
                break
    if isInFirst100:
        return websitelist
    else:
        return websitelist

def findtitle(websites):
    titles=[]
    for web in websites:
        try:
            htmlfile=urllib2.urlopen(web).read()
            title=re.findall(r'(?<=<title>).*?(?=</title>)',htmlfile,re.DOTALL)[0]
        except :
            print "嘻嘻~"
            title=""
        try:
            charset=re.findall(r'(?<=charset=").*?(?=")',htmlfile,re.DOTALL)[0]
        except:
            try :
                charset=re.findall(r'(?<=charset=).*?(?=")',htmlfile,re.DOTALL)[0]
            except :
                charset='utf-8'
        #charset=re.findall(r'(?<=charset=)["\w-\d]+?(?=")',htmlfile,re.DOTALL)[0]
        #charset=re.findall(r'(?<=charset=)["\w-\d]+"',htmlfile,re.DOTALL)[0]
        #if charset[0]=='"' or charset[0]=="'":
        #    charset = charset[1:-1]
        if charset=='gbk' :
            title=title.decode('gbk').encode('utf-8')
        if charset=='gb2312' :
            title=title.decode('gb2312').encode('utf-8')
        titles.append(title.strip())
    return titles

if __name__ == "__main__":
    while 1:
        input=raw_input('>>')
        #mysite = 'http://blog.ueseo.org'
        keyword=input
        titles=[]
        print "这个问题好奇怪，让陶瓷机器人我想一想~~~告诉你吧！"
        data = baidu30(keyword.decode('utf-8'))
        websites=ResultLinksFilter(data,'')
        titles=findtitle(websites)


        for i in range(0,3):
            print titles[i],
            print "---------陶瓷机器人我大发慈悲给你个链接吧 :",
            print websites[i]

        #print len(titles)
        #for i in range(0,2):
        #print titles[1].decode('gbk','ignore')+" "+websites[1]

        #print data
