import pyttsx3

engine = pyttsx3.init()

engine.say('Hello every body')

voices = engine.getProperty('voices')
# engine = setProperty('voice')

engine.runAndWait()

