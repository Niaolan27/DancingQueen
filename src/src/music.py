import math
import random
import mediapipe as mp
import cv2
import timeit
import librosa
import pygame
import os

class Music:
    def __init__(self, title):
        self.initPaths()
        self.songDict = {"I Knew You Were Trouble - Taylor Swift": self.taylor_path,
                         "Sorry - Justin Beiber": self.bieber_path,
                         "Dancing Queen - ABBA": self.abba_path,
                         "Hips Don't Lie - Shakira": self.shakira_path,
                         'Something Just Like This - Coldplay and The Chainsmokers': self.chainsmokers_path}
        self.bpm = 0
        self.duration = 0
        self.audioFile = ""
        print(title)
        self.title = title


    def initPaths(self):

        self.shakira_path = os.path.dirname(__file__)
        relative_path = "res\\shakira-hips_dont_lie.mp3"
        self.shakira_path = os.path.join(self.shakira_path, relative_path)

        self.abba_path = os.path.dirname(__file__)
        relative_path = "res\\abba-dancing.mp3"
        self.abba_path = os.path.join(self.abba_path, relative_path)

        self.chainsmokers_path = os.path.dirname(__file__)
        relative_path = "res\\chainsmokers-coldplay.mp3"
        self.chainsmokers_path = os.path.join(self.chainsmokers_path, relative_path)

        self.bieber_path = os.path.dirname(__file__)
        relative_path = "res\\justin_bieber-sorry.mp3"
        self.bieber_path = os.path.join(self.bieber_path, relative_path)

        self.taylor_path = os.path.dirname(__file__)
        relative_path = "res\\taylor_swift-trouble.mp3"
        self.taylor_path = os.path.join(self.taylor_path, relative_path)
        
    
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
    
    
