# -*- coding: utf-8 -*-
#encoding = utf-8
#import sys
import urllib ,urllib2
import re
import chardet
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
        except BaseException:
            print "嘻嘻~"
            title=""
#        try:
#            charset=re.findall(r'(?<=charset=").*?(?=")',htmlfile,re.DOTALL)[0].lower()
#        except:
#            try :
#                charset=re.findall(r'(?<=charset=).*?(?=")',htmlfile,re.DOTALL)[0].lower()
#            except :
#                charset='utf-8'
        #charset=re.findall(r'(?<=charset=)["\w-\d]+?(?=")',htmlfile,re.DOTALL)[0]
        #charset=re.findall(r'(?<=charset=)["\w-\d]+"',htmlfile,re.DOTALL)[0]
        #if charset[0]=='"' or charset[0]=="'":
        #    charset = charset[1:-1]
        try:
            charset=chardet.detect(htmlfile)['encoding'].lower()
            if charset=='gbk' :
                title = title.decode('gbk').encode('utf-8')
            if charset=='gb2312' :
                title = title.decode('gb2312').encode('utf-8')
            if charset=='utf-8' or charset=='utf8':
                #title = title.encode('utf-8')
                pass
        except BaseException:
            pass
        titles.append(title.strip())

    return titles

def searchtheweb(keyword):
    titles=[]
    print "这个问题好奇怪，让陶瓷机器人我想一想~~~告诉你吧！"
    data = baidu30(keyword.decode('utf-8'))
    websites=ResultLinksFilter(data,'')
    titles=findtitle(websites)
    for i in range(0,3):
        print titles[i],
        print "---------陶瓷机器人我大发慈悲给你个链接吧 :",
        print websites[i]


def starttalk():
    while 1:
        input=raw_input('>>')
        input=input.replace(" ","+")
        if input.startswith("!") or input.startswith("！"):
            searchtheweb(input)
        else:
            searchsimsimi(input)

def searchsimsimi(keyword):
    titles=[]
    url_ws='http://www.simsimi.com/func/req?lc=zh&msg='
    #urllib2.Request()
    request = urllib2.Request(str(url_ws)+keyword)
    request.add_header("Referer","http://www.simsimi.com")
    #request.add_header('Accept', 'application/json')
    #request.get_method = lambda: 'PUT'
    result = urllib2.urlopen(request).read()
    #print result
    try:
        print eval(result)["response"]
    except BaseException:
        #print "陶瓷机器人我也不知道"
        searchtheweb(keyword)
    #for i in range(0,3):
    #    print titles[i],


if __name__ == "__main__":
    starttalk()
    #searchtheweb("房山")