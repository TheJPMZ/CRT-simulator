import math
import turtle
from tkinter import *

#TODO: Documentation

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

Label(root, text="Voltaje de Aceleración").pack()

scale = Scale(root, from_=0, to=255,orient=HORIZONTAL)
scale.set(127)
scale.pack()

Label(root, text="Tiempo de latencia").pack()

latency = Scale(root, from_=1, to=100,orient=HORIZONTAL)
latency.set(50)
latency.pack()

Label(root, text="Voltaje de placas Verticales").pack()

placas_verticales = Scale(root, from_=-100, to=100,orient=HORIZONTAL)
placas_verticales.pack()
placas_verticales.set(0)

Label(root, text="Voltaje de placas Horizontales").pack()

placas_horizontales = Scale(root, from_=-100, to=100,orient=HORIZONTAL)
placas_horizontales.pack()
placas_horizontales.set(0)

Label(root, text="Desfase entre ambos oscilladores").pack()

desfase = Scale(root, from_=0, to=180,orient=HORIZONTAL)
desfase.pack()

Label(root, text="Frecuencia").pack()

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

Button(root, text = "Cambio de Modo",command=changemode).pack(side=LEFT)

Button(root, text = "Limpiar",command=canvasclear).pack(side=LEFT)

onLoop = True
def salir():
    global onLoop
    onLoop = False

Button(root, text = "Salir",command=salir).pack(side=LEFT)

changemode() 

turtle.Screen().bgcolor("Black")
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