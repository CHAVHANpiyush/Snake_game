from turtle import Screen
import time
from snake import Snake
from food import Food
from screboard import Scoreboard
WIDTH=600
LENGHT=600

screen=Screen()
screen.setup(width=WIDTH,height=LENGHT)
screen.bgcolor("black")
screen.title("Serpent Saga")
screen.tracer(0)
snake=Snake()
food=Food()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.up,"w")
screen.onkey(snake.down,"Down")
screen.onkey(snake.down,"s")
screen.onkey(snake.left,"Left")
screen.onkey(snake.left,"a")
screen.onkey(snake.right,"Right")
screen.onkey(snake.right,"d")
screen.onkey(snake.pause, "space")






game_is_on = True
   
while game_is_on:
    if snake.paused:
        screen.update()

    else:
        screen.update()
        time.sleep(0.1)
        snake.move()


        #Detect collision
        if snake.segments[0].distance(food) < 15:
            scoreboard.increase_score()
            snake.extend()
            food.refresh()


        #detect collision with wall
        if snake.segments[0].xcor()>((WIDTH/2)-10) or snake.segments[0].xcor()<-((WIDTH/2)-10) or snake.segments[0].ycor()>((LENGHT/2)-10) or snake.segments[0].ycor()<-((LENGHT/2)-10):
            scoreboard.reset()
            snake.reset()

        #dettect collision with tail

        for segment in snake.segments[1:]:
            if snake.segments[0].distance(segment)<10:
                scoreboard.reset()
                snake.reset()





screen.exitonclick()
