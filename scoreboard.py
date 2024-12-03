from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 12, "normal")


class ScoreBoard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.color("red")
        self.shape(None)
        self.hideturtle()
        self.score_number = 0
        self.setposition(x=0, y=280)
        self.update_score()

    def update_score(self):
         self.write(f"Score: {self.score_number}", move=False, align=ALIGNMENT, font=FONT)
    
    def increase_score(self):
        self.score_number += 1
        self.clear()
        self.update_score()
    
    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over", move=False, align=ALIGNMENT, font=FONT)