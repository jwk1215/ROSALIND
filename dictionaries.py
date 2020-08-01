#! /usr/bin/env python

txt = 'We tried list and we tried dicts also we tried Zen'

spl = txt.split(' ')

dic = {}

for i in spl:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1
print(dic)

for i in dic:
    print(i, dic[i])




