'''
                                        .......VERONICA CODE.......
    DEVELOPED BY: DIVYANSH SHARMA
    DEVELOPED ON: 25-05-2023
    TITLE:   VERONICA an AI VIRTUAL ASSISTANT
'''

import speech_recognition as sr
import os
import win32com.client
import webbrowser
import openai
import datetime
from config import apikey
import requests
import urllib.request
from datetime import datetime
import psutil         #battery finder
import speedtest #Speedtest
import pyautogui  # volume manage
import cv2
import pyttsx3
import pywhatkit
# import whatsapp
import pygame
import keyboard


# ALL FUNCTIONS START.................
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
def play_music(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
def stop_music():
    pygame.mixer.music.stop()

def change_music(file_path):
    stop_music()
    play_music(file_path)

def music():
    Speak("Playing Music Sir")
    print("Playing......")
    file_path = "Music\entry_song.mp3"
    play_music(file_path)

    while True:
        if keyboard.is_pressed('0'):  # Press 's' to change music
            Speak("Playing Another Music Sir")
            new_file_path = "Music\entry_song.mp3"
            change_music(new_file_path)

        if keyboard.is_pressed('1'):  # Press 's' to change music
            Speak("Playing Another Music Sir")
            new_file_path = "Music\sad.mp3"
            change_music(new_file_path)

        if keyboard.is_pressed('2'):  # Press 'm' to change music
            Speak("Playing Another Music Sir")
            new_file_path = "Music\mood.mp3"
            change_music(new_file_path)

        if keyboard.is_pressed('3'):  # Press 'a' to change music
            Speak("Playing Another Music Sir")
            new_file_path = "Music\loving.mp3"
            change_music(new_file_path)

        if keyboard.is_pressed('e'):  # Press 'e' to exit
            Speak("Music is now stop! Sir")
            stop_music()
            break


chatStr = ""
def Speak(audio):
    # print(" ")
    Assistant.say(audio)
    # print(" ")
    Assistant.runAndWait()

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


def TaskExecution():
    pyautogui.press("esc")
    print("Verification Successful...")
    Speak("Verification Successful")
    print("Welcome Back Divyansh Sir")
    Speak("Welcome Back Divyansh Sir")

# ChatGPT chatting with User
def chat(query):
    global chatStr
    # print(chatStr)
    openai.api_key = apikey
    chatStr +=  f"Sir: {query}\n Veronica: "
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt= chatStr,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    Speak((response["choices"][0]["text"]))
    chatStr +=f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]
    # with open(f"Openai/prompt-{random.randint(1, 2343434356)}", "w") as f:
    with open(f"User data/{''.join(prompt.split('intelligence')[1:]).strip()}.txt", "w") as f:
        f.write(text)



# ChatGPT User task requests
def ai(prompt):
    openai.api_key = apikey
    text = f"OpenAI response for Prompt: {prompt} \n *********************\n\n"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    print(response["choices"][0]["text"])
    text +=response["choices"][0]["text"]   #file write with text in it

    # OpenAI Folder creation if not exists
    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    # with open(f"Openai/prompt-{random.randint(1, 2343434356)}", "w") as f:
    with open(f"User data/{''.join(prompt.split('intelligence')[1:]).strip() }.txt", "w") as f:
        f.write(text)


