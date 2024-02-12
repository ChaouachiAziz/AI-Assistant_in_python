#Imports
import pyttsx3 #we use pyttsx3 because it's more customizable and work offline.
import datetime
import speech_recognition as sp
import wikipedia as wiki
#-----------------------------------------------------------------------------


ai = pyttsx3.init()
voices = ai.getProperty('voices')
ai.setProperty('voice', voices[1].id)


def speak(text):
    ai.say(text)
    ai.runAndWait()

def date():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day
    speak("the current date is")
    speak(year)
    speak(month)
    speak(day)


def time_now():
    time = datetime.datetime.now().strftime("%H,%M,%S")
    speak("the current time is:",)
    speak(time)


'''def wiki_search(req):
    speak("searching...")
    res = wiki.summary(req, sentences=3)#this will be the reult of our request using the summary function inside wikipedia library and the 2nd arguments is the number of sentences (customizable)
    speak("according to wikipedia")
    print(res)
    speak(res)'''
    
    
def welcome():
    hour = datetime.datetime.now().hour
    if (hour >= 6 and hour < 12):
        speak("good morning aziz")
    elif (hour >= 12 and hour < 18):
        speak("good afternoon aziz")
    elif (hour >= 18 and hour < 24):
        speak("good night aziz")
    else:
        speak("good night aziz")
    #date()
    #time_now()
    speak("How may i be of service today sir")


def commandInput():
    com = sp.Recognizer()
    with sp.Microphone() as src:
        print("Listening")
        com.pause_threshold = 1
        audio = com.listen(src)

    try : 
        print("Recognizing")
        req = com.recognize_google(audio, language='en-US')
        print(req)
    except Exception as e:
        print(e)
        print("could not recognize please repeat")
        return None
    return req


if __name__ == "__main__" :
    
    welcome()
    while True:
        req = commandInput().lower()
        if 'time' in req:
            time_now()
        if 'date' in req:
            date()
        if 'wikipedia' in req:
            speak("searching...")
            req = req.replace('wikipedia', '')
            res = wiki.summary(req, sentences=3)#this will be the reult of our request using the summary function inside wikipedia library and the 2nd arguments is the number of sentences (customizable)
            speak("according to wikipedia")
            speak(res)
            print(res)
            
