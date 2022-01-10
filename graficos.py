#graficos.py

import turtle

turtle.bgcolor('black')

p = turtle.Pen()

        #   0      1        2         3       4         5
cores = ['red', 'yellow', 'blue', 'green', 'orange', 'purple']

for x in range(100):
    indice = x % 6  #0..5
    cor = cores[indice]
    p.pencolor(cor)
    p.circle(x * 5)
    p.left(60)
    p.width(x / 10)

