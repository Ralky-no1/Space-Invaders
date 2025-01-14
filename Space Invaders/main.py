from turtle import Turtle, Screen
import time
import random

SCREEN_TOP = 400
SCREEN_BOTTOM = -370
SCREEN_LEFT = 500
SCREEN_RIGHT = 500
LASER_SPEED = 20
LASER_LENGTH = 20
ALIEN_SPEED = 1
aliens = []
lasers = []
timer = time.time()
score = 0


screen = Screen()
screen.setup(width = 1000, height = 800)
screen.bgcolor('black')
screen.title("Nick's Space Invaders game")
screen.tracer(0)

cannon = Turtle('square')
cannon.color('white')
cannon.penup()
cannon.goto(x = 0, y = SCREEN_BOTTOM)

scoreboard = Turtle()
scoreboard.hideturtle()
scoreboard.penup()
scoreboard.goto(x = -350, y = 350)
scoreboard.color('white')
scoreboard.write(f"|Score: {score}|", font = ('Ariel',20,'bold'))

def draw_cannon():
    cannon.clear()
    cannon.turtlesize(1, 4)  # Base
    cannon.stamp()
    cannon.sety(SCREEN_BOTTOM + 10)
    cannon.turtlesize(1, 1.5)  # Next tier
    cannon.stamp()
    cannon.sety(SCREEN_BOTTOM + 20)
    cannon.turtlesize(0.8, 0.3)  # Tip of cannon
    cannon.stamp()
    cannon.sety(SCREEN_BOTTOM)


def update_score():
    scoreboard.clear()
    scoreboard.write(f"|Score: {score}|", font = ('Ariel',20,'bold'))

def game_over():
    scoreboard.goto(-200,0)
    scoreboard.write('GAME OVER!', font = ('Ariel',40,'bold'))


def cannon_left():
    cannon.backward(15)
    draw_cannon()

def cannon_right():
    cannon.forward(15)
    draw_cannon()

def cannon_shoot():
    laser = Turtle('square')
    laser.shapesize(0.2,2)
    laser.setheading(90)
    lasers.append(laser)
    laser.pensize(2)
    laser.color('red')
    laser.hideturtle()
    laser.goto(y = SCREEN_BOTTOM + 50, x = cannon.xcor())


def create_alien():
    alien = Turtle('turtle')
    alien.penup()
    alien.setheading(270)
    alien.color(random.random(), random.random(), random.random())
    alien.goto(y = SCREEN_TOP, x = random.uniform(-SCREEN_RIGHT, SCREEN_RIGHT))
    aliens.append(alien)

def move_aliens():
    for alien in aliens:
        alien.forward(ALIEN_SPEED)


playing = True
while playing:
    time.sleep(0.01)

    screen.listen()
    screen.onkey(key='Left', fun=cannon_left)
    screen.onkey(key='Right', fun=cannon_right)
    screen.onkey(key=' ', fun=cannon_shoot)

    for laser in lasers:
        laser.clear()
        laser.forward(LASER_SPEED)
        laser.forward(LASER_LENGTH)
        for alien in aliens:
            if laser.distance(alien) <= 20:
                laser.penup()
                laser.clear()
                laser.goto(3000,3000)
                lasers.remove(laser)
                alien.goto(3000, 3000)
                aliens.remove(alien)
                score += 10
                update_score()

        if laser.ycor() == SCREEN_TOP:
            laser.penup()
            laser.clear()
            lasers.remove(laser)
            laser.goto(3000,3000)
    for alien in aliens:
        if alien.ycor() < SCREEN_BOTTOM:  # Remove alien if it goes out of the screen
            game_over()
            playing = False

    i = random.randint(1,300)
    if i ==1: create_alien()
    move_aliens()
    draw_cannon()
    if timer == 10:
        create_alien()
    screen.update()



screen.mainloop()
