#coding:utf-8
import os
import re
import shutil
import string
import codecs
from translate import Translator

def file_grep(inputDir,translator):
    count = 0
    
    # print inputDir
    for root,dirs,files in os.walk(inputDir):
        print "-----------------"+root+"--------------"
        for filespath in files:
                        
            target_file =  os.path.join(root,filespath)
            output_dir = string.replace(root,'projects','projects_chinese')
            output_file =  os.path.join(output_dir,filespath)
            if os.path.isdir(output_dir):
                pass
            else: 
                os.makedirs(output_dir)
            # print "output_file:",output_file

            if os.path.exists(output_file):
                count = count+1
                continue
            
            pattern_all = "^.*\.(nas|c|h)$"
            target_matched = re.match(pattern_all,filespath)
            
            if target_matched:
                translate_jpcomment_into_chinese(target_file,filespath,output_file,translator)
            else:
                shutil.copyfile(target_file,output_file)
    

#later should be reconstruct with decorator
def translate_jpcomment_into_chinese(target_file,filespath,output_file,translator):
    
    def nas_handling():
        # read file
        in_f = codecs.open(target_file,'r',encoding = "shift_jis")
        out_content = []
        while 1:
            line = in_f.readline()
            if not line:
                break
            ptr = "^(.*?)(;)(.*)$"
            m = re.match(ptr,line)
            
            if m:
                out_content.append(m.group(1))
                out_content.append(m.group(2))
                jp_comments = m.group(3)
                cn_comments = translator.translate(jp_comments.encode('utf8')) #translator.translate method only accepts utf-8
                cn_comments = cn_comments
                out_content.append(cn_comments+"\n")
            else:
                out_content.append(line)
        
        in_f.close()
        out_str = "".join(out_content)
        out_f = codecs.open(output_file,'w',encoding = "utf8")
        out_f.write(out_str)
        out_f.close()    

    def c_handling():
            # read file
        in_f = codecs.open(target_file,'r',encoding = "shift_jis")
        output_file = string.replace(target_file,'projects','projects_chinese')
        out_content = []  
        while 1:
            line = in_f.readline()
            if not line:
                break
            ptr = "^(.*?)(/\*)(.*?)(\*/.*)$"
            m = re.match(ptr,line)
            if m :
                out_content.append(m.group(1))
                out_content.append(m.group(2))
                jp_comments = m.group(3)
                cn_comments = translator.translate(jp_comments.encode('utf8')) #translator.translate method only accepts utf-8
                cn_comments = cn_comments
                out_content.append(cn_comments)
                out_content.append(m.group(4)+"\n")
            else:
                out_content.append(line)
        
        in_f.close()
        out_str = "".join(out_content)
        out_f = codecs.open(output_file,'w',encoding="utf8")
        out_f.write(out_str)
        out_f.close()    

    pattern_nas = "^.*\.nas"
    # pattern_c = "^.*\.(c|h)" # can be obmitted since no other files
    nas_matched = re.match(pattern_nas,filespath)
    
    
    if nas_matched:
        nas_handling()
    else: 
        c_handling()

    
    
    
    
if __name__ == "__main__":
    
    inputDir = r'C:\Users\RDT\Documents\routine\OS\DISK\projects'
    translator= Translator(from_lang = "ja",to_lang="zh")
    file_grep(inputDir.decode('utf8'),translator)
    
    