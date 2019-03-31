from tkinter import filedialog
from tkinter import* 


def mainscreen():
     print("This is the Main Program")

def File():
     print ("File!")
stem = Tk()
stem.title("This is my First Program")
stem.minsize(400,300)


     
    
lblimage = PhotoImage(file='bugatti.png')
lblimage = PhotoImage(file='chevrolet.png')
lblimage = PhotoImage(file='lamborghini.png')
Button(stem, text="Press Start ", width=10, command=mainscreen).grid(row=2, column=0, sticky=S)

def rock():
     lblimage = PhotoImage(file='bugatti.png')
def paper():                     
     lblimage = PhotoImage(file='chevrolet.png')
def scissor():                     
     lblimage = PhotoImage(file='lamborghini.png')

     
                     
Label(stem, text="Welcome To The game", bg="black",fg="aqua",
      font="none 20 bold"). grid(row=1, column =0, sticky=N)
Label(stem, image=lblimage ,
      bg="black").grid(row=4, column =0, sticky=W)
Label(stem, text ="start", width=10,
      command=start).grid(row=2, column=1, sticky=W)         

app = Frame(stem)
app.grid()
button1 = Button(app, text = "Rock")
button1.grid()

button2 = Button(app) 
button2.grid()
button2.configure(text = "Paper")

button3 = Button(app)
button3.grid
button3["text"] = "Scissors"

def start():
     Button(stem, text ="Rock ", width=5, command=rock).grid (row=4, column=1, sticky=W)
     Button(stem, text ="Paper ", width=5, command=paper).grid (row=3, column=1, sticky=W)
     Button(stem, text ="Scissors ", width=5, command=scissor).grid (row=5, column=1, sticky=W)

    












mainloop()
