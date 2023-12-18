from turtle import Turtle

FONT = ("Courier", 18, "normal")
SCORE_POSITION = (0, 270)
ALIGNMENT = "center"


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", mode="r") as game_data:
            self.high_score = int(game_data.read())
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(SCORE_POSITION)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}\t Highest Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()

    def reset_game(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as game_data:
                game_data.write(f"{self.high_score}")

    def game_over(self):
        pass