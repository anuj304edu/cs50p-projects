import cowsay
import pyttsx3
engine = pyttsx3.init()
this = input("what's this? ")
cowsay.tux(this)
engine.say(this)
engine.runAndWait()
