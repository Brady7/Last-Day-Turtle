# import turtle
# window=turtle.Screen()
# turtle=turtle.Turtle()
# sideLength=input ("What should the side lengths of the hexagon be?") 
# sideLength=int(sideLength)
# color=input ("What color should the hexagon be?")


# def hexagon(sideLength,color):
#   turtle.color(color)
#   variable=0
#   while variable<6:
#     turtle.forward(sideLength)
#     turtle.right(60)
#     variable=variable+1

# hexagon(sideLength,color)

import turtle
window=turtle.Screen()
window.setup(600,600)
window.bgcolor("black")
turtle=turtle.Turtle()
turtle.speed(50)
Play=True
def polygonPatterns (shape,length,color,turn,distance):
  variable=0
  Play=True
  if shape=="circle":
    turtle.color(color)
    turtle.penup()
    turtle.setposition(100,100)
    turtle.pendown()
    while variable<36:
      turtle.circle(length)
      turtle.right(turn)
      turtle.forward(distance)
      variable=variable+1
  elif shape=="square":
    turtle.color(color)
    turtle.penup()
    turtle.setposition(100,100)
    turtle.pendown()
    while variable<36:
      turtle.forward(length)
      turtle.right(90)
      turtle.forward(length)
      turtle.right(90)
      turtle.forward(length)
      turtle.right(90)
      turtle.forward(length)
      turtle.right(90)
      turtle.right(turn)
      turtle.forward(distance)
      variable=variable+1
  elif shape=="triangle":
    turtle.color(color)
    turtle.penup()
    turtle.setposition(100,100)
    turtle.pendown()
    while variable<36:
      turtle.forward(length)
      turtle.right(120)
      turtle.forward(length)
      turtle.right(120)
      turtle.forward(length)
      turtle.right(120)
      turtle.right(turn)
      turtle.forward(distance)
      variable=variable+1
  elif shape=="hexagon":
    turtle.color(color)
    turtle.penup()
    turtle.setposition(100,100)
    turtle.pendown()
    while variable<36:
        turtle.forward(length)
        turtle.right(60)
        turtle.forward(length)
        turtle.right(60)
        turtle.forward(length)
        turtle.right(60)
        turtle.forward(length)
        turtle.right(60)
        turtle.forward(length)
        turtle.right(60)
        turtle.forward(length)
        turtle.right(60)
        turtle.right(turn)
        turtle.forward(distance)
        variable=variable+1
  else:
    print ("Choose either square,triangle or square")
    polygonPatterns(shape,length,color,turn)
  answer=input ("Pattern complete! Do you want to draw another one? Y/N")
  if answer=="yes"or answer=="y":
    variable=0
    if Play==True:
      questions()
  elif answer=="no" or answer=="n":
    print ("Bye!")
    Play=False
    
def questions():
  shape=input ("What shape do you want to use in the pattern?")
  length=input("What should the length (or radius for circles) of the shapes be?")
  turn=input("How much do you want the shape to turn each time it repeats in the pattern?")
  distance=input("How far from the center should the shapes be?")
  color=input("What should the color of the pattern be?")
  polygonPatterns(shape,length,color,turn,distance)
if Play==True:
  questions()

