#!/usr/bin/python
#codig=UTF-8

for n in range(100, 1000):
	i = n/100
	j = n/10%10
	k = n % 10
	if n == int(i**3 + j**3 + k**3):
		print ("i=%d, j=%d, k=%d, n=%d" % (i,j,k,n),)
		print (n)
