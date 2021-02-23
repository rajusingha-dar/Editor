from gtts import gTTS
import speech_recognition as sr
import webbrowser
import datetime
import os
import cv2
import win32com.client
#import numpy as np


#speaker = win32com.client.Dispatch("SAPI.SpVoice")
def takeCommand():
    #It takes microphone input from the user and returns string output
    speaker = win32com.client.Dispatch("SAPI.SpVoice")

    r = sr.Recognizer()
    with sr.Microphone() as source:
        speaker.Speak("Listning")
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

def talkToMe(audio):
    print(audio)
    output = gTTS(text=audio, lang="en", slow = True)
    output.save("output.vbs")
    os.system('welcome.vbs')




def wishMe():

    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Raju Good Morning!  How may I help you")
        speaker.Speak("Raju Good Morning!  How may I help you")


    elif hour>=12 and hour<18:
        print("Good Afternoon! Raju  How may I help you")
        speaker.Speak("Good Afternoon! Raju  How may I help you")


    else:
        print("Good Evening! Raju  How may I help you")
        speaker.Speak("Good Evening! Raju  How may I help you")



if __name__ == "__main__":
    print("My name is Zack")
    speaker = win32com.client.Dispatch("SAPI.SpVoice")

    speaker.Speak("My name is Zack")

    wishMe()

    while True:


        query = takeCommand().lower()

        if 'spotify' in query:
            speaker = win32com.client.Dispatch("SAPI.SpVoice")
            speaker.Speak("Hello we are opening Sptify for you Raju")
            webbrowser.open("https://www.spotify.com/")

        elif 'open youtube' in query:
            speaker = win32com.client.Dispatch("SAPI.SpVoice")
            speaker.Speak("Hello we are opening Youtube for you Raju")
            webbrowser.open('https://www.youtube.com/')


        elif 'date' in query:
            cmd='date'
            speaker = win32com.client.Dispatch("SAPI.SpVoice")
            speaker.Speak("bla bla today's date is ")
            os.system(cmd)


        elif 'open notepad' in query:
            cmd='notepad'
            speaker = win32com.client.Dispatch("SAPI.SpVoice")
            speaker.Speak("Hello we are opening notepad for you Raju")
            os.system(cmd)


        elif 'open google' in query:
            speaker = win32com.client.Dispatch("SAPI.SpVoice")
            speaker.Speak("Hello we are opening google for you Raju")
            webbrowser.open('https://www.google.com/')

        elif 'office photo' in query:
            speaker = win32com.client.Dispatch("SAPI.SpVoice")
            speaker.Speak("Hello we are opening office photo for you Raju")
            img = cv2.imread("office0.jpg")
            imgResize = cv2.resize(img,(500,500))
            cv2.imshow("Image Resize",imgResize)
            cv2.waitKey(20)



        elif 'break'  in query:
            print("It was nice helping you ....!!!")
            speaker = win32com.client.Dispatch("SAPI.SpVoice")
            speaker.Speak("It was nice helping you ....!!!")

            break
