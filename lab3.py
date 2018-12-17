import turtle

turtle.forward(150)
turtle.right(144)
turtle.forward(150)
turtle.right(144)
turtle.forward(150)
turtle.right(144)
turtle.forward(150)
turtle.right(144)
turtle.forward(150)



##turtle.register_shape("2.gif")
##turtle.shape("2.gif")

turtle.speed(0)
colors=["black","blue","purple","pink","red"]
for i in range(500):
    turtle.pencolor(colors[i%5])
    turtle.forward(200)
    turtle.right(40)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(50)
    turtle.home()
    turtle.right(i)


turtle.mainloop()
