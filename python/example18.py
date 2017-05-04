#!/usr/bin/python
#coding=UTF-8
from functools import reduce
Tn = 0
Sn = []
n = int(input("n = :\n"))
a = int(input("a = :\n"))
for count in range(n):
    Tn = Tn + a
    a = a * 10
    Sn.append(Tn)
    print(Tn)

#S = reduce(lambda x,y :x+y, Sn)
S = list(map(lambda x:x**2, Sn))
print(S)