from tkinter import *

window = Tk()
window.title("Triangle area calculator")
window.geometry('500x200')

height = IntVar()
breadth = IntVar()


def area():
    area= 0.5*height.get()*breadth.get()
    label3.config(text="Area is : " + str(area))


label1 = Label(window, text="Enter the height :")
label1.grid(row=0,column=0)

textbox1 = Entry(window, textvariable=height)
textbox1.grid(row=0, column=1)

label2 = Label(window, text="Enter the breadth : ")
label2.grid(row=1, column=0)

textbox2 = Entry(window, textvariable=breadth)
textbox2.grid(row=1, column=1)

btn = Button(window, command=area, text="Calculate area")
btn.grid(row=2, column=0)

label3 = Label(window)
label3.grid(row=3, column=0)

window.mainloop()