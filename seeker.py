
class Seeker:
    def __init__(self, x):
        self.char = x
        self.row = 0
        self.col = 0
        self.snitches = 0

    def toString(self): #simple to string method
        info = "Seeker " + self.char + " at row " + str(self.row) + " and column " + str(self.col)
        info = info + " has captured " + str(self.snitches) + " snitches today."
        return info

    def getRow(self): # below are the setters and getters needed for this class
        return self.row

    def getCol(self):
        return self.col

    def getChar(self):
        return self.char

    def getSnitches(self):
        return self.snitches

    def setRow(self, r):
        self.row = r

    def setCol(self, c):
        self.col = c

    def setLocation(self, arena, x, y):#allows me to set the seekers position x = row y = column
        self.row = y
        self.col = x
        arena.clearAtPos(x, y)
        arena.placeChar(self.char, y, x)

    def moveRight(self):#movement methods for the seekers but it uses col and row rather than x and y
        self.col += 1

    def moveLeft(self):
        self.col -= 1

    def moveUp(self):
        self.row -= 1

    def moveDown(self):
        self.row += 1

    def captureSnitch(self):#capture snitch count
        self.snitches += 1
