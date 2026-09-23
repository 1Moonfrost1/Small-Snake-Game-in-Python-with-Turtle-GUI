import random
import turtle
from turtle import Turtle, Screen

def create_turtle(shape, xpos, ypos):
    turtle = Turtle(shape)
    turtle.penup()
    turtle.color("white")
    turtle.teleport(xpos,ypos)
    turtle.speed(100)
    return turtle

def create_apple(new_apple, snake):
    randx = random.randrange(-380, 380, 20)
    randy = random.randrange(-280, 280, 20)
    new_coords = True
    for part in snake:
        if part.position() == turtle.Vec2D(randx, randy):
            new_coords = False
            break

    if new_coords:
        new_apple.teleport(randx, randy)
    else:
        create_apple(new_apple, snake)

t3 = create_turtle("square", 0, 0)
t2 = create_turtle("square", t3.xcor()-20, 0)
t1 = create_turtle("square", t2.xcor()-20, 0)
tail = t3
snake_tail = [t1, t2, t3]

apple = create_turtle("circle", 0, 0)
create_apple(apple, snake_tail)

direction = "a"
can_change_direction = True

def check_edges(head):
    """Checks if the snake inside the area and returns false if it's not out of bounds"""
    if -400 < head.xcor() < 400 and -300 < head.ycor() < 300:
        return False
    return True

def change_direction(dir):
    global direction, can_change_direction

    if can_change_direction:
        if dir == "a" and direction != "d":
            direction = dir
        elif dir == "d" and direction != "a":
            direction = dir
        elif dir == "w" and direction != "s":
            direction = dir
        elif dir == "s" and direction != "w":
            direction = dir
        can_change_direction = False


def move_dir(xamnt, yamnt):
    for i in range(len(snake_tail)-1, 0, -1):
        snake_tail[i].setposition(snake_tail[i-1].xcor(), snake_tail[i-1].ycor())
    snake_tail[0].setposition(snake_tail[0].xcor()+xamnt, snake_tail[0].ycor()+yamnt)

def move():
    global apple, tail, can_change_direction

    if direction == "a":
        move_dir(-20, 0)
    elif direction == "d":
        move_dir(20, 0)
    elif direction == "w":
        move_dir(0, 20)
    elif direction == "s":
        move_dir(0, -20)

    if snake_tail[0].position() == apple.position():
        t4 = create_turtle("square", tail.xcor(), tail.ycor())
        snake_tail.append(t4)
        tail = t4
        create_apple(apple, snake_tail)

    for i in range(1, len(snake_tail)):
        if snake_tail[0].position() == snake_tail[i].position() or check_edges(snake_tail[0]):
            message = Turtle()
            message.setposition(0, 250)
            message.hideturtle()
            message.pencolor("white")
            message.write(f"GAME OVER. Your score is: {len(snake_tail)-3}.",
                          align = "center", font=("Courier", 25, "normal"))
            screen.update()
            return


    screen.update()
    can_change_direction = True
    screen.ontimer(move, 100)

screen = Screen()
turtle.title("Snake Game")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

screen.listen()

screen.onkeypress(key="a", fun= lambda : change_direction("a"))
screen.onkeypress(key="s", fun= lambda : change_direction("s"))
screen.onkeypress(key="d", fun= lambda : change_direction("d"))
screen.onkeypress(key="w", fun= lambda : change_direction("w"))

move()

screen.exitonclick()