#coding:utf8
import re
ptr = "^(.*?)(/\*)(.*?)(\*/)$"

line = "	io_sti(); /* IDT/PICの初期化が終わったのでCPUの割り込み禁止を解除 */"
m = re.match(ptr,line)
print m is not None
print repr(m.group(1))
print repr(m.group(2))
print repr(m.group(3))

print repr(m.group(4))
# print repr(m.group(5))

# print
# line = ";adfjad"
# m = re.match(ptr,line)

# print repr(m.group(1))
# print repr(m.group(2))
# print repr(m.group(3))
# print repr(m.group(4))
# print repr(m.group(5))