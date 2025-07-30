import turtle

screen = turtle.Screen()
screen.title("Square with Turtle")

square_turtle = turtle.Turtle()
square_turtle.pensize(3)
square_turtle.speed(2)

for _ in range(4):
    square_turtle.forward(100)  
    square_turtle.right(90)  
    
turtle.done()  

