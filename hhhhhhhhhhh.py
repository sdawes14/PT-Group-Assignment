from tkinter import filedialog
from tkinter import *

def rock():
    lblimage = PhotoImage(file="cars.png")

def paper():
    lblimage = PhotoImage(file="cars.png")

def scissor():
    lblimage = PhotoImage(file="cars.png")
                           
def mainscreen():
    print("This is the Main Program")

stem = Tk()
stem.title("This is my First Program")
stem.minsize(500,400)

def start():
    Button(stem, text ="Paper ", width=5, command=paper).grid (row=3, column=1, sticky=W)
    Button(stem, text ="Rock ", width=5, command=rock).grid (row=4, column=1, sticky=W)
    Button(stem, text ="Scissors ", width=5, command=scissor).grid (row=5, column=1, sticky=W)

Label(stem, text ="start", width=10, command=start).grid(row=2, column=1, sticky=W)


    













main()
