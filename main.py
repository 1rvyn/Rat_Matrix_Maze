import random
from Arena import Arena
from seeker import Seeker
import sys
import pygame
from pygame.locals import *

arena = Arena()
arena.players = [Seeker("<"), Seeker(">")]

FPS = 30  # frames per second to update the screen
WINWIDTH = 800  # width of the program's window, in pixels
WINHEIGHT = 600  # height in pixels
HALF_WINWIDTH = int(WINWIDTH / 2)  # you need to know 1/2 sizes so you can
HALF_WINHEIGHT = int(WINHEIGHT / 2)  # place things centrally

# The total width and height of each tile in pixels.
TILEWIDTH = 32
TILEHEIGHT = 32
TILEFLOORHEIGHT = 32

BRIGHTBLUE = (200, 20, 5)# making this a red background so that it fits with the chrismas theme
WHITE = (255, 255, 255)
BGCOLOR = BRIGHTBLUE
TEXTCOLOR = WHITE

IMAGESDICT = {'floor': pygame.image.load("Images/floor.gif"), 'wall': pygame.image.load("Images/wall.gif"), 'snitch': pygame.image.load("Images/snitch.gif"), 'seeker': pygame.image.load("Images/seeker.gif"), 'spacer': pygame.image.load("Images/spacer.gif")}

TILEMAPPING = {'#': IMAGESDICT['wall'], ' ': IMAGESDICT['floor'], '@': IMAGESDICT['snitch'], '/': IMAGESDICT['spacer'], '<': IMAGESDICT['seeker'], '>': IMAGESDICT['seeker']}

pygame.init()
FPSCLOCK = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((WINWIDTH, WINHEIGHT))
pygame.display.set_caption('Seeker Maze v 7.00')
try:
    BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
except:
    pass

level = 1
currentPlayer = True
""" these 4 functions are the movement methods each of them are the same thing 
    each function will look to see if its able to move first by checking what's
    inside the tile they are moving into - each move function will also count each 
    players move and assign it to arena.scores"""

def movePlayerLeft(cPlayer):
    print([x.getChar() for x in arena.players])
    moveable = arena.players[int(cPlayer)]
    x = arena.getCharAtPos(moveable.getRow(), moveable.getCol() - 1)
    if x == "#":
        print("This is a wall!")
    elif x in [x.getChar() for x in arena.players]:
        print("You cannot move into a place of a rat.")
    else:
        if x == "@":
            moveable.captureSnitch()
            arena.captureAllSnitches()
        arena.clearAtPos(moveable.getRow(), moveable.getCol())
        moveable.moveLeft()
        arena.placeChar(moveable.getChar(), moveable.getRow(), moveable.getCol())
        if arena.snitchMoveable:
            for snitch in arena.snitches:
                snitch.move(random.choice(["up", "down", "left", "right"]))
        arena.scores[moveable] = arena.scores.get(moveable) - 10
    print(arena.toString())
    print(moveable.toString())


def movePlayerRight(cPlayer):
    moveable = arena.players[int(cPlayer)]
    x = arena.getCharAtPos(moveable.getRow(), moveable.getCol() + 1)
    if x == "#":
        print("This is a wall!")
    elif x in [x.getChar() for x in arena.players]:
        print("You cannot move into a place of a rat.")
    else:
        if x == "@":
            moveable.captureSnitch()
            arena.captureAllSnitches()
        arena.clearAtPos(moveable.getRow(), moveable.getCol())
        moveable.moveRight()
        arena.placeChar(moveable.getChar(), moveable.getRow(), moveable.getCol())
        if arena.snitchMoveable:
            for snitch in arena.snitches:
                snitch.move(random.choice(["up", "down", "left", "right"]))
        arena.scores[moveable] = arena.scores.get(moveable) - 10
    print(arena.toString())
    print(moveable.toString())



def movePlayerUp(cPlayer):
    moveable = arena.players[int(cPlayer)]
    x = arena.getCharAtPos(moveable.getRow() - 1, moveable.getCol())
    if x == "#":
        print("This is a wall!")
    elif x in [x.getChar() for x in arena.players]:
        print("You cannot move into a place of a rat.")
    else:
        if x == "@":
            print("Yum yum! Dinner time!")
            moveable.captureSnitch()
            arena.captureAllSnitches()
        arena.clearAtPos(moveable.getRow(), moveable.getCol())
        moveable.moveUp()
        arena.placeChar(moveable.getChar(), moveable.getRow(), moveable.getCol())
        if arena.snitchMoveable:
            for snitch in arena.snitches:
                snitch.move(random.choice(["up", "down", "left", "right"]))
        arena.scores[moveable] = arena.scores.get(moveable) - 10
    print(arena.toString())
    print(moveable.toString())


