# Pantalla
import turtle
wn = turtle.Screen()
wn.title ('Pong')
wn.bgcolor ('black')
wn.setup (width=800, height=600)
wn.tracer (0)


# Pala A

pala_a = turtle.Turtle ()
pala_a.speed(0)
pala_a.shape('square')
pala_a.color('white')
pala_a.shapesize(stretch_wid=5, stretch_len=1)
pala_a.penup()
pala_a.goto(-350,0)


# Pala B

pala_b = turtle.Turtle ()
pala_b.speed(0)
pala_b.shape('square')
pala_b.color('white')
pala_b.shapesize(stretch_wid=5, stretch_len=1)
pala_b.penup()
pala_b.goto(350,0)


# Bola

bola = turtle.Turtle ()
bola.speed(0)
bola.shape('square')
bola.color('white')
bola.penup()
bola.goto(0,0)
bola.dx = 0.1
bola.dy = 0.1

#Marcador
mcdr = turtle.Turtle()
mcdr.speed(0)
mcdr.color('white')
mcdr.penup()
mcdr.hideturtle()
mcdr.goto(0, 260)
mcdr.write('Jugador 1: 0 Jugador2: 0', align= 'center', font= ('Courier', 24, 'normal'))




#Puntuaciones
puntos_a = 0
puntos_b = 0

#Funciones Pala A

def pala_a_arriba():
    y = pala_a.ycor()
    y += 30
    pala_a.sety(y)
def pala_a_abajo():
    y = pala_a.ycor()
    y -= 30
    pala_a.sety(y)

# funciones pala B

def pala_b_arriba():
    y = pala_b.ycor()
    y += 30
    pala_b.sety(y)
def pala_b_abajo():
    y = pala_b.ycor()
    y -= 30
    pala_b.sety(y)


#controles pala A

wn.listen()
wn.onkeypress(pala_a_arriba, 'w')

wn.listen()
wn.onkeypress(pala_a_abajo, 's')

#controles pala B

wn.listen()
wn.onkeypress(pala_b_arriba, '8')

wn.listen()
wn.onkeypress(pala_b_abajo, '5')


#mecanica
while True:
    wn.update()

    # movimiento de la bola

    bola.setx( bola.xcor() + bola.dx )
    bola.sety( bola.ycor() + bola.dy )

    #límites

    if bola.ycor() < -290:
        bola.sety(-290)
        bola.dy *= -1

    if bola.ycor() > 290:
        bola.sety( 290 )
        bola.dy *= -1

    if bola.xcor() > 390:
        bola.goto( 0, 0 )
        bola.dx *= -1
        puntos_a += 1
        mcdr.clear()
        mcdr.write( 'Jugador A: {} Jugador B: {}'.format(puntos_a , puntos_b), align='center', font=('Courier', 24, 'normal') )

    if bola.xcor() < -390:
        bola.goto( 0, 0 )
        bola.dx *= -1
        puntos_b += 1
        mcdr.clear()
        mcdr.write( 'Jugador A: {} Jugador B: {}'.format( puntos_a, puntos_b ), align='center', font=('Courier', 24, 'normal') )




    #colisiones con las palas

    if bola.xcor() > 340  and bola.xcor() < 350 and (bola.ycor() < pala_b.ycor() + 50 and bola.ycor() > pala_b.ycor() -50) :
        bola.setx(340)
        bola.dx *= -1

    if bola.xcor() < -340  and bola.xcor() > -350 and (bola.ycor() < pala_a.ycor() + 50 and bola.ycor() > pala_a.ycor() -50) :
        bola.setx(-340)
        bola.dx *= -1

