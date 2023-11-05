from game import Game
from view import View
from music import Music
from playsound import playsound
import time
import cv2

def isAlmostEqual(time1, time2):
    if abs(time1-time2) < 0.1:
        return True
    else:
        return False

if __name__ == "__main__":
    view = View()
    while True:
        if not view.showGame:
            print("Start screen!")
            view.loadStartScreen() #load the start screen
        else:
            print('Game initialized')
            poseResults = None
            startTime = time.time()
            songTitle = view.getSong()
            song = Music(songTitle)
            duration, bpm = song.getMusicStats()
            song.loadMusic()
            print(duration, bpm)
            game = Game() #initialize the game
            song.start()
            view.initGame()
            
            #interval = 15/bpm #interval to add rectangle
            while game.isRunning:
                currTime = round(time.time() - startTime, 1)
                dt = round(180/bpm,1)
                #print(dt)
                #print(currTime)
                game.generateRect(currTime,dt) #generates rectangles at the necessary intervals
                rectList = game.getRectList()
                #print(rectList)
                #rectList = [[250,350,250,350],[100,200,100,200]]
                view.loadGame(rectList, poseResults)
                cv2.waitKey(10)
                
                #print('Game loaded')
                frame = view.getFrame() 
                poseResults = game.poseDetection(frame) # positions of wrists

                

                if poseResults != None:
                    #print('Pose detected!')
                    game.updateScore(poseResults)
                if isAlmostEqual(currTime, duration + 3): #buffer of 3 seconds
                    game.isRunning = False
                    print('Destroy game!')
                    view.destroyGame()
                    view.loadEndScreen(game.score)








        






    # while True:
    #     rectList = controller.getRectList()
    #     loadOverlay(rectList)
