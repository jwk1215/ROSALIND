#! /usr/bin/env python

seq = 'GATATATGCATATACTT'
sub = 'ATAT'


tmp = ""

for i in range(0,len(seq)):
    tmp += seq[i:i+4]
    print(tmp)
    if seq[0:2] == seq[1:3]:
        print('hi')
        


