#Pong 
#----
#----
#By Scott

import turtle

wn = turtle.Screen()
wn.title("Pong by Scott")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#Border
brdr=turtle.Turtle()
brdr.hideturtle()
brdr.goto(-400,300)
brdr.forward(800)
brdr.left(90)
brdr.forward(600)
brdr.left(90)
brdr.forward(800)
brdr.left(90)
brdr.forward(600)

#Score
score_a=0
score_b=0

#Paddle A
paddle_a=turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("green")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

#Paddle B
paddle_b=turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("green")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

#Ball
ball=turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("green")
ball.penup()
ball.goto(0,0)
ball.dx=2.75
ball.dy=2.75

#Pen
pen=turtle.Turtle()
pen.speed(0)
pen.color("green")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0 Player B: 0", align="center", font=("courier", 24,"normal"))


####FUNCTIONS####
#move paddle A&B
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

#Keyboard binding
wn.listen()
wn.onkey(paddle_a_up, "w")
wn.onkey(paddle_a_down, "s")
wn.onkey(paddle_b_up, "Up")
wn.onkey(paddle_b_down, "Down")


#Main Game Loop
while True:
	wn.update()
	
	#Move the ball
	ball.setx(ball.xcor()+ball.dx)
	ball.sety(ball.ycor()+ball.dy)
	
	#Border Checking
	if ball.ycor()>290:
		ball.sety(290)
		ball.dy *= -1
		
	if ball.ycor()<-290:
		ball.sety(-290)
		ball.dy *= -1
		
	if ball.xcor()>390:
		ball.goto(0,0)
		ball.dx *=-1
		score_a += 1
		pen.clear()
		pen.write("Player A: {} Player B: {}".format(score_a,score_b), align="center", font=("courier", 24, "normal"))
		
	if ball.xcor()<-390:
		ball.goto(0,0)
		ball.dx *=-1
		score_b += 1
		pen.clear()
		pen.write("Player A: {} Player B: {}".format(score_a,score_b), align="center", font=("courier", 24, "normal"))
		
	#Paddle and Ball Collision
	if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50 ):
		ball.setx(340)
		ball.dx *= -1
		
	if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50 ):
		ball.setx(-340)
		ball.dx *= -1
	
	#END GAME CODE
	if score_a>9:
		ball.dx , ball.dy = ball.dx*0 , ball.dy*0
		paddle_a.goto(-350,0)
		paddle_b.goto(350,0)
		pen.color("green")
		pen.goto(0,100)
		pen.write("Player A Wins!",align="center", font=("courier",32,"normal"))
		
	if score_b>9:
		ball.dx , ball.dy = ball.dx*0 , ball.dy*0
		paddle_a.goto(-350,0)
		paddle_b.goto(350,0)
		pen.color("green")
		pen.goto(0,100)
		pen.write("Player B Wins!",align="center", font=("courier",32,"normal"))
