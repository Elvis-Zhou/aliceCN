# -*- coding:utf8 -*-
#encoding=utf-8
from ICTCLAS.ICTUtil import ICTUtil

newICT = ICTUtil()

class ChineseWordSegmentation():
    #def __init__(self):
        #self.input=words
        #self.output=newICT.ICTSeg(words)
    @staticmethod
    def seg(words):
        output=newICT.ICTSeg(words)
        return str(output)


def seg(words):
    output=newICT.ICTSeg(words)
    return output