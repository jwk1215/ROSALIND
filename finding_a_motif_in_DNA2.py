#! /usr/bin/env python

    
repeatlist=[]
def hay(s,t):
    for n in range(len(s)): 
        if s.find(t,n) == n:    
            repeatlist.append(s.find(t,n))   
            print("***=",repeatlist)
    
    print("repeatlist=",repeatlist)    
    repeats = ""
    for i in repeatlist:
        repeats += str(i+1) + " "
    return repeats[:-1]   

     
result= hay("GATATATGCATATACTT","ATAT")
print(result)
