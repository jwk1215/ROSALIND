#! /usr/bin/env python

f = 'GC.txt'

subject =""
dic_C = {}
dic_G = {}

C = 'C'
G = 'G'
cdic = {}

with open(f, 'r') as handle:
    for line in handle:
        linestrip = line.strip('\n')
        if line.startswith('>'):
            subject += line
        else:
            cdic['C'] +=1                    
            


#Ccnt = linestrip.count('C')
            #Ctotal += Ccnt
            #print(Ctotal)
            #Gcnt = linestrip.count('G')
            
            #print(Gtotal)
    
print(subject)        
#print(Ctotal)
#print(Gtotal)



