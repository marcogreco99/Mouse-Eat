
def dentrofinestra():
    a = topo.xcor()
    o = topo.ycor()
    return -274<a<274 and -274<o<274

def you_win():
    w = turtle.Turtle()
    w.hideturtle()
    w.penup()
    turtle.tracer(0)
    w.setposition(-50, 310)
    w.color("Green")
    w.write("YOU WIN", font = 50)
    turtle.tracer(1)

def you_lose():
    turtle.tracer(0)
    lose = turtle.Turtle()
    lose.up()
    img9='gameover.gif'
    wn.addshape(img9)
    lose.shape(img9)
    lose.setposition(0, 310)
    turtle.tracer(1)
    
def randomposition(h):
    turtle.tracer(0)
    x = random.randrange(-280, 281)
    y = random.randrange(-280, 281)
    h.setposition(x, y)
    turtle.tracer(1)

def sopra():
    topo.setheading(90)
    topo.heading()
    wn.listen()
def giu():
    topo.setheading(270)
    topo.heading()
    wn.listen()
def destra():
    topo.setheading(0)
    topo.heading()
    wn.listen()
def sinistra():
    topo.setheading(180)
    topo.heading()
    wn.listen()

def nuovatrappola(trappole):
    k = turtle.Turtle()
    k.shape(image3)
    k.up()
    randomposition(k)
    trappole.append(k)
    
    
#######################################################################
import turtle
import random
import winsound


#Schermata iniziale
turtle.setup(700, 700)
wn = turtle.Screen()
wn.title(" Mouse Eat ")
lol=turtle.Turtle()
pavimento = 'pavimento.gif'
wn.addshape(pavimento)
lol.shape(pavimento)

turtle.tracer(0)

text = turtle.Turtle()
diffishape = 'difficolta.gif'
wn.addshape(diffishape)
text.shape(diffishape)
text.penup()
text.setposition(0, 180)


facile = turtle.Turtle()
facile.setposition(0, 0)
facshape = 'faciles.gif'
wn.addshape(facshape)
facile.shape(facshape)


medio = turtle.Turtle()
medshape = 'medios.gif'
wn.addshape(medshape)
medio.shape(medshape)
medio.up()
medio.setposition(0, -100)


difficile = turtle.Turtle()
difshape = 'difficiles.gif'
wn.addshape(difshape)
difficile.shape(difshape)
difficile.up()
difficile.setposition(0, -200)


turtle.tracer(1)

#Scelta difficoltà
winsound.PlaySound("iniziale.wav", winsound.SND_LOOP|winsound.SND_ASYNC)
scelta=turtle.Turtle()
scelta.up()
scelta.hideturtle()
turtle.tracer(0)
scelta.goto(-355,-50)
wn.onclick(scelta.goto)
turtle.tracer(1)


difficult= 0

while difficult==0:
    scelta.forward(1)
    scelta.backward(1)
    scelta_x=scelta.xcor()
    scelta_y=scelta.ycor()
    #print(scelta_x,scelta_y) per capire gli intervalli delle coordinate
    if -148<scelta_x<144 and -30<scelta_y<31:
        difficult =2
    if -148<scelta_x<144 and -132<scelta_y<-69:
        difficult =5
    if -148<scelta_x<144 and -232<scelta_y<-168:
        difficult =8


