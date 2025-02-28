import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import pywhatkit


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):

    # Will give audio output

    engine.say(audio)
    engine.runAndWait()

def greet():
    print("Namaste, kya sahayata karu aapki...")
    speak(" Namastay, kya sahayataa karu aapki ")

def command():

    # For voice input

    r=sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold=1
        audio=r.listen(source)
    
    try:
        print("Recognizing.....")
        query=r.recognize_google(audio) 
        print("Command: ",query)
        
    except Exception as e:
        print(" Dubaara kahe.... ")
    return query

if __name__=="__main__" :

    greet()

    while True:

        query=command().lower()
        if 'who' in query:
            speak("Searching Wikipedia....")
            query=query.replace("who","")
            results=wikipedia.summary(query,sentences=4)
            speak("According to wikipedia..")
            print(results)
            speak(results)
        
        elif 'shubham' or 'gaurav' or 'amulya':
            print("He is my creator.")
            speak("He is my creator")

        elif 'youtube' in query:
            webbrowser.open("youtube.com")
        elif 'google' in query:
            webbrowser.open("google.com")
        elif 'time' in query:
            stime=datetime.datetime.now().strftime("%I:%M:%p")
            print("Samay hai "+stime)
            speak("  Samain hai "+stime)
        
        elif 'open vs code' in query:
            vspath="C:\\Users\\ASUS\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(vspath)
        
        elif 'open steam' in query:
            stpath="C:\\Program Files (x86)\\Steam\\steam.exe"
            os.startfile(stpath)
        
        elif 'open unity' in query:
            upath="C:\\Program Files\\Unity\\Hub\\Editor\\2022.3.16f1\\Editor\\Unity.exe"
            os.startfile(upath)
        
        elif 'open pycharm' in query:
            pypath="C:\\Program Files\\JetBrains\\PyCharm Community Edition 2023.3.2\\bin\\pycharm64.exe"
            os.startfile(pypath)

        elif 'play' in query:
            song=query.replace("play","")
            print("Playing...")
            speak("Playing...")
            pywhatkit.playonyt(song)

        elif 'search for' in query:
            query=query.replace("search for","")
            pywhatkit.search(query)

