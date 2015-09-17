import os
fp = open('contententry.txt','r')
i=0


## program which is used to put word by word into their respective file.........run only one time otherwise append coppied entry into existing data entry..
unris=a=['*','\\','/','?','<','>','|',':','\"']
for line in fp:
    i=i+1
    for word in line.split():

        if word[0] in unris:                      ## '\' will be the problem case not printing it..properly
            fp=open('C:\Python26\search engine(se)\searchtecni\\'+'special'+'.txt','a')
            fp.write(word+' '+ `i`+'\n')
            fp.close()
            continue
        
        if word[0]=='\0':
            continue
        fp=open('C:\Python26\search engine(se)\searchtecni\\'+word[0].lower()+'.txt','a')
        fp.write(word+' '+ `i`+'\n')
        fp.close()
        
            

            


            
            
       
        
