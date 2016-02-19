import turtle

def draw_square():

    window = turtle.Screen()
    window.bgcolor('red')

    brad = turtle.Turtle()
    brad.shape('circle')
    brad.color('pink', 'purple')
    brad.speed(5)

    num = 1

    while num < 5:
        brad.forward(100)
        brad.right(90)
        num += 1
 
    window.exitonclick()

def draw_circle():

    window = turtle.Screen()
    window.bgcolor('green')
    angie = turtle.Turtle()
    angie.shape('turtle')
    angie.circle(100)

    window.exitonclick()

def draw_triangle():

    window = turtle.Screen()
    window.bgcolor('blue')
    eden = turtle.Turtle()
    eden.shape('triangle')
    eden.speed(1)

    num = 1
    while num < 4:
        eden.forward(100)
        eden.right(120)
        num += 1

    window.exitonclick()

draw_triangle()
