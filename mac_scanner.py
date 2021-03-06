from tkinter import *
from tkinter.ttk import Progressbar
import os , subprocess , threading , keyboard , time
import concurrent , requests
from concurrent import futures
# Find devices in your local network.

def start_program() :

    def ping_range(start,count) :   # IP SCANNER


        prefix = "10.1.1."  # Input your own IP range here.
        condition = "Destination host unreachable" 
        condition2 = "Request timed out"
        list1 = []
        #list2 = []

        for xxx in range(start,start+count) :
        
            ip = prefix + str(xxx)
            code = "ping " + ip + " -n 1 -l 1"    
            code2 = "arp -a " + ip
            ping = os.popen(code).read()            
       
            if condition not in ping and condition2 not in ping:  # Checks if the IPs are alive.
                #print(G + ip)               
                #list1.append(ip)
                try:
                    arp = os.popen(code2).read().split('\n')  # Retrieve the MAC address.
                    arpS = str(arp[3])
                    mac_loc = arpS.find('-')
                    mac = arpS[(mac_loc-2):(mac_loc+15)]

                    macsite_url = "https://macvendors.com/query/" + mac
                    vendor_res = requests.get(macsite_url)   # Retrieve the MAC vendor.

                    if vendor_res.status_code == 200 :
                        vendor = vendor_res.text
                    else:
                        vendor = "[Not Found]"

                    IPnMACnVendor = ip + "  " + mac + "  " + vendor
                    list1.append(IPnMACnVendor)
            
                except Exception as e :             
                    #IPnNon = ip + "  [Not Found]"
                    #list1.append(IPnNon)
                    getmac = os.popen("getmac /V /FO LIST").read().split('\n\n')

                    for x in range(int(len(getmac))) :
    
                        if 'Wi-Fi' in getmac[x] :
                            getmc = getmac[x]

                    ps_adrs = getmc.find('Physical Address:')
                    mac2 = getmc[(ps_adrs+18):(ps_adrs+35)]
                    mac2.replace('-',':')

                    macsite_url = "https://macvendors.com/query/" + mac2
                    vendor_res = requests.get(macsite_url)   

                    if vendor_res.status_code == 200 :
                        vendor = vendor_res.text
                    else:
                        vendor = "[Not Found]"

                    IPnMACnVendor = ip + "  " + mac2 + "  " + vendor
                    list1.append(IPnMACnVendor)

        return list1 


    tasks = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=30) as executor :  # Multi Threading.
        for start in [0,11]:
            tasks.append(executor.submit(ping_range,start,10))
        
        for start in [21,31]:
            tasks.append(executor.submit(ping_range,start,10))
        
        for start in [41,51]:
            tasks.append(executor.submit(ping_range,start,10))
        
        for start in [61,71]:
            tasks.append(executor.submit(ping_range,start,10))
        
        for start in [81,91]:
            tasks.append(executor.submit(ping_range,start,10))
        
        for start in [101,111]:
            tasks.append(executor.submit(ping_range,start,10))
        
        for start in [121,131]:
            tasks.append(executor.submit(ping_range,start,10))
            #GH0STH4CK3R
        for start in [141,151]:
            tasks.append(executor.submit(ping_range,start,10))
        
        for start in [161,171]:
            tasks.append(executor.submit(ping_range,start,10))
        
        for start in [181,191]:
            tasks.append(executor.submit(ping_range,start,10))

        for start in [201,211]:
            tasks.append(executor.submit(ping_range,start,10))

        for start in [221,231]:
            tasks.append(executor.submit(ping_range,start,10))

        for start in [241,248]:
            tasks.append(executor.submit(ping_range,start,7))
        
    #empty_tsk = 0
    new_ilist = []
    
    for task in tasks:  # Output the values from each thread.
        if len(task.result()) == 1 :  
            new_ilist.append(task.result()[0])
        elif len(task.result()) > 1 :
            for elmnt in range(len(task.result())) :
                new_ilist.append(task.result()[elmnt])
    
    #print(new_ilist)
        #elif len(task.result()) == 0 :
            #empty_tsk += 1
    
    #if empty_tsk >= 254 :
        #print("No IPs found!")

    return new_ilist

# Tkinter GUI
window = Tk()
window.title("IP Scanner")
try:
    window.iconbitmap(r'C:\ipscanner.ico')
except Exception as iconbitmaperror:
    pass # Ignore the file path if icon is not found.

window.geometry("540x540")

lbl = Label(window, text="IP & MAC Address Scanner" , font=("Roboto",25),fg="blue")
lbl.grid(column=0,row=0,padx=70)

def clicked() :
    st_return = start_program()
    btn.config(text="Scan Complete!",bg="blue", fg="white")
    iplstnfo = "\n"

    txt2 = Label(window,anchor="w",text="IP ADDRESS |   MAC ADDRESS |   MANUFACTURER",font=("Montserrat",15),fg="blue")
    txt2.grid(column=0,row=3)

    for lll in range(len(st_return)) :

        iplstnfo += st_return[lll]  + "\n"    
    #print(iplstnfo)
    
    w = Text(window, height=12, borderwidth=0,font=("Montserrat",15),width=47)
    w.grid(column=0,row=5)
    w.insert(1.0, iplstnfo)
    w.configure(state="disabled")
    # Comment this section out if you want to use an older version of Tkinter.

    w.configure(inactiveselectbackground=w.cget("selectbackground"))
    #txt = Label(window,text=iplstnfo,font=("Century Gothic",18),justify=LEFT)
    #txt.grid(column=0,row=4)
    # lbl3 = Label(window, text="Add your own footer here" , font=("Roboto",15) ,fg="green")
    # lbl3.grid(column=0,row=10,pady=20)

btn = Button(window, text="   SCAN >  " , font=("Roboto",18) , command=clicked , fg="blue")
btn.grid(column=0,row=2,pady=35)



window.mainloop()   # Tkinter Mainloop. 