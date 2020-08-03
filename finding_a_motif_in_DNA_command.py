#! /usr/bin/env python

s = 'GATATATGCATATACTT'
t = 'ATAT'

#print(s.find(t))
#print(s.find(t,2))
#print(s.find(t,4))

#indexing = s.index(t)
#print(s[indexing]) #A
#print(s[indexing:5]) #ATAT

repeatlist = []
for n in range(len(s)):
    if s.find(t,n) == n: #index n번부터 t(ATAT)가 나타나는 index를 출력
        repeatlist.append(s.find(t,n))        

print(repeatlist) # [1,3,9]

repeats = ""
for i in repeatlist:
    #print(i) # 1 3 9
    repeats += str(i+1)+" " 

print(repeats)
    

























