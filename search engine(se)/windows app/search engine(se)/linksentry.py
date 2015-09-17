import os
fp=open('c:\python26\search engine(se)\computers.txt','r')
comp=fp.readlines()
fp.close()
noofcomp=len(comp)
i=0
fp3=open('c:/Python26/search engine(se)/contententry.txt','a')
fp4=open('c:/Python26/search engine(se)/linkentry.txt','a')
while i < noofcomp:
    lidir=os.listdir('c:/Python26/search engine(se)/share/'+comp[i].strip('\n')+'/')
    if len(lidir) == 0:
        i=i+1;
        continue
    k=0

    while k < len(lidir):

        if os.path.getsize('c:/Python26/search engine(se)/share/'+comp[i].strip('\n')+'/'+lidir[k]) == 0:
            k=k+1;
            continue
        fp2=open('c:/Python26/search engine(se)/share/'+comp[i].strip('\n')+'/'+lidir[k],'r')
        cont=fp2.readlines()
        j=0
        fp2.close()
        while j <len(cont):
            fp3.write(cont[j]+'\n')
            fp4.write('\\\\'+comp[i].strip('\n')+'\\'+lidir[k].strip('.txt')+'\\'+cont[j]+'\n')
            j=j+1

        k=k+1

    i=i+1    
        
