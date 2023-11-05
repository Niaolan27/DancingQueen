import math
import random
import mediapipe as mp
import cv2
import timeit

class Game:
    def __init__(self):
        self.isRunning = True
        self.score = 0
        self.rectList = []
        self.rectSize = 100
        self.right_wrist_x = 0
        self.right_wrist_y = 0
        self.left_wrist_x = 0
        self.left_wrist_y = 0
        
    def updateScore(self):
         # boolean variable for whether the whole program is running
        for wristLocation in poseDetection(self, frame):
            for rectangle in self.rectList:
                x1 = rectangle[0]
                x2 = rectangle[1]
                y1 = rectangle[2]
                y2 = rectangle[3]
                if (x1 < wristLocation[0] < x2) and (y1 < wristLocation[1] < y2): # using the bounding box to find the intersection
                    self.removeRectangle(rectangle)
                    self.score += 5

    def generateRect(self, currentTime, dt): # add the interval in which to add coords
        x1 = random.randint(0, 400)
        x2 = x1 + self.rectSize
        y1 = random.randint(0, 400)
        y2 = y1 + self.rectSize
        rectCoords = [x1, x2, y1, y2]
        if currentTime % dt == 0:
            self.rectList.append[rectCoords]
            
    
    def getRectList(self):
     return self.rectList
    
    def poseDetection(self, frame):
    # Convert the BGR image to RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        #
        mp_pose = mp.solutions.pose
        pose = mp_pose.Pose()
        # Perform pose estimation
        results = pose.process(rgb_frame)
        # Extract landmarks if pose detected
        if results.pose_landmarks:
            landmarks = results.pose_landmarks.landmark
            # You can access the landmarks like landmarks[mp_pose.PoseLandmark.WRIST_RIGHT.value]
            # or any other specific landmark.
            # Right wrist landmark (index is 16)
            self.right_wrist_x = int(landmarks[16].x * frame.shape[1])
            self.right_wrist_y = int(landmarks[16].y * frame.shape[0])

            # Left wrist landmark (index is 15)
            self.left_wrist_x = int(landmarks[15].x * frame.shape[1])
            self.left_wrist_y = int(landmarks[15].y * frame.shape[0])
        
            return [(self.right_wrist_x, self.right_wrist_y), (self.left_wrist_x, self.left_wrist_y)]
        
    
