print("G5 Conversion Tool")

degrees=["c" , "f"]
distance=["km" , "miles"]
weight=["lbs", "kg"]


def fahrenheit ():
    fahrenheit = (round(celsius*(9/5)+32))
    print(fahrenheit, "degrees f")

celsius = float(input("Enter Temperature in Celsius"))
fahrenheit ()

def celsius ():
    celsius = (round(fahrenheit-32)*(5/9,1))
    print(celsius, "degrees c")

fahrenheit = float(input("Enter Temperature in Fahrenheit"))
celsius ()

def miles ():
    miles = round(km/1.609,1)
    print(miles, "miles")

km = float(input("Enter Distance in Kilometers"))
miles()

def km ():
    km = round(miles*1.609)
    print(km, "km.")

miles = float(input("Enter Distance in Miles"))
km ()

def USD ():
    USD = round(JMD/125.13,2)
    print(USD,"USD")

JMD = float(input("Enter Amount in Jamaican Dollars (JMD)"))
USD()

def JMD ():
    JMD = round(USD*125.13)
    print(JMD, "JMD")

USD = float(input("Enter Amount in United States Dollars (USD)"))
JMD ()

def lbs ():
    lbs = round(kg*2.20462)
    print(lbs,"lbs.")

kg = int(input("Enter Weight in Kilograms (kgs.)"))
lbs ()

def kg ():
    kg = round(lbs/2.20462)
    print(kg,"kgs.")

lbs = int(input("Enter Weight in Pounds (lbs.)"))
kg ()





