#Original code by: https://repl.it/@nothplus

import turtle
Mohanad = turtle.Turtle()

Mohanad.speed(10)

colors = [
  "Red",
  "Orange",
  "Yellow",
  "Green",
  "Blue",
  "Purple"
]

colorIndex = -1

for i in range(100):
    colorIndex += 1
    if colorIndex == 6:
      colorIndex=-1
    else:
      Mohanad.color(colors[colorIndex])
      Mohanad.forward(180)
      Mohanad.left(70)
      Mohanad.forward(60)
      Mohanad.right(40)

      Mohanad.penup()
      Mohanad.setposition(0, 0)
      Mohanad.pendown()

      Mohanad.right(2)

turtle.done()
