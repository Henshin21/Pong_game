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


# Funkcje
def paddle_a_up():
    y = paddle_a.ycor

# Main game loop
while True:
    wn.update()
