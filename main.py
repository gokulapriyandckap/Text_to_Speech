import pyttsx3
# import os

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Text to be converted to speech
text = "Hey gokul"

# Convert the text to speech
engine.say(text)

# Play the speech
engine.runAndWait()
