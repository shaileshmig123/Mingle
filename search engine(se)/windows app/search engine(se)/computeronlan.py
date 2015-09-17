import os
os.system('net view > lancom.txt')
f = open('lancom.txt', 'r')
f.readline();f.readline();f.readline()

conn = []
host = f.readline()
if  os.path.isfile('c:\python26\search engine(se)\computers.txt'):
     
     fcompn=open('computers.txt','a+')
     comps=fcompn.readlines()
     
     while host[0] == '\\':
         
          hel=host[2:host.find(' ')]
          #print hel
          if not hel+'\n' in comps:
              fcompn.write(hel+'\n')
              
          host = f.readline()
     f.close()    
     fcompn.close()

##create files in mass for the shared folders of each computers....-_---------->>>>
fcompn=open('computers.txt','r')

noofcom=fcompn.readlines()
no=len(noofcom)
i=0
dircontent = os.listdir('c:\python26\search engine(se)\share\\') 
while i < no:
     if not noofcom[i].strip('\n')+'.txt' in dircontent:
          fp=open('c:\python26\search engine(se)\share\\'+noofcom[i].strip('\n')+'.txt','w')
          fp.close()
          os.makedirs('c:\python26\search engine(se)\share\\'+noofcom[i].strip('\n'))
     i=i+1
     
     
fcompn.close()


