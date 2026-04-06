import turtle
import random   

tela = turtle.Screen()
tela.title("Corrida das tartarugas.")
tela.bgcolor("gray")

#Cores da tartarugas
cores = ["red","blue","green","orange","purple","brown"]
tartarugas = []

#Criar e posicionar cada tartaruga:
y_inicial = -120
for cor in cores:
    t = turtle.Turtle(shape="turtle")
    t.color(cor)
    t.penup
    t.goto(-200, y_inicial)
    y_inicial += 50
    tartarugas.append(t)

#corrida
chegada = 200
while True:
    for t in tartarugas:
        t.forward(random.randint(1,20))
        if t.xcor() >= chegada:
            print(f"A tartaruga {t.pencolor()} venceu!")
            tela.mainloop()
            exit()