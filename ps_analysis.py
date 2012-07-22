# -*- coding:utf-8 -*-
# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="suzhouwei"
__date__ ="$2010-9-13 13:45:36$"


import sys
import urllib2
import urllib
import re
import os

'''
start
下面的变量都信赖于百度页面的结构
，因此如果百度搜索结果页面发生变
化时也需要做相应的改变
'''

s_baidu_tuiguang = '咨询热线：400-800-8888'
s_baidu_tuiguang_url = 'e.baidu.com'
s_decode = 'utf-8'
s_encode = 'gbk'

#正则：用来过滤出页面右侧百度推广
s_re_ad_html = '<table width="30%".+?</table>'
#正则：用来过滤出页面正文百度推广
s_re_ad_html_2 = '<table width="65%".+?</table>'
#正则：用来过滤得到百度推广的标题
s_re_ad_title = '<font size="3">.+?</a>'
#正则：用来过滤出页面右侧百度推广的摘要
s_re_ad_abstract = '<font size="-1" color="#000000">.+?</font><br>'
#正则：用来过滤出页面正文百度推广的摘要
s_re_ad_abstract_2 = '<font size="-1">.+?<font size="-1".*?>'
#正则：用来过滤出页面右侧百度推广的URL信息
s_re_ad_url = '<font size="-1" color="#008000">.+?</font>'
#正则：用来过滤出页面正文百度推广的URL信息
s_re_ad_url_2 = '<font size="-1" color="#008000" style="margin-left:5px;">.+?</font>'

#正则：用来过滤出页面正文搜索结果列表
s_re_content = '<table cellpadding="0" cellspacing="0" class="result".+?</table>'
#正则：用来过滤出页面正文搜索结果的标题
s_re_content_title = s_re_ad_title
#正则：用来过滤出页面正文搜索结果的摘要
s_re_content_abstract = '<font size="?-1"?>.+?<br/?>'
#正则：用来过滤出页面正文搜索结果的URL信息
s_re_content_url = '<font color="#008000">.+?</font>'

'''
end
'''

def printOptions():
    """打印参数帮助信息"""
    print '''\
This program prints search result to the standard output with given KEY word.
Options include:
  --version : Prints the version number
  --help    : Display this help
  [KEY WORD]: Prints the results of search by Baidu.com'''

def filter_tag(raw):           
    """此方法过滤掉内容中的<tag>标记"""
    p=re.compile('<.*?>')
    s=p.sub('',raw)
    return s


