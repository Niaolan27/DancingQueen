import math
import random
import mediapipe as mp
import cv2

a = True
def distance(x1, x2, y1, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2) # returns distance (may be unneccessary)

def generateRect(self, bpm, difficulty):
        #difficulty is between 1-3

        #generate coords of Rect
        x1 = random.randint(0, 400)
        x2 = x1 + self.rectLen
        y1 = random.randint(0, 400)
        y2 = y1 + self.rectLen
        rectCoords = (x1, x2, y1, y2)


        #generate speed of Rect
        speed = bpm * difficulty/3

def getRectList():
     return rectangleList

def scoreUpdate(self, gameController):
    while a: # boolean variable for whether the whole program is running
        for wristLocation in poseDetection(frame):
            for rectangle in rectangleList:
                x1, x2 = rectangle[0], rectangle[1]
                y1, y2 = rectangle[2], rectangle[3]
                if (x1 < wristLocation[0] < x2) and (y1 < wristLocation[1] < y2): # using the bounding box to find the intersection
                    gameController.removeRectangle(rectangle)
                    score += 5

def getMusicStats(self, game): # takes 
    audioFile = game.audioFile # 'random.mp3'
    y, sr = librosa.load(audio_file)

    duration = librosa.get_duration(y=y, sr=sr)
    tempoBPM = librosa.beat.beat_track(y=y, sr=sr)
    return (duration, tempoBPM) # returns the duration and tempoBPM

def poseDetection(frame):
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
        right_wrist_x = int(landmarks[16].x * frame.shape[1])
        right_wrist_y = int(landmarks[16].y * frame.shape[0])

        # Left wrist landmark (index is 15)
        left_wrist_x = int(landmarks[15].x * frame.shape[1])
        left_wrist_y = int(landmarks[15].y * frame.shape[0])
    
        return [(right_wrist_x, right_wrist_y), (left_wrist_x, left_wrist_y)]
     
     


        

    

    