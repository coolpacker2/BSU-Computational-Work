import math
class Player():
    def __init__(self, _name, _points):
        self.name = _name
        self.points = _points
    
    def getPoints (self):
        return self.points


class Dice:
    def __init__(self):
        self.val = 0
    def getVal (self):
        return self.val
    def randomVal (self):
        self.val = math.random.randInt(1,6)

class Game:
    def __init__(self):
        self.status = ""
        self.turn = True
    def run(self):
        while (self.status == ""):
            player1Name = input("Player 1 please enter your name: ")
            print(player1Name+" is player 1")
            player2Name = input("Player 2 please enter your name: ")
            print(player2Name+" is player 2")
            self.status == "Neutral"
            break
        if self.status == "Neutral":
            if self.Turn == True:
                Player(player1Name, Player.getPoints() + Dice.randomVal)
            else:
                Player(player2Name, Player.getPoints() + Dice.randomVal)
        else:
            



game = Game()
game.run()