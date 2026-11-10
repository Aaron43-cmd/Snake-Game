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

# Tubuh ular
tubuh = []

# Fungsi gerakan
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

    if kepala.direction == "down":
        kepala.sety(kepala.ycor() - 20)

    if kepala.direction == "left":
        kepala.setx(kepala.xcor() - 20)

    if kepala.direction == "right":
        kepala.setx(kepala.xcor() + 20)


# Kontrol keyboard
layar.listen()
layar.onkeypress(atas, "Up")
layar.onkeypress(bawah, "Down")
layar.onkeypress(kiri, "Left")
layar.onkeypress(kanan, "Right")

# Game loop
while True:
    layar.update()

    # Tabrak dinding
    if kepala.xcor() > 290 or kepala.xcor() < -290:
        break

    if kepala.ycor() > 290 or kepala.ycor() < -290:
        break

    # Jika makan makanan
    if kepala.distance(makanan) < 20:
        x = random.randint(-14, 14) * 20
        y = random.randint(-14, 14) * 20
        makanan.goto(x, y)

        bagian = turtle.Turtle()
        bagian.shape("square")
        bagian.color("lightgreen")
        bagian.penup()
        tubuh.append(bagian)

    # Gerakkan tubuh dari belakang
    for i in range(len(tubuh) - 1, 0, -1):
        tubuh[i].goto(tubuh[i - 1].xcor(), tubuh[i - 1].ycor())

    if len(tubuh) > 0:
        tubuh[0].goto(kepala.xcor(), kepala.ycor())

    bergerak()

    # Tabrak tubuh sendiri
    for bagian in tubuh:
        if bagian.distance(kepala) < 20:
            break

    time.sleep(0.1)

layar.bye()
