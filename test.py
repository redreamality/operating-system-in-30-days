#coding:utf8
import os
from translate import Translator
import re
import shutil
import string
import codecs

def main():
    # root = r'C:\Users\RDT\Documents\routine\OS\DISK\projects\01_day\helloos2'
    root = r'C:\Users\RDT\Documents\routine\OS\DISK\projects\11_day\harib08h'
    # filespath = "helloos.nas"
    filespath = "bootpack.c"
    translator= Translator(from_lang = "ja",to_lang="zh")
    target_file =  os.path.join(root,filespath)
    output_dir = string.replace(root,'projects','projects_chinese')
    output_file =  os.path.join(output_dir,filespath)
    if os.path.isdir(output_dir): 
        pass
    else: 
        os.makedirs(output_dir)
    print repr(output_file)
    
    translate_jpcomment_into_chinese(target_file,output_file,translator)

def translate_jpcomment_into_chinese(target_file,output_file,translator):
    # read file
    in_f = codecs.open(target_file,'r',encoding = "shift_jis")
    output_file = string.replace(target_file,'projects','projects_chinese')
    print output_file
    
    out_f = codecs.open(output_file,'w',encoding="utf8")
            
    while 1:
        line = in_f.readline()
        if not line:
            break
        ptr = "(.*?)(#.*)"
        m = re.match(ptr,line)
        
        if m :
            print "aha"
            out_f.write(m.group(1))
            jp_comments = m.group(2)
            cn_comments = translator.translate(jp_comments.encode('utf8')) #translator.translate method only accepts utf-8
            cn_comments = cn_comments
            out_f.write(cn_comments)
            out_f.write("\n")
            
        else:
            out_f.write(line)

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # ptr = "^(.*?)(;)(.*/\*)?(.*?)((\*/)?)$"
        # m = re.match(ptr,line)
        
                        
        # jp_ptr = u'(^.*?)([\u4e00-\u9fbf\u3040-\u309f\u30a0-\u30ff]+.*[\u4e00-\u9fbf\u3040-\u309f\u30a0-\u30ff]?)(.*$)' # .*? 表示非贪婪匹配，[\u4e00-\u9fbf\u3040-\u309f\u30a0-\u30ff]为日文字符集，包括中文（日汉字）
        # m = re.match(jp_ptr,line)
        # if m:
            # out_f.write(m.group(1)+"1")
            # try:
                # out_f.write(m.group(2)+"2")                
            # except:
                # pass
            # try:
                # out_f.write(m.group(3)+"3")
            # except:
                # pass
            # jp_comments = m.group(4) #group(n)为取出第n个括号里的
            # translator= Translator(from_lang = "ja",to_lang="zh")
            # cn_comments = translator.translate(jp_comments.encode('utf8')) #translator.translate method only accepts utf-8
            # out_f.write(cn_comments+"4")
            # try:
                # out_f.write(m.group(5)+"5")
            # except:
                # pass
            # try:
                # out_f.write(m.group(6)+"6")
            # except:
                # pass
            # out_f.write("\n")
        # else:
            # out_f.write(line)
            
    in_f.close()
    out_f.close()
            
            
if __name__ =="__main__":
    main()