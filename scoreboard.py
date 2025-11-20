from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self,screen_size):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()

        # Position scoreboard dynamically based on screen size
        top_y = (screen_size / 2) - 40
        self.goto(0, top_y)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Arial", 36, "bold"))
