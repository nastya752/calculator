from tkinter import*
app=Tk()
count=[0]
def Button_click(count=count):
    count[0] += 1
    dog["text"] = f"Hamster is clicked {count[0]} times"
    count_Label["text"] = f"Hamster square is {count[0] ** 2}"
parrot="Roboto"
app.geometry("1000x500+500+200")
both=Button(text="kitten",command=Button_click, width=50, bg="blue",fg="red",font=(parrot, 16,"italic"))
both.place(x=200,y=200)
dog=Label(text="hamster", font=(parrot, 24), bg="yellow", bd=20)
dog.place(x=450,y=100)
count_Label=Label(text="square", font=(count, 24), bg="pink", bd=15)
count_Label.place(x=450,y=20)
app.mainloop()
