import board
import busio
import adafruit_mpr121
import pygame
from pygame import mixer
from os import path

snd_dir = "/home/pi/jelly_project/sounds"
channelCount = 4
mixer.init()
pygame.init()
mixer.Channel(0).play(mixer.Sound(path.join(snd_dir, '1.wav')), -1)
mixer.Channel(1).play(mixer.Sound(path.join(snd_dir, '2.wav')), -1)
mixer.Channel(2).play(mixer.Sound(path.join(snd_dir, '3.wav')), -1)
mixer.Channel(3).play(mixer.Sound(path.join(snd_dir, '4.wav')), -1)
#mixer.Channel(3).play(mixer.Sound('3.wav'))
#mixer.Channel(4).play(mixer.Sound('4.wav'))

i2c = busio.I2C(board.SCL, board.SDA)
mpr121 = adafruit_mpr121.MPR121(i2c)

myFlag = []
for i in range(channelCount):
    myFlag.append(False)
    mixer.Channel(i).pause()

while True:
    for i in range(channelCount):
        if mpr121[i].value and myFlag[i] == False:
            print('{} ON'.format(i))
            mixer.Channel(i).unpause()
            myFlag[i] = True
        elif mpr121[i].value == False and myFlag[i] == True:
            print('{} OFF'.format(i))
            mixer.Channel(i).pause()
            myFlag[i] = False

