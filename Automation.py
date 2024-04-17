import os
import datetime
import speech_recognition as sr
import pyttsx3
from datetime import datetime

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

def Speak(audio):
    # print(" ")
    Assistant.say(audio)
    # print(" ")
    Assistant.runAndWait()

def Notepad():
    Speak("Tell Me the query")
    Speak("Iam Ready to write.")

    writes = takeCommand()
    time = datetime.now().strftime("%H:%M")

    filename = str(time).replace(":","-") + "-note.txt"

    with open(filename,"w") as file:
        file.write(writes)

    path_1 = "E:\\Projects\\Jarvis\\" + str(filename)
    path_2 = "E:\\Projects\\Jarvis\\User data\\Notepad\\" + str(filename)
    os.rename(path_1,path_2)
    os.startfile(path_2)


def CloseNotepad():
    os.system("TASKKILL /F /im Notepad.exe")

Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')
Assistant.setProperty("voice", voices[2].id)  # Selecting the female voice (index 1)
Assistant.setProperty("rate", 150)

