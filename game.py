import turtle


window = turtle.Screen() # initialize Screen
window.title("Hammam Ping Pong") # Title of the window
window.bgcolor("black") # set background color of the window
window.setup(width=800, height=600) # set width and height
window.tracer(0) # stops the window from updating automatically


#m1
m1 = turtle.Turtle() # initialize turtle object
m1.speed(0) # set the speed of the animation
m1.shape("square") # shape of the object
m1.color("blue") # color of the object
m1.shapesize(stretch_len=1,stretch_wid=5) # stretches the shape to meet the size
m1.penup() # stop the object from drawing lines
m1.goto(-350,0) # set the position of the object
#m2
m2= turtle.Turtle()
m2.speed(0)
m2.shape("square")
m2.color("yellow")
m2.shapesize(stretch_len=1,stretch_wid=5)
m2.penup()
m2.goto(350,0)

#ball
ball= turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = .5
ball.dy = .5

# score
score1 = 0
score2 = 0
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0,250)
score.write(f"Player 1: {score1} player 2:{score2}", align="center", font=("Courier", 24,"normal") )
    
    

#====================================
# Functions to move our game
def madrab1_up():
    y = m1.ycor() # get the y coordinate of the m1
    y += 30 # increment y by 20 
    m1.sety(y) # set the y of the m1 to y coordinate
def madrab1_down():
    y = m1.ycor()
    y -= 30
    m1.sety(y)

def madrab2_up():
    y = m2.ycor()
    y += 20
    m2.sety(y)
def madrab2_down():
    y = m2.ycor()
    y -= 20
    m2.sety(y)


#keyboard bindings 
window.listen()
window.onkeypress(madrab1_up, "w")
window.onkeypress(madrab1_down, "s")
window.onkeypress(madrab2_up, "Up")
window.onkeypress(madrab2_down, "Down")
    




# main game loop
while True:
    window.update() # Update the screen everytime the game run
    
    #move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border check
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        
        
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
     
     
        
    if ball.xcor() >390:
        ball.goto(0,0)
        ball.dx *= -1
        score1 += 1
        score.clear()
        score.write(f"Player 1: {score1} player 2:{score2}", align="center", font=("Courier", 24,"normal") )
        
    if ball.xcor() <-390:
        ball.goto(0,0)
        ball.dx *= -1
        score2 += 1
        score.clear()
        score.write(f"Player 1: {score1} player 2:{score2}", align="center", font=("Courier", 24,"normal") )
        
        
    # Tasadom madrab and ball
    if (ball.xcor() > 340 and ball.xcor()< 350) and (ball.ycor()< m2.ycor()+ 40 and ball.ycor()> m2.ycor() -40):
        ball.setx(340)
        ball.dx *=-1
        
    if (ball.xcor() <- 340 and ball.xcor() >- 350) and (ball.ycor()< m1.ycor()+ 40 and ball.ycor()> m1.ycor() -40):
        ball.setx(-340)
        ball.dx *=-1
        
        
    
    