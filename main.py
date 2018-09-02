import turtle
import time
import random

delay = 0.1

#Snake window
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("blue")
wn.setup(width=600, height=600)
wn.tracer(0)

#Snake Head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"

#Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

#Score
score = 0
scoreText = turtle.Turtle()
scoreText.speed(0)
scoreText.shape("square")
scoreText.color("white")
scoreText.penup()
scoreText.hideturtle()
scoreText.goto(200,260)
scoreText.write("Score: %d" % (score))

#High Score
high_score = 0
high_score_text = turtle.Turtle()
high_score_text.speed(0)
high_score_text.shape("square")
high_score_text.color("white")
high_score_text.penup()
high_score_text.hideturtle()
high_score_text.goto(200,230)
high_score_text.write("High-Score: %d" % (high_score))

segments = []

def die():
    time.sleep(1)
    head.goto(0,0)
    head.direction = 'stop'
     #hide segments
    for segment in segments:
        segment.goto(1000,1000)
    #clear segments list
    segments.clear()
    scoreText.clear()
    high_score_text.clear()
    scoreText.write("Score: %d" % (score))
    high_score_text.write("High-Score: %d" %(high_score))


#Functions
def go_up():
    if head.direction != 'down':
        head.direction = 'up'
def go_down():
    if head.direction != 'up':
        head.direction = 'down'
def go_left():
    if head.direction != 'right':
        head.direction = 'left'
def go_right():
    if head.direction != 'left':
        head.direction = 'right'

def move():
    if head.direction == 'up':
        y = head.ycor()
        head.sety(y+20)
    if head.direction == 'down':
        y = head.ycor()
        head.sety(y-20)
    if head.direction == 'left':
        x = head.xcor()
        head.setx(x-20)
    if head.direction == 'right':
        x = head.xcor()
        head.setx(x+20)

#Keyboard Bindings
wn.listen()
wn.onkeypress(go_up,"w")
wn.onkeypress(go_down,"s")
wn.onkeypress(go_left,"a")
wn.onkeypress(go_right,"d")

#Main Loop
while True:
    wn.update()

    #check for collision with border

    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        if score>high_score:
            high_score = score
        score = 0
        die()
       

    #check for collision with the food
    if head.distance(food) < 20:
        #move food to random spot on screen
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(x,y)

        #Add a segment to snake
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        #increase the score
        score+=1
        scoreText.clear()
        scoreText.write("Score: %d" % (score))
        
        
    
    #move end segments first in reverse order
    for index in range(len(segments)-1,0,-1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)

    #move segment 0 to location of head
    if len(segments) > 0:
        x=head.xcor()
        y=head.ycor()
        segments[0].goto(x,y)

    move()

    #check for head collision with the body segments
    for segment in segments:
        if segment.distance(head) < 20:
            if score>high_score:
                high_score = score
            score=0
            die()
            


    time.sleep(delay)

wn.mainloop()