from gtts import gTTS
import os
import pyglet
from time import sleep


def tts(text, lang, tld=None):
    # get audio from server
    tts = gTTS(text=text, lang=lang, tld=tld if tld != None else "com")

    filename = "hello.mp3"
    tts.save(filename)

    music = pyglet.media.load(filename, streaming=False)
    music.play()

    sleep(music.duration)  # prevent from killing
    os.remove(filename)  # remove temperory file
