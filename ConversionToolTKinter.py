#!/usr/bin/python

import tkinter
app = tkinter.Tk()
v = tkinter.IntVar()
v.set(1)
app.geometry('480x300') #Window Dimensions
app.title("Conversion Tool")	#Window Title

def convert(sv,v,ot): #Conversion Formulas Functions
	if (sv.get().isdigit()):
		print("v.get() :"+str(v.get())+" | sv.get(): "+str(sv.get()))
		if v.get() == 0:
			ot.set("Please select an option for conversions")
		elif v.get() == 1:
			ot.set(round(float(sv.get())*(9/5)+32)) #Celsius to Fahrenheit
		elif v.get() == 2:
			ot.set(round(float(sv.get())-32)*(5/9)) #Fahrenheit to Celsius
		elif v.get() == 3:
			ot.set(round(float(sv.get())/1.609,1)) #Kilometers to miles
		elif v.get() == 4:
			ot.set(round(float(sv.get())*1.609,1)) #Miles to Kilometers
		elif v.get() == 5:
			ot.set(str(round(float(sv.get())*0.0080,2))+" USD")	#JMD to USD
		elif v.get() == 6:
			ot.set(str(round(float(sv.get())*125.13,2))+" JMD")     #USD to JMD
		elif v.get() == 7:
			ot.set(round(float(sv.get())*2.20462,1)) #Kilograms to Pounds
		elif v.get() == 8:
			ot.set(round(float(sv.get())*0.453592,1)) #Pounds to Kilograms	
#Radiobutton Dimensions and Add-ons
L1=tkinter.Label(app, text="Choose your conversion:",justify="left",  padx = 20).grid(row=0, column=0, columnspan=1, sticky=tkinter.W+tkinter.E)
RB1=tkinter.Radiobutton(app, text="Celsius to Fahrenheit",justify="left",padx = 20, variable=v, value=1).grid(row=1, column=0, columnspan=1,sticky=tkinter.W+tkinter.E)
RB2=tkinter.Radiobutton(app, text="Fahrenheit to Celsius",justify="left",padx = 20, variable=v, value=2).grid(row=2, column=0, columnspan=1,sticky=tkinter.W+tkinter.E)
RB3=tkinter.Radiobutton(app, text="Kilometers to Miles",justify = "left",padx = 20, variable=v, value=3).grid(row=3, column=0, columnspan=1, sticky=tkinter.W+tkinter.E)
RB4=tkinter.Radiobutton(app, text="Miles to Kilometers",justify = "left",padx = 20, variable=v, value=4).grid(row=4, column=0, columnspan=1, sticky=tkinter.W+tkinter.E)
RB5=tkinter.Radiobutton(app, text="JMD to U.S. Dollars",justify = "left", padx = 20, variable=v, value=5).grid(row=5, column=0, columnspan=1, sticky=tkinter.W+tkinter.E)
RB6=tkinter.Radiobutton(app, text="U.S. Dollars to JMD",justify = "left", padx = 20, variable=v, value=6).grid(row=6, column=0, columnspan=1, sticky=tkinter.W+tkinter.E)
RB7=tkinter.Radiobutton(app, text="Kilograms to Pounds",justify = "left", padx = 20, variable=v, value=7).grid(row=7, column=0, columnspan=1, sticky=tkinter.W+tkinter.E)
RB8=tkinter.Radiobutton(app, text="Pounds to Kilograms",justify = "left", padx = 20, variable=v, value=8).grid(row=8, column=0, columnspan=1, sticky=tkinter.W+tkinter.E)
#Conversion Values Placed in this box with dimensions
L2=tkinter.Label(app, text="Value to convert:",justify = "left",  padx = 20).grid(row=10, column=1, columnspan=1, sticky=tkinter.W+tkinter.E)
#Functions Calls
ot = tkinter.StringVar()
sv = tkinter.StringVar()
sv.trace("w", lambda name, index, mode, sv=sv: convert(sv,v,ot))


#Entry label and box 
E1=tkinter.Entry(app, width=4,textvariable=sv).grid(row=4, column=3, columnspan=1, sticky=tkinter.W+tkinter.E)
L3=tkinter.Label(app, text="Converted Value:", fg="red", padx = 20).grid(row=11, column=0, columnspan=4, sticky=tkinter.W+tkinter.E)
E2=tkinter.Entry(app, width=4,state='disabled',textvariable=ot).grid(row=11, column=0, columnspan=4, sticky=tkinter.W+tkinter.E)

app.mainloop()  #Loop
