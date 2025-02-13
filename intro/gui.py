from tkinter import *

window = Tk()
window.title("Sample gui program")
window.geometry('450x450')

data = IntVar()
# data = StringVar()

def myfunction():
    label2.config(text="you entered number is : " + str(data.get()))

label1 = Label(window, text="Enter a number : " )
label1.grid(row=0,column=0)

textbox = Entry(window, textvariable=data)
textbox.grid(row=0,column=1)

btn = Button(window,command=myfunction, text='Click here')
btn.grid(row=1,column=1)

label2 = Label(window)
label2.grid(row=2,column=1)

window.mainloop()