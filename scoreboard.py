from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 15, 'bold')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_track = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(-10, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(arg=f'Score: {self.score_track}', align=ALIGNMENT, font=FONT)

    def track_of_score(self):
        self.score_track += 1
        self.clear()
        self.update_scoreboard()


    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(arg='Game Over', align='center', font=('Courier', 20, 'bold'))

        self.goto(0, -30)
        self.write(arg=f"Your score is {self.score_track}", align=ALIGNMENT, font=('Courier', 18, 'bold'))





