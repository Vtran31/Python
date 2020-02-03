import turtle
import time

#player score
score_a = 0
score_b = 0

#create screen 
wm = turtle.Screen()
wm.title("Pong game bt Vinh Tran")
wm.bgcolor("black")
wm.setup(width= 800, height= 600 )
wm.tracer(0)

#Padle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-375,0)
print(paddle_a.ycor())

#Pable B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(375,0)

#create ball 
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("yellow")
ball.penup()
ball.goto(0,0)
ball.dx = -1    #velocity on x
ball.dy = -1     #velocity on y

#pen to write score 
pen = turtle.Turtle()
pen.speed(10)
pen.color("green")
pen.penup()
pen.hideturtle()
pen.goto(0,260)

#Function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)
    
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)
    

def check_touch(): 
    'check touch on top'
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy = -ball.dy
    
    'check touch on bottom'
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy = -ball.dy
        
    'check ball touch paddle a'
    if(ball.ycor() > paddle_a.ycor() - 50 and \
       ball.ycor() < paddle_a.ycor() + 50 and \
       ball.xcor() < -365 )               or  \
      (ball.ycor() > paddle_b.ycor() - 50 and \
       ball.ycor() < paddle_b.ycor() + 50 and \
       ball.xcor() > 365 )    :
        ball.dx *= -1
               
    'check if ball move pass paddle a'
    if ball.xcor() < -395 :
        ball.goto(0,0)
        global score_b
        score_b  += 1
     
    'check if ball move pass paddle b'
    if ball.xcor() > 395 :
        ball.goto(0,0)
        global score_a
        score_a += 1
        

#Keyboard binding ( tell the program listen to the keyboard input)
wm.listen()
wm.onkeypress(paddle_a_up, "w")
wm.onkeypress(paddle_a_down, "s")
wm.onkeypress(paddle_b_up, "p")
wm.onkeypress(paddle_b_down, "l")

#Main game
while True:
    time.sleep(0.01)
    pen.clear()
    pen.write(f"Player A: {score_a} player B: {score_b}", font=('Courier', 24, 'normal'), align= 'center')
    wm.update()
    
    #move the ball 
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    #check touch 
    check_touch()
    
    #check winner 
    if score_b > 4 :
        pen.goto(0,0)
        pen.write("PLAYER B WIN", move= True, align= "center", font=( 'Courier', 72, 'normal'))
        time.sleep(3)
        break
    if score_a > 4 :
        pen.goto(0,0)
        pen.write("PLAYER A WIN", move= True, align= "center", font=( 'Courier', 72, 'normal'))
        time.sleep(3)
        break
    