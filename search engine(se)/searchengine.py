import linecache
line = raw_input("enter the string:")
con=[]
for word in line.split():
    s=word[0].lower()
    #raw_input("press<enter>")
    lits=open('C:\Python26\search engine(se)\searchtecni\\'+s+'.txt','r')
    contents=lits.readlines()
    length=len(contents)
    i=0
    wordlen=len(word)
    if wordlen<4:
        per=1
        eitper=1
    if wordlen>=4:
        per=0.3
        eitper=int(wordlen*per)
    
    while i<length:
        j=0
        check=0
        list3=contents[i].split()
        search=list3[0]
        lino=list3[1].strip('\n')
        ##print search
        search=search.lower()
        ##raw_input('press<enter>')
        tupl=[]
        while j < wordlen:
            if wordlen-(j)< int(wordlen*per):## chech the lenght of the search string if less then 80 % then it will removw out of loop
                break

            k=0
            count=0
            if check>=eitper:
                ##print check
                ##raw_input('press<enter>')
                break
            while k<=len(search):
                if k+j>wordlen-1:             ## case when the lenght of the word is less the range
                    if count>=eitper:
                        newper=(count/wordlen)*100
                        tupl=[count,lino]
                        check=count
                        ##print tupl
                    
                    
                    break
                if k>(len(search)-1):## lenght of range is greater for searched string...
                    if count>=eitper:
                        newper=(count/wordlen)*100
                        tupl=[count,lino]
                        check=count
                        ##print tupl
                     
                    break
                    
                    
                ##print k+j
                if word[k+j]==search[k]:
                    count=count+1
                    k=k+1
                else:
                    if count>=eitper:
                        newper=(count/wordlen)*100
                        tupl=[count,lino]
                        check=count
                        ##print tupl
                    
                    
                    break
            j=j+1
        if tupl!=[]:
            con.append(tupl)
        i=i+1
    #print con
    #raw_input('press<enter>')
print con
raw_input('press<enter>')
d={}
for key, val in con:## to convert tuple of tuples of two values..into a dictionary having for given length corrosponding line number
    d.setdefault(key, []).append(val)  

print d
print 'here'
lent=len(con)
##s=0
'''while s<lent:
    value=int(con[s][1])
    print value
    line = linecache.getline('C:\Python26\search engine(se)\linkentry.txt', value)
    print line
    s=s+1'''
dic={}
final={}
for key in d:
    c=d[key]
    dic={}
    single=list(set(c))
    i=0
    while i<len(single):
        count=c.count(single[i])
        dic.setdefault(count, []).append(single[i])
        i=i+1
    final.setdefault(key,[]).append(dic)
    print dic
    print final
print final
print 'here'
raw_input('press<enter>')
listk=[]
for key in final:
    listk.append(key)
    
listk.sort()


lenghtic= len(final)
listfinal=[]
for key in listk:
    secdic=final[key]
    print secdic[0]
    tempdic=secdic[0]
    ##print listfinal
    raw_input('press<enter>')
    for key2 in tempdic:
        listfinal=listfinal+tempdic[key2]
print listfinal        
s=1

## to remove the duplicate entries...from the final list....

i=0
a=listfinal

b=a
c=[]
lengh=len(a)
print 'here1'
while i<(len(b)):
    j=0
   ## print b[i:lengh]
    if b[i] not in b[i+1:lengh]:
        c.append(b[i])
    i=i+1    

listfinal=c

lenf=len(listfinal)
print listfinal


while s<=lenf:
    value=int(listfinal[lenf-s])
    print value
    line = linecache.getline('C:\Python26\search engine(se)\linkentry.txt', value)
    print line
    s=s+1
    

raw_input('press<enter>')
##note this is working on correct and approximate lenght of searched string...but error correction is working properly...
## you need to transfer the all lines on to the dictionary keys.....not on the lenght of their percentage..!!!!!!
##home work and to solve the issue of the line containing same word again and again (search problem)...and apply approximation on percentage basis..(100,90,80,70)..



