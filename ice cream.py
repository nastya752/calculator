from tkinter import*
import random
app=Tk()
list_ice=["chocolate", "vanila", "strawbery", "carmel", "nuts"]
x_ingredit=0
def Button_click():
    color = f"#{random.randint(0, 255):02x}{random.randint(0, 255):02x}"
    app["bg"]=color
for ingredient in list_ice:
    button=Button(text=ingredient, width=10, font=("Arial", 14))
    x_ingredit+=1
    button.grid(column=x_ingredit, row=1, padx=8, pady=20)
count=[0]
app.geometry("700x500+500+200")
app.title("first window")
app["bg"]="#e5a3e5"
app.grid_columnconfigure(0, minsize=10)
app.grid_rowconfigure(0, minsize=20)
ice=Label(text="ice cream", font=("ice cream", 24), bg="light blue")
ice.grid(column=1, row=0, columnspan=6)
app.mainloop()
