import turtle

# Configuração da caneta
flor=turtle.Turtle()
flor.color("red")
flor.pensize(3)
flor.speed(0)
#pen = turtle.Turtle()
# pen.speed(0)
# pen.color("green")

#lista de cores
cores = ["red", "orange", "yellow", "green", "blue", "purple"]

# Configuração da tela
tela = turtle.Screen()
tela.bgcolor("black")
tela.title("Flor Colorida")

# Função para desenhar uma flor
def draw_flower():
    for i in range(360):
        flor.color(cores[i % len(cores)])  # Muda a cor da caneta ciclicamente
        flor.circle(100)
        flor.left(60)

# Desenha a flor
draw_flower()

# Mantém a tela aberta
flor.hideturtle()
tela.exitonclick()