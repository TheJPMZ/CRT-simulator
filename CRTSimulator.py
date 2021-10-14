import math
import turtle
from tkinter import *

root = Tk() 
root.config(bd=15)

Omega1 = 1
Omega2 = 1

def x(t):
    return (placas_horizontales.get()/100) * math.cos((Omega1*t))

def y(t):
    return (placas_verticales.get()/100) * math.cos((Omega2*t)+degreeToRad(desfase.get()))

def degreeToRad(a):
    return (a * math.pi / 180)

def canvasclear():
    x_value.clear()
    y_value.clear()
    screen_value.clear()
   
current_mode = 1
def changemode():
    global current_mode,Omega1,Omega2
    if current_mode == 0:
         
        placas_verticales.set(100)
        placas_horizontales.set(100)
        
        label_3["state"] = "disable"
        label_4["state"] = "disable"
        label_5["state"] = "normal"
        label_6["state"] = "normal"
        
        placas_horizontales["state"] = "disable"
        placas_verticales["state"] = "disable"
        desfase["state"] = "normal"
        R1["state"] = "normal"
        R2["state"] = "normal"
        R3["state"] = "normal"
        R4["state"] = "normal"
        
        
        current_mode = 1
        
    else: 
        desfase.set(0)
        
        label_3["state"] = "normal"
        label_4["state"] = "normal"
        label_5["state"] = "disable"
        label_6["state"] = "disable"
    
        placas_horizontales["state"] = "normal"
        placas_verticales["state"] = "normal"
        desfase["state"] = "disable"
        R1["state"] = "disable"
        R2["state"] = "disable"
        R3["state"] = "disable"
        R4["state"] = "disable"
        
        Omega1 = 0
        Omega2 = 0
       
        current_mode = 0

label_1 = Label(root, text="Acceleration Voltage")
label_1.pack()

scale = Scale(root, from_=0, to=255,orient=HORIZONTAL)
scale.set(127)
scale.pack()

label_2 = Label(root, text="\nLatency")
label_2.pack()

latency = Scale(root, from_=1, to=100,orient=HORIZONTAL)
latency.set(50)
latency.pack()

label_3 = Label(root, text="\n\nVertical plate voltage")
label_3.pack()

placas_verticales = Scale(root, from_=-100, to=100,orient=HORIZONTAL)
placas_verticales.pack()
placas_verticales.set(0)

label_4 = Label(root, text="\nHorizontal plate voltage")
label_4.pack()

placas_horizontales = Scale(root, from_=-100, to=100,orient=HORIZONTAL)
placas_horizontales.pack()
placas_horizontales.set(0)

label_5 = Label(root, text="\n\nPhase shift between both oscillators")
label_5.pack()

desfase = Scale(root, from_=0, to=180,orient=HORIZONTAL)
desfase.pack()

label_6 = Label(root, text="\nFrequency")
label_6.pack()

var = StringVar()

def changeOmega():
    global Omega1,Omega2
    list = var.get().split(",")
    
    Omega1 = int(list[0])
    Omega2 = int(list[1])

R1 = Radiobutton(root, justify=CENTER, text="1:1", variable=var, value="1,1",command=changeOmega)
R1.pack( anchor = CENTER,side=TOP)

R2 = Radiobutton(root, justify=CENTER, text="1:2", variable=var, value="1,2",command=changeOmega)
R2.pack( anchor = CENTER ,side=TOP)

R3 = Radiobutton(root,justify=CENTER, text="1:3", variable=var, value="1,3",command=changeOmega)
R3.pack( anchor = CENTER,side=TOP)

R4 = Radiobutton(root,justify=CENTER, text="2:3", variable=var, value="2,3",command=changeOmega)
R4.pack( anchor = CENTER,side=TOP)

Button(root, text = "Change mode",command=changemode).pack(side=LEFT)

Button(root, text = "Clean Screen",command=canvasclear).pack(side=LEFT)

onLoop = True
def salir():
    global onLoop
    onLoop = False

Button(root, text = "Leave",command=salir).pack(side=LEFT)

changemode()    


turtle.screensize(canvwidth=400,canvheight= 400,bg = "Black")
turtle.Screen().colormode(255)


x_value = turtle.Turtle()
y_value = turtle.Turtle()
screen_value = turtle.Turtle()

x_value.shape("circle")
y_value.shape("circle")
screen_value.shape("circle")

x_value.color("Red")
y_value.color("Blue")

x_value.penup()
y_value.penup()
screen_value.penup()

screen_value.turtlesize(0.5)
screen_value.pensize(5)       

def draw(time):

    x_axis = x(time*0.1*(latency.get()/50))
    y_axis = y(time*0.1*(latency.get()/50))
    
    x_value.goto(x_axis*100,300)
    y_value.goto(300,+y_axis*100)
    screen_value.goto(x_axis*100,y_axis*100)

    screen_value.pencolor(scale.get(),0,scale.get())
    
    screen_value.pendown()
    y_value.pendown()
    x_value.pendown()

def main():
    
    time = 0
    while onLoop:
        draw(time)
        time += 1


if __name__ == "__main__":
    main()