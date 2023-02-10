import turtle

wn = turtle.Screen()
wn.title("Pong by @Tai") # tytuł
wn.bgcolor("black") # kolor background'u
wn.setup(width=800, height=600) # rozmiar okienka
wn.tracer(0)

# Rakietka A
paddle_a =turtle.Turtle()
paddle_a.speed(0) # prędkość animacji
paddle_a.shape("square") # forma rakietki
paddle_a.color("white") # kolor rakietki
paddle_a.shapesize(stretch_wid=5, stretch_len=1) # długość i szerokość rakietki
paddle_a.penup()
paddle_a.goto(-350, 0) #ustawienie rakietki na start

#Rakietka B
paddle_b =turtle.Turtle()
paddle_b.speed(0) # prędkość animacji
paddle_b.shape("square") # forma rakietki
paddle_b.color("white") # kolor rakietki
paddle_b.shapesize(stretch_wid=5, stretch_len=1) # długość i szerokość rakietki
paddle_b.penup()
paddle_b.goto(350, 0) #ustawienie rakietki na start

#Piłka
ball =turtle.Turtle()
ball.speed(0) # prędkość animacji
ball.shape("square") # forma piłki
ball.color("white") # kolor piłki
ball.penup()
ball.goto(0, 0) #ustawienie piłki na start
ball.dx = 1
ball.dy = 1

#Pen
pen = turtle.Trutle()
pen.speed(0)
pen.color("white")
pen.up()
pen.hidetrutle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align= "center")


# Funkcje
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")


# Main game loop
while True:
    wn.update()
    
    # porusznie się piłki
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Sprawdzanie granicy
    if ball.ycor() > 290: # jeżeli piłki trafi na granic 290 (górny krawężnik)
        ball.sety(290)
        ball.dy *= -1     # to piłka odleci w odwróconą stronę

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    
    if ball.xcor() > 390: #jeżeli piłka trafi na granice 390 (prawy krawężnik)
        ball.goto(0, 0)
        ball.dx *= -1     #to piłka wróci z powrotem na miejsce

    if ball.xcor() < -390: 
        ball.goto(0, 0)
        ball.dx *= -1

    #odbicie piłki od paletki
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1