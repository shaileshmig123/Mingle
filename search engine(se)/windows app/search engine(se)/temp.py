i=0
a=[1,2,3,4,1,2,3,13,4,5,6,1]
b=a
c=[]
lengh=len(a)
while i<(len(b)):
    j=0
    print b[i:lengh]
    if b[i] not in b[i+1:lengh]:
        c.append(b[i])
        
        
        
    else:
        pass
    i=i+1
print c
raw_input('press<enter>')

 
