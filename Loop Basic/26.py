import turtle

height = 5
width = 5

turtle.shape("turtle")
turtle.color("blue")
turtle.speed(5)
turtle.penup()

for y in range(height):
    for x in range(width):
        turtle.dot()
        turtle.forward(20)
    turtle.backward(20 * width)
    turtle.right(90)
    turtle.forward(20)
    turtle.left(90)

turtle.exitonclick()