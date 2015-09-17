import os
fp=open('c:\python26\search engine(se)\computers.txt','r')
comp=fp.readlines()
fp.close()
noofcomp=len(comp)
i=0
## content file... checks the respective computers(shared folders)..if any then browse the folders and content paste into the respective computers shared folder text file..(note: that only new entries are permissible.)(only make or update existing file if file exist..)
while i < noofcomp:
    print comp[i]
    if os.path.getsize('c:/Python26/search engine(se)/share/'+comp[i].strip('\n')+'.txt') == 0:
        i=i+1;
        continue
    
    fp=open('c:/Python26/search engine(se)/share/'+comp[i].strip('\n')+'.txt','r')
    shar=fp.readlines()
    fp.close()
    noofshar=len(shar)
    j=0
  
    while j < noofshar:
        print '\\\\'+comp[i].strip('\n')+'\\'+shar[j].strip('\n')+'\\'

        if os.path.isdir('\\\\'+comp[i].strip('\n')+'\\'+shar[j].strip('\n')+'\\'):
          ##  print 'success'
            print '\\\\'+comp[i].strip('\n')+'\\'+shar[j].strip('\n')+'\\'
            
            
            fp1=open('c:/Python26/search engine(se)/share/'+comp[i].strip('\n')+'/'+shar[j].strip('\n')+'.txt','a+')
            
            try:
                con=os.listdir('\\\\'+comp[i].strip('\n')+'\\'+shar[j].strip('\n')+'\\')
            except:
                j=j+1
                continue
            conlen=len(con)
            k=0
            content=fp1.readlines()
            while k < conlen:
                if not con[k]+'\n' in content:
                    fp1.write(con[k]+'\n')
                k=k+1
                
            fp1.close()    
            fp.close()
            
            j=j+1
        else:
            j=j+1
         
    i=i+1
                          
raw_input('press<enter>')

