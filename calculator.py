from tkinter import*
import random
lblx=0
lbly=0
nul=0
zeronul=0
def btnznak(z):
    global nul, zeronul, znak, lblx, lbly
    Label_division["text"] += z
    nul = 0
    zeronul = 1
    znak = z
def btpl():
    btnznak("+")

def btmin():
    btnznak("-")

def btmn():
    btnznak("*")

def qc():
    global znak, nul, lblx, lbly, zeronul
    znak = "n"
    Label_division["text"] = "0"
    lblx = 0
    lbly = 0
    nul = 0
    zeronul = 0

def btdel():
    btnznak("÷")
def q(number):
    global nul
    global zeronul
    global lblx
    global lbly
    if nul == 0:
        nul = 1
        Label_division["text"] = str(number)
    else:
        Label_division["text"] += str(number)
    if zeronul == 0:
        lblx = int(Label_division["text"])
    else:
        lbly = int(Label_division["text"])

def w():
    global lblx,lbly,znak,nul,zeronul
    try:
        if znak=="+":
            Label_division["text"]=f"{lblx+lbly}"
        elif znak == "-":
            Label_division["text"] = f"{lblx - lbly}"
        elif znak == "*":
            Label_division["text"] = f"{lblx * lbly}"
        elif znak == "/":
            if lbly == 0:
                Label_division["text"] =("nelza")
            else:
                Label_division["text"] = f"{lblx / lbly}"
        lblx = 0
        lbly = 0
        nul = 0
        zeronul = 0
    except Exception as e:
        print(e)

def q1():
    q(1)

def q2():
    q(2)

def q3():
    q(3)

def q4():
    q(4)
def q5():
    q(5)
def q6():
    q(6)
def q7():
    q(7)
def q8():
    q(8)
def q9():
    q(9)
def q0():
    q(0)
app=Tk()
app.title("calculator")
app.geometry("500x650+500+40")
app["bg"]="#ffffff"

app.resizable(False, False)
color = f"#{random.randint(0, 255):02x}{random.randint(0, 255):02x}"
button=Button(text="1",)
button.grid(row=1, column=1, padx=10, pady=10)
button_2=Button(text="2",command=q2, bg="#52bfc5", font=("arial", 24))
button.grid(row=1, column=2, padx=10, pady=10)
button_3=Button(text="3",command=q3, bg="#52bfc5", font=("arial", 24))
button.grid(row=1, column=3, padx=10, pady=10)
button_4=Button(text="0",command=q0, bg="#52bfc5", font=("arial", 24))
button.grid(row=1, column=4, padx=10, pady=10)
button_5=Button(text="4",command=q4, bg="#52bfc5", font=("arial", 24))
button.grid(row=2, column=1, padx=10, pady=10)
button_6=Button(text="5",command=q5, bg="#52bfc5", font=("arial", 24))
button.grid(row=2, column=2, padx=10, pady=10)
button_7=Button(text="6",command=q6, bg="#52bfc5", font=("arial", 24))
button.grid(row=2, column=3, padx=10, pady=10)
button_8=Button(text="-",command= btmin, bg="#52bfc5", font=("arial", 24))
button.grid(row=2, column=4, padx=10, pady=10)
button_9=Button(text="7",command=q7, bg="#52bfc5", font=("arial", 24))
button.grid(row=3, column=1, padx=10, pady=10)
button_0=Button(text="8",command=q8, bg="#52bfc5", font=("arial", 24))
button.grid(row=3, column=2, padx=10, pady=10)
button_minus=Button(text="9",command=q9, bg="#52bfc5", font=("arial", 24))
button.grid(row=3, column=3, padx=10, pady=10)
button_plus=Button(text="+",command=btpl, bg="#52bfc5", font=("arial", 24))
button.grid(row=3, column=4, padx=10, pady=10)
button_multiplication=Button(text="*",command=btmn, bg="#52bfc5", font=("arial", 24))
button.grid(row=4, column=1, padx=10, pady=10)
button_division=Button(text="/",command=btdel, bg="#52bfc5", font=("arial", 24))
button.grid(row=4, column=2, padx=10, pady=10)
button_division=Button(text="=",command=w, bg="#52bfc5", font=("arial", 24))
button.grid(row=4, column=3, padx=10, pady=10)
button_division=Button(text=".",command=qc, bg="#52bfc5", font=("arial", 24))
button.grid(row=4, column=4, padx=10, pady=10)
Label_division=Label(text=".", bg="#3cc1ca", font=("arial", 24))
Label_division.place(x=25, y=25, width=450, height=100)
app.mainloop()