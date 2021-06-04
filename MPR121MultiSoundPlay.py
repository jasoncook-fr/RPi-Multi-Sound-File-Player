#!/usr/bin/python3
'''
On a Raspberry Pi, using a proximity capacitve touch sensor controller - MPR121
The mixer function from the pygame module is used to play multiple channels of
sound when designated touch sensors are activated.
Sound files are to be prepared 16-bit wav.
The user must place the sound files in the declared folder before launching the program.
It is preferable to number your files as such: 001.wav 002.wav 003.wav ... and so on
'''
import board
import busio
import adafruit_mpr121
import pygame
from pygame import mixer
from os import path
import os

# declare directory path for sound files
snd_dir = "/home/pi/jelly_project/sounds"

# declare an empty sound file list
sndFile = []

# discover available sound files and add them to our list (sndFile.append())
for root, dirs, files in os.walk(snd_dir):
    count = 0
    for file in files:
        if file.endswith('.wav'):
            sndFile.append(str(file))
            count += 1

# establish total of .wav files discovered, store the number in a variable
channelCount = len(sndFile)

# initialise pygame and mixer
mixer.init()
pygame.init()
mixer.set_num_channels(channelCount)

# prepare I2C bus
i2c = busio.I2C(board.SCL, board.SDA)
mpr121 = adafruit_mpr121.MPR121(i2c)

playFlag = []
for i in range(channelCount):
    playFlag.append(False)
    mixer.Channel(i).play(mixer.Sound(path.join(snd_dir, sndFile[i])), -1)
    mixer.Channel(i).pause()

while True:

    for i in range(channelCount):
        if mpr121[i].value and playFlag[i] == False:
            print('{} ON'.format(i))
            mixer.Channel(i).unpause()
            playFlag[i] = True
        elif mpr121[i].value == False and playFlag[i] == True:
            print('{} OFF'.format(i))
            mixer.Channel(i).pause()
            playFlag[i] = False

