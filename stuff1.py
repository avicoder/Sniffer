# -*- coding: cp1252 -*-
from Tkinter import *
import time
curtime = ''
def main():

    root=Tk()
    root.minsize(700,500)
    root.maxsize(700,500)
    root.geometry("700x500")
    root.title("Packet Sniffer 0.1")

    def callback():
        print "called the callback!"

   # def quit(self):
   #     root.destroy()

    menu= Menu(root)
    root.config(menu=menu)

    filemenu=Menu(menu)
    menu.add_cascade(label="File",menu=filemenu,)
    filemenu.add_command(label="New",underline=0,background='white',activebackground='orange',command=callback)
    filemenu.add_command(label="Open",command=callback)
    filemenu.add_separator()
    filemenu.add_command(label="Exit",command=callback)

    helpmenu=Menu(menu)
    menu.add_cascade(label="Help", menu=helpmenu)
    helpmenu.add_command(label="About...",command=callback)
  
    #Label(root, text='This is a label program').pack(pady=10)
    ################################################################
    
    fm = Frame(root, width=500, height=500,bg= "#374a89")
 


    xf=Frame(fm, relief=SOLID, borderwidth=1,pady=5)
    Label(xf, text="SELECT INTERFACE",relief='flat',bg='#526aba', fg='white').pack(pady=10,padx=10,side=LEFT)

    interface=IntVar()
    Radiobutton(xf, text='eth0', variable=interface,
                value='eth0').pack(side=LEFT, anchor=W,padx=15)
    Radiobutton(xf, text='wlan0', variable=interface,
                value='wlan0').pack(side=LEFT, anchor=W,padx=15)
    Radiobutton(xf, text='lo', variable=interface,
                value='lo').pack(side=LEFT, anchor=W,padx=15)
    
    label1=Label(xf,text='ENTER MANUALLY',relief='flat',bg='#526aba', fg='white').pack(side=LEFT,anchor=W)

    InterfaceText=StringVar()
    InterfaceEntry=Entry(xf,textvariable=InterfaceText)
    InterfaceEntry.focus_set()
    InterfaceEntry.pack(side=LEFT,anchor=W,padx=15)
    #InterfaceText.set(interface)
    #.set(InterfaceText)

    def setInterface(): interface=InterfaceText
    bt1=Button(xf,text="Okay",relief='groove',width=15, command=setInterface,bg='#526aba', fg='white').pack(side=LEFT,anchor=W,padx=5,pady=2)
    xf.pack(side=TOP , anchor=NW,expand=NO,fill=BOTH)
    #f.pack(side=TOP, anchor=NW)





    # t2 = Toplevel(root)
    #Label(t2, text='Result will be shown Here').pack(padx=10, pady=10)
    #t2.transient(root)
    
    # create a toolbar
    toolbar = Frame(root,  bg="#374a89" , relief='raised')

    b = Button(toolbar, text="new", width=6, command=callback)
    b.pack(side=LEFT, padx=2, pady=2)

    b = Button(toolbar, text="open", width=6, command=callback)
    b.pack(side=LEFT, padx=2, pady=2)


    clock = Label(toolbar,bg='#374a89',fg='white')
    clock.pack(side=RIGHT,anchor=NE)

    def tick():
        global curtime
        newtime = time.strftime('%H:%M:%S')
        if newtime != curtime:
            curtime = newtime
            clock.config(text=curtime)
        clock.after(200, tick)

    tick()
    
    toolbar.pack(side=TOP, fill=X)

    
    #################################################
    Label(fm, text='FILTER',relief='solid',bg="black",fg="white",height=1,width=7,bd=5).pack(side=LEFT,anchor=NW,padx=1,pady=6)

    SelectProtocol=Frame(fm,bg="#91d46a",relief='ridge',bd=2)

    
    

    class Dummy: pass
    var = Dummy()

    for castmember, row, col, status in [
        ('TCP', 0,0,NORMAL), ('ICMP', 0,1,NORMAL),
        ('IP', 0,2,NORMAL)]:
        setattr(var, castmember, IntVar())
        Checkbutton(SelectProtocol, text=castmember, state=status, anchor=W,
          variable = getattr(var, castmember),height=1,relief='flat',bg='#91d46a').grid(row=row, column=col, sticky=W)

    
    
    SelectProtocol.pack(side=LEFT,anchor=NW,padx=1,pady=6)




    
    ##################################################
    CountFrame=Frame(fm,relief='ridge',bg='#91d46a',bd=1)
    Label(fm, text='NUMBER OF PACKETS TO CAPTURE',relief='solid',bg="black",fg="white",height=1,width=30,bd=5).pack(side=LEFT,anchor=NW,padx=5,pady=6)
    
    var = StringVar()
    entry = Entry(CountFrame, textvariable=var,width=5,relief='ridge',bd=1)
    entry.focus_set()
    entry.pack(side=LEFT,padx=3)
    var.set(root.title())
    def changeTitle(): root.title(var.get())
    var.set(20)
    
    Button(CountFrame, text="SET", command=changeTitle,bg='#004e00', fg='white').pack()
    CountFrame.pack(side=LEFT,anchor=NW,pady=6,padx=1)
    ###############################################################################################
    
    





    ######################################################################################
        

    print InterfaceText
 ##############################################################################################################

    MainButton=Button(fm,text="Start Capture",bg="Red", fg="white",width=25,height=4,relief='solid').pack(side=BOTTOM,anchor=SW)
    

    #######################################################################
    fm.pack(side=TOP, expand=YES, fill=BOTH)
    root.mainloop()

if __name__=="__main__":
   
    main()
    
