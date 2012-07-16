#encoding=utf-8
import mmseg
#from pymmseg import mmseg   
#mmseg.dict_load_defaults()    

f = open('MMSEGoutput.txt','w')
input = open('testinput.txt')
while True:
    text=input.readline()
    for i in mmseg.seg_txt(text):
        print >>f,i,' ',
    #f.write(testseg)
    print >>f
    if len(text)==0:
        break
f.flush()
f.close()
input.close()
#f=open('1.txt','w')
#for i in mmseg.seg_txt(text):
    #print >>f,i
#algor = mmseg.Algorithm(text)
#for tok in algor:
    #print >>f,'%s [%d..%d]' % (tok.text, tok.start, tok.end)
    #print '%s' % tok.text
