import turtle
import math
import random
from alphabet import alphabet
################################
wn = turtle.Screen()
wn.bgcolor('black')
#############################
myPen = turtle.Turtle()
myPen.hideturtle()
myPen.speed(1)
window = turtle.Screen()
window.bgcolor("#000000")
myPen.pensize(2)

def displayMessage(message,fontSize,color,x,y):
  myPen.color(color)
  message=message.upper()
  
  for character in message:
    if character in alphabet:
      letter=alphabet[character]
      myPen.penup()
      for dot in letter:
        myPen.goto(x + dot[0]*fontSize, y + dot[1]*fontSize)
        myPen.pendown() 
        
      x += fontSize
      
    if character == " ":
      x += fontSize
    x += characterSpacing 

#############################
fontSize = 30
characterSpacing = 9
fontColor = "blue"

message = "ONURONON"
displayMessage(message,fontSize,fontColor,-130,250)

###############################
Tamim = turtle.Turtle()
Tamim.speed(0)
Tamim.color('white')
rotate=int(360)
def drawCircles(t,size):
    for i in range(10):
        t.circle(size)
        size=size-4
def drawSpecial(t,size,repeat):
  for i in range (repeat):
    drawCircles(t,size)
    t.right(360/repeat)
drawSpecial(Tamim,100,10)
t2 = turtle.Turtle()
t2.speed(0)
t2.color('yellow')
rotate=int(90)
def drawCircles(t,size):
    for i in range(4):
        t.circle(size)
        size=size-10
def drawSpecial(t,size,repeat):
    for i in range (repeat):
        drawCircles(t,size)
        t.right(360/repeat)
drawSpecial(t2,100,10)
t3 = turtle.Turtle()
t3.speed(0)
t3.color('blue')
rotate=int(80)
def drawCircles(t,size):
    for i in range(4):
        t.circle(size)
        size=size-5
def drawSpecial(t,size,repeat):
    for i in range (repeat):
        drawCircles(t,size)
        t.right(360/repeat)
drawSpecial(t3,100,10)
t4 = turtle.Turtle()
t4.speed(0)
t4.color('orange')
rotate=int(90)
def drawCircles(t,size):
    for i in range(4):
        t.circle(size)
        size=size-19
def drawSpecial(t,size,repeat):
    for i in range (repeat):
        drawCircles(t,size)
        t.right(360/repeat)
drawSpecial(t4,100,10)
t5 = turtle.Turtle()
t5.speed(0)
t5.color('pink')
rotate=int(90)
def drawCircles(t,size):
    for i in range(4):
        t.circle(size)
        size=size-20
def drawSpecial(t,size,repeat):
    for i in range (repeat):
        drawCircles(t,size)
        t.right(360/repeat)
drawSpecial(t5,100,10)
wn.exitonclick()