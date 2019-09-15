#test
import sys
from win10toast import ToastNotifier
import threading
import Tmodules.treye as treye
import Tmodules.welcome as welcome

from sqlite3 import *
import time
import os
toaster = ToastNotifier()

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import GUI_support
import os.path
import bitly_api
import psycopg2
import runpy
import tkinter.messagebox


#Bitly
API_USER = os.environ['BITLY_API_USER']
API_KEY = os.environ['BITLY_KEY']
bitly = bitly_api.Connection(API_USER, API_KEY) 




def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    global prog_location,varEntry,varEntry2,varEntry3
    prog_call = sys.argv[0]
    prog_location = os.path.split(prog_call)[0]
    root = tk.Tk()
    root.iconbitmap('icon\icon.ico')
    varEntry = tk.StringVar(root,value="")
    varEntry2 = tk.StringVar(root,value="")
    varEntry3 = tk.StringVar(root,value="")
    top = Toplevel1 (root)
    root.geometry("1027x642+300+100")
    root.resizable(0, 0)
    #root.overrideredirect(True)
    GUI_support.init(root, top)
    root.mainloop()


def close_window (): 
    root.destroy()

def test_notification():
    toast_logo = os.path.join(prog_location,"../Python main/icon/icon.ico")
    toaster.show_toast("Treye","This is a test Notification!",icon_path=toast_logo,duration=5,threaded=True)
    treye.testmessage()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    global prog_location
    prog_call = sys.argv[0]
    prog_location = os.path.split(prog_call)[0]
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    GUI_support.init(w, top, *args, **kwargs)
    return (w, top)

def status(self,text=None):
        Text ='Treye Status : ' + text
        self.Label4_3.configure(text=Text)
        root.update()


def destroy_Toplevel1():
    global w
    w.destroy()
    w = None


class Toplevel1:
    def nointernet(self):
        #tkinter.messagebox.askretrycancel("Treye","Please check your internet connection and try again.\nError: No Internet Connection")
        retrycancel = tkinter.messagebox.askretrycancel("Treye","Please check your internet connection and try again.\nError: No Internet Connection")
        #print(retrycancel)
        if retrycancel == True:
            self.check_internet_connection()

    def status(self,text=None):
        Text ='Treye Status : ' + text
        self.Label4_3.configure(text=Text)
        root.update()

    def onlinestatusd(self,status=None):
        if status == True:
            self.onlinestatus.configure(text='• Online')
            root.update()
        else:
            self.onlinestatus.configure(text='• Offline')
            root.update()


    def check_internet_connection(self):
        try:
            bitly_d=bitly.shorten('https://www.google.com')
            self.onlinestatusd(status=True)
        except (bitly_api.bitly_api.BitlyError) as error:
            a = str(error)
            if a == '<urlopen error [Errno 11001] getaddrinfo failed>':
                self.onlinestatusd(status=False)
                self.status('No internet connection')
                self.Label4_3.configure(text='')
                root.update()
                self.nointernet()
            else:
                self.status(str(error))
                print(error)


    def refresh_data_entry(self):

        global url_titlen,url_titleh,prod_pricem,short_linkh
# auto Entry
        try:
            connection = psycopg2.connect(user = "postgres",
                                        password = "mr5tr4n63",
                                        host = "127.0.0.1",
                                        port = "5432",
                                        database = "Treye_data")
            cursor = connection.cursor()

            cursor.execute("SELECT * FROM data")
            connection.commit()
            numrows = int(cursor.rowcount) - 1
            # if numrows = 0 
            self.status("Fetching Data Please wait..")
            for x in range(0,numrows):
                row = cursor.fetchone()
                print (row[1])
                url_titleh = row[1]
                url_titlem =  url_titlel[:33]
                prod_pricem = row[3]
                short_linkh = url_titlem + '..... Rs. ' + str(prod_pricem)
                self.lstbx1.insert('end', short_linkl)
                root.update()
                #time.sleep(0.5)
            connection.commit()
            self.Label4_3.configure(text='')
            root.update()

        except (Exception, psycopg2.DatabaseError) as error :
            print ("Treye Module Error:Error while creating PostgreSQL table", error)


    def refresh_data(self):
        global url_titlen,url_titlel,prod_pricen,short_linkl
