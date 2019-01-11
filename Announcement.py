
import turtle

wn = turtle.Screen()

graveyard_1 = turtle.Turtle()
graveyard_2 = turtle.Turtle()

graveyard_1.penup()
graveyard_2.penup()

graveyard_1.setpos(-375, 200)
graveyard_2.setpos(375, 200)

graveyard_1.write('Player 1 Graveyard', align="center", font=("Arial", 20, "bold"))
graveyard_2.write('Player 2 Graveyard', align="center", font=("Arial", 20, "bold"))

wn.mainloop()