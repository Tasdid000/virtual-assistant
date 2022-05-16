import pyttsx3
import speech_recognition as sr
import datetime
import pywhatkit
import wikipedia  #pip install wikipedia
import webbrowser
import os
import smtplib
import requests
from bs4 import BeautifulSoup
from wikipedia.wikipedia import search


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour <= 11:
        speak("Good Morning Siam!")
    elif 12 <= hour <= 18:
        speak("Good Afternoon Siam!")
    else:
        speak("Good night Siam!")
    speak("It's")
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    print("It's" +" " + strTime)
    speak(strTime)
    speak("Hi I am mili. How can i help you master")
    '''search="temperature is sylhet"
    url = f"https://www.google.com/search?q={search}"
    r = requests.get(url)
    data= BeautifulSoup(r.text,"html.parser")
    temp = data.find("div", class_="BNeawe").text
    print(f"The current {search} is {temp}")
    speak(f"The current {search} is {temp}")
    speak("I'm mele. How can i help you siam?")'''



def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone(device_index=0) as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")

        query = r.recognize_google(audio, language='en-in')  # Using google for voice recognition.

        print(f"User said: {query}\n")
    except Exception as e:
        #print(e)
        print("Say any thing...")  # Say that again will be printed in case of improper voice
        return "None"  # None string will be returned
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    sender_email = open("H:\\siam\\si\\email.txt", "r").read()
    sender_pass = open("H:\\siam\\si\\password.txt", "r").read()
    server.login(sender_email, sender_pass )
    server.sendmail(sender_email, to, content)
    server.close()



if __name__ == "__main__":
    wishme()
    while True:
        # if 1:
        query = takeCommand().lower()  # Converting user query into lower case

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak("Opening youtube")

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
            speak("Opening facebook")

        elif 'open classroom' in query:
            webbrowser.open("classroom.google.com")
            speak("Opening Google classroom")

        elif 'open google' in query:
            speak("Opening Google")
            webbrowser.open("google.com")

        elif 'open gmail' in query:
            speak("Opening Gmail")
            webbrowser.open("gmail.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
            speak("Opening stackoverflow")

        elif 'what is your name' in query:
            speak("My name is mele")
        elif 'hey mili' in query:
            speak("Hi Siam. How can I help you?")

        elif 'who are you' in query:
            speak("I'm the personal assistant of my master Tasdid .")

        elif 'who gave your name' in query:
            speak("This name is given to my sir siam.")

        elif 'who is your boss' in query:
            speak("His name is Tasdid Hasnain. He is a university student. He study in Bsc in cse from Metropolitan University. He live in sylhet, Bangladesh.")

        elif 'who am i' in query:
            speak("Your nane is Tasdid Hasnain. You are a university student. You study in Bsc in cse from Metropolitan University. You live in sylhet, Bangladesh.")

        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
            speak("Opening play music")

        elif 'what time is it' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir, the time is {strTime}")


        elif 'open vs code' in query:
            speak("Opening vs code")
            codePath = "C:\\Users\\Public.DESKTOP-RDP38Q2\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open pycharm' in query:
            speak("Opening pycharm")
            codePath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2021.2.2\\bin\\pycharm64.exe"
            os.startfile(codePath)


        elif 'send email' in query:
            speak("Opening email.")
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "hasubul.syl@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Siam. I am not able to send this email")

        elif'play' in query:
            song = query.replace("play", "")
            speak("playing" + song)
            pywhatkit.playonyt(song)

        elif 'temperature' in query:
            search="temperature is sylhet"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data= BeautifulSoup(r.text,"html.parser")
            temp = data.find("div", class_="BNeawe").text
            speak(f"Current {search} is {temp}")
            print(f"Current {search} is {temp}")

        elif 'stop mili' in query:
            speak("Good by Siam! See you again and love you siam.")
            exit()

