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

    for i in range(1,73):
        draw_diamond(anna)
        anna.right(5)
    anna.right(90)
    anna.forward(200)

    window.exitonclick()

draw_art()
