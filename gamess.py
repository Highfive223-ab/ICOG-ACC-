import turtle
window=turtle.Screen()
window.title("pong")
window.bgcolor('black')
window.setup(width=800,height=600)
window.tracer(0)
#paddle1
paddle1=turtle.Turtle()
paddle1.speed(0)
paddle1.shape('square')
paddle1.color('white')
paddle1.shapesize(stretch_wid=10,stretch_len=1)
paddle1.penup()
paddle1.goto(-350,0)
#paddle2
paddle2=turtle.Turtle()
paddle2.speed(0)
paddle2.shape('square')
paddle2.color('white')
paddle2.shapesize(stretch_wid=10,stretch_len=1)
paddle2.penup()
paddle2.goto(350,0)

#ball
ball=turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('white')
ball.shapesize(stretch_wid=2,stretch_len=2)
ball.penup()
ball.goto(0,0)
ball.dx=1
ball.dy=-1
#functions
def paddle1_up():
      y=paddle1.ycor()
      y+=20
      paddle1.sety(y)


def paddle2_up():
    y = paddle1.ycor()
    y += 20
    paddle1.sety(y)

def paddle1_down():
    y = paddle1.ycor()
    y -= 20
    paddle1.sety(y)
def paddle2_down():
    y = paddle1.ycor()
    y -= 20
    paddle1.sety(y)

#key listener
window.listen()
window.onkeypress(paddle1_up(),'w')
window.onkeypress(paddle2_up(),'UP')
window.onkeypress(paddle1_down(),'s')
window.onkeypress(paddle2_down(),'DOWN')
while True:
    window.update()

    #movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    #border
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy==-1
    if ball.ycor()>-290:
        ball.sety(-290)
        ball.dy+=1
    if ball.xcor()>390:
        ball.goto(0,0)
        ball.dx==-1
