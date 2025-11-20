from turtle import Screen, Turtle
from food import Food
from snake import Snake
from food import Food
from snake import Snake
import time
from scoreboard import Scoreboard

screen_size = int(input("Enter the screen size (e.g., 600 for 600x600): "))


# Added a difficulty setting
difficulty = input("Choose a difficulty: Easy, Medium, Hard: ").lower()
close_values = [20,15,10]
if difficulty == "easy":
    time.sleep(0.2)
    close = close_values[0]
elif difficulty == "medium":
    time.sleep(0.1)
    close = close_values[1]
elif difficulty == "hard":
    time.sleep(0.005)
    close = close_values[2]
else:
    print("Invalid difficulty. Defaulting to Easy.")
    time.sleep(0.2)
    close = close_values[0]
print(f"The difficulty is set to: {difficulty}")


how_close = 20
screen = Screen()
screen.setup(width=screen_size, height=screen_size)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
scoreboard = Scoreboard()
snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #detect collision with food
    if snake.head.distance(food) < how_close:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    #detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 5:
            game_is_on = False
            scoreboard.game_over()

    # Detect Collision with wall
    if snake.head.xcor() > screen_size-10 or snake.head.xcor() < -screen_size+10 or snake.head.ycor() > screen_size -10 or snake.head.ycor() < -screen_size+10:
        game_is_on = False
        scoreboard.game_over()






















screen.exitonclick()