if difficult!=0:
    winsound.PlaySound("select.wav", winsound.SND_ASYNC)
    facile.hideturtle()
    medio.hideturtle()
    difficile.hideturtle()
    text.hideturtle()

    #Bordo
    
    bordo = turtle.Turtle()
    bordo.hideturtle()
    bordo.color("pink")
    turtle.tracer(0)
    bordo.penup()
    bordo.setposition(-300, -300)
    bordo.pendown()

    #bordo.begin_fill()
    for i in range(4):
        bordo.forward(600)
        bordo.left(90)
    turtle.tracer(1)
    #bordo.end_fill()

    #topo

    image = "topo.gif"
    wn.addshape(image)
    topo = turtle.Turtle()
    topo.shape(image)
    topo.penup()

    #Trappole

    trappole = []
    image3="trappola.gif"
    wn.addshape(image3)

    #Punteggio

    SCORE = 0
    s = turtle.Turtle()
    s.hideturtle()
    s.penup()
    turtle.tracer(0)
    s.setposition(-280, 310)
    s.color("White")
    s.write("Punteggio = " + str(SCORE), font = 50)
    turtle.tracer(1)

    #Formaggio

    image2 = "cheese.gif"
    wn.addshape(image2)
    cheese = turtle.Turtle()
    cheese.shape(image2)
    cheese.penup()
    randomposition(cheese)

    #Vite

    vita = turtle.Turtle()
    vita.up()
    image4 = "cuore.gif"
    wn.addshape(image4)
    vita.shape(image4)
    turtle.tracer(0)
    vita.setposition(200, 315)
    turtle.tracer(1)

    vita2 = turtle.Turtle()
    vita2.up()
    vita2.shape(image4)
    turtle.tracer(0)
    vita2.setposition(230, 315)
    turtle.tracer(1)

    vita3 = turtle.Turtle()
    vita3.up()
    vita3.shape(image4)
    turtle.tracer(0)
    vita3.setposition(260, 315)
    turtle.tracer(1)

    vite=3
    lifes=0
    newlife=[]

    #Programma

    wn.listen()
    while dentrofinestra()==True:
        wn.onkey(sopra,"Up")
        wn.onkey(giu,"Down")
        wn.onkey(destra,"Right")
        wn.onkey(sinistra,"Left")
        topo.forward(difficult)
        
        

        if topo.distance(cheese)<35:
            winsound.PlaySound("preso.wav", winsound.SND_ASYNC)
            
            randomposition(cheese)
            nuovatrappola(trappole)
            s.clear()
            SCORE +=1
            s.write("Punteggio = " + str(SCORE), font = 50)
        
        for i in trappole:
            if topo.distance(i)<32:
                winsound.PlaySound("incorrect.wav", winsound.SND_ASYNC)
                vita.hideturtle()
                trappole.remove(i)
                vite -=1
                i.hideturtle()
        if vite == 1:
            vita2.hideturtle()
        elif vite == 0 :
            vita3.hideturtle()

    #VITA AGGIUNTIVA

        if SCORE%10==0 and SCORE!=0:
            while lifes == 0:
                life = turtle.Turtle()
                image5 = "life.gif"
                wn.addshape(image5)
                life.shape(image5)
                life.up()
                randomposition(life)
                lifes+=1
                newlife.append(life)
                break

        if SCORE == 11 or SCORE == 21 or SCORE == 31 or SCORE == 41:
            lifes=0

        for k in newlife:
            if topo.distance(k)<25 and vite != 3:
                winsound.PlaySound("newlife.wav", winsound.SND_ASYNC)
                k.hideturtle()
                newlife.remove(k)
                if vite == 2:
                    vita.showturtle()
                    vite+=1
                elif vite == 1:
                    vita2.showturtle()
                    vite+=1

        if vite==0:
            you_lose()
            winsound.PlaySound("lose.wav", winsound.SND_ASYNC)
            break
            
        elif SCORE == 50:
            you_win()
            winsound.PlaySound("success.wav", winsound.SND_ASYNC)
            break
        
    if dentrofinestra()==False:
        you_lose()
        winsound.PlaySound("lose.wav", winsound.SND_ASYNC)
        vita.hideturtle()
        vita2.hideturtle()
        vita3.hideturtle()

    #Quanto hai totalizzato ?
    s.clear()
    x = turtle.Turtle()
    x.hideturtle()
    x.penup()
    turtle.tracer(0)
    x.setposition(-180, 30)
    x.color("Yellow")

    casella = turtle.Turtle()
    casella.hideturtle()
    casella.up()
    casella.setposition(-205, 85)
    casella.color("blue")

    casella.begin_fill()
    casella.forward(410)
    casella.right(90)
    casella.forward(80)
    casella.right(90)
    casella.forward(410)
    casella.right(90)
    casella.forward(80)
    turtle.tracer(1)
    casella.end_fill()

    if SCORE == 1:
        x.write("HAI TOTALIZZATO " + str(1) + " PUNTO !!", font = ("Comic Sans MS",18))
    else:
        x.write("HAI TOTALIZZATO " + str(SCORE) + " PUNTI !!", font = ("Comic Sans MS",18))
    turtle.tracer(1)

wn.listen()
wn.mainloop()
wn.exitonclick()
