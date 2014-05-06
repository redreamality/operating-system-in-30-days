import os
import string


root = r'C:\Users\RDT\Documents\routine\OS\DISK\projects\11_day\harib08h'
filespath = "bootpack.c"
target_file =  os.path.join(root,filespath)
output_dir = string.replace(root,'projects','projects_chinese')
output_file =  os.path.join(output_dir,filespath)
    
print os.path.exists(target_file)
print os.path.exists(output_dir)
print os.path.exists(output_file)