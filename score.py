import turtle
xx = open("h_score.txt", "r+")
class  Score_board(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("green")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.highestscore()
        self.p = xx.read()
        self.write(f"Score is {self.score}      highest {self.p}", align="center", font=("Arial", 20, "normal"))





    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over \n Score is {self.score}", align="center", font=("Arial", 20, "normal"))


    def increase_score(self,g):
        self.score += 1
        self.clear()
        self.write(f"Score is {self.score}      highest {str(int(g) + 1)}", align="center", font=("Arial", 24, "normal"))

    def highestscore(self):
        self.high = 0
        if self.high < self.score:
            xx = open("h_score.txt", "r+")
            xx.write(str(self.score))










