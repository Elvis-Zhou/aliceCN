# -*- coding:utf8 -*-
#encoding=utf-8
from ICTCLAS.ICTUtil import ICTUtil

newICT = ICTUtil()
class ChineseWordSegmentation:

    def __init__(self,words):
        self.input=words
        self.output
    def seg(self,words):
        self.output=newICT.ICTSeg(words)
        return self.output


