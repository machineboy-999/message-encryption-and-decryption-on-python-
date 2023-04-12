from tkinter import*
from tkinter import messagebox
import time
#-----------------Login Page------------------#
def login():
    uname = e1.get()
    password = e2.get()

    if (uname == "" and password == ""):
        messagebox.showinfo("", "blank not allowed")
    elif (uname == "deadpool" and password == "livingpool"):              # deadpool, livingpool
        messagebox.showinfo("", "login successful")
    else:
        messagebox.showinfo("", "invalid username or password")


window = Tk()
window.geometry("800x600")
window.title("Secret Service Agency")
window.configure(background = "black")


global uname
global password


Tops1 = Frame(window, width=600, relief=SUNKEN)
Tops1.pack(side = TOP)


f3 = Frame(window, width= 600, height= 500, relief= SUNKEN, background= "black")
f3.pack(side= TOP)


Label(window,font=('arial', 16, 'bold'),
      text= "UserName", fg='white',bg='red',bd='10',anchor='w' ).place(x= 200, y=100)
Label(window,font=('arial', 16, 'bold'),
      text= "Password", fg='white',bg='red',bd='12',anchor='w').place(x= 200, y=200)


e1 = Entry(window, font=('helvetica', 18),
                      text="UserName", bd=10, insertwidth=5, bg='grey')
e1.place(x= 330, y=100)

e2 = Entry(window, font=('helvetica', 18),
                      text="Password", bd=10, insertwidth=5, bg='grey')
e2.place(x= 330, y= 200)


btn3 = Button(f3, text="LOGIN", height=4, width=16, bg="red", fg="white", command= login)
btn3.place(x=250, y=300)

#--------------------For Encoding---------------------#

def encrypt():
    window = Tk()
    window.geometry("1200x6000")
    window.configure(bg='black')
    window.title("Superior Secret Agency")
    Tops = Frame(window, width=1600, bg='black')
    Tops.pack(side=TOP)


    f1 = Frame(window, width=800, height=700, bg='black')
    f1.pack(side=LEFT)

    localtime = time.asctime(time.localtime(time.time()))
    lblinfo = (Label(Tops,font=('georgia', 50, 'bold'),
                    text="Welcome to SSA ",
                    fg="white",bg = 'black'))
    lblinfo.grid(row=0, column=0)
    lblInfo = Label(Tops,font=('arial', 20, 'bold'),
                    text=localtime, fg="light grey",bg = "black")
    lblInfo.grid(row=1, column=0)

    Msg = StringVar()
    key = StringVar()
    result = StringVar()

    def qExit():
        window.destroy()
    def reset():
        Msg.set("")
        key.set("")
        result.set("")



    confirm = (Label(f1,font=('arial', 16, 'bold'),
                     text="Enter the message:",
                     fg='orange',bg='black',bd='10',anchor='w')).grid(row=0, column=0)

    confirm_entry= Entry(f1,font=('helvetica', 18),
                          text=Msg, bd=10, insertwidth= 5, bg='grey').grid(row=0, column=1)

    key_command = (Label(f1,font=('arial', 18),
                         text= 'Enter the key:', fg='orange', bg='black', bd='10', anchor='w')).grid(row=3, column=0)

    key_entry= Entry(f1,font=('helvetica', 18),
                     text= key, bd=10, insertwidth= 5, bg='grey').grid(row=3, column=1)

    result_command = (Label(f1,font=('arial',18, 'bold'),
                    text="Encoded message:", fg='sky blue', bg='black',
                            bd='10', anchor='w',justify='right')).grid(row=2, column=2)


    result_entry= Entry(f1,font=('helvetica',20),
                        text=result, bd=10, justify='right', bg='grey').grid(row=2, column=3)
    import base64


    #-----------------Function to encode-----------------#

    def encode(key, clear):
        enc = []

        for i in range(len(clear)):
            key_c = key[i % len(key)]
            enc_c = chr((ord(clear[i]) +
                         ord(key_c)) % 256)

            enc.append(enc_c)

        return base64.urlsafe_b64encode("".join(enc).encode()).decode()

    def ref():

        clear = Msg.get()
        k = key.get()
        result.set(encode(k,clear))


    btnTotal = Button(f1, padx=16, pady=8, bd=16, fg="black",
                      font=('arial', 16, 'bold'), width=10,
                      text="Show Message", bg="yellow",
                      command=ref).grid(row=7, column=0)

    btnreset = Button(f1, padx=16, pady=8, bd=16, fg="black",
                      font=('arial', 16, 'bold'), width=10,
                      text="Reset", bg="Green",
                      command=reset).grid(row=7, column=1)
    btnexit = Button(f1, padx=16, pady=8, bd=16, fg="black",
                      font=('arial', 16, 'bold'), width=10,
                      text="Exit", bg="Red",
                      command=qExit).grid(row=7, column=2)


