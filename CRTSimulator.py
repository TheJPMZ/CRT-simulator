import math
import sys
from typing import final
import numpy
import matplotlib.pyplot as plt
import threading
import time
import turtle
from tkinter import *
import pygame





#TODO Refactoring para que sea mejor
#TODO Interaccion con el usuario


from numpy.core.fromnumeric import trace
from numpy.lib.function_base import _select_dispatcher

root = Tk() 
root.config(bd=15)

#Hz = ocillaciones/minuto

Fi1 = 1
Fi2 = 3*math.pi/4 

Omega1 = 2
Omega2 = 3



A1 = 1   
A2 = 1 

def porcentajechido(r,rep):
    if r == 0:
        print("⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜ 0% done")   
    elif r == rep/10:
        print("⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜ 10% done")
    elif r == rep/5:
        print("⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜ 20% done")
    elif r == rep*3/10:
        print("⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜ 30% done")
    elif r == rep*2/5:
        print("⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜ 40% done")
    elif r == rep*5/10:
        print("⬛⬛⬛⬛⬛⬜⬜⬜⬜⬜ 50% done")
    elif r == rep*6/10:
        print("⬛⬛⬛⬛⬛⬛⬜⬜⬜⬜ 60% done")
    elif r == rep*7/10:
        print("⬛⬛⬛⬛⬛⬛⬛⬜⬜⬜ 70% done")
    elif r == rep*8/10:
        print("⬛⬛⬛⬛⬛⬛⬛⬛⬜⬜ 80% done")
    elif r == rep*9/10:
        print("⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜ 90% done")
    elif r == rep:
        print("⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛ 100% done")


def x(t):
    return A1 * math.cos((Omega1*t)+Fi1)

def y(t):
    return A2 * math.cos((Omega2*t)+Fi2)
    
n1 = StringVar()

Label(root, text="Voltaje de Aceleración").pack()
Entry(root, justify=CENTER, textvariable=n1).pack()
Label(root, text="Voltaje de placas Verticales").pack()
Entry(root, justify=CENTER, textvariable=n1).pack()
Label(root, text="Voltaje de placas Horizontales").pack()
Entry(root, justify=CENTER, textvariable=n1).pack()


rainbow = ['red', 'yellow', 'green', 'cyan', 'blue', 'magenta']

turtle.Screen().bgcolor("Black")



pedro = turtle.Turtle()
pedronegro = turtle.Turtle()
juana = turtle.Turtle()
pancho = turtle.Turtle()



pedro.shape("circle")
juana.shape("circle")
pancho.shape("circle")

pedro.color("Red")
pedronegro.color("Cyan")
pedronegro.hideturtle()
juana.color("Blue")


pedro.speed(9)
juana.speed(9)
pancho.speed(9)


pedro.penup()
juana.penup()
pancho.penup()
pedro.goto(-300,600)
juana.goto(-600,-300)
pancho.turtlesize(1)



for i in range(0,700): 
    
    porcentajechido(i,100)
    #print(x(i*0.01),y(i*0.01)) 
    equis = x(i*0.1)
    de = y(i*0.1)
    equismenosuno = x((i-1)*0.1)
    demenosuno = y((i-1)*0.1)
    
    pedro.pendown()
    pedro.goto(equis*100,300)

    juana.goto(300,+de*100)
    
    
    pancho.goto(equis*100,de*100)
    pancho.color(rainbow[i%6])
    pancho.pendown()
    juana.pendown()
    #plt.scatter(equis,de,s=100,c="#1f77b4")
    #plt.show()
    

        

    
def funcion():
    if(threading.current_thread().getName()) == "Thread-1":
        contador = 0
    elif (threading.current_thread().getName()) == "Thread-2":
        contador = 100
    elif (threading.current_thread().getName()) == "Thread-2":
        contador = 200
    else:
        contador = 300
    
    while contador < contador+100:
        contador += 1
        i = contador
        plt.scatter(x(i*0.01), y(i*0.01),s=100,c="#1f77b4")
 


#hilo2.start()
#hilo3.start()


#plt.show()

width=500
height=500
Color_screen=(49,150,100)
Color_line=(255,0,0)

def main():
    screen=pygame.display.set_mode((width,height))
    screen.fill(Color_screen)
    pygame.draw.dot(0,0,0,0)
    pygame.draw.line(screen, Color_line, (60, 80), (130, 100))
    pygame.display.flip()
    

if __name__ == "__main__":
    main()
