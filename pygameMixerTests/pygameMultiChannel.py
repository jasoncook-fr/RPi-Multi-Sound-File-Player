from pygame import mixer
from time import sleep

mixer.pre_init()
mixer.init()
#find another way to change volume
#mixer.music.set_volume(0.3)

while True:
    mixer.Channel(0).play(mixer.Sound('1.wav'))
    mixer.Channel(2).play(mixer.Sound('2.wav'))
    mixer.Channel(3).play(mixer.Sound('3.wav'))
    mixer.Channel(4).play(mixer.Sound('4.wav'))
    sleep(5)
