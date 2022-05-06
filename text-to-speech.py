import os
from pygame import mixer
import time
from gtts import gTTS

os.add_dll_directory(os.getcwd())

text = "Hello mahesh!"
tts = gTTS(text)
tts.save('hi.mp3')

mixer.init()
mixer.music.load("greeting.mp3")
mixer.music.play()
while mixer.music.get_busy():  # wait for music to finish playing
    time.sleep(1)



