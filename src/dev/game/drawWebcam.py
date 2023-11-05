import numpy as np
import cv2
import time
import random
import math
import mediapipe as mp
import tkinter as tk
from tkinter import PhotoImage
from tkinter import font

'''


'''

class View:

    def __init__(self):
        self.rectLen = 100
        self.showOverlay = False


    def initOverlay(self):
        # Open the camera
        self.cap = cv2.VideoCapture(0)
        self.foreground = np.ones((100,100,3),dtype='uint8')*255


    def start_game(self, difficulty, root):
        if difficulty == 'Dancing Queen by ABBA' or difficulty == 'Sorry by Justin Beiber' or difficulty == 'I Knew You Were Trouble by Taylor Swift' or difficulty == "Hips Don't Lie by Shakira" or difficulty == 'Something Just Like This by Coldplay and The Chainsmokers':
            print('hi')
            self.showOverlay = True
            root.destroy()
            self.initOverlay()
            # startGame


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

        # Load the background image
        background_image = background_image = PhotoImage(file="C:\\Users\\wands\\Documents\\CS_15112\\justDance3.png")  # Replace "background.png" with your image file name

        # Create a label to display the background image
        background_label = tk.Label(root, image=background_image)
        background_label.place(relwidth=1, relheight=1)  # Make the label cover the entire window


        # Create a frame to center the buttons
        frame = tk.Frame(root)
        frame.pack(expand=True)  # Expand the frame to fill the window


        # Create a font object with your desired font properties
        custom_font = font.Font(family="Times New Roman", size=20, weight="bold")

        # Create and configure buttons for easy, medium, and hard difficulties
        song_1 = tk.Button(root, text="Dancing Queen by ABBA", font = custom_font, command=lambda: self.start_game("Dancing Queen by ABBA", root))
        song_2 = tk.Button(root, text="Sorry by Justin Beiber", font = custom_font, command=lambda: self.start_game("Sorry by Justin Beiber", root))
        song_3 = tk.Button(root, text="I Knew You Were Trouble by Taylor Swift", font = custom_font, command=lambda: self.start_game("I Knew You Were Trouble by Taylor Swift", root))
        song_4 = tk.Button(root, text="Hips Don't Lie by Shakira", font = custom_font, command=lambda: self.start_game("Hips Don't Lie by Shakira", root))
        song_5 = tk.Button(root, text="Something Just Like This by Coldplay and The Chainsmokers", font = custom_font, command=lambda: self.start_game("Something Just Like This by Coldplay and The Chainsmokers", root))


        # Use the pack geometry manager to center the buttons
        song_1.pack(side="top", pady=30)  # Add padding to separate the buttons
        song_2.pack(side="top", pady=30)
        song_3.pack(side="top", pady=30)
        song_4.pack(side="top", pady=30)
        song_5.pack(side="top", pady=30)


        # Start the main loop
        root.mainloop()


    def loadRect(self, background, rectCoords):
        x1,x2,y1,y2 = rectCoords
        # Select the region in the background where we want to add the image and add the images using cv2.addWeighted()
        added_image = cv2.addWeighted(background[x1:x2,y1:y2,:],0,self.foreground[0:100,0:100,:],1,0)
        # Change the region with the result
        background[x1:x2,y1:y2] = added_image
        # For displaying current value of alpha(weights)
        cv2.imshow('a',background)


    def loadOverlay(self, rectList):
        '''
        Args:
        rectList
        
        [[x1,x2,y1,y2], [x1,x2,y1,y2]]
        
        '''

        # read the background
        ret, background = self.cap.read()
        background = cv2.flip(background,1)

        for rectCoords in rectList:
            print(rectCoords)
            self.loadRect(background, rectCoords)


    def destroyOverlay(self):
        self.cap.release()
        cv2.destroyAllWindows()
            
    


if __name__ == '__main__':

    #controller = Controller()

    view = View()

    while True:
        print(view.showOverlay)
        if not view.showOverlay:
            view.loadStartScreen()
        else:
            view.initOverlay()
            while True:
                #rectList = controller.getRectList()
                rectList = [[250,350,250,350],[100,200,100,200]]
                view.loadOverlay(rectList)

                k = cv2.waitKey(10)
                # Press q to break  
                if k == ord('q'):
                    view.destroyOverlay()
                    view.showOverlay = False
                    break