# auto Entry
        try:
            connection = psycopg2.connect(user = "postgres",
                                        password = "mr5tr4n63",
                                        host = "127.0.0.1",
                                        port = "5432",
                                        database = "Treye_data")
            cursor = connection.cursor()

            cursor.execute("SELECT * FROM data")
            connection.commit()
            numrows = int(cursor.rowcount)
            if numrows > 0: 
                self.status("Fetching Data Please wait..")
                for x in range(0,numrows):
                    row = cursor.fetchone()
                    print (row[1])
                    url_titlel = row[1]
                    url_titlen =  url_titlel[:33]
                    prod_pricen = row[3]
                    short_linkl = url_titlen + '..... Rs. ' + str(prod_pricen)
                    self.lstbx1.insert('end', short_linkl)
                    root.update()
                    time.sleep(0.2)
            elif numrows == 0:
                time.sleep(2)
                self.status("data not found")
                print("data not found")
            connection.commit()
            self.Label4_3.configure(text='')
            root.update()

        except (Exception, psycopg2.DatabaseError) as error :
            print ("Treye Module Error:Error while creating PostgreSQL table", error)

    def add_link(self):
        global status,i,url_title,prod_price
        self.status(text='Please wait Reading Data')
        to_add = varEntry.get()
        try:
            bitly_d=bitly.shorten(to_add)
        except (bitly_api.bitly_api.BitlyError) as error:
            a = str(error)
            if a == '<urlopen error [Errno 11001] getaddrinfo failed>':
                self.onlinestatusd(status=False)
                self.status('No internet connection')
                self.Label4_3.configure(text='')
                root.update()
                self.nointernet() 
        varEntry.set('')
        root.update()
        self.status(text='Validating Data')
        try:
            treye.crawler(to_add,API_USER,API_KEY)
        except (bitly_api.bitly_api.BitlyError) as error:
            a = str(error)
            if a == '<urlopen error [Errno 11001] getaddrinfo failed>':
                self.onlinestatusd(status=False)
                self.status('No internet connection')
                self.Label4_3.configure(text='')
                root.update()
                self.nointernet()
        self.status(text='Product Found')
        time.sleep(1)
        url_title = treye.title()
        prod_price = treye.productprice()
        short_link = url_title[:33] + '..... Rs. ' + str(prod_price)
        time.sleep(2)
        self.status(text='Adding Previous Entry')
        self.refresh_data_entry()
        self.status(text='Adding Entry')
        self.lstbx1.insert('end',short_link)
        self.status(text='Done')
        treye.notify()
        url_title = treye.title()
        prod_price = treye.productprice()
        #curval.execute("INSERT INTO Links VALUES(" + str(i) + ",'" + url_title +"','" + short_link + "'," + str(prod_price) + ")")
        #curval.execute("commit")
        #print("INSERT INTO Links VALUES(" + str(i) + ",'"+ url_title +"','" + short_link + "'," + str(prod_price) +")\n\n")

    def add_shortlink(self):
        global short_url
        main_url = varEntry2.get()
        #print(main_url)
        bitly_data = bitly.shorten(main_url)
        short_url = bitly_data["url"]
        #print(short_url) 
        #self.newurltxt.configure(varEntry2.set(short_url))
        varEntry3.set(short_url)

    def __init__(self, top=None):
        root.after(2000, self.refresh_data)
        root.after(5000, self.check_internet_connection )
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font10 = "-family Calibri -size 14 -weight bold -slant roman "  \
            "-underline 0 -overstrike 0"
        font15 = "-family Calibri -size 20 -weight bold -slant roman "  \
            "-underline 0 -overstrike 0"
        font17 = "-family Calibri -size 16 -weight bold -slant roman "  \
            "-underline 0 -overstrike 0"
        font19 = "-family Calibri -size 12 -weight bold -slant roman "  \
            "-underline 0 -overstrike 0"
        font20 = "-family Calibri -size 13 -weight bold -slant roman "  \
            "-underline 0 -overstrike 0"

        top.geometry("1032x661+439+196")
        top.title("Treye")
        top.configure(background="#323539")

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.0, rely=-0.015, height=66, width=1032)
        self.Label2.configure(background="#2A2D30")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(width=1032)

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.097, rely=1.142, height=46, width=185)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        photo_location = os.path.join(prog_location,"../Python main/icon/Main-01.png")
        global _img0
        _img0 = tk.PhotoImage(file=photo_location)
        self.Label1.configure(image=_img0)
        self.Label1.configure(text='''Label''')
        self.Label1.configure(width=185)

        self.Label3 = tk.Label(top)
        self.Label3.place(relx=0.0, rely=0.008, height=45, width=182)
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        photo_location = os.path.join(prog_location,"../Python main/icon/Main-01.png")
        global _img1
        _img1 = tk.PhotoImage(file=photo_location)
        self.Label3.configure(image=_img1)
        self.Label3.configure(text='''Label''')
        self.Label3.configure(width=182)

       
        # self.exit = tk.Button(top)
        # self.exit.place(relx=0.94, rely=0.0, height=30, width=56)
        # self.exit.configure(activebackground="#ececec")
        # self.exit.configure(activeforeground="#000000")
        # self.exit.configure(background="#d9d9d9")
        # self.exit.configure(borderwidth="0")
        # self.exit.configure(disabledforeground="#a3a3a3")
        # self.exit.configure(foreground="#000000")
        # self.exit.configure(highlightbackground="#d9d9d9")
        # self.exit.configure(highlightcolor="black")
        # photo_location = os.path.join(prog_location,"../Python main/icon/Close-02-02.png")
        # global _img2
        # _img2 = tk.PhotoImage(file=photo_location)
        # self.exit.configure(image=_img2)
        # self.exit.configure(pady="0")
        # self.exit.configure(text='''Button''')
        # self.exit.configure(width=62)
        # self.exit.configure(command = close_window)

        
        # self.minimize = tk.Button(top)
        # self.minimize.place(relx=0.877, rely=0.0, height=30, width=56)
        # self.minimize.configure(activebackground="#ececec")
        # self.minimize.configure(activeforeground="#000000")
        # self.minimize.configure(background="#d9d9d9")
        # self.minimize.configure(borderwidth="0")
        # self.minimize.configure(disabledforeground="#a3a3a3")
        # self.minimize.configure(foreground="#000000")
        # self.minimize.configure(highlightbackground="#d9d9d9")
        # self.minimize.configure(highlightcolor="black")
        # photo_location = os.path.join(prog_location,"../Python main/icon/Minimize-01.png")
        # global _img3
        # _img3 = tk.PhotoImage(file=photo_location)
        # self.minimize.configure(image=_img3)
        # self.minimize.configure(pady="0")
        # self.minimize.configure(text='''Button''')
        # self.minimize.configure(width=57)

        self.APT = tk.Label(top)
        self.APT.place(relx=0.078, rely=0.106, height=29, width=362)
        self.APT.configure(background="#323539")
        self.APT.configure(borderwidth="0")
        self.APT.configure(disabledforeground="#a3a3a3")
        self.APT.configure(font=font15)
        self.APT.configure(foreground="#ffffff")
        self.APT.configure(text='''AMAZON PRICE TRACKER''')
        self.APT.configure(width=362)

        # self.radioamzn = tk.Radiobutton(top)
        # self.radioamzn.place(relx=0.097, rely=0.166, relheight=0.053
        #         , relwidth=0.112)
        # self.radioamzn.configure(activebackground="#323539")
        # self.radioamzn.configure(activeforeground="white")
        # self.radioamzn.configure(activeforeground="#33CFDB")
        # self.radioamzn.configure(background="#323539")
        # self.radioamzn.configure(borderwidth="0")
        # self.radioamzn.configure(disabledforeground="#323539")
        # self.radioamzn.configure(font=font10)
        # self.radioamzn.configure(foreground="#ffffff")
        # self.radioamzn.configure(highlightbackground="#323539")
        # self.radioamzn.configure(highlightcolor="#323539")
        # self.radioamzn.configure(highlightthickness="0")
        # self.radioamzn.configure(justify='left')
        # self.radioamzn.configure(text='''AMAZON''')

        # self.radioflp = tk.Radiobutton(top)
        # self.radioflp.place(relx=0.252, rely=0.166, relheight=0.061
        #         , relwidth=0.14)
        # self.radioflp.configure(activebackground="#323539")
        # self.radioflp.configure(activeforeground="white")
        # self.radioflp.configure(activeforeground="#33CFDB")
        # self.radioflp.configure(background="#323539")
        # self.radioflp.configure(borderwidth="0")
        # self.radioflp.configure(disabledforeground="#323539")
        # self.radioflp.configure(font=font10)
        # self.radioflp.configure(foreground="#ffffff")
        # self.radioflp.configure(highlightbackground="#323539")
        # self.radioflp.configure(highlightcolor="#323539")
        # self.radioflp.configure(highlightthickness="0")
        # self.radioflp.configure(justify='left')
        # self.radioflp.configure(text='''FLIPKART''')
        # self.radioflp.configure(width=144)

        self.newadtxt = tk.Entry(top)
        self.newadtxt.place(relx=0.078, rely=0.303,height=44, relwidth=0.353)
        self.newadtxt.configure(background="white")
        self.newadtxt.configure(disabledforeground="#a3a3a3")
        self.newadtxt.configure(font=font17)
        self.newadtxt.configure(foreground="#000000")
        self.newadtxt.configure(insertbackground="black")
        self.newadtxt.configure(width=364)
        self.newadtxt.configure(textvariable=varEntry)
        self.newadtxt.bind('<Return>',lambda addnew:self.add_link())


        self.Label4_2 = tk.Label(top)
        self.Label4_2.place(relx=0.068, rely=0.257, height=29, width=182)
        self.Label4_2.configure(activebackground="#f9f9f9")
        self.Label4_2.configure(activeforeground="black")
        self.Label4_2.configure(background="#323539")
        self.Label4_2.configure(borderwidth="0")
        self.Label4_2.configure(disabledforeground="#a3a3a3")
        self .Label4_2.configure(font=font17)
        self.Label4_2.configure(foreground="#ffffff")
        self.Label4_2.configure(highlightbackground="#d9d9d9")
        self.Label4_2.configure(highlightcolor="black")
        self.Label4_2.configure(text='''ADD NEY LINK''')
        self.Label4_2.configure(width=182)

        self.Label4_3 = tk.Label(top)
        self.Label4_3.place(relx=0.078, rely=0.378, height=29, width=312)
        self.Label4_3.configure(activebackground="#f9f9f9")
        self.Label4_3.configure(activeforeground="black")
        self.Label4_3.configure(background="#323539")
        self.Label4_3.configure(borderwidth="0")
        self.Label4_3.configure(disabledforeground="#a3a3a3")
        self.Label4_3.configure(font=font19)
        self.Label4_3.configure(foreground="#ffffff")
        self.Label4_3.configure(highlightbackground="#d9d9d9")
        self.Label4_3.configure(highlightcolor="black")
        self.Label4_3.configure(text='')
        self.Label4_3.configure(width=312)
        self.Label4_3.configure(anchor='w')

        self.onlinestatus = tk.Label(top)
        self.onlinestatus.place(relx=0.005, rely=0.960, height=29, width=312)
        self.onlinestatus.configure(activebackground="#f9f9f9")
        self.onlinestatus.configure(activeforeground="black")
        self.onlinestatus.configure(background="#323539")
        self.onlinestatus.configure(borderwidth="0")
        self.onlinestatus.configure(disabledforeground="#a3a3a3")
        self.onlinestatus.configure(font=font19)
        self.onlinestatus.configure(foreground="#ffffff")
        self.onlinestatus.configure(highlightbackground="#d9d9d9")
        self.onlinestatus.configure(highlightcolor="black")
        self.onlinestatus.configure(text='')
        self.onlinestatus.configure(width=312)
        self.onlinestatus.configure(anchor='w')

        self.lstbx1 = tk.Listbox(top)
        self.lstbx1.place(relx=0.078, rely=0.424, relheight=0.3, relwidth=0.353)
        self.lstbx1.configure(background="white")
        self.lstbx1.configure(borderwidth="0")
        self.lstbx1.configure(disabledforeground="#a3a3a3")
        self.lstbx1.configure(font=font20)
        self.lstbx1.configure(foreground="#000000")
        self.lstbx1.configure(highlightthickness="0")
        self.lstbx1.configure(width=364)

        # self.refreshbtn = tk.Button(top)
        # self.refreshbtn.place(relx=0.155, rely=0.802, height=53, width=206)
        # self.refreshbtn.configure(activebackground="#33CFDB")
        # self.refreshbtn.configure(activeforeground="#000000")
        # self.refreshbtn.configure(background="#33CFDB")
        # self.refreshbtn.configure(borderwidth="0")
        # self.refreshbtn.configure(disabledforeground="#ffffff")
        # self.refreshbtn.configure(font=font20)
        # self.refreshbtn.configure(foreground="#000000")
        # self.refreshbtn.configure(highlightbackground="#33cfdb")
        # self.refreshbtn.configure(highlightcolor="black")
        # self.refreshbtn.configure(pady="0")
        # self.refreshbtn.configure(text='''REFRESH LIST''')
        # self.refreshbtn.configure(width=206)
        # self.refreshbtn.configure(command=self.refresh_data)

        self.Label4_4 = tk.Label(top)
        self.Label4_4.place(relx=0.581, rely=0.106, height=29, width=362)
        self.Label4_4.configure(activebackground="#f9f9f9")
        self.Label4_4.configure(activeforeground="black")
        self.Label4_4.configure(background="#323539")
        self.Label4_4.configure(borderwidth="0")
        self.Label4_4.configure(disabledforeground="#a3a3a3")
        self.Label4_4.configure(font=font15)
        self.Label4_4.configure(foreground="#ffffff")
        self.Label4_4.configure(highlightbackground="#d9d9d9")
        self.Label4_4.configure(highlightcolor="black")
        self.Label4_4.configure(text='''URL SHORTNER''')

        self.Label4_5 = tk.Label(top)
        self.Label4_5.place(relx=0.591, rely=0.197, height=29, width=182)
        self.Label4_5.configure(activebackground="#f9f9f9")
        self.Label4_5.configure(activeforeground="black")
        self.Label4_5.configure(background="#323539")
        self.Label4_5.configure(borderwidth="0")
        self.Label4_5.configure(disabledforeground="#a3a3a3")
        self.Label4_5.configure(font=font17)
        self.Label4_5.configure(foreground="#ffffff")
        self.Label4_5.configure(highlightbackground="#d9d9d9")
        self.Label4_5.configure(highlightcolor="black")
        self.Label4_5.configure(text='''ADD LINK''')


        
        self.newurltxt = tk.Entry(top)
        self.newurltxt.place(relx=0.601, rely=0.242,height=44, relwidth=0.353)
        self.newurltxt.configure(background="white")
        self.newurltxt.configure(disabledforeground="#a3a3a3")
        self.newurltxt.configure(font=font17)
        self.newurltxt.configure(foreground="#000000")
        self.newurltxt.configure(highlightbackground="#d9d9d9")
        self.newurltxt.configure(highlightcolor="black")
        self.newurltxt.configure(insertbackground="black")
        self.newurltxt.configure(selectbackground="#c4c4c4")
        self.newurltxt.configure(selectforeground="black")
        self.newurltxt.configure(textvariable=varEntry2)
        self.newurltxt.bind('<Return>',lambda f:self.add_shortlink())
        

        self.Label4_6 = tk.Label(top)
        self.Label4_6.place(relx=0.591, rely=0.348, height=29, width=182)
        self.Label4_6.configure(activebackground="#f9f9f9")
        self.Label4_6.configure(activeforeground="black")
        self.Label4_6.configure(background="#323539")
        self.Label4_6.configure(borderwidth="0")
        self.Label4_6.configure(disabledforeground="#a3a3a3")
        self.Label4_6.configure(font=font17)
        self.Label4_6.configure(foreground="#ffffff")
        self.Label4_6.configure(highlightbackground="#d9d9d9")
        self.Label4_6.configure(highlightcolor="black")
        self.Label4_6.configure(text='''SHORT LINK''')

        self.newsurltxt = tk.Entry(top)
        self.newsurltxt.place(relx=0.601, rely=0.408,height=44, relwidth=0.353)
        self.newsurltxt.configure(background="white")
        self.newsurltxt.configure(disabledforeground="#a3a3a3")
        self.newsurltxt.configure(font=font17)
        self.newsurltxt.configure(foreground="#000000")
        self.newsurltxt.configure(highlightbackground="#d9d9d9")
        self.newsurltxt.configure(highlightcolor="black")
        self.newsurltxt.configure(insertbackground="black")
        self.newsurltxt.configure(selectbackground="#c4c4c4")
        self.newsurltxt.configure(selectforeground="black")
        self.newsurltxt.configure(textvariable=varEntry3)
        

        self.addnew = tk.Button(top)
        self.addnew.place(relx=0.388, rely=0.303, height=44, width=46)
        self.addnew.configure(activebackground="#33CFDB")
        self.addnew.configure(activeforeground="#000000")
        self.addnew.configure(background="#33CFDB")
        self.addnew.configure(borderwidth="0")
        self.addnew.configure(disabledforeground="#a3a3a3")
        self.addnew.configure(foreground="#000000")
        self.addnew.configure(highlightbackground="#33CFDB")
        self.addnew.configure(highlightcolor="black")
        photo_location = os.path.join(prog_location,"../Python main/icon/Add-02.png")
        global _img4
        _img4 = tk.PhotoImage(file=photo_location)
        self.addnew.configure(image=_img4)
        self.addnew.configure(pady="0")
        self.addnew.configure(width=46)
        self.addnew.configure(command = self.add_link)

        self.addlink = tk.Button(top)
        self.addlink.place(relx=0.911, rely=0.242, height=44, width=46)
        self.addlink.configure(activebackground="#33CFDB")
        self.addlink.configure(activeforeground="#000000")
        self.addlink.configure(background="#33CFDB")
        self.addlink.configure(borderwidth="0")
        self.addlink.configure(disabledforeground="#a3a3a3")
        self.addlink.configure(foreground="#000000")
        self.addlink.configure(highlightbackground="#33CFDB")
        self.addlink.configure(highlightcolor="black")
        photo_location = os.path.join(prog_location,"../Python main/icon/Add-02.png")
        global _img5
        _img5 = tk.PhotoImage(file=photo_location)
        self.addlink.configure(image=_img5)
        self.addlink.configure(pady="0")
        self.addlink.configure(text='''Button''')
        self.addlink.configure(width=52)
        self.addlink.configure(command = self.add_shortlink)

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.959, rely=0.938, height=33, width=36)
        self.Button1.configure(activebackground="#33CFDB")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#33CFDB")
        self.Button1.configure(borderwidth="0")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#33CFDB")
        self.Button1.configure(highlightcolor="black")
        photo_location = os.path.join(prog_location,"../Python main/icon/Test-02.png")
        global _img6
        _img6 = tk.PhotoImage(file=photo_location)
        self.Button1.configure(image=_img6)
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Button''')
        self.Button1.configure(width=36)
        self.Button1.configure(command=test_notification)
    


        self.check_now = tk.Button(top)
        self.check_now.place(relx=0.917, rely=0.938, height=33, width=36)
        self.check_now.configure(activebackground="#33CFDB")
        self.check_now.configure(activeforeground="#000000")
        self.check_now.configure(background="#33CFDB")
        self.check_now.configure(borderwidth="0")
        self.check_now.configure(disabledforeground="#a3a3a3")
        self.check_now.configure(foreground="#000000")
        self.check_now.configure(highlightbackground="#33CFDB")
        self.check_now.configure(highlightcolor="black")
        photo_location = os.path.join(prog_location,"../Python main/icon/intrefresh-01.png")
        global _img9
        _img9 = tk.PhotoImage(file=photo_location)
        self.check_now.configure(image=_img9)
        self.check_now.configure(pady="0")
        self.check_now.configure(text='''Button''')
        self.check_now.configure(width=36)
        self.check_now.configure(command=self.check_internet_connection)




if __name__ == '__main__':
    #t = threading.Thread(target=vp_start_gui)
    #t.start()
    vp_start_gui()
    





