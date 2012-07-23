__author__ = 'Administrator'
# -*- coding: utf-8 -*-
#encoding = utf-8
#import sys
import urllib ,urllib2
import re

urllib2.socket.setdefaulttimeout(30)


def starttalk():
    while 1:
        input=raw_input('>>')
        keyword=input
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
    print result
    try:
        print eval(result)["response"]
    except BaseException:
        print "小黄鸡也不知道"
    #for i in range(0,3):
    #    print titles[i],


if __name__ == "__main__":
    starttalk()