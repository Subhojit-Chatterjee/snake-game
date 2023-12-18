from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title(titlestring="My Snake Game")

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.2)
    snake.move()

    if snake.head.distance(food) < 15:
        # Detect whether the snake's head collides with the food or not
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        # Detects the collision of the snake with the wall
        game_is_on = False
        scoreboard.reset_game()
        continue_game = input("Do you wish to continue the game? (Y/N): ")
        if continue_game.lower() == "y":
            snake.reset_game()
        else:
            scoreboard.game_over()

    # Detect collision with the snake head and part of the snake's tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.reset_game()
            continue_game = input("Do you wish to continue? (Y/N): ")
            if continue_game.lower() == "y":
                snake.reset_game()
            else:
                scoreboard.game_over()
screen.exitonclick()
