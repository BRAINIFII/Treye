from tkinter import *
import random
import base64

root = Tk()
#root.attributes('-fullscreen', True)
#root.geometry("1920x1018")
#root.title("Message Encryption")
Tops = Frame(root, width=1600, relief=FLAT)
Tops.pack(side=TOP)

f1 = Frame(root, width=800, height=700, relief=FLAT)
f1.pack(side=LEFT)
lblInfo = Label(Tops, font=('Cambria Math', 50, 'bold'),
               text="MESSAGE ENCRYPTION",
               fg="Black", bd=10, anchor='w')

lblInfo.grid(row=0, column=0)

rand = StringVar()
Msg = StringVar()
key = StringVar()
mode = StringVar()
Result = StringVar()

#exit
def qExit():
   root.destroy()

#reset
def Reset():
   rand.set("")
   Msg.set("")
   key.set("")
   mode.set("")
   Result.set("")


lblReference = Label(f1, font=('arial', 16, 'bold'),
                    text="Name:", bd=1, anchor="w")

lblReference.grid(row=0, column=0)

txtReference = Entry(f1, font=('arial', 16, 'bold'),
                    textvariable=rand, bd=1,
                    insertwidth=4, justify='left')
txtReference.grid(row=0, column=1)

# labels
lblMsg = Label(f1, font=('arial', 16, 'bold'),
              text="MESSAGE", bd=1, anchor="w")

lblMsg.grid(row=1, column=0)

txtMsg = Entry(f1, font=('arial', 16, 'bold'),
              textvariable=Msg, bd=1, insertwidth=4,
              justify='left')

txtMsg.grid(row=1, column=1)

lblkey = Label(f1, font=('arial', 16, 'bold'),
              text="KEY", bd=1, anchor="w")

lblkey.grid(row=2, column=0)

txtkey = Entry(f1, font=('arial', 16, 'bold'),
              textvariable=key, bd=1, insertwidth=4
              , justify='left')

txtkey.grid(row=2, column=1)

lblmode = Label(f1, font=('arial', 16, 'bold'),
               text="MODE(e for encrypt, d for decrypt)",
               bd=1, anchor="w")

lblmode.grid(row=3, column=0)

txtmode = Entry(f1, font=('arial', 16, 'bold'),
               textvariable=mode, bd=1,
               insertwidth=4, justify='left')

txtmode.grid(row=3, column=1)

lblService = Label(f1, font=('arial', 16, 'bold'),
                  text="The Result-", bd=1, anchor="w")

lblService.grid(row=2, column=2)

txtService = Entry(f1, font=('arial', 16, 'bold'),
                  textvariable=Result, bd=1,
                  insertwidth=4, justify='left')

txtService.grid(row=2, column=3)

import base64


# Function to encode
def encode(key, clear):
   enc = []

   for i in range(len(clear)):
       key_c = key[i % len(key)]
       enc_c = chr((ord(clear[i]) +
                    ord(key_c)) % 256)

       enc.append(enc_c)

   return base64.urlsafe_b64encode("".join(enc).encode()).decode()


# Function to decode
def decode(key, enc):
   dec = []

   enc = base64.urlsafe_b64decode(enc).decode()
   for i in range(len(enc)):
       key_c = key[i % len(key)]
       dec_c = chr((256 + ord(enc[i]) -
                    ord(key_c)) % 256)

       dec.append(dec_c)
   return "".join(dec)


def Ref():
   print("Message= ", (Msg.get()))

   clear = Msg.get()
   k = key.get()
   m = mode.get()

   if (m == 'e'):
       Result.set(encode(k, clear))
   elif (m == 'd'):
       Result.set(decode(k, clear))
   else:
       Result.set("Error please select 'e' for encrypting and 'd' for decrypting")


# Show message button
btnTotal = Button(f1, padx=16, pady=8, bd=1, fg="black",
                 font=('arial', 16, 'bold'), width=10,
                 text="Encryption Key",
                 command=Ref).grid(row=9, column=1)

# Reset button
btnReset = Button(f1, padx=16, pady=8, bd=1,
                 fg="black", font=('arial', 16, 'bold'),
                 width=10, text="Reset",
                 command=Reset).grid(row=9, column=2)

# Exit button
btnExit = Button(f1, padx=16, pady=8, bd=1,
                fg="black", font=('arial', 16, 'bold'),
                width=10, text="Exit",
                command=qExit).grid(row=9, column=3)

# keeps window alive
root.mainloop()

