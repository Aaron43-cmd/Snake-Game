
import turtle
import time
import random

# Pengaturan layar
layar = turtle.Screen()
layar.title("Snake Game")
layar.bgcolor("black")
layar.setup(width=600, height=600)
layar.tracer(0)

# Kepala ular
kepala = turtle.Turtle()
kepala.shape("square")
kepala.color("green")
kepala.penup()
kepala.goto(0, 0)
kepala.direction = "stop"

# Makanan
makanan = turtle.Turtle()
makanan.shape("circle")
makanan.color("red")
makanan.penup()
makanan.goto(100, 100)

tubuh = []

# Skor
skor = 0
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0", align="center", font=("Arial", 18, "normal"))

# Kontrol
def atas():
    if kepala.direction != "down":
        kepala.direction = "up"

def bawah():
    if kepala.direction != "up":
        kepala.direction = "down"

def kiri():
    if kepala.direction != "right":
        kepala.direction = "left"

def kanan():
    if kepala.direction != "left":
        kepala.direction = "right"

def bergerak():
    if kepala.direction == "up":
        kepala.sety(kepala.ycor() + 20)
    elif kepala.direction == "down":
        kepala.sety(kepala.ycor() - 20)
    elif kepala.direction == "left":
        kepala.setx(kepala.xcor() - 20)
    elif kepala.direction == "right":
        kepala.setx(kepala.xcor() + 20)

layar.listen()
layar.onkeypress(atas, "Up")
layar.onkeypress(bawah, "Down")
layar.onkeypress(kiri, "Left")
layar.onkeypress(kanan, "Right")

# Game loop
game_over = False

while not game_over:
    layar.update()

    # Tabrak dinding
    if abs(kepala.xcor()) > 280 or abs(kepala.ycor()) > 280:
        game_over = True
        break

    # Gerakkan tubuh
    for i in range(len(tubuh) - 1, 0, -1):
        tubuh[i].goto(
            tubuh[i - 1].xcor(),
            tubuh[i - 1].ycor()
        )

    if len(tubuh) > 0:
        tubuh[0].goto(kepala.xcor(), kepala.ycor())

    bergerak()

    # Makan makanan
    if kepala.distance(makanan) < 20:
        x = random.randint(-13, 13) * 20
        y = random.randint(-13, 12) * 20
        makanan.goto(x, y)

        bagian = turtle.Turtle()
        bagian.shape("square")
        bagian.color("lightgreen")
        bagian.penup()
        tubuh.append(bagian)

        skor += 10
        pen.clear()
        pen.write(
            f"Score: {skor}",
            align="center",
            font=("Arial", 18, "normal")
        )

    # Tabrak tubuh sendiri
    for bagian in tubuh:
        if bagian.distance(kepala) < 20:
            game_over = True
            break

    time.sleep(0.1)

# Game Over
pen.goto(0, 0)
pen.write(
    "GAME OVER",
    align="center",
    font=("Arial", 30, "bold")
)

layar.update()
layar.mainloop()
