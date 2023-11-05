import math
import random
import mediapipe as mp
import cv2
import timeit
import librosa

class Music:
    def __init__(self, title):
        self.songDict = {'I knew you were trouble - Taylor Swift': file1, 'Sorry - Justin Beiber': file2, 'Dancing Queen - ABBA': file3, "Hips don't lie - Shakira": file4, "Something just like this - Coldplay": file5}
        self.bpm = 0
        self.duration = 0
        self.audioFile = ""
    
    def getAudioFile(self, title):
        self.audioFile = self.songDict[title]
        return self.audioFile

    def getMusicStats(self, title):
        audioFile = self.getAudioFile(title) # 'random.mp3'
        y, sr = librosa.load(audioFile)

        duration = librosa.get_duration(y=y, sr=sr)
        tempoBPM = librosa.beat.beat_track(y=y, sr=sr)
        return (duration, tempoBPM) 
    
    
