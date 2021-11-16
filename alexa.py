import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour < 12:
        speak("Good morning sir!")
    elif hour >=12 and hour < 18:
        speak("Good afternoon sir!")
    else:
        speak("Good Evening sir!")
    
    speak("I am your virtual assistant. How may I help you sir.")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        speak("Please wait for recognition.")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query
    
if __name__ == "__main__":
    wishMe()
    while True:
    #if 1:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching in wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=10)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open code.org' in query or 'open code' in query:
            webbrowser.open("code.org")

        elif 'open whatsappweb' in query or 'open whatsapp' in query or 'open chrome' in query or 'open' in query:
            webbrowser.open("web.whatsapp.com")
        elif 'the time' in query or 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir the time is {strTime}")

        elif 'open code editor' in query or 'open vs code' in query or 'open vs editor' in query or 'open vs' in query:
            code_path = "C:\\Users\hello\\AppData\\Local\\Programs\\Microsoft VS Code\Code.exe"
            os.startfile(code_path)

        else:
            speak("Say that again please...")
