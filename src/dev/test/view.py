import numpy as np
import cv2
import time
import random
import math
import mediapipe as mp
import tkinter as tk
from tkinter import PhotoImage
from tkinter import font
from game import Game

'''


'''

class View:

    def __init__(self):
        self.rectLen = 100
        self.showGame = False
        self.currSong = None
        self.songList = ['Dancing Queen - ABBA',
                         'Sorry - Justin Beiber',
                         'I Knew You Were Trouble - Taylor Swift', 
                         "Hips Don't Lie - Shakira",
                         'Something Just Like This - Coldplay and The Chainsmokers']
        


    def initGame(self):
        # Open the camera
        self.showGame = True
        self.cap = cv2.VideoCapture(0)
        self.rect = np.ones((50,50,3),dtype='uint8')*255
        self.body = np.full((10,10,3),[255,0,0], dtype='uint8')
        


    def startGame(self, song, root):
        if song in self.songList:
            
            self.currSong = song
            self.showGame = True
            root.destroy()
            self.initGame()
            # startGame


    #get methods

    def getKey(self):
        k = cv2.waitKey(10)
        return k

    def getSong(self):
        return self.currSong


    def getIsGame(self):
        return self.showGame


    def getFrame(self):
        return self.frame


    def loadStartScreen(self):

        # Create the main window
        root = tk.Tk()
        root.title("Just Dance Start Screen")

        # Set the window size to be larger (e.g., 600x400)
        window_width = 800
        window_height = 600
        root.geometry(f"{window_width}x{window_height}")

        # Create a Label widget to display the image
        # image_label = tk.Label(root, image=image)
        # image_label.pack(pady=20)  # Add padding to separate the image from buttons

        # Load the frame image
        background_image = background_image = PhotoImage(file="C:\\Users\\wands\\Documents\\CS_15112\\hack112\\justDance3.png")  # Replace "frame.png" with your image file name

        # Create a label to display the frame
        background_label = tk.Label(root, image=background_image)
        background_label.place(relwidth=1, relheight=1)  # Make the label cover the entire window


        # Create a frame to center the buttons
        frame = tk.Frame(root)
        frame.pack(expand=True)  # Expand the frame to fill the window


        # Create a font object with your desired font properties
        custom_font = font.Font(family="Times New Roman", size=20, weight="bold")

        # Create and configure buttons for easy, medium, and hard difficulties
        song_1 = tk.Button(root, text="Dancing Queen - ABBA", font = custom_font, command=lambda: self.startGame("Dancing Queen - ABBA", root))
        song_2 = tk.Button(root, text="Sorry - Justin Beiber", font = custom_font, command=lambda: self.startGame("Sorry - Justin Beiber", root))
        song_3 = tk.Button(root, text="I Knew You Were Trouble - Taylor Swift", font = custom_font, command=lambda: self.startGame("I Knew You Were Trouble - Taylor Swift", root))
        song_4 = tk.Button(root, text="Hips Don't Lie - Shakira", font = custom_font, command=lambda: self.startGame("Hips Don't Lie - Shakira", root))
        song_5 = tk.Button(root, text="Something Just Like This - Coldplay and The Chainsmokers", font = custom_font, command=lambda: self.startGame("Something Just Like This - Coldplay and The Chainsmokers", root))


        # Use the pack geometry manager to center the buttons
        song_1.pack(side="top", pady=30)  # Add padding to separate the buttons
        song_2.pack(side="top", pady=30)
        song_3.pack(side="top", pady=30)
        song_4.pack(side="top", pady=30)
        song_5.pack(side="top", pady=30)


        # Start the main loop
        root.mainloop()


    def loadRect(self, rectCoords):
        x1 = rectCoords[0]
        x2 = rectCoords[1]
        y1 = rectCoords[2]
        y2 = rectCoords[3]
        

        # Select the region in the frame where we want to add the image and add the images using cv2.addWeighted()
        added_image = cv2.addWeighted(self.frame[x1:x2,y1:y2,:],0,self.rect[0:50,0:50,:],1,0)
        # Change the region with the result
        self.frame[x1:x2,y1:y2] = added_image
        # For displaying current value of alpha(weights)


    def loadGame(self, rectList, bodyList):
        '''
        Args:
        rectList
        
        [[x1,x2,y1,y2], [x1,x2,y1,y2]]
        
        '''

        # read the frame
        ret, self.frame = self.cap.read()
        
        #self.frame = cv2.flip(self.frame,1)

        for rectCoords in rectList:
            self.loadRect(rectCoords)
        if bodyList != None:
            
            for body in bodyList:
                self.loadBody(body)

        cv2.imshow('hi',self.frame)


    def loadBody(self, body):
        cv2.circle(self.frame, body, 10, (0,0,255), -1)
        

        # x1, y1 = body
        # x2, y2 = x1 + 10, y1 + 10
        # if 0 < x1 < 400 and 0 < y1 < 400:
        #     if 0 < x2 < 400 and 0 < y2 < 400:
        #         print('Show Body!')
        #         added_image = cv2.addWeighted(self.frame[x1:x2,y1:y2,:],0,self.body[0:10,0:10,:],1,0)
        #         # Change the region with the result
        #         self.frame[x1:x2,y1:y2] = added_image
        #         cv2.imshow('a',self.frame)



    def destroyGame(self):
        self.showGame = False
        self.currSong = None
        self.cap.release()
        cv2.destroyAllWindows()


    def loadEndScreen(score):
        print('End screen loaded!')
        pass
            
    





