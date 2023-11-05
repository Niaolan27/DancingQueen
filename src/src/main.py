from game import Game
from view import View
from music import Music
import time
import cv2

def isAlmostEqual(time1, time2):
    if abs(time1-time2) < 0.1:
        return True
    else:
        return False
    

def checkKey(key):
    if key == ord('q'):
        view.destroyGame()
        song.stop()
        view.showGame = False
        game.isRunning = False
    

if __name__ == "__main__":
    view = View()
    while True:
        if not view.showGame:
            print("Start screen!")
            view.loadStartScreen() #load the start screen
        else:
            print('Game initialized')
            poseResults = None
            currScore = 0
            startTime = time.time()
            songTitle = view.getSong()
            song = Music(songTitle)
            duration, bpm = song.getMusicStats()
            song.loadMusic()
            print(duration, bpm)
            game = Game() #initialize the game
            view.initGame()
            song.start()

            while game.isRunning:
                currTime = round(time.time() - startTime, 1)
                dt = round(90/bpm,1)
                game.generateRect(currTime,dt) #generates rectangles at the necessary intervals
                rectList = game.getRectList()
                view.loadGame(rectList, poseResults, currScore)

                key = view.getKey()
                checkKey(key)
                
                #print('Game loaded')
                frame = view.getFrame() 
                poseResults = game.poseDetection(frame) # positions of wrists
                currScore = game.getScore()


                
                if poseResults != None:
                    #print('Pose detected!')
                    game.updateScore(poseResults)
                if isAlmostEqual(currTime, duration + 3): #buffer of 3 seconds
                    game.isRunning = False
                    print('Destroy game!')
                    view.destroyGame()
                    view.loadEndScreen(game.score)
