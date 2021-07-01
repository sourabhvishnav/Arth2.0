import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import subprocess


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak('Good Morning')

    elif hour >= 12 and hour < 18:
        speak('Good Afternoon')

    else:
        speak('Good Evening')

    speak('I am Arth How can I help you')


def takeComand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print('You said : ', query)

    except Exception as e:
        print(e)
        print('Say that again Please')
        return "None"

    return query


if __name__ == "__main__":
    wish()
    while True:
        query = takeComand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=5)
            speak('According To Wikipedia')
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
        elif 'open google' in query:
            webbrowser.open('google.com')
        elif 'open github' in query:
            webbrowser.open('github.com')
        elif 'open instagram' in query:
            webbrowser.open('instagram.com')
        elif 'open chrome' in query:
            path = r"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(path)
        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open(
                "https://www.google.nl/maps/place/"+location + "")
        elif 'exit' in query:
            speak("Thanks for giving me your time")
            exit()
