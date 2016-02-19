import turtle

def draw_square(some_square):

    for i in range(1,5):
        some_square.forward(100)
        some_square.right(90)

def draw_diamond(some_diamond):

    for i in range (1,3):    
        some_diamond.forward(50)
        some_diamond.right(60)
        some_diamond.forward(50)
        some_diamond.right(120)
    
def draw_triangle(some_triangle):

    some_triangle.fill(True)
    for i in range(1,4):
        some_triangle.forward(20)
        some_triangle.left(120)
    some_triangle.fill(False)
    
def draw_art():

    window = turtle.Screen()
    window.bgcolor('yellow')

    rose = turtle.Turtle()
    rose.shape('classic')
    rose.speed(1)
    rose.color('blue')
    """
    for i in range(1, 37):
        draw_square(rose)
        rose.right(10)
    """
    anna = turtle.Turtle()
    anna.shape('classic')
    anna.speed(8)
    #code for drawing flower
    """
    for i in range(1,73):
        draw_diamond(anna)
        anna.right(5)
    anna.right(90)
    anna.forward(200)
    """
    #code for drawing fractals
    """
    elsa = turtle.Turtle()
    elsa.shape('classic')
    elsa.color('blue', 'green')
    elsa.speed(5)
    draw_triangle(elsa)
    """

    # write my initials for Bjorn Lee
    bjorn = turtle.Turtle()
    bjorn.shapesize(0.1,0.1,0.1)
    bjorn.shape('turtle')
    bjorn.speed('0.1')
    bjorn.color('blue')
    bjorn.left(90)
    bjorn.forward(100)
    bjorn.right(135)
    bjorn.forward(35)
    bjorn.right(90)
    bjorn.forward(35)
    bjorn.left(90)
    bjorn.forward(35)
    bjorn.right(90)
    bjorn.forward(35)

    window.exitonclick()

draw_art()
