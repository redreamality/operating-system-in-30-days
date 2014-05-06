#coding:utf-8
import os
import re
import shutil
import string
import codecs

inputDir = r'C:\Users\RDT\Documents\routine\OS\DISK\projects\01_day\helloos2'

target_file =  os.path.join(inputDir,"helloos.nas")
# print target_file
output_file = string.replace(target_file,'projects','projects_chinese')
# print output_file

in_f = codecs.open(target_file,'r',encoding = "shift_jis")
while 1:
    line = in_f.readline()
    if not line:
        break
    print repr(line)
    
    
    # ptr = ".*;(.*)"
    # m = re.match(ptr,line)
    # if m:
        # print m.group(1)
        
    jp_ptr = u'^.*?([\u4e00-\u9fbf\u3040-\u309f\u30a0-\u30ff]+)' # .*? 表示非贪婪匹配，[\u4e00-\u9fbf\u3040-\u309f\u30a0-\u30ff]为日文字符集，包括中文（日汉字）
    m = re.match(jp_ptr,line)
    if m:
        print m.group(1) #group(n)为取出第n个括号里的
        
    

# shutil.copyfile(target_file,output_file)