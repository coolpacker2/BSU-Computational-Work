import time
import random
class Player:
    def __init__(self):
        self.name = ""
        self.points = 0
        self.roll = 0
    def getPoints(self):
        return self.points
    def setPoints(self, pointsToAdd):
        self.points = self.points + pointsToAdd
    def set_name(self, name):
        self.name = name
class Dice:
    def __init__(self):
        self.val = 0
    def randomVal (self):
        self.val = random.randrange(1,6,1)
    def getVal(self):
        return self.val

class Game:

    def __init__(self):
        self.turn = True
        self.introduction = False
        self.completed = False
        self.round = 0
        self.maxRounds = 6
    def run(self):
        while self.introduction == False:
           
            player1 = Player()
            player1.set_name(input("Player 1 please enter your name: "))
            print(player1.name+" is player 1")
            player2 = Player()
            player2.set_name(input("Player 2 please enter your name: "))
            print(player2.name+" is player 2")
            self.introduction = True
  
        while self.round<self.maxRounds:
            if self.completed == True:
                if not self.maxRounds == self.round:
                    if player1.roll > player2.roll:
                        player1.setPoints(1)
                        print(player1.name+" gets one point!")
                        time.sleep(0.3)
                        print(player1.name + " has " + str(player1.getPoints()) + " and "+ player2.name + " has " + str(player2.getPoints())) # i didnt use get or set methods because im lazy
                    elif player2.roll > player1.roll:
                        player2.setPoints(1)
                        print(player2.name+" gets one point!")
                        time.sleep(0.3)
                        print(player2.name + " has " + str(player2.getPoints()) + " and "+ player1.name + " has " + str(player1.getPoints()))
                    elif player2.roll == player1.roll:
                        player1.setPoints(1)
                        player2.setPoints(1)
                        print(player1.name+" and "+player2.name+" get one point!")
                        time.sleep(0.3)
                        print(player1.name + " has " + str(player1.getPoints()) + " and "+ player2.name + " has " + str(player2.getPoints())) # i didnt use get or set methods because im lazy
                    self.completed = False
        
            elif self.completed == False:
                if self.turn == True:
                    input("Press enter to roll " + player1.name + " aka player1")
                    die = Dice() # create object for Dice, doing Dice.randomVal() is an instance
                    die.randomVal()
                    player1.roll = die.getVal()
                    print(player1.name+" rolled a " + str(player1.roll))
                    self.turn = False
                elif self.turn == False:
                    input("Press enter to roll " + player2.name + " aka player2")
                    die = Dice() # create object for Dice, doing Dice.randomVal() is an instance
                    die.randomVal()
                    player2.roll = die.getVal()
                    print(player2.name+" rolled a " + str(player2.roll))
                    self.turn = True
                    self.round = self.round+1
                    self.completed = True
        if player1.points > player2.points:
            print(player2.name + " has won with " + str(player1.points)+ " Points")
        elif player2.points > player1.points:
            print(player2.name + " has won with " + str(player2.points) + " Points")
        
                
        

game = Game()
game.run()
