# -*- coding: utf-8 -*-
#encoding=utf-8
from ICTCLAS.ICTUtil import ICTUtil
newICT = ICTUtil()
f = open('ICTCLASoutput.txt','w')
input = open('testinput.txt')
while True:
    text=input.readline()
    testseg = newICT.ICTSeg(text)
    f.write(testseg)
    if len(text)==0:
        break
f.close()
input.close()
#testpos = newICT.ICTTag('python是一门非常可爱方便的编程语言')
#print testpos
newICT.Exit()
