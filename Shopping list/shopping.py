# -*- coding: utf-8 -*-
f = open('shopping.txt')
r = 1
for s in f:
    if 'Shopping list:' in s:
        print(str(s))
    else:
        print('%s) '%r + str(s))
        r+=1

