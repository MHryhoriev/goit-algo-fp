from turtle import Turtle
import math

def draw_branch(t: Turtle, branch_length: float, angle: float, depth: int) -> None:
    """
    Draws a branch of the Pythagoras tree fractal recursively.
    
    Parameters:
        t (Turtle): The turtle used to draw.
        branch_length (float): The length of the branch.
        angle (float): The angle to turn the turtle.
        depth (int): The recursion depth.
    """
    if depth == 0:
        return
    
    t.forward(branch_length)

    position = t.position()
    heading = t.heading()

    t.left(angle)
    draw_branch(t, branch_length * math.sqrt(2) / 2, angle, depth - 1)

    t.setheading(heading)
    t.setposition(position)

    t.right(angle)
    draw_branch(t, branch_length * math.sqrt(2) / 2, angle, depth - 1)

    t.setheading(heading)
    t.backward(branch_length)
