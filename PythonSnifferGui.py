# -*- coding: cp1252 -*-

#Modules Required

                                                                #USED FOR-->
from Tkinter import *                                           #GUI Development
import time                                                     #time shown on ststus bar
from tkFileDialog   import askopenfilename,asksaveasfilename    #Dialog box opened when open and save file using menu
from pcapy import findalldevs,open_live                         #Finding all interfaces on the computer
from impacket import ImpactDecoder, ImpactPacket                #Decoding the Raw Packets Captured
import thread                                                   #Threading the Sniffer so it will not freeze the mainloop of GUI    
import sys                                                      #
import tkMessageBox                                             #Popup box


 


                                                        #GLOBAL VARIABLES

var=''                                                          #var is the variable for checkboxes(select the interface)
curtime = ''                                                    #time shown on the statusbar
interface1=''                                                   #Interface for sniffing

                                                        ####MAIN FUNCTION programming#######

def main():                                                     #Main function
    def sel():                                                  #A function for Selecting the interface    
        global interface1                                       #global keyword is used for accesing global variable   
        interface1 =  str(var1.get())                           #retriving value from Radiobutton variable 'var' using get method 

    devices = findalldevs();                                    #Find all Devices "eth0,lo, wlan0 ..etc" All values are in array 'devices'

    eth0=str(devices[0])                                        # saving the devices value in linux style  [ethernet cable]
    wlan0=str(devices[1])                                       # """""""""""""""""""""""""""""""""""""""  [Wireless LAN]
    nflog=str(devices[2])                                       # """""""""""""""""""""""""""""""""""""""  [Kernel...High level]
    lo=str(devices[3])                                          # """""""""""""""""""""""""""""""""""""""  [Local host]

    
    try :                                                       # Exceptional Handling [try keyword]  
        def sniffme():                                          # Function for beginning sniffer

            global interface1                                   #Accesing global variable
            print "Sniffer Initiated "                          #printing message
            for i in range(10):                                 #for loop is used to write 10 number of dots before printing ant result [just for fun ] No offence
                sys.stdout.write('.')                           # use of sys module to access stdout "which prints ['.']"
                time.sleep(.3)                                  #sleep for 300ms after printing '.'
            sys.stdout.write('Here we Go -->')                  #Same as Before
            time.sleep(.3)    
            pc = open_live(interface1, 65536, True, 1000)   ####OPen_live is a function in Pcapy for sniffing the real time packets. Arguments passed-->"Name of the Interface",Number of Bytes to capture,"Promiscus mode on/off","time to read"
            pc.setfilter('tcp')                                 #Default packet filter is set to TCP


                                                            ####DECODING OF RAW PACKET
            def processPacket(hdr, data):                       #A Function name processPacket
                decoder = ImpactDecoder.EthDecoder()            #use of Decoder module and method
                packet=decoder.decode(data)                     #here data is the raw data capture by pcapy's open_live function
                ippacket=packet.child()                         #ip packets
                tcppacket=packet.child()                        #TCP packets
                print tcppacket                                 #Final capture Packets are printed on console 
            packet_limit = -1                                   #local variable set for looping the printing of live packet captures
            pc.loop(packet_limit, processPacket)                #pc.loop [here pc is the pcapy open_live function output]
    except(KeyboardInterrupt, SystemExit):                      #If any Keyboard interrupt happens then the sniffer stops and exits
                cleanup_stop_thread();                          #Stoping thread
                 
                
            

                                    ####################GRAPHICAL USER INTERFACE ########################
    
    root=Tk()                                                   #Main Window [Whole]
    root.minsize(700,500)                                       #minimum size is set too 700 wide and 500 height
    root.maxsize(700,500)                                       #Maximum """""""""""""""""""""""""""""""""""""""
    root.geometry("700x500")                                    #Normal Geometry [size] when program run 
    root.title("Packet Sniffer 0.1")                            # Title of the Window [Titlebar]

    
    

    def callback():                                             #Test Function to print a message
        print "called the callback!"
        
    def OpenFile():                                                                                             
        name = askopenfilename(filetypes=[("PCAP file","*.pcap")],title="Open PCAP file")                           #dialog box for opening a file

    def SaveFile():
        asksaveasfilename(filetypes=[("PCAP file","*.pcap")],title="Save PCAP file")                                #Dialog Box for Saving a file 

    def quitGui():                                                                                                  # Quiting the Program   
        tkMessageBox.showinfo(title = 'Quit', message = "Do you really Want to Exit? ")                             #Message box asking the action
        root.destroy()                                                                                              #Gui Closed

    menu= Menu(root)                                                                                                #Menubar Created under main'root' window
    root.config(menu=menu)                                                                                          #name of the menubar is menu   

    filemenu=Menu(menu)                                                                                             #first parent menu 'filemenu' in menubar named 'menu'
    menu.add_cascade(label="File",menu=filemenu)                                                                    #name of the parent menu is 'File'
    filemenu.add_command(label="Open",command=OpenFile)                                                             #submenu with action[command to execute]
    filemenu.add_command(label="Save",underline=0,background='white',activebackground='orange',command=SaveFile)    #submenu with action"""""""""""""""""""

    filemenu.add_separator()                                                                                        #                                               
    filemenu.add_command(label="Exit",command=root.quit)                                                            #
    helpmenu=Menu(menu)                                                                                             #Same function as above
    menu.add_cascade(label="Help", menu=helpmenu)                                                                   #
    helpmenu.add_command(label="About...",command=callback)                                                         #
  
    
    ################################################################
    
    fm = Frame(root, width=500, height=500,bg= "#374a89")                                                           #Frame is created under root with given Dimentions
    xf2=Frame(root,height=200,width=500,bg="green")                                                                 #anather frame with attributes 'bg is background'
                                                                                                                    #Note:Attributes are Case Sensitive 
    xf=Frame(fm, relief="solid", borderwidth=2,pady=8,bg='grey')                                                    #pady is padding in y direction
    Label(xf, text="SELECT INTERFACE",relief='flat',bg='#526aba', fg='white').pack(pady=3,padx=10,side=LEFT)        #side is the "where to place in respect of previous one"

    var1=StringVar()
    Radiobutton(xf, text='eth0', variable=var1,
                value=eth0,command=sel).pack(side=LEFT, anchor=W,padx=3)
    Radiobutton(xf, text='wlan0', variable=var1,
                value=wlan0,command=sel).pack(side=LEFT, anchor=W,padx=3)
    Radiobutton(xf, text='lo', variable=var1,
                value=lo,command=sel).pack(side=LEFT, anchor=W,padx=3)
    Radiobutton(xf, text='nflog', variable=var1,
                value=nflog,command=sel).pack(side=LEFT, anchor=W,padx=3)
    
    
    label1=Label(xf,text='ENTER MANUALLY',relief='flat',bg='#526aba', fg='white').pack(side=LEFT,anchor=W)

    InterfaceText=StringVar()
    InterfaceEntry=Entry(xf,textvariable=InterfaceText)
    InterfaceEntry.focus_set()
    InterfaceEntry.pack(side=LEFT,anchor=W,padx=15)


    def setInterface(): interface1=InterfaceText
    bt1=Button(xf,text="Okay",relief='ridge',width=15, command=setInterface,bg='#526aba', fg='white').pack(side=LEFT,anchor=W,padx=5,pady=2)
    xf.pack(side=TOP , anchor=NW,expand=NO,fill=BOTH)
    #f.pack(side=TOP, anchor=NW)





    # t2 = Toplevel(root)
    #Label(t2, text='Result will be shown Here').pack(padx=10, pady=10)
    #t2.transient(root)
    
    # create a toolbar
    toolbar = Frame(root,  bg="#374a89" , relief='raised')



    openbutton = Button(toolbar, text="Open", width=6, command=OpenFile)
    openbutton.pack(side=LEFT, padx=2, pady=2)

    b = Button(toolbar, text="Save", width=6, command=SaveFile)
    b.pack(side=LEFT, padx=2, pady=2)
    
    saveandexit = Button(toolbar, text="  Exit  ", command=quitGui)
    saveandexit.pack(side=RIGHT, padx=2, pady=2,anchor=N)

    clock = Label(toolbar,bg='#374a89',fg='white')
    clock.pack(anchor=CENTER,padx=0)


    def tick():
        global curtime
        newtime = time.strftime('%H:%M:%S')
        if newtime != curtime:
            curtime = newtime
            clock.config(text=curtime)
        clock.after(200, tick)

    tick()


    
    toolbar.pack(side=TOP, fill=BOTH,expand=NO)

    
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
    Label(fm, text='NUMBER OF BYTES TO CAPTURE',relief='solid',bg="black",fg="white",height=1,width=30,bd=5).pack(side=LEFT,anchor=NW,padx=5,pady=6)
    
    var = StringVar()
    entry = Entry(CountFrame, textvariable=var,width=5,relief='ridge',bd=1)
    entry.focus_set()
    entry.pack(side=LEFT,padx=3)
    var.set(root.title())
    def changeTitle(): root.title(var.get())
    var.set(1024)
    
    Button(CountFrame, text="SET", command=changeTitle,bg='#004e00', fg='white').pack()
    CountFrame.pack(side=LEFT,anchor=NW,pady=6,padx=1)
    ###############################################################################################
    scrollbar = Scrollbar(xf2)
    scrollbar.pack(side=RIGHT, fill=Y)

    listbox = Text(xf2, yscrollcommand=scrollbar.set,bg='black',fg='red')
    Z="""                                   ..:::::::::..          
                               ..:::aad8888888baa:::..      
                            .::::d:?88888888888?::8b::::.           
                          .:::d8888:?88888888??a888888b:::.       
                        .:::d8888888a8888888aa8888888888b:::.       
                       ::::dP::::::::88888888888::::::::Yb::::       
                      ::::dP:::::::::Y888888888P:::::::::Yb::::         
                     ::::d8:::::::::::Y8888888P:::::::::::8b::::        
                    .::::88::::::::::::Y88888P::::::::::::88::::.      
                    :::::Y8baaaaaaaaaa88P:T:Y88aaaaaaaaaad8P:::::      
                    :::::::Y88888888888P::|::Y88888888888P:::::::      
                    ::::::::::::::::888:::|:::888::::::::::::::::      
                    `:::::::::::::::8888888888888b::::::::::::::'       
                     :::::::::::::::88888888888888::::::::::::::      
                      :::::::::::::d88888888888888:::::::::::::        
                       ::::::::::::88::88::88:::88::::::::::::       
                        `::::::::::88::88::88:::88::::::::::'          
                          `::::::::88::88::P::::88::::::::'          
                            `::::::88::88:::::::88::::::'    
                               ``:::::::::::::::::::''     
                Packet Sniffer      ``:::::::::''      Beta*

                    Gathering Realtime Data in the Network  """
    listbox.insert(END,Z)
    listbox.pack(side=LEFT, fill=BOTH,expand=YES)

    scrollbar.config(command=listbox.yview)



    ######################################################################################
        

    print "[+]Please Select the Interface "
    ##############################################################################################################
    def threadone():
        try:
            thread.start_new_thread(sniffme,())
        except (KeyboardInterrupt, SystemExit):
            cleanup_stop_thread();
            sys.exit()
            

    def threadinterrupt():
        thread.interrupt_main()

    MainButton1=Button(fm,text="Stop Capture",bg="Red", fg="white",height=2,relief='ridge',command=quitGui,activebackground='#eb0000',activeforeground='white').pack(side=RIGHT,anchor=NE,pady=1,expand=YES,fill=X)
    MainButton=Button(fm,text="Start Capture",bg="#004e00", fg="white",height=2,relief='ridge',command=threadone,activebackground='#003a00',activeforeground='white').pack(side=RIGHT,anchor=NE,pady=1,padx=2,expand=YES,fill=X)


    ##############################################################################

    
    #######################################################################
    fm.pack(side=TOP, expand=YES, fill=X)
    xf2.pack()

    root.mainloop()
if __name__=="__main__":
   
    main()
    
