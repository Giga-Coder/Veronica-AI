import os
import speech_recognition as sr

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-in" )
            print(f"User Said: {query}")
            return query
        except Exception as e:
            return "Some Error Occured. Sorry From Veronica"

while True:
    wake_Up = takeCommand()

    if 'wake up' in wake_Up:
        os.startfile("main.py")

    else: print("Nothing")