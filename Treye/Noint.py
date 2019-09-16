import sys
import GUI

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

import Noint_support
import os.path

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    global prog_location
    prog_call = sys.argv[0]
    prog_location = os.path.split(prog_call)[0]
    root = tk.Tk()
    top = Toplevel1 (root)
    root.resizable(0, 0)
    #root.overrideredirect(True)                 #hide root border and titlebar
    Noint_support.init(root, top)
    root.mainloop()

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
    Noint_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

def close_window (): 
    root.destroy()

def min_window ():
    root.overrideredirect(False)
    #root.withdraw()
    root.iconify()
    #root.overrideredirect(True)
    #root.after(5000, root.overrideredirect, True)
class Toplevel1:
    def tryagain(self):
        #GUI.Toplevel1.check_internet_connection(self)
        os.system('python GUI.py')
        root.destroy()


    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font10 = "-family Calibri -size 17 -weight bold -slant roman "  \
            "-underline 0 -overstrike 0"
        font9 = "-family Calibri -size 14 -weight bold -slant roman "  \
            "-underline 0 -overstrike 0"

        top.geometry("609x383+659+304")
        top.title("New Toplevel")
        top.configure(background="#323539")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.0, rely=0.0, height=36, width=612)
        self.Label1.configure(background="#2A2D30")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(width=612)

        # self.Button1 = tk.Button(top)
        # self.Button1.place(relx=0.895, rely=0.0, height=29, width=56)
        # self.Button1.configure(activebackground="#ececec")
        # self.Button1.configure(activeforeground="#000000")
        # self.Button1.configure(background="#d9d9d9")
        # self.Button1.configure(borderwidth="0")
        # self.Button1.configure(disabledforeground="#a3a3a3")
        # self.Button1.configure(foreground="#000000")
        # self.Button1.configure(highlightbackground="#d9d9d9")
        # self.Button1.configure(highlightcolor="black")
        # photo_location = os.path.join(prog_location,"../Python Project/icon/Close-02-02.png")
        # global _img0
        # _img0 = tk.PhotoImage(file=photo_location)
        # self.Button1.configure(image=_img0)
        # self.Button1.configure(pady="0")
        # self.Button1.configure(text='''Button''')
        # self.Button1.configure(command = close_window)

        # self.Button2 = tk.Button(top)
        # self.Button2.place(relx=0.796, rely=0.0, height=29, width=56)
        # self.Button2.configure(activebackground="#ececec")
        # self.Button2.configure(activeforeground="#000000")
        # self.Button2.configure(background="#d9d9d9")
        # self.Button2.configure(borderwidth="0")
        # self.Button2.configure(disabledforeground="#a3a3a3")
        # self.Button2.configure(foreground="#000000")
        # self.Button2.configure(highlightbackground="#d9d9d9")
        # self.Button2.configure(highlightcolor="black")
        # photo_location = os.path.join(prog_location,"../Python Project/icon/Minimize-02.png")
        # global _img1
        # _img1 = tk.PhotoImage(file=photo_location)
        # self.Button2.configure(image=_img1)
        # self.Button2.configure(pady="0")
        # self.Button2.configure(text='''Button''')
        # self.Button2.configure(command = min_window)

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.246, rely=0.117, height=36, width=292)
        self.Label2.configure(background="#323539")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font10)
        self.Label2.configure(foreground="#ffffff")
        self.Label2.configure(text='''No product found''')
        self.Label2.configure(width=292)

        self.Label2_1 = tk.Label(top)
        self.Label2_1.place(relx=0.115, rely=0.196, height=36, width=462)
        self.Label2_1.configure(activebackground="#f9f9f9")
        self.Label2_1.configure(activeforeground="black")
        self.Label2_1.configure(background="#323539")
        self.Label2_1.configure(disabledforeground="#a3a3a3")
        self.Label2_1.configure(font=font10)
        self.Label2_1.configure(foreground="#ffffff")
        self.Label2_1.configure(highlightbackground="#d9d9d9")
        self.Label2_1.configure(highlightcolor="black")
        self.Label2_1.configure(text='''I think you forgot something''')
        self.Label2_1.configure(width=462)

        self.Label3 = tk.Label(top)
        self.Label3.place(relx=0.378, rely=0.313, height=101, width=133)
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        photo_location = os.path.join(prog_location,"../Python Project/icon/Nointernetc.png")
        global _img2
        _img2 = tk.PhotoImage(file=photo_location)
        self.Label3.configure(image=_img2)
        self.Label3.configure(text='''Label''')
        self.Label3.configure(width=133)

        self.Label2_2 = tk.Label(top)
        self.Label2_2.place(relx=0.115, rely=0.574, height=36, width=462)
        self.Label2_2.configure(activebackground="#f9f9f9")
        self.Label2_2.configure(activeforeground="black")
        self.Label2_2.configure(background="#323539")
        self.Label2_2.configure(disabledforeground="#a3a3a3")
        self.Label2_2.configure(font=font10)
        self.Label2_2.configure(foreground="#ffffff")
        self.Label2_2.configure(highlightbackground="#d9d9d9")
        self.Label2_2.configure(highlightcolor="black")
        self.Label2_2.configure(text='''Your Internet Connection''')

        self.Button3_3 = tk.Button(top)
        self.Button3_3.place(relx=0.591, rely=0.783, height=53, width=186)
        self.Button3_3.configure(activebackground="#33cfdb")
        self.Button3_3.configure(activeforeground="#000000")
        self.Button3_3.configure(background="#33CFDB")
        self.Button3_3.configure(borderwidth="0")
        self.Button3_3.configure(disabledforeground="#a3a3a3")
        self.Button3_3.configure(font=font9)
        self.Button3_3.configure(foreground="#000000")
        self.Button3_3.configure(highlightbackground="#d9d9d9")
        self.Button3_3.configure(highlightcolor="black")
        self.Button3_3.configure(pady="0")
        self.Button3_3.configure(text='''TRY AGAIN''')
        self.Button3_3.configure(width=186)
        self.Button3_3.configure(command = self.tryagain)

        self.Button3_4 = tk.Button(top)
        self.Button3_4.place(relx=0.099, rely=0.783, height=53, width=186)
        self.Button3_4.configure(activebackground="#ececec")
        self.Button3_4.configure(activeforeground="#000000")
        self.Button3_4.configure(background="#ffffff")
        self.Button3_4.configure(borderwidth="0")
        self.Button3_4.configure(disabledforeground="#a3a3a3")
        self.Button3_4.configure(font=font9)
        self.Button3_4.configure(foreground="#000000")
        self.Button3_4.configure(highlightbackground="#d9d9d9")
        self.Button3_4.configure(highlightcolor="black")
        self.Button3_4.configure(pady="0")
        self.Button3_4.configure(text='''GO BACK''')

if __name__ == '__main__':
    vp_start_gui()





