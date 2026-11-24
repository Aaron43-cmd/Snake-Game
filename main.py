
import turtle
import random

# Pengaturan layar
screen = turtle.Screen()
screen.title("Snake Nokia Classic")
screen.bgcolor("#9bbc0f")
screen.setup(600, 600)
screen.tracer(0)

# Kepala ular
head = turtle.Turtle()
head.shape("square")
head.color("#253406")
head.penup()
head.goto(0, 0)

# Makanan
food = turtle.Turtle()
food.shape("square")
food.color("#253406")
food.penup()

# Tulisan skor
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.color("#253406")
pen.goto(0, 260)

# Data game
snake = [(0, 0)]
segments = []
direction = "stop"
score = 0
game_over = False

def update_score():
    pen.clear()
    pen.write(
        "SCORE: " + str(score),
        align="center",
        font=("Arial", 16, "bold")
    )

def spawn_food():
    while True:
        x = random.randint(-14, 14) * 20
        y = random.randint(-14, 11) * 20

        if (x, y) not in snake:
            food.goto(x, y)
            break

def up():
    global direction
    if direction != "down":
        direction = "up"

def down():
    global direction
    if direction != "up":
        direction = "down"

def left():
    global direction
    if direction != "right":
        direction = "left"

def right():
    global direction
    if direction != "left":
        direction = "right"

def game_loop():
    global snake, score, game_over

    if game_over:
        return

    if direction != "stop":
        x, y = snake[0]

        if direction == "up":
            y += 20
        elif direction == "down":
            y -= 20
        elif direction == "left":
            x -= 20
        elif direction == "right":
            x += 20

        new_head = (x, y)
        eating = head.distance(food) < 1

        # Tabrak dinding
        if abs(x) > 280 or abs(y) > 280:
            end_game()
            return

        # Tabrak tubuh
        check_body = snake if eating else snake[:-1]

        if new_head in check_body:
            end_game()
            return

        snake.insert(0, new_head)

        if not eating:
            snake.pop()
        else:
            score += 10
            update_score()
            spawn_food()

        # Tambah segmen jika diperlukan
        while len(segments) < len(snake) - 1:
            part = turtle.Turtle()
            part.shape("square")
            part.color("#253406")
            part.penup()
            segments.append(part)

        # Gambar ular
        head.goto(snake[0])

        for i, part in enumerate(segments):
            part.goto(snake[i + 1])

    screen.update()

    # Timer, bukan loop berat
    screen.ontimer(game_loop, 120)

def end_game():
    global game_over
    game_over = True

    pen.goto(0, 0)
    pen.write(
        "GAME OVER\nSCORE: " + str(score),
        align="center",
        font=("Arial", 22, "bold")
    )

# Kontrol keyboard
screen.listen()
screen.onkeypress(up, "Up")
screen.onkeypress(down, "Down")
screen.onkeypress(left, "Left")
screen.onkeypress(right, "Right")

# Mulai permainan
spawn_food()
update_score()
game_loop()

screen.mainloop()
