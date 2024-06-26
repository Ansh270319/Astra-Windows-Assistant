from fastapi.security import APIKeyQuery
import speech_recognition as sr 
import os
import webbrowser
import datetime
import pygame
import openai
import random

def ai(prompt):
    openai.api_key = APIKeyQuery
    response = openai.Completions.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    ai_response = response.choices[0].text.strip()
    print(ai_response)

    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    with open(f"Openai/prompt-{random.randint(1, 234234356)}.txt", "w") as file:
        file.write(f"Prompt: {prompt}\n")
        file.write(f"Response: {ai_response}\n")

    return ai_response

def say(text):
    os.system(f"say {text}")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.6
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}") 
            return query
        except Exception as e:
            print(f"Error: {e}")
            return "Some Error Occurred. Sorry"

def play_music(song_name):
    music_directory = "C:/Users/Admin/Documents/Rockstar Games/GTA V/User Music"
    song_path = None
    for root, dirs, files in os.walk(music_directory):
        for file in files:
            if song_name.lower() in file.lower():
                song_path = os.path.join(root, file)
                break
        if song_path:
            break

    if song_path:
        pygame.mixer.init()
        pygame.mixer.music.load(song_path)
        pygame.mixer.music.play()
        say(f"Playing {song_name}")
    else:
        say("Song not found")

if __name__ == '__main__':
    print("Admin")    
    say("Hello, I am ASTRA")
    while True:
        print("Listening....")
        query = takecommand().lower()

        sites = [
            ["youtube", "https://youtube.com/"], 
            ["wikipedia", "https://www.wikipedia.org/"], 
            ["google", "https://google.com/"],
            ["facebook", "https://www.facebook.com/"],
            ["instagram", "https://www.instagram.com/"],
            ["twitter", "https://twitter.com/"],
            ["reddit", "https://www.reddit.com/"],
            ["linkedin", "https://www.linkedin.com/"],
            ["github", "https://github.com/"],
            ["stackoverflow", "https://stackoverflow.com/"]
        ]

        for site in sites:
            if f"open {site[0]}" in query:
                say(f"Opening {site[0]}, Sir....")
                webbrowser.open(site[1])

        if "play music" in query:
            song_name = query.replace("play music", "").strip()
            if song_name:
                play_music(song_name)
            else:
                say("Please specify the song name.")

        if "the time" in query:        
            strfTime = datetime.datetime.now().strftime("%H:%M:%S")
            say(f"Sir, the time is {strfTime}")

        if "open whatsapp" in query:
            whatsapp_path = r"c:\Program Files\WindowsApps\5319275A.WhatsAppDesktop_2.2424.6.0_x64__cv1g1gvanyjgm\WhatsApp.exe"
            if os.path.exists(whatsapp_path):
                os.startfile(whatsapp_path)
                say("Opening WhatsApp")
            else:
                say("WhatsApp application not found")

        if "using artificial intelligence" in query:
            ai_response = ai(prompt=query)
            say(ai_response)
