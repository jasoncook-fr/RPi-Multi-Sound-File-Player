import time
import board
import busio
import adafruit_mpr121
from pygame import mixer

channelCount = 2
mixer.init()
mixer.Channel(0).play(mixer.Sound('song1.wav'))
mixer.Channel(1).play(mixer.Sound('song2.wav'))
#mixer.Channel(3).play(mixer.Sound('3.wav'))
#mixer.Channel(4).play(mixer.Sound('4.wav'))

i2c = busio.I2C(board.SCL, board.SDA)
mpr121 = adafruit_mpr121.MPR121(i2c)

myFlag = [False, False]
'''
for i in range(channelCount):
    myFlag.append(False)
'''

while True:
    for i in range(channelCount):
        if mpr121[i].value and myFlag[i] == False:
            print('ON')
            mixer.Channel(i).unpause()
            myFlag[i] = True
        elif mpr121[i].value == False and myFlag[i] == True:
            print('OFF')
            mixer.Channel(i).pause()
            myFlag[i] = False

