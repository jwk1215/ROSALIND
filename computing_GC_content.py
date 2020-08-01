#! /usr/bin/env python

"""
fasta = 'CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT'

num0 = fasta.count('C')
num1 = fasta.count('G')   
num2 = num0+num1 

print((num2/len(fasta))*100)
"""

f = 'GC.txt'

with open(f, 'r') as handle:
    for line in handle:
        if line.startswith('>'):
            continue
        ''.join(line)
        print(line)




