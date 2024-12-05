import turtle

initial_angle = 45
angle_step = 135
num_lines = 8
lenght = 400
animation_speed = 10

turtle.hideturtle()
turtle.speed(animation_speed)
turtle.left(initial_angle)

for count in range(num_lines):
    turtle.forward(lenght)
    turtle.left(angle_step)

turtle.done