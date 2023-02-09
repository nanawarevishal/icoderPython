import sys
import pyttsx3
from pyttsx3.drivers import sapi5
import datetime
import  speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib



engine = pyttsx3.init("sapi5")  # to take input of the voice command
voices = engine.getProperty("voices")
# print(voices[1].id)

engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio) 
    engine.runAndWait()
    

def wishMe():
    hour = int(datetime.datetime.now().hour)

    if(hour >=0 and hour < 12):
        speak("Good Morning Sir....!")

    elif (hour>=12 and hour < 18):
        speak("Good Afternoon Sir..!")

    else:
        speak("Good Evening sir...!")

    speak("Hello sir, I am Friaday. Please tell how may i can help you? ")


def takeCommand():
    # It takes the command as the input from the user and return string output
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...!")

        r.pause_threshold =  1
        audio = r.listen(source)

    try:
        print("Recognising...!")
        query = r.recognize_google(audio,language="en-in")

        print(f"User said : {query}\n")

    except Exception as e:
        # print(e)
        speak("Sorry Sir i am not able to understand it say it again....!")
        return "None"

    return query





if __name__=="__main__":
    
    wishMe()

    while(True):
        query = takeCommand().lower()

        #  Logic to executing tasks based on the query

        if 'wikipedia' in query:
          speak("Searching Wikipedia......!")
          query = query.replace("wikipedia","")
          results = wikipedia.summary(query,sentences=2)
          speak("According to wikipedia")
          print(results)
          speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open get Bootstrap' in query:
            webbrowser.open("getboostrap.com")

        elif 'play music' in query:
            music_dir = "C:\\Users\\DELL\\Music"
            songs = os.listdir(music_dir)
            print(songs)
            a = random.randrange(0,len(songs))
            # print(a)
            os.startfile(os.path.join(music_dir,songs[a]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is {strTime}")

        elif 'open code' in query:
            vsCodeDir = "C:\\Users\\DELL\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(vsCodeDir)

        # elif 'email to Harry' in query:
        #     try:
        #         speak("What should i say?")
        #         content = takeCommand()
        #         to = "harry@gmail.com"
        #         sendEmail(to,content)
        #         speak("Email has been sent")
        #
        #     except Exception as e:
        #         speak("Sorry Sir i am not able sent the email...!")

        elif 'quit' in query:
            speak("Thank you sir have a Good day")
            sys.exit()

        
