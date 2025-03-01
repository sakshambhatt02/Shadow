import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import pywhatkit
import screen_brightness_control as sbc  # Brightness Control Module


# Initialize text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    """Converts text to speech."""
    engine.say(audio)
    engine.runAndWait()

def greet():
    """Greets the user."""
    print("Namaste, kya sahayata karu aapki...")
    speak("Namaste, kya sahayataa karu aapki")

def command():
    """Listens to voice input and returns recognized text."""
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print(f"Command: {query}")
        return query.lower()

    except Exception as e:
        print("Dubaara kahe...")
        return "None"

if __name__ == "__main__":
    greet()

    while True:
        query = command()

        if query == "None":
            continue  # If no command is received, listen again

        # Wikipedia Search
        if 'who' in query:
            speak("Searching Wikipedia...")
            query = query.replace("who", "")
            try:
                results = wikipedia.summary(query, sentences=2)
                print(results)
                speak(results)
            except wikipedia.exceptions.DisambiguationError as e:
                speak("The search term is ambiguous. Please be more specific.")
            except wikipedia.exceptions.PageError:
                speak("Sorry, I couldn't find any relevant information.")

        # Recognizing Creators
        elif 'saksham' in query or 'ayush' in query:
            print("He is my creator.")
            speak("He is my creator.")

        elif 'keya' in query or 'anamika' in query:
            print("She is my creator.")
            speak("She is my creator.")

        # Opening Websites
        elif 'youtube' in query:
            webbrowser.open("https://www.youtube.com")

        elif 'google' in query:
            webbrowser.open("https://www.google.com")

        # Telling Time
        elif 'time' in query:
            stime = datetime.datetime.now().strftime("%I:%M %p")
            print(f"Samay hai {stime}")
            speak(f"Samay hai {stime}")

        # Opening VS Code
        elif 'open vs code' in query:
            vspath = "C:\\Users\\ASUS\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(vspath)

        # Playing a song on YouTube
        elif 'play' in query:
            song = query.replace("play", "").strip()
            print(f"Playing {song} on YouTube...")
            speak(f"Playing {song} on YouTube...")
            pywhatkit.playonyt(song)

        # Google Search
        elif 'search for' in query:
            search_query = query.replace("search for", "").strip()
            print(f"Searching for {search_query} on Google...")
            speak(f"Searching for {search_query} on Google...")
            pywhatkit.search(search_query)

        # **Brightness Control**
        elif 'increase brightness' in query:
            current_brightness = sbc.get_brightness()
            new_brightness = min(current_brightness[0] + 10, 100)  # Increase by 10%, max 100%
            sbc.set_brightness(new_brightness)
            print(f"Brightness increased to {new_brightness}%")
            speak(f"Brightness increased to {new_brightness} percent")

        elif 'decrease brightness' in query:
            current_brightness = sbc.get_brightness()
            new_brightness = max(current_brightness[0] - 10, 0)  # Decrease by 10%, min 0%
            sbc.set_brightness(new_brightness)
            print(f"Brightness decreased to {new_brightness}%")
            speak(f"Brightness decreased to {new_brightness} percent")

        elif 'set brightness to' in query:
            try:
                brightness_value = int(query.split()[-1])  # Extract number from command
                brightness_value = max(0, min(brightness_value, 100))  # Keep within 0-100 range
                sbc.set_brightness(brightness_value)
                print(f"Brightness set to {brightness_value}%")
                speak(f"Brightness set to {brightness_value} percent")
            except ValueError:
                print("Invalid brightness value")
                speak("Invalid brightness value. Please specify a number between zero and one hundred.")

        # Exit the program
        elif 'exit' in query or 'quit' in query or 'bye' in query:
            print("Thank you for using me.")
            speak("Thank you for using me. Have a great day!")
            break
