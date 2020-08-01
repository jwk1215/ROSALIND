#! /usr/bin/env python

seq1 = 'GAGCCTACTAACGGGAT'
seq2 = 'CATCGTAATGACGGCCT'

cnt = 0

for i in range(0, len(seq1)):
    if seq1[i] != seq2[i]:
        cnt +=1
    else:
        pass

print(cnt)


