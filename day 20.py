# Snake game
# 1 Set up screen - ratio: screen.setup(width=600, height=600) background-color: screen.bgcolor("black")
# 2 screen.update() function is used to show new position of objects after changes on a screen (in our case a game)
# 3 time.sleep() function is used to delay the changes making them seemlessly

from turtle import Screen, Turtle
import time
from snake import Snake
from control import Control
from food import Food
from scoreboard import ScoreBoard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()



screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

#automaticly move morward
game_is_on = True
while game_is_on ==True:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Distance collision with food snake.head keeps first objects cordinates and argument food is compared by distance()
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        score.increase_score()
    
    #Detect collision with the wall
    if snake.head.xcor() > 290 or snake.head.xcor()< -290 or snake.head.ycor() > 290 or snake.head.ycor()< -290:
        game_is_on = False 
        score.game_over()
    
    #Detect collision with tail
    for segment in range(len(snake.segments), 1):
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()


screen.exitonclick()
