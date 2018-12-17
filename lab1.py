#import turtle
#print("layan")


#for i in range(100):
#    print("layan")


#number1=3
#number2=number1/2
#print(number2)

##sum=0
##x=[1,2,3]
##for i in x:
##    print("i= ",i)
##    print("double i= ",i*2)
##    sum=sum+i
##print("total=",sum)

#turtle.goto(100,100)
x=0
y=0
challenge
turtle.pensize(20)
for i in range(3):
     y=y+150
     turtle.circle(100)
     turtle.penup()
     turtle.goto(x+y,0)
     turtle.pendown()
                         
turtle.penup()
turtle.goto(70,-150)
turtle.pendown()
turtle.circle(100)
###x=-150+150
turtle.goto(turtle.xcor()+150,70)
turtle.circle(100)


turtle.mainloop()