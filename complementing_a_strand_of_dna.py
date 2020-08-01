#! /usr/bin/env python

seq = 'AAACCCGGT'

outseq = seq.replace('A','Q').replace('C','W').replace('G','E').replace('T','R')

outseq2 = outseq.replace('Q','T').replace('W','G').replace('E','C').replace('R','A')

print(outseq2[::-1])

 



