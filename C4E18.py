import turtle


animation_speed = 10
num_lines = 50
starting_lenght = 1
ending_lenght = 500
step = 10
angle = 90



turtle.hideturtle()
turtle.speed(animation_speed)

for lenght in range(starting_lenght, ending_lenght, step):
    turtle.forward(lenght)
    turtle.left(angle)

turtle.done