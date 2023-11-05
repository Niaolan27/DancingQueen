from game-30 import Game
from view import View
from music import Music
import time

def isAlmostEqual(time1, time2):
    if abs(time1-time2) < 0.1:
        return True
    else:
        return False

if __name__ == 'main':
    view = View()
    while True:
        if not view.showGame:
            view.loadStartScreen() #load the start screen
        else:
            view.initGame()
            startTime = time.time()
            song = Music()
            duration = song.duration
            bpm = song.bpm
            interval = 60/bpm #interval to add rectangle
            game = Game() #initialize the game
            while game.isRunning():
                currTime = round(time.time() - startTime, 1)
                dt = round(60/bpm,1)
                game.generateRect(currTime,dt) #generates rectangles at the necessary intervals
                frame = view.getFrame() 
                poseResults = game.poseDetection(frame) # positions of wrists
                game.updateScore(poseResults)
                if isAlmostEqual(currTime, duration + 3): #buffer of 3 seconds
                    game.isRunning = False
                    view.destroyGame
                    view.loadEndScreen(game.score)








        






    # while True:
    #     rectList = controller.getRectList()
    #     loadOverlay(rectList)