import smtplib

import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess

from PIL import ImageGrab
from ecapture import ecapture as ec
import wolframalpha
import json
import requests
import ctypes
import struct

from uptime import uptime

print('Loading your AI personal assistant - Maryo')

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', 'voices[0].id')

def browser():
    os.system("start chrome.exe")


def music():
    os.system("start wmplayer.exe")


# close apps
def musicClose():
    os.system("taskkill /IM wmplayer.exe /F")


def stopBrowser():
    os.system("taskkill /IM chrome.exe /F")


def speak(text):
    engine.say(text)
    engine.runAndWait()


def wishMe():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak("Hello,Good Morning")
        print("Hello,Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening")
        print("Hello,Good Evening")

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('senderemail@gmail.com', 'sender-password')
    server.sendmail('senderemail@gmail.com', to, content)
    server.close()

def takeCommand():
     r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

        try:
            statement = r.recognize_google(audio, language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("Pardon me, please say that again")
            return "None"
        return statement


speak("Loading your AI personal assistant Maryo")
wishMe()

if __name__ == '__main__':

    while True:
        speak("Tell me how can I help you now?")
        statement = takeCommand()
        if statement == 0:
            continue

        if "good bye" in statement or "ok bye" in statement or "stop" in statement:
            speak('your personal assistant Maryo is shutting down,Good bye')
            print('your personal assistant Maryo is shutting down,Good bye')
            break

        if 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement = statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'take screenshot' in statement:
            image = ImageGrab.grab()
            image.show()
            speak('Here is screenshot of current screen')

        elif 'computer uptime' in statement:
            s = uptime()
            m, s = (divmod(s, 60))
            h, m = divmod(m, 60)
            d, h = divmod(h, 60)
            hr=int(h)
            mint=int(m)
            speak(f'Your computer was started {hr}{mint} before ')
            print(
                int(h), 'hrs', '', int(m), 'min'
            )

        elif 'open browser' in statement:
            browser()
            speak('your browser has started')

        elif 'close browser' in statement:
            stopBrowser()
            speak('your browser has been closed')

        elif 'open mediaplayer' in statement:
            music()
            speak('your mediaplayer is opened now')

        elif 'close mediaplayer' in statement:
            musicClose()
            speak('your mediaplayer has been closed')

        elif 'which architecture' in statement:
            pi = struct.calcsize('P') * 8
            print(pi)

        elif 'empty recycle bin' in statement:
            os.system('rd /s c:\$Recycle.Bin /q')

        elif 'change background' in statement:
            SPI_SETDESKWALLPAPER = 20
            path = b'wallpaper\\aerial-view-of-beautiful-spring-landscape-with-ita-HPA3RNS.jpg'
            ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path, 3)

        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
            time.sleep(5)

        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome is open now")
            time.sleep(5)

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail open now")
            time.sleep(5)

        elif "weather" in statement:
            api_key = "8ef61edcf1c576d65d836254e11ea420"
            base_url = "https://api.openweathermap.org/data/2.5/weather?"
            speak("whats the city name")
            city_name = takeCommand()
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name
            response = requests.get(complete_url)
            x = response.json()
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))

            else:
                speak(" City Not Found ")



        elif 'time' in statement:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        elif 'who are you' in statement or 'what can you do' in statement:
            speak('I am Maryo version 1 point O your persoanl assistant. I am programmed to minor tasks like'
                  'opening youtube,google chrome,gmail and stackoverflow ,predict time,take a photo,search wikipedia,predict weather'
                  'in different cities , get top headline news from times of india and you can ask me computational or geographical questions too!')


        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built by Qasim uddin")
            print("I was built by Qasim")

        elif "open stackoverflow" in statement:
            webbrowser.open_new_tab("https://stackoverflow.com/login")
            speak("Here is stackoverflow")

        elif 'news' in statement:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India,Happy reading')
            time.sleep(6)

        elif "camera" in statement or "take a photo" in statement:
            ec.capture(0, "robo camera", "img.jpg")

        elif 'search' in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(5)

        elif 'send email' in statement:
            try:
                speak("What should I say?")
                content = statement
                to = "recieverEmail@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry there is an issue. Try again")

        elif 'ask' in statement:
            speak('I can answer to computational and geographical questions and what question do you want to ask now')
            question = takeCommand()
            app_id = "R2K75H-7ELALHR35X"
            client = wolframalpha.Client('R2K75H-7ELALHR35X')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)


        elif "log off" in statement or "sign out" in statement:
            speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])

time.sleep(3)
