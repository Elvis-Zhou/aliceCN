#encoding=utf-8
#-*-coding:utf-8 -*-
import re
import mmseg
import urllib2
import BaiduResult

dict={
    "浦发银行怎么样":"陶瓷机器人我认为：＜１＞与总盘相比九项重要的财务指标中，有３项超好（效益、现金净流量、主营利润、） \n，有１项极好（财务综合分、），有２项很好（净资产、公积金、），\n有３项较好（未分利润、应收帐、净 资产收益、），且财务综合分在总盘评比中属于０级出色。\n＜２＞该股所属行业为国民经济支柱型特别重点 ．．\n所以我看好它！”",
    "浦发银行" : '现价7.67 -0.02‎ (-0.26%‎) 开盘: 	7.69 \n 最高: 	7.69 最低: 	7.60 成交量: 	47,630,983  \n 资本总市值: 	1430.72亿',
    "华夏银行怎么样":'18日 华夏银行 (600015 )技术点评：\n 短期非市场热点，走势滞后指数；从交易情况来看，明日上涨几率大。近2日下跌势头减弱；该股近期的主力成本为10.54元，\n股价处成本以下，弱市反弹，快进快出；股价周线处于下跌趋势，阻力位9.41元，中线持币为主；\n前景长期看仍然不乐观；..',
    "华夏银行":"600015‎ - 华夏银行  现价 8.72 +0.05‎ (0.58%‎) 7月18日 \n开盘: 	8.66 最高: 	8.74 最低: 	8.55 成交量: 	21,613,019 \n 资本总市值: 	597.30亿",
    "今天天气怎么样啊":"嘿嘿~~让我想想，哦~知道了。请看 http://zhidao.baidu.com/question/367975887.html"
}
f=open('temp.txt','w')
t=""
page='http://www.baidu.com/s?wd=key&rsv_bp=0&rsv_spt=3&inputT=2201'
compare=r'%s' % t
pattern=re.compile(compare,re.DOTALL)
while 1:
    input=raw_input('>>')
    """
    pageurl=page.replace('key',input)
    flag=0

    for keywords in mmseg.seg_txt(input):
        #print keywords

        for words in dict:
            if input==words:
                print dict[words]
                flag=1
                break
            else :
                if input==keywords:
                    print dict[words]
                    flag=1
                    break
                else :
                    if keywords==words:
                        print dict[words]
        if flag==1:
            break
"""
        #urls=urllib2.urlopen(pageurl).read()
        #print >>f,urls
        #f.flush()




