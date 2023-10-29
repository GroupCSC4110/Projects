import subprocess
import turtle
import random
import math

# Set up the screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")
wn.setup(width=720, height=480)

# Draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-360, -240)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(720 if side % 2 == 0 else 480)
    border_pen.lt(90)
border_pen.hideturtle()

# Set the score to 0
score = 0

# Draw the score on the screen
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-340, 210)
scorestring = "Score: %s" % score
score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()

# Create the player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0, -220)
player.setheading(90)

playerspeed = 15

# Choose a number of enemies
number_of_enemies = 5
# Create an empty list of enemies
enemies = []

# Add enemies to the list
for i in range(number_of_enemies):
    # Create the enemy
    enemy = turtle.Turtle()
    enemy.color("red")
    enemy.shape("triangle")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-350, 350)
    y = random.randint(100, 230)
    enemy.setposition(x, y)
    # Give each enemy their own speed
    enemy.speed = random.randint(2, 5)
    enemies.append(enemy)


# Create the player's bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("circle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletspeed = 20

# Define bullet state
# ready - ready to fire
# fire - bullet is firing
bulletstate = "ready"

# Move the player left and right
def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -340:
        x = -340
    player.setx(x)

def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 340:
        x = 340
    player.setx(x)

def fire_bullet():
    # Declare bulletstate as a global if it needs changed
    global bulletstate
    if bulletstate == "ready":
        bulletstate = "fire"
        # Move the bullet to the just above the player
        x = player.xcor()
        y = player.ycor() +10
        bullet.setposition(x, y)
        bullet.showturtle()

def is_collision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 15:
        return True
    else:
        return False

# Create keyboard bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")

# Main game loop
while True:

    for enemy in enemies:
        # Move the enemy
        x = enemy.xcor()
        x += enemy.speed
        enemy.setx(x)

        # Move the enemy back and down
        if enemy.xcor() > 340 or enemy.xcor() < -340:
            # Move the enemy down
            y = enemy.ycor()
            y -= 40
            enemy.sety(y)
            # Change this enemy's direction
            enemy.speed *= -1

        # Check for a collision between the bullet and the enemy
        if is_collision(bullet, enemy):
            # Reset the bullet
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, -400)
            # Reset the enemy
            x = random.randint(-350, 350)
            y = random.randint(100, 230)
            enemy.setposition(x, y)

        # Check for a collision between the enemy and the player
        if is_collision(player, enemy):
            player.hideturtle()
            enemy.hideturtle()
            print ("Game Over")
            break

    # Move the bullet
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    # Check to see if the bullet has gone to the top
    if bullet.ycor() > 235:
        bullet.hideturtle()
        bulletstate = "ready"
