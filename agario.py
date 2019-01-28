import turtle
import time
import random
import math
from ball import Ball

turtle.colormode(1.0)

turtle.tracer(0)
turtle.hideturtle()
running=True
screen_width=turtle.getcanvas().winfo_width()/2
screen_height=turtle.getcanvas().winfo_height()/2

my_ball=Ball(100,50,2,2,50,"blue")
number_of_balls=5
minimum_ball_radius=10
maximum_ball_radius=100
minimum_ball_dx=-2
maximum_ball_dx=2
minimum_ball_dy=-2
maximum_ball_dy=2


BALLS=[my_ball]

for i in range(number_of_balls):
    x=random.randint(-screen_width + maximum_ball_radius,screen_width - maximum_ball_radius)
    y=random.randint(-screen_height + maximum_ball_radius,screen_height - maximum_ball_radius)
    dx=random.randint(minimum_ball_dx,maximum_ball_dx)
    dy=random.randint(minimum_ball_dy,maximum_ball_dy)
    radius=random.randint(minimum_ball_radius,maximum_ball_radius)
    color=(random.random(), random.random(), random.random()) 
    ball1=Ball(x,y,dx,dy,radius,color)
    BALLS.append(ball1)

def move_all_balls():
    for j in BALLS:
        j.move(screen_width,screen_height)


def collide(ball_a,ball_b):
    if (ball_a==ball_b):
        return False
    distance=math.sqrt(math.pow(ball_b.xcor()-ball_a.xcor(),2)+math.pow(ball_b.ycor()-ball_a.ycor(),2))
    if (distance<=ball_a.r+ball_b.r):
        return True
    else:
        return False
def check_all_balls_collisions():
    global running
    global score1
    score1 = 0
    all_balls=[]
    all_balls.append(my_ball)
    for ball in BALLS:
        all_balls.append(ball)
    for ball_a in BALLS:
        for ball_b in BALLS:
            if (collide(ball_a,ball_b)):
                r1=ball_a.r
                r2=ball_b.r
                x=random.randint(-screen_width + maximum_ball_radius,screen_width - maximum_ball_radius)
                y=random.randint(-screen_height + maximum_ball_radius,screen_height - maximum_ball_radius)
                dx=random.randint(minimum_ball_dx,maximum_ball_dx)
                dy=random.randint(minimum_ball_dy,maximum_ball_dy)
                radius=random.randint(minimum_ball_radius,maximum_ball_radius)
                color=(random.random(), random.random(), random.random())
                while(dx==0):
                     dx=random.randint(minimum_ball_dx,maximum_ball_dx)

                while(dy==0):
                    dy=random.randint(minimum_ball_dy,maximum_ball_dy)
##                ball3=Ball(x,y,dx,dy,radius,color)
##                while collide(ball3,my_ball):
##                    x=random.randint(-screen_width + maximum_ball_radius,screen_width - maximum_ball_radius)
##                    y=random.randint(-screen_height + maximum_ball_radius,screen_height - maximum_ball_radius)
##                    dx=random.randint(minimum_ball_dx,maximum_ball_dx)
##                    dy=random.randint(minimum_ball_dy,maximum_ball_dy)
##                    radius=random.randint(minimum_ball_radius,maximum_ball_radius)
##                    color=(random.random(), random.random(), random.random())
##                    while(dx==0):
##                         dx=random.randint(minimum_ball_dx,maximum_ball_dx)
##
##                    while(dy==0):
##                        dy=random.randint(minimum_ball_dy,maximum_ball_dy)
##                    ball3=Ball(x,y,dx,dy,radius,color)
##                ball3.hideturtle()

                if (r1>r2):
                    ball_b.new_ball(x,y,dx,dy,radius,color)
                    ball_a.r=ball_a.r+4
                    ball_a.shapesize(ball_a.r/10)
                    if (ball_b==my_ball):
                        print("my ball eaten")
                        running=False
                       
                   
                else:
                    ball_a.new_ball(x,y,dx,dy,radius,color)
                    ball_b.r=ball_b.r+4
                    ball_b.shapesize(ball_b.r/10)
                    if (ball_a==my_ball):
                        print("my ball eaten")
                        running=False
                        
                  

    
                

def movearound():
    my_ball.goto(turtle.getcanvas().winfo_pointerx() - screen_width*2,1.4*screen_height - turtle.getcanvas().winfo_pointery())
                    

                 
while(running==True):
    c=0  
    screen_width=turtle.getcanvas().winfo_width()/2
    screen_height=turtle.getcanvas().winfo_height()/2
    movearound()
    move_all_balls()
    check_all_balls_collisions()
    turtle.update()
    time.sleep(.1)
    if my_ball.r >= screen_height:
        running=False
        
        
    for i in BALLS:
        if my_ball.r<=i.r:
            c=c+1
    print(c)
    print(len(BALLS))
    if len(BALLS)==c:
        print("making smaller ball")
        x=random.randint(-screen_width + maximum_ball_radius,screen_width - maximum_ball_radius)
        y=random.randint(-screen_height + maximum_ball_radius,screen_height - maximum_ball_radius)
        dx=random.randint(minimum_ball_dx,maximum_ball_dx)
        dy=random.randint(minimum_ball_dy,maximum_ball_dy)
        radius=random.randint(minimum_ball_radius,my_ball.r)
        color=(random.random(), random.random(), random.random())
        ball2=Ball(x,y,dx,dy,radius,color)
        BALLS.append(ball2)
        ball2.move(screen_width,screen_height)
        
        
        
        

turtle.mainloop()
    
    
    
                
                
                
                
        


        
    
