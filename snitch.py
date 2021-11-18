import random

class Snitch:

    def __init__(self, arenaObj, x, y):
        self.arenaObj = arenaObj
        self.x = x
        self.y = y
        arenaObj.placeChar("@", y, x)
        #move method that can move left, right, up, down depending on the value the direction method holds -
        #it will also look thru the getchar method to see if the snitch can actually move into the tile

    def move(self, direction):
        self.arenaObj.clearAtPos(self.y, self.x)#checks if it is clear for the snitch to move
        if direction == "up":#if the direction is up
            x = self.arenaObj.getCharAtPos(self.y - 1, self.x)#set x = to the position if might move into
            if x != "#" and x not in [x.getChar() for x in self.arenaObj.players]:#this makes sure it will only move into a tile with nothing in it
                self.y -= 1#y coord decreases by one to move UP
            else:#if the tile is NOT empty >>
                return self.move(random.choice(["up", "down", "left", "right"])) #if its not empty and this ELSE goes it will randomly choose a new option
        if direction == "down":
            x = self.arenaObj.getCharAtPos(self.y + 1, self.x)
            if x != "#" and x not in [x.getChar() for x in self.arenaObj.players]:
                self.y += 1
            else:
                return self.move(random.choice(["up", "down", "left", "right"]))
        if direction == "right":
            x = self.arenaObj.getCharAtPos(self.y, self.x + 1)
            if x != "#" and x not in [x.getChar() for x in self.arenaObj.players]:
                self.x += 1
            else:
                return self.move(random.choice(["up", "down", "left", "right"]))
        if direction == "left":
            x = self.arenaObj.getCharAtPos(self.y, self.x - 1)
            if x != "#" and x not in [x.getChar() for x in self.arenaObj.players]:
                self.x -= 1
            else:
                return self.move(random.choice(["up", "down", "left", "right"]))
        self.arenaObj.placeChar("@", self.y, self.x)
#not going to repeat the comments for the other 3 movement loops as its LITERALLY THE SAME just a different direction