def search_by_key(key):
    """
    根据参数进行搜索，在这个方法中主要包含两个部分：百度推广和搜索结果部分
    百度推广包含页面右侧的部分以及正文中推广链接部分
    搜索结果部分则是正文中除了推广链接部分的其它部分
    """
    #Windows=>'nt'|Linux/Unix=>'posix'
    
    if(os.name.lower()=='posix'):
        s_encode = 'utf-8'
        print '操作系统为: Linux/Unix'
        utf8 = key.decode('utf-8').encode('gbk')
        print '您搜索的关键字是： '+ key
    else:
        s_encode = 'gbk'
	print '操作系统为: Windows'.decode('utf-8').encode(s_encode)
        utf8 = key.decode('gbk').encode('gbk')
        print '您搜索的关键字是： '.decode('utf-8').encode('gbk')+ key
    
    url='http://www.baidu.com/s?wd='+urllib.quote(utf8)
    print 'URL:  '+url
    req=urllib2.Request(url)
    response=urllib2.urlopen(req)
    if(os.name.lower()=='posix'):
        html = response.read().decode('gbk').encode('utf-8')
    else:
        html = response.read()

    #推广链接，搜索结果页面右侧
    #将搜索结果也使用相同的方法展示出来
   
    print '\n========================================================\n\t\t\t百度推广\n========================================================'.decode(s_decode).encode(s_encode)
    p=re.compile(s_re_ad_html,re.S)
    HTML_ad=p.search(html).group()  #HTML_ad存放的是整个推广版块的HTML代码
    p=re.compile(s_re_ad_html_2,re.S)
    HTML_ad_2=p.finditer(html)      #HTML_ad_2存放的是正文版块中广告的版块列表
    print '\n【推广标题】'.decode(s_decode).encode(s_encode)
    p=re.compile(s_re_ad_title)
    HTML_ad_list=p.finditer(HTML_ad)
    index = 1
    for match in HTML_ad_list:
        print str(index)+': '+filter_tag(match.group())
        index += 1
    p=re.compile(s_re_ad_title,re.S)
    for match in HTML_ad_2:
        HTML_ad_list_2=p.finditer(match.group())
        for match in HTML_ad_list_2:
            print str(index)+': (正文)'+filter_tag(match.group())
            index += 1
    print '\n【对应摘要】'.decode(s_decode).encode(s_encode)
    p=re.compile(s_re_ad_abstract)
    HTML_ad_list_abstract=p.finditer(HTML_ad)
    index = 1
    for match in HTML_ad_list_abstract:
        print str(index)+': '+filter_tag(match.group())
        index += 1
    print str(index)+': '+s_baidu_tuiguang.decode(s_decode).encode(s_encode)
    index += 1
    p=re.compile(s_re_ad_html_2,re.S)
    HTML_ad_2=p.finditer(html)      #HTML_ad_2存放的是正文版块中广告的版块列表
    p=re.compile(s_re_ad_abstract_2)
    for match in HTML_ad_2:
        print str(index)+': (正文)'+filter_tag(p.search(match.group()).group())
        index += 1
    print '\n【对应的URL】'.decode(s_decode).encode(s_encode)
    p=re.compile(s_re_ad_url)
    HTML_ad_list_url=p.finditer(HTML_ad)
    index = 1
    for match in HTML_ad_list_url:
        print str(index)+': '+filter_tag(match.group())
        index += 1
    print str(index)+": "+s_baidu_tuiguang_url
    index+=1
    p=re.compile(s_re_ad_html_2,re.S)
    HTML_ad_2=p.finditer(html)      #HTML_ad_2存放的是正文版块中广告的版块列表
    p=re.compile(s_re_ad_url_2)
    for match in HTML_ad_2:
        print str(index)+': (正文)'+filter_tag(p.search(match.group()).group())
        index += 1


    #正文部分
    print '\n========================================================\n\t\t\t搜索结果\n========================================================'.decode(s_decode).encode(s_encode)
    p=re.compile(s_re_content)
    HTML_search_list=p.finditer(html)
    print '\n【结果标题】'.decode(s_decode).encode(s_encode)
    p=re.compile(s_re_content_title)
    index=1
    for match in HTML_search_list:
        print str(index)+': '+filter_tag(p.search(match.group()).group())
        index +=1
    #
    p=re.compile(s_re_content)
    HTML_search_list=p.finditer(html)
    
    print '\n【结果摘要】'.decode(s_decode).encode(s_encode)
    p=re.compile(s_re_content_abstract)
    index=1
    for match in HTML_search_list:
        print str(index)+': '+filter_tag(p.search(match.group()).group())
        index +=1
    #
    p=re.compile(s_re_content)
    HTML_search_list=p.finditer(html)
    print '\n【结果URL】'.decode(s_decode).encode(s_encode)
    p=re.compile(s_re_content_url)
    index=1
    for match in HTML_search_list:
        print str(index)+': '+filter_tag(p.search(match.group()).group()).split()[0]
        index +=1
"""
if len(sys.argv)<2:
    print 'No action apecified.'
    printOptions()
    sys.exit()

if sys.argv[1].startswith('--'):
    option = sys.argv[1][2:]
    if option=='version':
        print 'Version 1.0'
    elif option=='help':
        printOptions()
    else:
        print 'Unknown option.'
        printOptions()
        sys.exit()
else:
    key = sys.argv[1]
    search_by_key(key)
"""
if __name__=='__main__':
    key="hello world"
    search_by_key("")
    #print