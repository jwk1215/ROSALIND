#! /usr/bin/env python

dic={"C":0 , "G":0 , "TT":0 , "AV":0}
dic_gb=[]
list_rst=[]

gb=0

with open('GC.txt','r') as f:

    for line_value in f:
        print(len(line_value))
        linestrip = line_value.strip()
        if line_value[0:1] ==">":
            print(linestrip)          
            dic_gb.append(line_value)
            if gb != 0:  
                dic["AV"]=(dic["C"] + dic["G"]) / dic["TT"]
                print("rst=",dic_gb[gb-1],end="") 
                print(dic["C"],dic["G"],dic["TT"],dic["AV"])                
                av=dic["AV"]       
                list_rst.append(dic["AV"]) 
# 문자수 Count Dictionary Clear 
            dic["C"]=0
            dic["G"]=0       
            dic["TT"]=0
            dic["AV"]=0             
            gb += 1     
            continue 
                                
        for i in linestrip:
            dic["TT"] += 1      # 전체문자수 Count       
            if i in dic: 
                dic[i] += 1     # C/G 문자수 Count   
#                print("dic==",i,dic[i])     

dic["AV"]=(dic["C"] + dic["G"]) / dic["TT"]
print("rst=",dic_gb[gb-1],end="") 
print(dic["C"],dic["G"],dic["TT"],dic["AV"])  
list_rst.append(dic["AV"]) 

sv_idx=0
idx=0
save_val=0
for i in list_rst:
    idx +=1
    if save_val < i:
       save_val = i         
       sv_idx = idx
#print("save_idx=",sv_idx)       

print("")   
print("=============  Result ==========")   
print("* 구분 : %s" ,dic_gb[sv_idx-1],end="") 
print("* 비율 : %3.2f" %(list_rst[sv_idx-1]*100))

#print(dic)
#print(dic_gb)
#print(list_rst)


