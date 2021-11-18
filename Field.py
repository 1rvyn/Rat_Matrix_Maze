# inheritance evidence

class Field:

    def __init__(self):
        self.matrix = [[]]
        self.snitches = []
        self.snitchCount = 0
        self.width = 0
        self.height = 0
        self.players = []
        self.scores = {}
        self.snitchMoveable = False

    def toString(self): #simple to string method so i can see the arena
        printme = ""
        for i in range(0, len(self.matrix)):
            for j in self.matrix[i]:
                printme = printme + j
            printme = printme + "\n"
        return printme

    def placeChar(self, char, row, column): #allows me to place characters
        self.matrix[row][column] = char

    def clearAtPos(self, row, col): #method to check if a tile is clear
        self.matrix[row][col] = " "

    def getCharAtPos(self, row, col): #the same as above but its for a specific character not if its empty
        return self.matrix[row][col]

    def captureAllSnitches(self): #method to capture all the snitches
        self.snitches.clear()

    def getWidth(self): #width and height getters
        return self.width

    def getHeight(self):
        return self.height

    def getCurrentMatrix(self): #get the current matrix ie get current arena
        return self.matrix

    def levelCompleted(self):  # the arena is called a matrix here as its what its supposed to be called in game dev
        completed = True  # if its completed the loop will start
        for y in range(len(self.matrix)):  # loop thru the arena
            for x in range(len(self.matrix[y])):
                if self.matrix[y][x] == "@":  # if the item is a @ as in a snitch completed is not true
                    completed = False

        return completed