def movePlayerDown(cPlayer):
    moveable = arena.players[int(cPlayer)]
    x = arena.getCharAtPos(moveable.getRow() + 1, moveable.getCol())
    if x == "#":
        print("This is a wall!")
    elif x in [x.getChar() for x in arena.players]:
        print("You cannot move into a place of a rat.")
    else:
        if x == "@":
            print("Yum yum! Dinner time!")
            moveable.captureSnitch()
            arena.captureAllSnitches()
        arena.clearAtPos(moveable.getRow(), moveable.getCol())
        moveable.moveDown()
        arena.placeChar(moveable.getChar(), moveable.getRow(), moveable.getCol())
        if arena.snitchMoveable:
            for snitch in arena.snitches:
                snitch.move(random.choice(["up", "down", "left", "right"]))
        arena.scores[moveable] = arena.scores.get(moveable) - 10
    print(arena.toString())
    print(moveable.toString())

def main():# runs main game loop
    global FPSCLOCK, DISPLAYSURF, IMAGESDICT, TILEMAPPING, BASICFONT, level, currentPlayer
    arena.setupLevel1() # setup the first level as it just makes sense to do it first
    for p in arena.players: # loop through the players arena to get where they are and their corresponding characters
        arena.placeChar(p.getChar(), p.getRow(), p.getCol())
    print(arena.toString()) # prints the arena to the screen but in text form
    drawMap()

    while True:
        # thread 1 - look for an action
        for event in pygame.event.get():  # event handling loop
            if event.type == QUIT:
                # Player clicked the "X" at the corner of the window.
                terminate()
            elif event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    movePlayerRight(currentPlayer)
                    currentPlayer = not currentPlayer
                elif event.key == K_UP:
                    movePlayerUp(currentPlayer)
                    currentPlayer = not currentPlayer
                elif event.key == K_LEFT:
                    movePlayerLeft(currentPlayer)
                    currentPlayer = not currentPlayer
                elif event.key == K_DOWN:
                    movePlayerDown(currentPlayer)
                    currentPlayer = not currentPlayer
                elif event.key == K_SPACE:
                    restart()
                else:
                    pass
            mapNeedsRedraw = True#this will check to see if the player presses any arrow keys and then if they are
                                #it will call the movePlayer function corresponding to the arrow key pressed

                            # here is where we check whether the level is complete!
            if level == 1: #simple methods to check if either level 1 or level 2 is cimplete by using the "completedarena" class
                if arena.levelCompleted():
                    # level is completed
                    print("Level completed!")
                    arena.setupLevel2()
                    level = 2
            elif level == 2:
                if arena.levelCompleted():
                    # level 2 is completed
                    print("Level 2 complete!")
                    print("Game completed!")
                    terminate()


        # thread 2: redraw the screen
        DISPLAYSURF.fill(BGCOLOR)  # draws the turquoise background
        DISPLAYSURF.blit(BASICFONT.render(f"Player 1: {arena.scores.get(arena.players[0])}", True, (255, 255, 255)), (20, 20))#player one counter
        DISPLAYSURF.blit(BASICFONT.render(f"Player 2: {arena.scores.get(arena.players[1])}", True, (255, 255, 255)), (640, 20))#player two counter
        controlsText = BASICFONT.render(f"[SPACE] Restart", True, (255, 255, 255))#restart control indicator
        DISPLAYSURF.blit(controlsText, (330, 536))

        # if something has changed then redraw the map
        if mapNeedsRedraw:
            mapSurf = drawMap()
            mapNeedsRedraw = False

        mapSurfRect = mapSurf.get_rect()
        mapSurfRect.center = (HALF_WINWIDTH, HALF_WINHEIGHT)

        # Draw the map on the DISPLAYSURF object.
        DISPLAYSURF.blit(mapSurf, mapSurfRect)
        pygame.display.update()  # draw DISPLAYSURF to the screen.
        FPSCLOCK.tick()


def drawMap():
    # draw the tile sprites onto this surface.
    # this creates the visual map!
    mapSurfWidth = arena.getWidth() * TILEWIDTH
    mapSurfHeight = arena.getHeight() * TILEHEIGHT
    mapSurf = pygame.Surface((mapSurfWidth, mapSurfHeight))
    mapSurf.fill(BGCOLOR)
    for h in range(arena.getHeight()):
        for w in range(arena.getWidth()):
            thisTile = pygame.Rect((w * TILEWIDTH, h * TILEFLOORHEIGHT, TILEWIDTH, TILEHEIGHT))
            if arena.getCharAtPos(h, w) in TILEMAPPING:
                # checks in the TILEMAPPING directory above to see if there is a
                # matching picture, then renders it
                baseTile = TILEMAPPING[arena.getCharAtPos(h, w)]

            # Draw the tiles for the map.
            mapSurf.blit(baseTile, thisTile)
    return mapSurf

#restart function to resetup the levels and call the drawMap function
def restart():
    # arena.__init__()
    if level == 1:
        arena.setupLevel1()
    if level == 2:
        arena.setupLevel2()
    drawMap()

#terminate function incase the user needs it i dont think i actually use this but i used it while testing
def terminate():
    # shutdown routine
    pygame.quit()
    sys.exit()
# Makes sure the program get ran by through running main.py only and not through imports
if __name__ == '__main__':
    main()
