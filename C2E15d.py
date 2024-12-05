import turtle

RADIUS = 100
STARTING_X = -250
STARTING_Y = 0
H_SHIFT = 125
V_SHIFT = 100


x = STARTING_X
y = STARTING_X
turtle.penup()
turtle.goto(x, y)
turtle.pendown()
turtle.circle(RADIUS)


x = x + H_SHIFT
y = y - V_SHIFT
turtle.penup()
turtle.goto(x, y)
turtle.pendown()
turtle.circle(RADIUS)


x = x + H_SHIFT
y = y + V_SHIFT
turtle.penup()
turtle.goto(x, y)
turtle.pendown()
turtle.circle(RADIUS)


x = x + H_SHIFT
y = y - V_SHIFT
turtle.penup()
turtle.goto(x, y)
turtle.pendown()
turtle.circle(RADIUS)