import socket
from tkinter import *
HEADER = 64
PORT = 5080
FORMAT = 'UTF-8'
DISCONNECT_MESSAGE = "!disconnect"
SERVER = "192.168.29.113"
#SERVER = "26.218.246.40"
ADDR = (SERVER,PORT)
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)
count = 0

def submit():
    global GUESS
    GUESS = str(In.get())
    cond = True
    for i in GUESS:
        if not (i.isalpha()):
            cond = False
            break
    if((len(GUESS) != 5) or cond == False):
        Error.place(x=820, y=520)
    else:
        Error.place_forget()
        GUESS = GUESS.upper()
        send(GUESS)

def send(msg):
    global count
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length =  str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    rec = client.recv(2048).decode(FORMAT)
    count += 1
    if count == 1:
        L11.configure(text = GUESS[0])
        L12.configure(text=GUESS[1])
        L13.configure(text=GUESS[2])
        L14.configure(text=GUESS[3])
        L15.configure(text=GUESS[4])
        if rec[0] == "V":
            L11.configure(bg = "green")
        elif rec[0] == "O":
            L11.configure(bg = "orange")
        elif rec[0] == "X":
            L11.configure(bg = "red")
        if rec[1] == "V":
            L12.configure(bg = "green")
        elif rec[1] == "O":
            L12.configure(bg = "orange")
        elif rec[1] == "X":
            L12.configure(bg = "red")
        if rec[2] == "V":
            L13.configure(bg = "green")
        elif rec[2] == "O":
            L13.configure(bg = "orange")
        elif rec[2] == "X":
            L13.configure(bg = "red")
        if rec[3] == "V":
            L14.configure(bg = "green")
        elif rec[3] == "O":
            L14.configure(bg = "orange")
        elif rec[3] == "X":
            L14.configure(bg = "red")
        if rec[4] == "V":
            L15.configure(bg = "green")
        elif rec[4] == "O":
            L15.configure(bg = "orange")
        elif rec[4] == "X":
            L15.configure(bg = "red")
        if rec == "VVVVV":
            win.place(x = 730,y=570)
            return




    elif count == 2:
        L21.configure(text=GUESS[0])
        L22.configure(text=GUESS[1])
        L23.configure(text=GUESS[2])
        L24.configure(text=GUESS[3])
        L25.configure(text=GUESS[4])
        if rec[0] == "V":
            L21.configure(bg = "green")
        elif rec[0] == "O":
            L21.configure(bg = "orange")
        elif rec[0] == "X":
            L21.configure(bg = "red")
        if rec[1] == "V":
            L22.configure(bg = "green")
        elif rec[1] == "O":
            L22.configure(bg = "orange")
        elif rec[1] == "X":
            L22.configure(bg = "red")
        if rec[2] == "V":
            L23.configure(bg = "green")
        elif rec[2] == "O":
            L23.configure(bg = "orange")
        elif rec[2] == "X":
            L23.configure(bg = "red")
        if rec[3] == "V":
            L24.configure(bg = "green")
        elif rec[3] == "O":
            L24.configure(bg = "orange")
        elif rec[3] == "X":
            L24.configure(bg = "red")
        if rec[4] == "V":
            L25.configure(bg = "green")
        elif rec[4] == "O":
            L25.configure(bg = "orange")
        elif rec[4] == "X":
            L25.configure(bg = "red")
        if rec == "VVVVV":
            win.place(x=730, y=570)
            return
    elif count == 3:
        L31.configure(text=GUESS[0])
        L32.configure(text=GUESS[1])
        L33.configure(text=GUESS[2])
        L34.configure(text=GUESS[3])
        L35.configure(text=GUESS[4])
        if rec[0] == "V":
            L31.configure(bg = "green")
        elif rec[0] == "O":
            L31.configure(bg = "orange")
        elif rec[0] == "X":
            L31.configure(bg = "red")
        if rec[1] == "V":
            L32.configure(bg = "green")
        elif rec[1] == "O":
            L32.configure(bg = "orange")
        elif rec[1] == "X":
            L32.configure(bg = "red")
        if rec[2] == "V":
            L33.configure(bg = "green")
        elif rec[2] == "O":
            L33.configure(bg = "orange")
        elif rec[2] == "X":
            L33.configure(bg = "red")
        if rec[3] == "V":
            L34.configure(bg = "green")
        elif rec[3] == "O":
            L34.configure(bg = "orange")
        elif rec[3] == "X":
            L34.configure(bg = "red")
        if rec[4] == "V":
            L35.configure(bg = "green")
        elif rec[4] == "O":
            L35.configure(bg = "orange")
        elif rec[4] == "X":
            L35.configure(bg = "red")
        if rec == "VVVVV":
            win.place(x = 730,y=570)
            return
    elif count == 4:
        L41.configure(text=GUESS[0])
        L42.configure(text=GUESS[1])
        L43.configure(text=GUESS[2])
        L44.configure(text=GUESS[3])
        L45.configure(text=GUESS[4])
        if rec[0] == "V":
            L41.configure(bg = "green")
        elif rec[0] == "O":
            L41.configure(bg = "orange")
        elif rec[0] == "X":
            L41.configure(bg = "red")
        if rec[1] == "V":
            L42.configure(bg = "green")
        elif rec[1] == "O":
            L42.configure(bg = "orange")
        elif rec[1] == "X":
            L42.configure(bg = "red")
        if rec[2] == "V":
            L43.configure(bg = "green")
        elif rec[2] == "O":
            L43.configure(bg = "orange")
        elif rec[2] == "X":
            L43.configure(bg = "red")
        if rec[3] == "V":
            L44.configure(bg = "green")
        elif rec[3] == "O":
            L44.configure(bg = "orange")
        elif rec[3] == "X":
            L44.configure(bg = "red")
        if rec[4] == "V":
            L45.configure(bg = "green")
        elif rec[4] == "O":
            L45.configure(bg = "orange")
        elif rec[4] == "X":
            L45.configure(bg = "red")
        if rec == "VVVVV":
            win.place(x = 730,y=570)
            return
    elif count == 5:
        L51.configure(text=GUESS[0])
        L52.configure(text=GUESS[1])
        L53.configure(text=GUESS[2])
        L54.configure(text=GUESS[3])
        L55.configure(text=GUESS[4])
        if rec[0] == "V":
            L51.configure(bg = "green")
        elif rec[0] == "O":
            L51.configure(bg = "orange")
        elif rec[0] == "X":
            L51.configure(bg = "red")
        if rec[1] == "V":
            L52.configure(bg = "green")
        elif rec[1] == "O":
            L52.configure(bg = "orange")
        elif rec[1] == "X":
            L52.configure(bg = "red")
        if rec[2] == "V":
            L53.configure(bg = "green")
        elif rec[2] == "O":
            L53.configure(bg = "orange")
        elif rec[2] == "X":
            L53.configure(bg = "red")
        if rec[3] == "V":
            L54.configure(bg = "green")
        elif rec[3] == "O":
            L54.configure(bg = "orange")
        elif rec[3] == "X":
            L54.configure(bg = "red")
        if rec[4] == "V":
            L55.configure(bg = "green")
        elif rec[4] == "O":
            L55.configure(bg = "orange")
        elif rec[4] == "X":
            L55.configure(bg = "red")
        if rec == "VVVVV":
            win.place(x = 730,y=570)
            return

    elif count == 6:
        L61.configure(text=GUESS[0])
        L62.configure(text=GUESS[1])
        L63.configure(text=GUESS[2])
        L64.configure(text=GUESS[3])
        L65.configure(text=GUESS[4])
        if rec[0] == "V":
            L61.configure(bg = "green")
        elif rec[0] == "O":
            L61.configure(bg = "orange")
        elif rec[0] == "X":
            L61.configure(bg = "red")
        if rec[1] == "V":
            L62.configure(bg = "green")
        elif rec[1] == "O":
            L62.configure(bg = "orange")
        elif rec[1] == "X":
            L62.configure(bg = "red")
        if rec[2] == "V":
            L63.configure(bg = "green")
        elif rec[2] == "O":
            L63.configure(bg = "orange")
        elif rec[2] == "X":
            L63.configure(bg = "red")
        if rec[3] == "V":
            L64.configure(bg = "green")
        elif rec[3] == "O":
            L64.configure(bg = "orange")
        elif rec[3] == "X":
            L64.configure(bg = "red")
        if rec[4] == "V":
            L65.configure(bg = "green")
        elif rec[4] == "O":
            L65.configure(bg = "orange")
        elif rec[4] == "X":
            L65.configure(bg = "red")
        if rec == "VVVVV":
            win.place(x = 730,y=570)
        else:
            lose.place(x = 730,y=570)


