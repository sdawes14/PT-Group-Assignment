from tkinter import filedialog
from tkinter import *


def NewFile():
    print ("New File!")
def OpenFile():
    mywin.filename =  filedialog.askopenfilename(initialdir = "/",
        title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    print (root.filename)
def About():
    print ("This is a simple example of a menu")
def mainscreen():
    nextwin = Toplevel(mywin)
    Label(mywin, text="New Window")
    
    
    
mywin = Tk()
mywin.minsize(300,400)
mywin.title('This is my first program')
menu = Menu(mywin)
mywin.config(menu=menu)

filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=NewFile)
filemenu.add_command(label="Open...", command=OpenFile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=mywin.quit)

helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=About)

lblimage = PhotoImage(file="car.png")
Label(mywin, text="Welcome to Nats Systems", fg="black",
      font="none 20 bold"). grid(row=1, column =0, sticky=N)
Label(mywin, image=lblimage).grid(row=4, column = 0, sticky=W)

Button(mywin, text="Let's Begin ! ", width=10, command=mainscreen).grid(row=7,
        column=0, columnspan=2, padx=15, pady=15)


mainloop()
