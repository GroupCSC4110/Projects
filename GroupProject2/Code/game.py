"""
This creates a space indavers game using turtle and tkinter
"""

# Import needed packages
import turtle
import random
import subprocess

# set up the SCREEN
SCREEN = turtle.SCREEN()
SCREEN.title("Space Invaders")
SCREEN.bgpic('Content/Background.gif')
SCREEN.setup(width=800, height=600)

CHARACTER = None

bullets = []

enemies = []

# spawn rate
Spawn = 200
timer = Spawn

score = 0
health = 100

# score display
ShowScore = turtle.Turtle()
ShowScore.speed(0)
ShowScore.color("white")
ShowScore.penup()
ShowScore.hideturtle()
ShowScore.goto(-380, 260)
ShowScore.write(f"Score: {score}", align="left", font=("Arial", 16, "normal"))

# health bar
ShowHealth = turtle.Turtle()
ShowHealth.speed(0)
ShowHealth.color("red")
ShowHealth.penup()
ShowHealth.hideturtle()
ShowHealth.goto(380, 260)
ShowHealth.write(f"Health: {health}%", align="right", font=("Arial", 16, "normal"))

turtle.register_shape("Content/Character.gif")
# create the character
def charct():
    """
    param: None
    paramType: None
    return: None
    returnType: None
    """
    CHARACTER = turtle.Turtle()
    CHARACTER.shape('Content/Character.gif')
    turtle.register_shape("Character.gif")
# Function to create the character
def create_character():
    #global characte    character = turtle.Turtle()
    CHARACTER.shape('Character.gif')
    CHARACTER.speed(0)
    CHARACTER.penup()
    CHARACTER.goto(0,-250)
    CHARACTER.dx = 20

# move the character to the left
def left():
    """
    param: None
    paramType: None
    return: None
    returnType: None
    """
    x = CHARACTER.xcor()
    x -= CHARACTER.dx
    if x < -380:
        x = -380
    CHARACTER.setx(x)

# move the character to the right
def right():
    """
    param: None
    paramType: None
    return: None
    returnType: None
    """
    x = CHARACTER.xcor()
    x += CHARACTER.dx
    if x > 380:
        x = 380
    CHARACTER.setx(x)

# shoot a bullet
def shoot():
    """
    param: None
    paramType: None
    return: None
    returnType: None
    """
    bullet = turtle.Turtle()
    bullet.shape("triangle")
    bullet.color("yellow")
    bullet.speed(0)
    bullet.penup()
    bullet.shapesize(stretch_wid=0.5, stretch_len=0.1)
    bullet.goto(CHARACTER.xcor(), CHARACTER.ycor() + 10)
    bullet.dy = 30
    bullets.append(bullet)

turtle.register_shape("Content/Enemies.gif")
# create an enemy
def enem():
    """
    param: None
    paramType: None
    return: None
    returnType: None
    """
    enemy = turtle.Turtle()
    enemy.shape('Content/Enemies.gif')

turtle.register_shape("Enemies.gif")
# Function to create an enemy
def create_enemy():
    """
    param: None
    paramType: None
    return: None
    returnType: None
    """
    enemy = turtle.Turtle()
    enemy.shape('Enemies.gif')
    #enemy.color("red")
    enemy.speed(0)
    enemy.penup()
    enemy.goto(random.randint(-380, 380), 250)
    enemy.dy = -5
    enemies.append(enemy)

# keyboard binds
SCREEN.listen()
SCREEN.onkeypress(left, "Left")
SCREEN.onkeypress(right, "Right")
SCREEN.onkeypress(shoot, "space")

charct()

# main
def game():
    """
    param: None
    paramType: None
    return: None
    returnType: None
    """
    global score, health, Spawn, timer
    while True:
        SCREEN.update()

        # move the bullets
        for bullet in bullets:
            y = bullet.ycor()
            y += bullet.dy
            bullet.sety(y)        
        for bullet in bullets.copy():
            if bullet.ycor() > 300:
                bullets.remove(bullet)
                bullet.hideturtle()
        for enemy in enemies:
            y = enemy.ycor()
            y += enemy.dy
            enemy.sety(y)
            # check for collision between bullets and enemies
            for bullet in bullets.copy():
                for enemy in enemies.copy():
                    if enemy.distance(bullet) < 20:
                        bullets.remove(bullet)
                        bullet.hideturtle()
                        enemies.remove(enemy)
                        enemy.hideturtle()
                        Spawn -= 5
                        enem()
                        score += 10
                        ShowScore.clear()
                        ShowScore.write(f"Score: {score}", align="left",
                                        font=("Arial", 16, "normal"))

            # check if enemies pass the character
            for enemy in enemies.copy():
                if enemy.ycor() < CHARACTER.ycor():
                    health -= 10
                    ShowHealth.clear()
                    ShowHealth.write(f"Health: {health}%", align="right",
                                     font=("Arial", 16, "normal"))
                    enemies.remove(enemy)
                    enemy.hideturtle()
                    Spawn += 10

        # remove enemies that go off SCREEN
        for enemy in enemies.copy():
            if enemy.ycor() < -300:
                enemies.remove(enemy)
                enemy.hideturtle()

        # check if health reaches 0, and end the game
        if health <= 0:
            end = turtle.Turtle()
            end.speed(0)
            end.color("red")
            end.penup()
            end.hideturtle()
            end.goto(0, 0)
            end.write("GAME OVER", align="center", font=("Arial", 32, "bold"))
            subprocess.run("menu.exe")
        timer -= 1
        if timer <= 0:
            enem()
            timer = Spawn

        # Cap the minimum spawn rate
        if Spawn < 50:
            Spawn = 50
game()

SCREEN.onclick(game)

turtle.mainloop()
