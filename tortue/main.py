import turtle

def carre(taille):
    for i in range(0, 4):
        t.forward(taille)
        t.left(90)

def carres(taille_depart, nb):
    for i in range(0, nb):
        carre((i + 1) * taille_depart)

def escalier(taille, nb):
    for i in range(0, nb):
        t.forward(taille)
        t.left(90)
        t.forward(taille)
        t.right(90)

    t.forward(taille)

t = turtle.Turtle()

carres(10, 10)

turtle.done()