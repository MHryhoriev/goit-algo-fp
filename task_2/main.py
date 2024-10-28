from turtle import Screen, Turtle
from draw import draw_branch
from turtle_setup import setup_turtle

def main():
    """
    Main function to set up the screen and turtle, and start drawing the Pythagoras tree.
    """
    screen = Screen()
    screen.setup(width=800, height=600)
    screen.title("Pythagoras Tree Fractal")

    recursion_depth = int(screen.numinput("Input", "Enter recursion depth:", minval=1, maxval=15))

    t = Turtle()
    t.speed(0)
    t.left(90)

    setup_turtle(t, color=(128/255, 0, 32/255), pensize=2)  # Set up the turtle's appearance
    draw_branch(t, branch_length=100, angle=45, depth=recursion_depth)

    t.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()
