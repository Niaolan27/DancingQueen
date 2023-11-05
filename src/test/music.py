import math
import random
import mediapipe as mp
import cv2
import timeit
import librosa
import pygame

class Music:
    def __init__(self, title):
        self.songDict = {"I Knew You Were Trouble - Taylor Swift": 'C:\\Users\\wands\\Documents\\CS_15112\\hack112\\taylor_swift-trouble.mp3',
                         "Sorry - Justin Beiber": 'C:\\Users\\wands\\Documents\\CS_15112\\hack112\\justin_bieber-sorry.mp3',
                         "Dancing Queen - ABBA": 'C:\\Users\\wands\\Documents\\CS_15112\\hack112\\abba-dancing.mp3',
                         "Hips Don't Lie - Shakira": 'C:\\Users\\wands\\Documents\\CS_15112\\hack112\\shakira-hips_dont_lie.mp3',
                         "Something Just Like This - Coldplay": 'C:\\Users\\wands\\Documents\\CS_15112\\hack112\\chainsmokers-coldplay.mp3'}
        self.bpm = 0
        self.duration = 0
        self.audioFile = ""
        print(title)
        self.title = title
        
    
    def getAudioFile(self):
        self.audioFile = self.songDict[self.title]
        return self.audioFile

    def getMusicStats(self):
        audioFile = self.getAudioFile() # 'random.mp3'
        y, sr = librosa.load(audioFile)

        self.duration = librosa.get_duration(y=y, sr=sr)
        self.bpm = librosa.beat.beat_track(y=y, sr=sr)[0]
        return (self.duration, self.bpm)
     
    def loadMusic(self):
        pygame.init()
        pygame.mixer.music.load(self.audioFile)

    def start(self):
        pygame.mixer.music.play(loops=1)

    def stop(self):
        pygame.mixer.music.stop()
    
    
