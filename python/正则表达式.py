#!/usr/bin/python
#coding = UTF-8
import re

# """
#re
#将正则表达式编译成Pattern对象
# pattern = re.compile(r'(\w+) (\w*) *(\w+)')
#
# # 使用Pattern匹配文本，获得匹配结果，无法匹配时将返回None
# match1 = pattern.match('helloa111 world 12323')
# if match1:
#     # 使用Match获得分组信息
#     print (match1.group())



#########end re############
# """

#match
m = re.match(r'(\w+) (\w+) (?P<sign>.*)', 'hello world adda')

print("m.string: ", m.string)
print("m.re: ", m.re)
print("m.pos: ", m.pos)
print("m.endpos: ", m.endpos)
print("m.lastgroup: ", m.lastgroup)
print("m.lastindex: ", m.lastindex)
print("m.group(1,2): ", m.group(1,2))
print("m.groups(): ", m.groups())
print("m.groupdict(): ", m.groupdict())
print("m.start('sign'): ", m.start('sign'))
print("m.end(3): ", m.end(3))
print("m.span(3): ", m.span(3))
print("m.expand(r'\2 \1\3'): ", m.expand(r'\2 \1\3'))

if m:
    print(m.group('sign'))
#end match

