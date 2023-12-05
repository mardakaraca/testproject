import turtle
import random

screen = turtle.Screen()
screen.title("Catch the Turtle")
screen.setup(width=600, height=600)
screen.bgcolor("light blue")

target = turtle.Turtle()
target.shape("turtle")
target.shapesize(2, 2)
target.color("green")
target.penup()

top_height = screen.window_height() / 2
text_place = top_height - top_height / 10

score_writer = turtle.Turtle()
score_writer.penup()
score_writer.hideturtle()
score_writer.goto(x=0, y=text_place - 30)

time_writer = turtle.Turtle()
time_writer.penup()
time_writer.hideturtle()
time_writer.goto(x=0, y=text_place)

start_writer = turtle.Turtle()
start_writer.penup()
start_writer.hideturtle()
start_writer.goto(x=0, y=0)

score = 0
high_score = 0
game_over = False
FONT = ('Arial', 20, 'normal')

x_coordinates = [-250, -200, -150, -100, -50, 0, 50, 100, 150, 200, 250]
y_coordinates = [-250, -200, -150, -100, -50, 0, 50, 100, 150, 200, 250]


def target_func():
    global x_coordinates, y_coordinates, target
    x_position = random.choice(x_coordinates)
    y_position = random.choice(y_coordinates)
    target.hideturtle()
    target.goto(x=y_position, y=x_position)
    target.showturtle()
    screen.ontimer(target_func, 500)


def countdown(time):
    global time_writer, game_over
    if time > 0:
        time_writer.clear()
        time_writer.write("Time:{}".format(time), move=False, align="center", font=FONT)
        screen.ontimer(lambda: countdown(time - 1), 1000)
    else:
        game_over = True
        time_writer.clear()
        hide_target()
        time_writer.write("GAME OVER!".format(time), move=False, align="center", font=FONT)


def hide_target():
    target.hideturtle()


def click():
    global score, high_score
    score_writer.write("Score:{} High Score:{}".format(score, high_score), move=False, align="center",
                       font=FONT)

    def score_func(x, y):
        global score, high_score
        score += 1
        score_writer.clear()
        if score >= high_score:
            new_high_score = score
            score_writer.write("Score:{} High Score:{}".format(score, new_high_score), move=False, align="center",
                               font=FONT)
        else:
            score_writer.write("Score:{} High Score:{}".format(score, high_score), move=False, align="center",
                               font=FONT)

    target.onclick(score_func)


def game_functions():
    global game_over
    game_over = False
    turtle.tracer(0)
    target_func()
    countdown(30)
    click()
    turtle.tracer(1)


game_functions()
turtle.mainloop()