def get_weather(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    weather_data = response.json()
    temperature = weather_data["main"]["temp"]
    weather = weather_data["weather"][0]["description"]
    return temperature, weather


def verify_password():
    password = "1234"  # Change to your desired password
    print("Enter your Password:=> ")
    Speak("Enter your Password Sir")
    user_password = input()
    if user_password == password:
        print("Password verified successfully!")
        TaskExecution()
        return True
    else:
        print("Incorrect password!")
        return False

# # Prompt the user to choose password verification or face recognition
# max_attempts = 5
# attempt_counter = 0
#
# while attempt_counter < max_attempts:
#     if verify_password():
#             print("Access granted!")
#             Speak("Access granted! Welcome Sir")
#             break  # Exit the loop if access is granted
#     else:
#             attempt_counter += 1
#             print("Access denied!")
#             Speak("Access denied. Please enter correct password again")
#
#
# if attempt_counter >= max_attempts:
#     print("Maximum number of attempts reached. Exiting program.")
#     Speak("Maximum number of attempts reached. Exiting program.")
#     exit()
# else:
#     print("Welcome!")
#
# # End of the code
#

# Microphone Listening

# Tasks
# Repeated task
def TaskExe():
    while True:
                                    # todo listening
        print("Listening...")
        query= takeCommand()
        print("Recognizing......")
        # Speak(query)
        sites = [["youtube", "https://www.youtube.com"], ["wikipedia","https://www.wikipedia.com"],["google", "https://www.google.com"],["flipkart", "https://www.flipkart.com/"],["Amazon", "https://www.amazon.in/"],["pdf editor", "https://www.sejda.com/pdf-editor"],["pdf converter", "https://www.freepdfconvert.com/"],["facebook", "https://www.facebook.com/"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                Speak(f"Opening {site[0]} Sir...")
                webbrowser.open(site[1])

        # Date and time
        if "the time" in query:
            strfTime = datetime.datetime.now().strftime("%H:%M:%S")
            Speak(f"Sir the time is {strfTime}")


 #todo Image Generator
        elif "image".lower() in query:
            openai.api_key = apikey
            # user_prompt = input("Please describe the image: ")
            print("Please describe the image: ")
            Speak("Please describe the image you would like in a short sentence")
            print("Listening...")
            user_prompt = takeCommand()
            print("Generating the image. Please wait...")
            Speak("Generating the image. Give me some time...")
            response = openai.Image.create(
                prompt=user_prompt,
                n=1,
                size="1024x1024"
            )

            image_url = response['data'][0]['url']
            print(image_url)
            Speak("Image has been Generated...")
            final_name = user_prompt.split("of")[1:]
            print(final_name)

            file_name = ''.join(final_name) + datetime.now().strftime('%Y-%d-%H-%M') + ".png" ''
            file_path = os.path.join("User data/Images", file_name)
            urllib.request.urlretrieve(image_url, file_path)
            Speak("Your desired PNG file has been saved in your desired Location")


    # todo Weather report of desired cities
        elif "weather report" in query :
            # Replace 'YOUR_API_KEY' with your actual API key
            api_key = "7e6ca7423b56a66527829e134cbbdbed"
            Speak("Please Provide me the name of city:")
            query = takeCommand()
            city = query
            temperature, weather = get_weather(api_key, city)
            # temp = print(f"The temperature in {city} is {temperature}°C.")
            print(f"The temperature in {city} is {temperature}°C.")
            Speak(f"The temperature in {city} is {temperature}°C.")
            print(f"Today's weather is {weather}.")
            Speak(f"Today's weather is {weather}.")


        elif "Using artificial intelligence".lower() in query.lower():
            ai(prompt=query)

            # Chatting with user

    # Basic Function done by Veronica
        elif "Veronica Quit".lower() in query.lower() or "Quit".lower() in query.lower() or "Stop".lower() in query.lower():
            Speak("Alright Sir! Meet you soon ")
            exit()

        elif "reset chat".lower() in query.lower() or "clear".lower() in query.lower():
            Speak("Chat Has been Reseted")

        
        # playing music 
        elif 'music' in query:
            music()
           

        elif "tell me something about you".lower() in query.lower()  or "who are you ".lower() in query.lower() or "about you".lower() in query.lower():
            Speak("Ladies and gentlemen,Today, I am thrilled to introduce myself, Veronica, your personal Artificial Intelligence Assistant. My name, Veronica, stands for 'Just A Rather Very Intelligent System'. Developed and designed by Divyansh , I am the culmination of years of research and technological innovation.")

        elif "developer".lower() in query.lower() or "made you".lower() in query.lower() or "invented you".lower()in query.lower() or "your inventer".lower() in query.lower():
            Speak("My Developer name is Divyansh")

    # Battery check in system

        elif "how much power left" in query or "how much power we have" in query or "battery" in query:
            battery = psutil.sensors_battery()
            percentage = battery.percent
            print(percentage)
            Speak(f"sir our system have {percentage} percent battery")
            if percentage<40:
                Speak("Please Charge Up your Laptop. Battery is below 40 Percent")

    # Internet speed check in system
        elif "internet speed" in query:
            st = speedtest.Speedtest()
            dl = st.download()
            up = st.upload()
            dl_mbps = int(dl/1000000)
            up_mbps = int(up/1000000)
            print(f"Downloading Speed: {dl_mbps} Mbps\nUploading Speed: {up_mbps} Mbps")
            Speak(f"Sir we have {dl_mbps}Megabit per second downloading speed and {up_mbps} Megabit per second uploading speed ")
            
    # Volume adjusting
        elif 'volume up' in query:
            pyautogui.press("volumeup")
        elif 'volume down' in query:
            pyautogui.press("volumedown")
        elif'volume mute' in query or 'mute' in query:
            pyautogui.press("volumemute")


        elif 'youTube search'.lower() in query.lower():
            Speak("Ok Sir, This is best I can found for your search!")
            query = query.replace("Veronica","")
            query = query.replace("youTube search","")
            web = "https://www.youtube.com/results?search_query=" + query
            webbrowser.open(web)
            Speak("Done Sir!")

        elif 'google search' in query.lower():
            Speak("This is what I found for your Search Sir!")
            query = query.replace("Veronica","")
            query = query.replace("Google search","")
            pywhatkit.search(query)
            Speak("Done Sir!")


        elif 'screenshot' in query:
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
            screenshot_path = f"User data/Screenshots/screenshot_{timestamp}.png"
            pyautogui.screenshot(screenshot_path)
            Speak("Screenshot has been Captured")

        elif 'write a note' in query:
            from Automation import Notepad
            Notepad()

        elif 'dismiss' in query:
            from Automation import CloseNotepad
            CloseNotepad()



        elif "jarvis" or "Chatgpt" or "" in query:
            Speak("My name is veronica! Sir. Please Call me again by my name.")


        # elif 'send message' in query.lower():
        #     query = query.replace("veronica","")
        #     query = query.replace("send", "")
        #     query = query.replace("whatsapp message", "")
        #     query = query.replace("to", "")
        #     name = query
        #     Speak("Waiting Sir....")
        #     if"anshu" in name.lower():
        #         numb = "8219939225"
        #         Speak(f"What's the messsage for {name}")
        #         mess = takeCommand()
        #         whatsapp.whatsapp(numb,mess)
        #
        #     elif 'shubham' in name:
        #         numb = ""
        #         Speak(f"What's the messsage for {name}")
        #         mess = takeCommand()
        #         whatsapp.whatsapp(numb, mess)
        #
        #     elif 'now' in name:
        #         gro = ""
        #         Speak(f"What's the message for {name}")
        #         mess = takeCommand()
        #         whatsapp.Whatsapp_Grp(gro, mess)


        else:
            print("Chatting...")
            chat(query)

# FUNCTION ENDS HERE...............

# Code start here
clear_terminal()
                                    # Speaking
Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')
Assistant.setProperty("voice", voices[1].id)  # Selecting the female voice (index 1)
Assistant.setProperty("rate", 150)

# while 1:
print("Hello! Iam Veronica an AI")
Speak("Hello! Iam Veronica an virtual AI Assistant. ")
Speak("How may I help you ...")

TaskExe()




