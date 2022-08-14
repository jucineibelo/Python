desenho = str(input("Qual figura você deseja desenhar? "
                    "\n C para circulo "
                    "\n Q para Quadrado "
                    "\n escolha:  "))
import turtle
if desenho == "C":
    turtle.shape("turtle")
    turtle.fillcolor("orange")
    turtle.begin_fill()
    turtle.color("yellow")
    turtle.pencolor("red")
    turtle.fillcolor("orange")
    turtle.pensize(3)
    turtle.circle(80)
    turtle.end_fill()
    turtle.done()
elif desenho == "Q":
    turtle.shape("turtle")
    turtle.fillcolor('yellow')
    turtle.pensize(3)
    turtle.begin_fill()
    turtle.pencolor("blue")
    turtle.forward(120)
    turtle.left(90)
    turtle.forward(120)
    turtle.left(90)
    turtle.forward(120)
    turtle.left(90)
    turtle.forward(120)
    turtle.left(180)
    turtle.forward(120)
    turtle.end_fill()
    turtle.done()