box_h = 3
box_w = 7
box_x = 250
box_y = 150
pad = 90
pady = 40
m = Tk(className="Wordle")
m.geometry("1280x720")
m.configure(bg="black")
label = Label(m, text="ONLINE WORDLE", bg="black", fg="green", font=("Courier New", 32))
label.place(x=450,y=40)
L11 = Label(m,text = " ",fg = "white",height = box_h,width = box_w)
L11.place(x=box_x,y = box_y)
L12 = Label(m,text = " ",fg = "white",height = box_h,width = box_w)
L12.place(x=box_x + pad,y = box_y)
L13 = Label(m,text = " ",fg = "white",height = box_h,width = box_w)
L13.place(x=box_x + (2*pad),y = box_y)
L14 = Label(m,text = " ",fg = "white",height = box_h,width = box_w)
L14.place(x=box_x + (3*pad),y = box_y)
L15 = Label(m,text = " ",fg = "white",height = box_h,width = box_w)
L15.place(x=box_x + (4*pad),y = box_y)


L21 = Label(m,text = " ",fg = "white",height = box_h,width = box_w)
L21.place(x=box_x,y = box_y + (2*pady))
L22 = Label(m,text = " ",fg = "white",height = box_h,width = box_w)
L22.place(x=box_x + pad,y = box_y + (2*pady))
L23 = Label(m,text = " ",fg = "white",height = box_h,width = box_w)
L23.place(x=box_x + (2*pad),y = box_y + (2*pady))
L24 = Label(m,text = " ",fg = "white",height = box_h,width = box_w)
L24.place(x=box_x + (3*pad),y = box_y + (2*pady))
L25 = Label(m,text = " ",fg = "white",height = box_h,width = box_w)
L25.place(x=box_x + (4*pad),y = box_y + (2*pady))

