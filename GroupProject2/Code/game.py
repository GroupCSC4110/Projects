import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.title("Space Invaders")
screen.bgpic('Background.gif')
screen.setup(width=800, height=600)

# Title
title = turtle.Turtle()
title.speed(0)
title.color("white")
title.penup()
title.hideturtle()
title.goto(0, 240)
title.write("SPACE INVADERS", align="center", font=("Arial", 32, "bold"))

# Start button
start_button = turtle.Turtle()
start_button.speed(0)
start_button.color("green")
start_button.penup()
start_button.hideturtle()
start_button.goto(0, -50)
start_button.write("START", align="center", font=("Arial", 24, "bold"))


character = None  


bullets = []


enemies = []

# Enemy spawn rate
enemy_spawn_rate = 200  
enemy_spawn_timer = enemy_spawn_rate


score = 0
health = 100

# Score display
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(-380, 260)
score_display.write(f"Score: {score}", align="left", font=("Arial", 16, "normal"))

# Health bar display
health_display = turtle.Turtle()
health_display.speed(0)
health_display.color("red")
health_display.penup()
health_display.hideturtle()
health_display.goto(380, 260)
health_display.write(f"Health: {health}%", align="right", font=("Arial", 16, "normal"))

turtle.register_shape("D:\OneDrive\Fall 2023\Software Engineering\TetrisTryout\Character.gif")
# Function to create the character
def create_character():
    global character
    character = turtle.Turtle()
    character.shape('D:\OneDrive\Fall 2023\Software Engineering\TetrisTryout\Character.gif')
    character.speed(0)
    character.penup()
    character.goto(0, -250)
    #character.shapesize(stretch_wid=1, stretch_len=2) 
    character.dx = 20  

# Move the character to the left
def move_left():
    x = character.xcor()
    x -= character.dx
    if x < -380:  
        x = -380
    character.setx(x)

# Move the character to the right
def move_right():
    x = character.xcor()
    x += character.dx
    if x > 380:  
        x = 380
    character.setx(x)

# Function to shoot a bullet
def shoot_bullet():
    bullet = turtle.Turtle()
    bullet.shape("triangle")
    bullet.color("yellow")
    bullet.speed(0)
    bullet.penup()
    bullet.shapesize(stretch_wid=0.5, stretch_len=0.1)
    bullet.goto(character.xcor(), character.ycor() + 10)  
    bullet.dy = 30  
    bullets.append(bullet)

turtle.register_shape("D:\OneDrive\Fall 2023\Software Engineering\TetrisTryout\Enemies.gif")
# Function to create an enemy
def create_enemy():
    enemy = turtle.Turtle()
    enemy.shape('D:\OneDrive\Fall 2023\Software Engineering\TetrisTryout\Enemies.gif')
    #enemy.color("red")
    enemy.speed(0)
    enemy.penup()
    enemy.goto(random.randint(-380, 380), 250)  
    enemy.dy = -5  
    enemies.append(enemy)

# Keyboard binds
screen.listen()
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")
screen.onkeypress(shoot_bullet, "space")


create_character()

# Main game loop
def play_game():
    global score, health, enemy_spawn_rate, enemy_spawn_timer
    while True:
        screen.update()

        # Move the bullets
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

            # Check for collision between bullets and enemies
            for bullet in bullets.copy():
                for enemy in enemies.copy():
                    if enemy.distance(bullet) < 20:  
                        bullets.remove(bullet)
                        bullet.hideturtle()
                        enemies.remove(enemy)
                        enemy.hideturtle()
                        enemy_spawn_rate -= 5  
                        create_enemy()  
                        score += 10  
                        score_display.clear()  
                        score_display.write(f"Score: {score}", align="left", font=("Arial", 16, "normal"))

            # Check if enemies pass the character
            for enemy in enemies.copy():
                if enemy.ycor() < character.ycor():
                    health -= 10
                    health_display.clear()
                    health_display.write(f"Health: {health}%", align="right", font=("Arial", 16, "normal"))
                    enemies.remove(enemy)
                    enemy.hideturtle()
                    enemy_spawn_rate += 10  

        # Remove enemies that go off-screen
        for enemy in enemies.copy():
            if enemy.ycor() < -300:
                enemies.remove(enemy)
                enemy.hideturtle()

        # Check if health reaches 0
        if health <= 0:
            
            game_over_display = turtle.Turtle()
            game_over_display.speed(0)
            game_over_display.color("red")
            game_over_display.penup()
            game_over_display.hideturtle()
            game_over_display.goto(0, 0)
            game_over_display.write("GAME OVER", align="center", font=("Arial", 32, "bold"))
            break 

        
        enemy_spawn_timer -= 1

        # Create a new enemy when the timer reaches 0 and reset the timer
        if enemy_spawn_timer <= 0:
            create_enemy()
            enemy_spawn_timer = enemy_spawn_rate

        # Cap the minimum spawn rate
        if enemy_spawn_rate < 50:
            enemy_spawn_rate = 50

# Set up the start button click
def start_game(x, y):
    # Clear the start button
    start_button.clear()
    start_button.hideturtle()

   
    play_game()


screen.onclick(start_game)


turtle.mainloop()

