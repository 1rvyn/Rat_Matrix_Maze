# irvyn hall
# v12.2
# 22/12/20
# arena class to hold both levels and keep track of how many moves the players take

from Field import Field
from snitch import Snitch


class Arena(Field):
#creates my Arena class

    def setupLevel1(self):
        self.matrix = [['#', '#', '#', '#', '#', '#', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', '#'],
        ['#', '#', '#', '#', '#', '#', '#']]
        self.snitchCount = 1
        self.width = 7
        self.height = 7
        # self.sprouts.clear()  # commented due to it being level 1 and list already being empty
        self.snitches.append(Snitch(self, 3, 4)) #this will spawn the sprout in the first level
        self.players[0].setLocation(self, 1, 1) #this line and the one below will set / spawn the location of the player
        self.players[1].setLocation(self, 5, 1)
        for p in self.players:
            self.scores[p] = 200 #move counter

    def setupLevel2(self):
        self.matrix = [['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
                     ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
                     ['#', '#', '#', ' ', '#', '#', ' ', '#', '#', '#'],
                     ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
                     ['#', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', '#'],
                     ['#', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', '#'],
                     ['#', ' ', ' ', ' ', '#', '#', ' ', ' ', ' ', '#'],
                     ['#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#'],
                     ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
                     ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#']]
        self.snitchCount = 1
        self.width = 10
        self.height = 10
        self.snitches.clear()
        self.snitches.append(Snitch(self, 5, 7)) #see level 1 for the logic of these lines same as before just different values
        self.players[0].setLocation(self, 1, 1)
        self.players[1].setLocation(self, 8, 1)
        self.snitchMoveable = True #the snitch in the second class can actually move so we set this to true
        for p in self.players:
            self.scores[p] = 200
