# Jarvis Project
# pip install pyqt5
# pip install speechrecognition
# pip install pyttsx3
# pip install pyaudio
# pip install wikipedia

import speech_recognition as sr
import datetime
import wikipedia
import pyttsx3
import webbrowser
import random
import os
import requests

# Text to Speech
# Make a speaker who speaks your attachs

engine = pyttsx3.init()

voices = engine.getProperty('voices')
# print(voices)

engine.setProperty('voice', voices[0].id) # Selecting 1nd Voice

def speak(audio): # Here Audio is var which contain text
    engine.say(audio) 
    engine.runAndWait() # Wait

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning sir i am Virtual Assistant Jarvis")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon sir i am Virtual Assistant Jarvis")
    else:
        speak("Good night sir i am Virtual Assistant Jarvis")

# Now convert audio to text

def takecom():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        audio = r.listen(source)
    try:
        print("Recognising.")
        text = r.recognize_google(audio, language='en-in') # Use Google Api
        print(text)
    except Exception:          # Error handling
        speak("Error....")
        print("Network connection error")
        return "none"
    return text

def temperature(city):
    api_add = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=' # Here add appid 
    print(api_add);
    json_data = requests.get(api_add).json()
    temp = json_data["main"]["temp"]
    cond = json_data["weather"][0]["description"]
    name = json_data["name"]
    speak(f"temperature of {name} is {temp} degree celcius and the condition is {cond}")
    print(f"temperature of {name} is {temp} degree celcius and the condition is {cond}")


# For Main Function

if __name__ == "__main__":
    wish()  # Jarvis Wishes u at the start
    while True:
        query = takecom().lower()

        if "wikipedia" in query:
            speak("Searching details......Wait")
            query.replace("wikipedia", "")
            results = wikipedia.summery(query, sentences=2)
            print(results)
            speak(results)
        elif "temperature of" in query:
            speak("please wait")
            idx = query.index("f") + 2
            city = query[idx:]
            temperature(city)
        elif 'open youtube' in query or "open video online" in query:
            webbrowser.open("https://www.youtube.com")
            speak("opening youtube")
        elif 'open google' in query:
            webbrowser.open("https://www.google.com")
            speak("opening google")
        elif 'open facebook' in query:
            webbrowser.open("https://www.facebook.com")
            speak("opening facebook")
        elif 'open gmail' in query:
            webbrowser.open("https://www.gmail.com")
            speak("opening gmail")
        elif 'open github' in query:
            webbrowser.open("https://www.github.com")
            speak('opening github')
        elif 'music from pc' in query or "music" in query:
            speak("ok i am playing music")
            music_dir = './music'
            musics = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, musics[0])) 
        elif 'video from pc' in query or "video" in query:
            speak("ok i am playing videos")
            video_dir = "./video"
            videos = os.listdir(video_dir)
            os.startfile(os.path.join(video_dir, videos[0]))
        elif 'good bye' in query:
            speak("Good Bye")
            exit()
        elif "shutdown" in query:
            speak("shutting down")
            os.system('shutdown -s')  # Shut Down Pc
        elif "whats up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!',
                      'I am nice and full of energy', 'i am okey ! How are you']
            ans_q = random.choice(stMsgs)
            speak(ans_q)
            ans_take_from_user_how_are_you = takecom()
            if 'fine' in ans_take_from_user_how_are_you or 'happy' in ans_take_from_user_how_are_you or 'okey' in ans_take_from_user_how_are_you:
                speak('okey..')
            elif 'not' in ans_take_from_user_how_are_you or 'sad' in ans_take_from_user_how_are_you or 'upset' in ans_take_from_user_how_are_you:
                speak('oh sorry..')
        elif 'make you' in query or 'created you' in query or 'develop you' in query:
            ans_m = " For your information Aritra Sen Created me ! I give Lot of Thannks to Him "
            print(ans_m)
            speak(ans_m)
        elif "who are you" in query or "about you" in query or "your details" in query:
            about = "I am Jarvis an A I based computer program but i can help you lot like a your close friend ! i promise you ! Simple try me to give simple command ! like playing music or video from your directory i also play video and song from web or online ! i can also entain you i so think you Understand me ! ok Lets Start "
            print(about)
            speak(about)
        elif "hello" in query or "hello Jarvis" in query:
            hel = "Hello Aritra Sir ! How May i Help you.."
            print(hel)
            speak(hel)
        elif "your name" in query or "sweat name" in query:
            na_me = "Thanks for Asking my name my self ! Jarvis"
            print(na_me)
            speak(na_me)
        elif "you feeling" in query:
            print("feeling Very sweet after meeting with you")
            speak("feeling Very sweet after meeting with you")
        elif query == 'none':
            continue
        elif 'exit' in query or 'abort' in query or 'stop' in query or 'bye' in query or 'quit' in query:
            ex_exit = 'I feeling very sweet after meeting with you but you are going! i am very sad'
            speak(ex_exit)
            exit()
        else:
            temp = query.replace(' ', '+')
            g_url = "https://www.google.com/search?q="
            res_g = 'sorry! i cant understand but i search from internet to give your answer ! okay'
            print(res_g)
            speak(res_g)
            webbrowser.open(g_url+temp)