#-----------------For Decoding-----------------#

def decrypt():
    window = Tk()
    window.geometry("1200x6000")
    window.configure(bg='black')
    window.title("Superior Secret Agency")
    Tops1 = Frame(window, width=1600, relief=SUNKEN, bg='black')
    Tops1.pack(side=TOP)

    f2 = Frame(window, width=800, height=700, relief=SUNKEN, bg='black')
    f2.pack(side=LEFT)
    localtime1 = time.asctime(time.localtime(time.time()))
    lblinfo1 = (Label(Tops1, font=('georgia', 50, 'bold'),
                     text="Welcome to SSA ",
                     fg="white", bg='black'))
    lblinfo1.grid(row=0, column=0)
    lblInfo1 = Label(Tops1, font=('arial', 20, 'bold'),
                    text=localtime1, fg="light grey", bg="black")
    lblInfo1.grid(row=1, column=0)

    Msg1 = StringVar()
    key1 = StringVar()
    result1 = StringVar()

    def qExit():
        window.destroy()

    def reset():
        Msg1.set("")
        key1.set("")
        result1.set("")

    confirm1 = (Label(f2, font=('arial', 16, 'bold'),
                     text="Enter the Secret message:",
                     fg='orange', bg='black', bd='10', anchor='w')).grid(row=0, column=0)

    confirm_entry1 = Entry(f2, font=('helvetica', 18),
                          text=Msg1, bd=10, insertwidth=5, bg='grey').grid(row=0, column=1)

    key_command1 = (Label(f2, font=('arial', 18),
                         text='Enter the key:', fg='orange', bg='black', bd='10', anchor='w')).grid(row=3, column=0)

    key_entry1 = Entry(f2, font=('helvetica', 18),
                      text=key1, bd=10, insertwidth=5, bg='grey').grid(row=3, column=1)

    result_command1 = (Label(f2, font=('arial', 18, 'bold'),
                            text="Decoded message:", fg='sky blue', bg='black', bd='10', anchor='w',
                            justify='right')).grid(row=2, column=2)

    result_entry1 = Entry(f2, font=('helvetica', 20),
                         text=result1, bd=10, justify='right', bg='grey').grid(row=2, column=3)

    import base64

# -----------------Function to decode-----------------#
    def decode(key, enc):
        dec = []

        enc = base64.urlsafe_b64decode(enc).decode()
        for i in range(len(enc)):
            key_c = key[i % len(key)]
            dec_c = chr((256 + ord(enc[i]) -
                         ord(key_c)) % 256)

            dec.append(dec_c)
        return "".join(dec)

    def ref1():

        clear = Msg1.get()
        k = key1.get()
        result1.set(decode(k, clear))

    btnTotal1 = Button(f2, padx=16, pady=8, bd=16, fg="black",
                      font=('arial', 16, 'bold'), width=10,
                      text="Show Message", bg="yellow",
                      command=ref1).grid(row=7, column=0)

    btnreset1 = Button(f2, padx=16, pady=8, bd=16, fg="black",
                      font=('arial', 16, 'bold'), width=10,
                      text="Reset", bg="Green",
                      command=reset).grid(row=7, column=1)
    btnexit1 = Button(f2, padx=16, pady=8, bd=16, fg="black",
                     font=('arial', 16, 'bold'), width=10,
                     text="Exit", bg="Red",
                     command=qExit).grid(row=7, column=2)

#-----------------Button-----------------#


window = Tk()
window.geometry("1200x1600")
window.title("Secret Service Agency")
window.configure(background = "black")

Tops = Frame(window, width = 1600, relief = SUNKEN)
Tops.pack(side = TOP)

f1 = Frame(window, width = 800, height = 700, relief = SUNKEN, background= "black")
f1.pack(side= TOP)

localtime = time.asctime(time.localtime(time.time()))
lblinfo = (Label(Tops,font=('georgia', 50, 'bold'),
                text="Welcome to SSA ",
                fg="white",bg = 'black'))
lblinfo.grid(row=0, column=0)
lblInfo = Label(Tops,font=('arial', 20, 'bold'),
                text=localtime, fg="white",bg = "black")
lblInfo.grid(row=1, column=0)


btn1 = Button(f1,text= "ENCODE",height= 4,width= 16 ,bg= "green",fg= "white", command=encrypt)
btn1.place(x=350, y=200)
btn2 = Button(f1,text= "DECODE",height= 4,width= 16 , bg= "red", fg= "white", command=decrypt)
btn2.place(x=350, y=300)

window.mainloop()

