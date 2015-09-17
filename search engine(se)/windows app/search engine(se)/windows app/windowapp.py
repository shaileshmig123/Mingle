import Tkinter as tk
import thread
import Tix 
from Tkinter import *
import tkMessageBox
from PIL import Image, ImageTk
import linecache
import os
from ttk import Combobox
import shutil
#----------------------------------------------------------------------
#----------------------------------------------------------------------
class OtherFrame(tk.Toplevel):
    """"""
 
    #----------------------------------------------------------------------
    def __init__(self):
        
        """Constructor"""
        tk.Toplevel.__init__(self)
        self.geometry("900x670")
        
    def onbuttonleft(self,event):
        ##print s
        pass


#----------------------------------------------------------------------
class MyApp(object):
    """"""
 
    #----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        self.root = parent
        self.root.title("Main frame")
        menubar = Menu(self.root)
        parent.config(bg='green') 
        # create a pulldown menu, and add it to the menu bar
        filemenu = Menu(menubar, tearoff=0)
        handler3 = lambda: self.openFrame(0)
        filemenu.add_command(label="Open",command=handler3 )
        filemenu.add_command(label="Save",)
        filemenu.add_command(label="upadate",command=self.update)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=root.quit)
        menubar.add_cascade(label="File", menu=filemenu)

        # create more pulldown menus
        editmenu = Menu(menubar, tearoff=0)
        editmenu.add_command(label="Cut", )
        editmenu.add_command(label="Copy", )
        editmenu.add_command(label="Paste",)
        menubar.add_cascade(label="Edit", menu=editmenu)

        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="About", )
        menubar.add_cascade(label="Help", menu=helpmenu)
        Label (self.root,text='xyz',fg="blue",font=(" Verdana",100),bg='green').place(x=300,y=60)
        self.var=0
        self.lenf=0
        self.st=[]
        self.h=0
        self.root.entryVariable = StringVar()
        ##handler1 = lambda: self.OnPressEnter(self)
        
        self.root.entry1 = Entry(self.root,width=50,textvariable=self.root.entryVariable)
        self.root.entry1.place(x=250,y=250)#side='top',padx=300,pady=10)
       ## self.root.entry1.bind("<Return>",self.root.OnPressEnter)
        self.text= self.root.entryVariable.get()
        handler1 = lambda: self.cheking(self.root.entryVariable.get(),0,0,2,3)
        self.root.button=Button(self.root,text='Search',width=10,command= handler1).place(x=270,y=300)
        self.root.button=Button(self.root,text='You\'r feeling lucky',width=20).place(x=410,y=300)
 # display the menu
        self.root.config(menu=menubar) 
        #btn = Tk.Button(self.frame, text="Open Frame", command=self.openFrame)
    def update(self):
        refresh=1
        self.root.destroy()       #btn.pack()
    def hide(self):
        """"""
        self.root.withdraw() 

    def onbuttonclick(self,stri,varinc,subframe,new,excep):
        refresh=1
        self.hide()
        if stri=='' and excep==2:
            stri=self.glob
        #if stri=='' and excep==3:
            #self.cheking(stri)
        self.glob=stri.lower()
        if varinc==0 and stri!='null' and subframe==0:
            subframe=OtherFrame()
            
        
        ######print len(stri)
        subframe.config(bg='green')
        if new==2:
            self.var=0
            self.lenf=0
            self.st=[]
        Label (subframe,text='Search:',fg="blue",bg='green',font=(" Verdana",20)).place(x=10,y=20)
        Label (subframe,text='\t\t\t\t\t\t\t\t\t',fg="blue",bg='green',font=("Times",10)).place(x=150,y=60)
        for co in range(11):
            Label (subframe,text='\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t',fg="blue",bg='green',font=(" Times",10)).place(x=100,y=90+co*50)
            
            
        
        
        subframe.entryVariable = tk.StringVar()
       
        
        subframe.entry1 = tk.Entry(subframe,width=55,textvariable=subframe.entryVariable)
        subframe.entry1.place(x=120,y=30)#side='top',padx=300,pady=10)
        subframe.entry1.bind("<Button-1>", subframe.onbuttonleft)
        handler111 = lambda: self.onbuttonclick(subframe.entryVariable.get(),0,subframe,2,2)
        subframe.button=Button(subframe,text='Search',width=10,command= handler111).place(x=550,y=23)
        if  subframe.entryVariable.get() == '' :
             subframe.entryVariable.set(self.glob)
        else:
            subframe.entryVariable.set(self.glob)
            
            
             
        ##else:
            ##subframe.entryVariable.set(subframe.entryVariable.get())
            
        if varinc==0 and stri!='null' and new==2:
            self.st=self.process(stri) 
        '''for i in range (10):
            Label (subframe,text='>>>>>'+stri,fg="blue",font=(" Verdana",15)).place(x=30,y=10+50*(i+1))
        '''
        s=1
        line =[]
        lenf=len(self.st)
        if lenf<11:
            print 'no. of solutions are less..'
            raw_input('press<enter>')
        self.lenf=lenf
        #if lenf<11:
         #   exit()
        if lenf<11:
            he=lenf
        else:
            he=11
        while s<=lenf-(lenf-he):
               value=int(self.st[lenf-s-he*varinc])
               ######print value
               ##hand=handler+`s`
              
               temp = linecache.getline('C:\Python26\search engine(se)\linkentry.txt', value)
               line.append(temp)
              
               s=s+1
  ## for first search.......
        i=0
        per=50
        color='green'
        Label (subframe,text='total results found are...'+`lenf`,fg="blue",bg=color,font=("Times",10)).place(x=150,y=60)
        handler1 = lambda: self.oflineonline(line[0])
        handler11 = lambda: self.oflineonline1(line[0])
        handler1220 = lambda: self.download(line[0],0)
        sta=''
        '''sts=self.status(line[0])
        if sts==1:
            sta='online'
            self.var1=2
        else:
            sta='ofline'
            self.var1=2'''
        Label (subframe,text= line[0].strip('\n')+sta,fg="blue",bg=color,font=(" Times",10)).place(x=100,y=90+i*per)
        subframe.button1=Button(subframe,text='Play>>',activebackground=color,relief=FLAT,bg=color,width=10,command= handler1).place(x=150,y=110+i*per)
        subframe.button11=Button(subframe,text='Status>>',activebackground=color,relief=FLAT,bg=color,width=10,command= handler11).place(x=300,y=110+i*per)
        subframe.button11=Button(subframe,text='Download',activebackground=color,relief=FLAT,bg=color,width=10,command= handler1220).place(x=400,y=110+i*per)

        '''sts=self.status(line[1])
        if sts==1:
            sta='online'
        else:
            sta='ofline'''
        handler2 = lambda: self.oflineonline(line[1])
        handler22 = lambda: self.oflineonline1(line[1])
        Label (subframe,text=line[1].strip('\n')+sta,fg="blue",bg=color,font=(" Times",10)).place(x=100,y=90+(i+1)*per)
        subframe.button=Button(subframe,text='Play>>',activebackground=color,relief=FLAT,bg=color,width=10,command= handler2).place(x=150,y=110+(i+1)*per)
        subframe.button=Button(subframe,text='Status>>',activebackground=color,relief=FLAT,bg=color,width=10,command= handler22).place(x=300,y=110+(i+1)*per)
        
        '''sts=self.status(line[2])
        if sts==1:
            sta='online'
        else:
            sta='ofline'''
        handler3 = lambda: self.oflineonline(line[2])
        handler33 = lambda: self.oflineonline1(line[2])
        Label (subframe,text=line[2].strip('\n')+sta,fg="blue",bg=color,font=(" Times",10)).place(x=100,y=90+(i+2)*per)
        subframe.button=Button(subframe,text='Play>>',activebackground=color,relief=FLAT,bg=color,width=10,command= handler3).place(x=150,y=110+(i+2)*per)
        subframe.button=Button(subframe,text='Status>>',activebackground=color,relief=FLAT,bg=color,width=10,command= handler33).place(x=300,y=110+(i+2)*per)
        '''sts=self.status(line[3])
        if sts==1:
            sta='online'
        else:
            sta='ofline'''
        handler4 = lambda: self.oflineonline(line[3])
        handler44 = lambda: self.oflineonline1(line[3])
        Label (subframe,text=line[3].strip('\n')+sta,fg="blue",bg=color,font=(" Times",10)).place(x=100,y=90+(i+3)*per)
        subframe.button=Button(subframe,text='Play>>',activebackground=color,relief=FLAT,bg=color,width=10,command= handler4).place(x=150,y=110+(i+3)*per)
        subframe.button=Button(subframe,text='Status>>',activebackground=color,relief=FLAT,bg=color,width=10,command= handler44).place(x=300,y=110+(i+3)*per)
        '''sts=self.status(line[4])
        if sts==1:
            sta='online'
        else:
            sta='ofline'''

        handler5 = lambda: self.oflineonline(line[4])
        handler55 = lambda: self.oflineonline1(line[4])
        Label (subframe,text=line[4].strip('\n')+sta,fg="blue",bg=color,font=(" Times",10)).place(x=100,y=90+(i+4)*per)
        subframe.button=Button(subframe,text='Play>>',activebackground=color,relief=FLAT,bg=color,width=10,command= handler5).place(x=150,y=110+(i+4)*per)
        subframe.button=Button(subframe,text='Status>>',activebackground=color,relief=FLAT,bg=color,width=10,command= handler55).place(x=300,y=110+(i+4)*per)
        '''sts=self.status(line[5])
        if sts==1:
            sta='online'
        else:
            sta='ofline'''

        handler6 = lambda: self.oflineonline(line[5])
        handler66 = lambda: self.oflineonline1(line[5])
        
        Label (subframe,text=line[5].strip('\n')+sta,fg="blue",bg=color,font=(" Times",10)).place(x=100,y=90+(i+5)*per)
        subframe.button=Button(subframe,text='Play>>',activebackground=color,relief=FLAT,bg=color,width=10,command= handler6).place(x=150,y=110+(i+5)*per)
        subframe.button=Button(subframe,text='Status>>',activebackground=color,relief=FLAT,bg=color,width=10,command= handler66).place(x=300,y=110+(i+5)*per)


        '''sts=self.status(line[6])
        if sts==1:
            sta='online'
        else:
            sta='ofline'''
        handler7 = lambda: self.oflineonline(line[6])
        handler77 = lambda: self.oflineonline1(line[6])
        Label (subframe,text=line[6].strip('\n')+sta,fg="blue",bg=color,font=(" Times",10)).place(x=100,y=90+(i+6)*per)
        subframe.button=Button(subframe,text='Play>>',activebackground=color,relief=FLAT,bg=color,width=10,command= handler7).place(x=150,y=110+(i+6)*per)
        subframe.button=Button(subframe,text='Status>>',activebackground=color,relief=FLAT,bg=color,width=10,command= handler77).place(x=300,y=110+(i+6)*per)

        '''sts=self.status(line[7])
        if sts==1:
            sta='online'
        else:
            sta='ofline'''

        handler8 = lambda: self.oflineonline(line[7])
        handler88 = lambda: self.oflineonline1(line[7])

        Label (subframe,text=line[7].strip('\n')+sta,fg="blue",bg=color,font=(" Times",10)).place(x=100,y=90+(i+7)*per)
        subframe.button=Button(subframe,text='Play>>',activebackground=color,relief=FLAT,bg=color,width=10,command= handler8).place(x=150,y=110+(i+7)*per)
        subframe.button=Button(subframe,text='Status>>',activebackground=color,relief=FLAT,bg=color,width=10,command= handler88).place(x=300,y=110+(i+7)*per)
        
        '''sts=self.status(line[8])
        if sts==1:
            sta='online'
        else:
            sta='ofline'''
        handler9 = lambda: self.oflineonline(line[8])
        handler99 = lambda: self.oflineonline1(line[8])   
        Label (subframe,text=line[8].strip('\n')+sta,fg="blue",bg=color,font=(" Times",10)).place(x=100,y=90+(i+8)*per)
        subframe.button=Button(subframe,text='Play>>',activebackground=color,relief=FLAT,bg=color,width=10,command= handler9).place(x=150,y=110+(i+8)*per)
        subframe.button=Button(subframe,text='Status>>',activebackground=color,relief=FLAT,bg=color,width=10,command= handler99).place(x=300,y=110+(i+8)*per)
        '''sts=self.status(line[9])
        if sts==1:
            sta='online'
        else:
            sta='ofline'''

        handler10 = lambda: self.oflineonline(line[9])
        handler100 = lambda: self.oflineonline1(line[9])
        Label (subframe,text=line[9].strip('\n')+sta,fg="blue",bg=color,font=(" Times",10)).place(x=100,y=90+(i+9)*per)
        subframe.button=Button(subframe,text='Play>>',activebackground=color,relief=FLAT,bg=color,width=10,command= handler10).place(x=150,y=110+(i+9)*per)
        subframe.button=Button(subframe,text='Status>>',activebackground=color,relief=FLAT,bg=color,width=10,command= handler100).place(x=300,y=110+(i+9)*per)
        '''sts=self.status(line[10])
        if sts==1:
            sta='online'
        else:
            sta='ofline'''
        handler11 = lambda: self.oflineonline(line[10])
        handler111 = lambda: self.oflineonline1(line[10])
        
        Label (subframe,text=line[10].strip('\n')+sta,fg="blue",bg=color,font=(" Times",10)).place(x=100,y=90+(i+10)*per)
        subframe.button=Button(subframe,text='Play>>',activebackground=color,relief=FLAT,bg=color,width=10,command= handler11).place(x=150,y=110+(i+10)*per)
        subframe.button=Button(subframe,text='Status>>',activebackground=color,relief=FLAT,bg=color,width=10,command= handler111).place(x=300,y=110+(i+10)*per)
        handle12=lambda:self.back(subframe)
        subframe.button1=Button(subframe,text='Back',width=10,command=handle12).place(x=170,y=640)
        handle=lambda:self.check(subframe)
        subframe.button2=Button(subframe,text='Next',width=10,command=handle).place(x=600,y=640)
    def cheking(self,str1,val,stri,val1,val2):
        if str1=='':
            tkMessageBox.showinfo("one","cannot be empty")
        else:
            self.onbuttonclick(str1,val,stri,val1,val2)
            
    '''def status(self,string):
        if self.var1=1:
            os.system('net view > lancom.txt')
        f = open('lancom.txt', 'r')
        lis1=[]
        lis1=f.readlines()
        lens=len(lis1)
        st=string.split('\\')
        i=0
        while i in range(lens):
            lis1[i]=lis1[i].lower()
            
            if st[2] in lis1[i]:
                return 1
            i=i+1
        return 0'''    
            
            




        
    def oflineonline(self,string):
        #print string
        #raw_input("press<enter>")
        '''hello=string.split()
        hello=hello[0].split('\\')
        #print hello
        list1=''
        for i in range(len(hello)-1):
            list1=list1+hello[i]+'\\'
            
        #print list1
        try:
            con=os.listdir(list1)
            return 1
        except:
            return 0'''
        t=0
        if os.path.isdir(string.strip('\n')) or os.path.isfile(string.strip('\n')):
             tkMessageBox.showinfo("one","content is available \n click OK to download and traverse into \n folder \n otherwise cancel it!!!!")
             t=1
            
        else:
            tkMessageBox.showinfo("one"," CAN'T PLAY\ncontent is not available!!!!")
        if t==1:
            os.startfile(string.strip('\n'))
    def oflineonline1(self,string):
        #print string
        #raw_input("press<enter>")
        '''hello=string.split()
        hello=hello[0].split('\\')
        #print hello
        list1=''
        for i in range(len(hello)-1):
            list1=list1+hello[i]+'\\'
            
        #print list1
        try:
            con=os.listdir(list1)
            return 1
        except:
            return 0'''
        t=0
        if os.path.isdir(string.strip('\n')) or os.path.isfile(string.strip('\n')):
             tkMessageBox.showinfo("one","content is available ")
             t=1
            
        else:
            tkMessageBox.showinfo("one","content is not available")
               
        
        
        

    
    def check(self,subframe):
        self.h=0
        
        if self.var*11<self.lenf:
            self.var=self.var+1
            self.onbuttonclick(self.glob,self.var,subframe,1,4)
        else:
            tkMessageBox.showinfo("one","Next is not possible")

        
    def back(self,subframe):
        
        if self.var>0:
           
            self.var=self.var-1
            self.onbuttonclick(self.glob,self.var,subframe,1,4)
        else:
             tkMessageBox.showinfo("one","Back not posible")
    def download(self,string,copy):
        
        if os.path.isdir(string.strip('\n')) or os.path.isfile(string.strip('\n')):
            location=self.copylocation(string)
            size=os.path.getsize(string.strip('\n'))
            print size
            try:
                thread.start_new_thread( self.copy, ("Thread-1", string,location, ) )
                thread.start_new_thread( self.progress, ("Thread-2", location,size, ) )
            except:
                tkMessageBox.showinfo("one","Error in download")
        else:
             tkMessageBox.showinfo("one","content is not present")
            
                
    def copy(self,thread,string,copy):
        print 'I am in copy'
        shutil.move(string.strip('\n'),copy)
    def progress(self,copy,size):
        '''if os.path.isdir(copy)or os.path.isfile(copy):
            print 'yes'
        while os.path.getsize(copy)<=size:
                print (os.path.getsize(copy)/size)*100
        else :
            print 'not present'''

        try:
            while i in range(10):
                    print i
        except:
            print ' possible'
            
        

        
    def copylocation(self,string):
        '''co=tk.Tk()
        co.geometry("300x200")
        Label (co,text='copy location',font=(" Times",10)).place(x=5,y=90)
        co.entryVariable = tk.StringVar()
       
        
        co.entry1 = tk.Entry(co,width=30,textvariable=co.entryVariable)
        co.entry1.place(x=110,y=90)#side='top',padx=300,pady=10)
        handle=lambda:self.dest(co.entryVariable.get())
        return co.entryVariable.get()
        co.button2=Button(co,text='copy',width=10,command=handle).place(x=200,y=120)'''
        return 'd:\\h.txt'
        
       


        
    def onbuttonleft(self,s):
        
        ######print s
        pass
           
    def process(self,stri):
        line = stri.lower()
        
        con=[]
        for word in line.split():
            s=word[0].lower()
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
                        if k+j>wordlen-1:## case when the lenght of the word is less the range
                            if count>=eitper:
                                newper=(count/wordlen)*100
                                tupl=[count,lino]
                                check=count
                                ##print tupl
                    
                            break
                        if k>(len(search)-1):
                            ## lenght of range is greater for searched string...
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
        d={}
        for key, val in con:## to convert tuple of tuples of two values..into a dictionary having for given length corrosponding line number
            d.setdefault(key, []).append(val)  

        ######print d
        lent=len(con)
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
            ###### print dic
            ######print final
        ######print final
        lenghtic= len(final)
        listfinal=[]
        listk=[]
        for key in final:
            listk.append(key)
        listk.sort()

        
        
            
        for key in listk:
             secdic=final[key]
             ######print secdic[0]
             tempdic=secdic[0]
             ##print listfinal
             ######raw_input('press<enter>')
             for key2 in tempdic:
                 listfinal=listfinal+tempdic[key2]   
        ######print listfinal        
        s=1    
        i=0
        a=listfinal

        b=a
        c=[]
        lengh=len(a)
        while i<(len(b)):
              
              j=0
              ## print b[i:lengh]
              if b[i] not in b[i+1:lengh]:
                  c.append(b[i])
              i=i+1
        listfinal=c
        lenf=len(listfinal)
        ######print listfinal
    
        while s<=lenf:
               value=int(listfinal[lenf-s])
               ######print value
               line = linecache.getline('C:\Python26\search engine(se)\linkentry.txt', value)
               ######print line
               s=s+1
        return listfinal;

           
        
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x600")
   ## canvas = Canvas(root, width=800, height=600)
   ## canvas.place(x=0,y=30)
   ## root.configure(background='yellow')
   
   ## im = Image.open("c:/Python26/4.png")
   
   ## cropped = im.crop((0, 0, 800, 570))
   ## tk_im = ImageTk.PhotoImage(im)
    ##canvas.create_image(600, 400, image=tk_im)
    app = MyApp(root)
    root.mainloop()
