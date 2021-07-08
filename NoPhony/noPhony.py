import turtle
import random

score = 0
lives = 3

wn = turtle.Screen() # innitiate screen
wn.title("No Phony") # title
wn.bgcolor("green") # background color
wn.bgpic("rye.gif")
wn.setup(width=800, height=600) # screen size
wn.tracer(0)

wn.register_shape("baseballGlove.gif")
wn.register_shape("greenKid.gif")
wn.register_shape("redKid.gif")

# Add the player
player = turtle.Turtle() 
player.speed(0) 
player.shape("baseballGlove.gif") 
player.color("white") 
player.penup() 
player.goto(0, -250) 
player.direction = "stop"

# List of good guys
good_guys = []

# Add the good_guy
for _ in range (10):
    good_guy = turtle.Turtle() 
    good_guy.speed(0) 
    good_guy.shape("greenKid.gif") 
    good_guy.color("blue") 
    good_guy.penup() 
    good_guy.goto(100, 250) 
    good_guy.speed = random.randint(1,2)
    good_guys.append(good_guy)

# List of bad guys
bad_guys = []

# Add the bad_guy
for _ in range (2):
    bad_guy = turtle.Turtle() 
    bad_guy.speed(0) 
    bad_guy.shape("redKid.gif") 
    bad_guy.color("red") 
    bad_guy.penup() 
    bad_guy.goto(-100, 250) 
    bad_guy.speed = random.randint(1,2)
    bad_guys.append(bad_guy)

# Creating the pen
pen = turtle.Turtle() 
pen.hideturtle()
pen.speed(0) 
pen.shape("square")
pen.color("white") 
pen.penup() 
pen.goto(0, 260) 
pen.write("Score: {}    Lives: {}".format(score, lives), align="center", font=("Courier", 24, "normal"))


# Functions
def go_left():
    player.direction = "left"

def go_right():
    player.direction = "right"

# Keyboard binding
wn.listen()
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

# Main game loop
while True:
    # Update screen
    wn.update()

    # Move the player
    if player.direction == "left":
        x = player.xcor()
        x -=3
        player.setx(x)

    if player.direction == "right":
        x = player.xcor()
        x +=3
        player.setx(x)

    # Moving the good guys
    for good_guy in good_guys:
        y = good_guy.ycor()
        y -= good_guy.speed
        good_guy.sety(y)

        # Check if off screen
        if y < -300:
            x = random.randint(-380, 380)
            y = random.randint (300, 400)
            good_guy.goto(x, y)

        # Detect collision
        if good_guy.distance(player) < 75:
            x = random.randint(-380, 380)
            y = random.randint (300, 400)
            good_guy.goto(x, y)
            score += 10
            pen.clear()
            pen.write("Score: {}    Lives: {}".format(score, lives), align="center", font=("Courier", 24, "normal"))
    
    # Moving the bad guys
    for bad_guy in bad_guys:
        y = bad_guy.ycor()
        y -= bad_guy.speed
        bad_guy.sety(y)

        # Check if off screen
        if y < -300:
            x = random.randint(-380, 380)
            y = random.randint (300, 400)
            bad_guy.goto(x, y)

        # Detect collisions
        if bad_guy.distance(player) < 75:
            x = random.randint(-380, 380)
            y = random.randint (300, 400)
            bad_guy.goto(x, y)
            score -= 10
            lives -= 1
            pen.clear()
            pen.write("Score: {}    Lives: {}".format(score, lives), align="center", font=("Courier", 24, "normal"))


