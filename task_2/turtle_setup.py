from turtle import Turtle

def setup_turtle(t: Turtle, color: str, pensize: int) -> None:
    """
    Configures the turtle with the specified color and pensize.
    
    Parameters:
        t (Turtle): The turtle to configure.
        color (str): The color for the turtle's pen.
        pensize (int): The thickness of the pen.
    """
    t.pencolor(color)
    t.pensize(pensize)
