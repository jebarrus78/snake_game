from turtle import Screen, Turtle
from food import Food
from snake import Snake
from food import Food
from snake import Snake
import time
from scoreboard import Scoreboard

screen_size = int(input("Enter the screen size (e.g., 600 for 600x600): "))

close= 20

# Added a difficulty setting
difficulty = input("Choose a difficulty: Easy, Medium, Hard: ").lower()

# close = distance to detect food
# delay = time between moves (speed)
# snake_size = turtle size

if difficulty == "easy":
    close = 20
    delay = 0.2
    snake_size = 1.0
elif difficulty == "medium":
    close = 15
    delay = 0.1
    snake_size = 0.75
elif difficulty == "hard":
    close = 15
    delay = 0.05
    snake_size = 0.5
else:
    print("Invalid difficulty. Defaulting to Easy.")
    difficulty = "easy"
    close = 20
    delay = 0.2
    snake_size = 1.0
print(f"The difficulty is set to: {difficulty}")
print(f"Snake size: {snake_size}, food distance: {close}, speed delay: {delay}")

screen = Screen()
screen.setup(width=screen_size, height=screen_size)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


# --- Game objects ---
scoreboard = Scoreboard(screen_size)
snake = Snake(size=snake_size)   # ✅ pass size into Snake
food = Food()

# Controls
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


#Game Loop
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #detect collision with food
    if snake.head.distance(food) < close:
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