L31 = Label(m,text = " ",fg = "white",height = box_h,width = box_w)
L31.place(x=box_x,y = box_y + (4*pady))
L32 = Label(m,text = " ",fg = "white",height = box_h,width = box_w)
L32.place(x=box_x + pad,y = box_y + (4*pady))
L33 = Label(m,text = " ",fg = "white",height = box_h,width = box_w)
L33.place(x=box_x + (2*pad),y = box_y + (4*pady))
L34 = Label(m,text = " ",fg = "white",height = box_h,width = box_w)
L34.place(x=box_x + (3*pad),y = box_y + (4*pady))
L35 = Label(m,text = " ",fg = "white",height = box_h,width = box_w)
L35.place(x=box_x + (4*pad),y = box_y + (4*pady))

L41 = Label(m,text = " ",fg = "white",height = box_h,width = box_w)
L41.place(x=box_x,y = box_y + (6*pady))
L42 = Label(m,text = " ",fg = "white",height = box_h,width = box_w)
L42.place(x=box_x + pad,y = box_y + (6*pady))
L43 = Label(m,text = " ",fg = "white",height = box_h,width = box_w)
L43.place(x=box_x + (2*pad),y = box_y + (6*pady))
L44 = Label(m,text = " ",fg = "white",height = box_h,width = box_w)
L44.place(x=box_x + (3*pad),y = box_y + (6*pady))
L45 = Label(m,text = " ",fg = "white",height = box_h,width = box_w)
L45.place(x=box_x + (4*pad),y = box_y + (6*pady))


L51 = Label(m,text = " ",fg = "white",height = box_h,width = box_w)
L51.place(x=box_x,y = box_y + (8*pady))
L52 = Label(m,text = " ",fg = "white",height = box_h,width = box_w)
L52.place(x=box_x + pad,y = box_y + (8*pady))
L53 = Label(m,text = " ",fg = "white",height = box_h,width = box_w)
L53.place(x=box_x + (2*pad),y = box_y + (8*pady))
L54 = Label(m,text = " ",fg = "white",height = box_h,width = box_w)
L54.place(x=box_x + (3*pad),y = box_y + (8*pady))
L55 = Label(m,text = " ",fg = "white",height = box_h,width = box_w)
L55.place(x=box_x + (4*pad),y = box_y + (8*pady))

L61 = Label(m,text = " ",fg = "white",height = box_h,width = box_w)
L61.place(x=box_x,y = box_y + (10*pady))
L62 = Label(m,text = " ",fg = "white",height = box_h,width = box_w)
L62.place(x=box_x + pad,y = box_y + (10*pady))
L63 = Label(m,text = " ",fg = "white",height = box_h,width = box_w)
L63.place(x=box_x + (2*pad),y = box_y + (10*pady))
L64 = Label(m,text = " ",fg = "white",height = box_h,width = box_w)
L64.place(x=box_x + (3*pad),y = box_y + (10*pady))
L65 = Label(m,text = " ",fg = "white",height = box_h,width = box_w)
L65.place(x=box_x + (4*pad),y = box_y + (10*pady))

Make = Label(m,text = "Make a guess",bg = "black", fg = "red",font = ("Courier New", 32))
Make.place(x = 820,y = 200)

In = Entry(m,width=30)
In.place(x = 850,y = 320)

lose = Label(m,text = "You had six guesses and you still couldn't get it?",bg = "black", fg = "red",font = ("Courier New", 12))
win = Label(m,text = "Congrats Amogh will buy you a cupcake now",bg = "black", fg = "green",font = ("Courier New", 12))


Error = Label(m,text = "Input must be a 5 letter word",bg = "black", fg = "red",font = ("Courier New", 18))
Error.place(x=820, y=520)

submit = Button(m,text = "Submit",bg="white",fg = "black",height = 2,width = 10,command = submit)
submit.place(x = 850,y = 420)


m.attributes('-fullscreen',True)
m.mainloop()







