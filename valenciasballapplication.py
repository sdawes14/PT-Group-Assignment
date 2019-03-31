#Date edited: 3/30/2019
#Purpose: Creating a Bouncing Ball Simulator

from tkinter import filedialog
from tkinter import ttk
from tkinter import*

def mainscreen():
    print('Sample Main Program')

def About():
    print ("This is a bouncing ball application")


def bounceball():
    try:
        bouncing = int(bounce.get())
        canvas.set(image, -10, 0)
    except ValueError:
        pass
    

def bounceentry():#Defining the bounceentry command 
    bounce = StringVar()#Defining the variable as a string
    bounceentry = ttk.Entry(valwindow, width=7, textvariable=bounce)
    bounceentry.grid(column=1, row=8, sticky=(S, E)) #This creates the entry box
    ttk.Label(valwindow, text='Enter your Number of Bounces', font='none 10 bold').grid(row=7, column=1, sticky=(S,E))

    
valwindow=Tk()#This is the main window
valwindow.title('Bouncing Ball Application')
valwindow.minsize(400, 200)


 
canvas = tk.Canvas(valwindow, width=100, height=100)#creating a canvas

 
img = tk.PhotoImage(file="pinkball.gif")
image = canvas.create_image(10, 10, anchor=tk.NW, image=img)
 


labelimage=PhotoImage(file='pinkball.gif')#this is the file location of the image
Label(valwindow, text="Welcome to the Bouncing Ball Application",bg='pink',fg='black',font='none 20 bold').grid(row=1, column=0, sticky=N)
Label(valwindow, image=img). grid(row=7, column =0)

#This button will bring up the entry box 
button_one=Button(valwindow, text='LETS START!', width=10, command=bounceentry).grid(row=10, column=0, sticky=S, padx=15, pady=15)

#This button closes the window
button_two=Button(valwindow, text='QUIT', width=10, command=valwindow.destroy).grid(row=10, column=1,padx=15, pady=15 )

#This button will command the ball to bounce
buttonbounce=Button(valwindow, text='BOUNCE',width=10, command=bounceball).grid(row=9, column=1, sticky=(S,E))


    

 







valwindow.mainloop()#This loops the program until its closed. 



