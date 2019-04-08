from random import *
from tkinter import *


# choice section
def user_choicefire():
    user_choice = "Fire"
    turn(user_choice)
    userImage.configure(image=FireImage)


def user_choicewind():
    user_choice = "Wind"
    turn(user_choice)
    userImage.configure(image=WindImage)


def user_choicewater():
    user_choice = "Water"
    turn(user_choice)
    userImage.configure(image=WaterImage)


# Game Menu

def newgame():
    print("New Game!")


def restartgame():
    print('Restart Game')


def about():
    print('RULES: '
          'WATER BEATS FIRE'
          '-FIRE BEATS WIND'
          '-WIND BEATS WATER')



# gameplay setion
def turn(user_choice):
    opponent = ['Fire', 'Wind', 'Water']
    opponentChoice = opponent[randint(0, 2)]

    if opponentChoice == 'Fire':
        opponentImage.configure(image=FireImage)
    elif opponentChoice == 'Wind':
        opponentImage.configure(image=WindImage)


    else:
        opponentImage.configure(image=WaterImage)

    if opponentChoice == user_choice:
        turnResult.configure(text="It's a draw.", fg="brown")
        compare.configure(text="VS")
    elif ((opponentChoice == 'Water' and user_choice == 'Fire') or (
            opponentChoice == 'Fire' and user_choice == 'Wind') or (
                  opponentChoice == 'Wind' and user_choice == 'Water')):
        turnResult.configure(text="You lost!!:(", fg="red")
        compare.configure(text="VS")
    else:
        turnResult.configure(text="You win !!:D", fg="green")
        compare.configure(text="VS")


# main program
stem = Tk()
stem.title("Battle Of Elements")
menu = Menu(stem)

stem.config(menu=menu)
stemmenu = Menu(menu)
menu.add_cascade(label="File", menu=stemmenu)
stemmenu.add_command(label="New Game", command=newgame)
stemmenu.add_command(label="Restart...", command=restartgame)
stemmenu.add_separator()
stemmenu.add_command(label="Exit", command=stem.quit)

helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=about)

WindButton = Button(stem, width=20, text="WIND!", justify=CENTER, font="ALGERIAN", command=user_choicewind,
                    activebackground='yellow', activeforeground='black')
WaterButton = Button(stem, width=20, text="WATER!", justify=CENTER, font="ALGERIAN", command=user_choicewater,
                     activebackground='yellow', activeforeground='black')
FireButton = Button(stem, width=20, text="FIRE!", justify=CENTER, font="ALGERIAN", command=user_choicefire,
                    activebackground='yellow', activeforeground='black')

# images
WindImage = PhotoImage(file="Air.gif")
WaterImage = PhotoImage(file="Water.gif")
FireImage = PhotoImage(file="Fire.gif")
userImage = Label(image=WindImage)
userImage.image = WindImage
compare = Label(stem, justify=CENTER, font=("ALGERIAN", 30))
opponentImage = Label(image=WaterImage)
opponentImage.image = WaterImage
turnResult = Label(stem, width=20, justify=CENTER, font=("ALGERIAN", 20))

# Tk GUI grid
WindButton.grid(row=2, column=1)
WaterButton.grid(row=2, column=2)
FireButton.grid(row=2, column=3)
userImage.grid(row=3, column=1)
compare.grid(row=3, column=2)
opponentImage.grid(row=3, column=3)
turnResult.grid(row=4, column=2)

# mainloop
stem.mainloop()
