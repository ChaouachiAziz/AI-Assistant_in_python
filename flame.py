#Imports
import pyttsx3 #we use pyttsx3 because it's more customizable and work offline.
import datetime
import speech_recognition as sp
import wikipedia as wiki
import smtplib
import webbrowser as wb
import os
import psutil
import pyjokes
import pyautogui as pt
import time
import random as rd
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


def wiki_search(req):
    speak("searching...")
    req = req.replace('wikipedia', '')
    res = wiki.summary(req, sentences=3)#this will be the reult of our request using the summary function inside wikipedia library and the 2nd arguments is the number of sentences (customizable)
    speak("according to wikipedia")
    print(res)
    speak(res)
    
    
    
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
    except sp.WaitTimeoutError:
        print("timed out , please repeat")
        
    except Exception as e:
        print(e)
        print("could not recognize please repeat")
        return None
    return req

def mailSender():
    speak("what should i say: ") 
    contains = commandInput()
    speak("to whom should i send this")
    to = input("please provide the receiver mail adress: ")
    speak("sending the email which contains")
    speak(contains)
    print(contains)
    smtp_port = 587
    smtp_server = "smtp@gmail.com"
    mail_adr = ""
    mail_pass = ""
    serv = smtplib.SMTP(smtp_server, smtp_port)
    serv.ehlo()
    serv.starttls()
    serv.login(mail_adr, mail_pass)
    serv.sendmail(mail_adr, to, contains)
    serv.close()
    

def com_domain(find):
    chrome = 'C:\Program Files\Google\Chrome\Application\chrome.exe %s'
    wb.open(find + '.com')

def yt_search():
    find = commandInput().lower()
    speak("working on it")
    wb.open('https://www.youtube.com/results?search_query=' + find )
    
def google_search():
    find = commandInput().lower()
    speak("on it")
    wb.open('https://www.google.com/search?q=' + find)
    
def cmd():
     com = commandInput().lower()
     os.system(com)

def usage():
    cpu = str(psutil.cpu_percent())
    speak("cpu is using " + cpu)
    battery = str(psutil.sensors_battery())
    speak("battery is at " + battery)
    
def tell_joke():
    jk = str(pyjokes.get_joke())
    speak(jk)

#customize this function to open whatever you want , notice that i will improve it later on by using a list that contains the path of the most used apps and iterate through it.
def open_vscode():
    speak("opening the code editor")
    vscode_path = r"C:\Users\Chaouachi Aziz\AppData\Local\Programs\Microsoft VS Code\Code.exe" # r is used to tell python that '\' is literal character not an escape character
    os.startfile(vscode_path)

def write_note():
    speak("what are your thoughts today")
    note = commandInput()
    #f = open(r"C:\Users\Chaouachi Aziz\Desktop\notes.txt", 'w') desktop
    f = open("notes.txt", 'w')
    f.write(note)
    tr = True
    while(tr):    
        speak("want to add another line sir")
        rep = commandInput()
        if (rep == 'yes'):
            speak("I am listening")
            more = commandInput()
            f.write("\n")
            f.write(more)
        else:
            tr = False
    speak("done writing your note")
    f.close()

def show_note():
    speak("here you go sir")
    #f = open(r"C:\Users\Chaouachi Aziz\Desktop\notes.txt", 'r') in desktop
    f = open("notes.txt", 'r') #current directory
    print(f.read())
    speak(f.read())

i=0
def screen_shot():
    speak("screenshot is being taken ")
    global i
    ss = pt.screenshot()
    ss.save(r'C:\Users\Chaouachi Aziz\Desktop\aiAssistant\screenshots\a'+str(i)+r'.png')
    i+=1

def play_music():
    music_path = r'C:\Users\Chaouachi Aziz\Desktop\Data\Music'
    music = os.listdir(music_path)
    speak("which song do you want to listen to")
    req = commandInput().lower()
    while('number' not in req and req != 'random' and req != 'shuffle' and req != 'choose'):
        speak("could not understand please repeat")
        req = commandInput().lower()

    if 'choose for me' in req or 'random' in req or 'shuffle' in req:
        num = rd.randint(0,len(music))
        os.startfile(os.path.join(music_path, music[num]))
        
    else:
        num = int(req.replace('number', ''))
        time.sleep(2)
        speak("playing music")
        os.startfile(os.path.join(music_path, music[num])) #after listing the directory we join the paths of the directory which contains the music and the list we made to have access to the song equivalent to the index
            
def save_it():
    speak("what should i save")
    memo = commandInput().lower()
    save = open("saved.txt", 'w')
    save.write(memo)
    speak("saved successfully")
    save.close()

def remember():
    memo = open("notes.txt", 'r')
    speak("this is what i remember " + memo.readline())

    
if __name__ == "__main__" :
    
    welcome()
    while True:
        req = commandInput().lower()
        if 'time' in req:
            time_now()
            
        elif 'date' in req:
            date()
            
        elif 'wikipedia' in req:            
            speak("according to wikipedia")
            wiki_search(req) 
            
        elif 'emai' in req or 'mail' in req:
            try:  
                mailSender()
                speak("email has been sent successfully")
            except Exception as e:
                print(e)
                speak("unable to send please repeat")
                print("could not send email")
        
        elif 'website' in req:
            speak("which website should i open for you sir")
            find = commandInput().lower()
            com_domain(find)            
        
        elif 'youtube' in req:
            speak("what do you want to watch")
            try:
                yt_search()
            except Exception as e:
                print(e)
                speak("error")
                print("error")
                
        elif 'chrome' in req or 'search' in req:
            try:
                google_search()
            except Exception as e:
                print(e)
                speak("could not search")
                print("could not search")
                
        elif 'terminal' in req:
            cmd()
        
        elif 'cpu' in req or 'battery' in req :
            usage()
            
        elif 'joke' in req :
            tell_joke()

        elif 'code' in req :
            open_vscode()
                        
        elif 'write note' in req:
            write_note()
        
        elif 'show note' in req:
            speak("showing notes")
            show_note()
        
        elif 'screenshot' in req:
            screen_shot()
        
        elif 'restart' in req:
            speak("restarting now")
            print("restarting now")
            time.sleep(3)
            os.system('python flame.py')
         
        elif 'play music' in req:
            try:
                play_music()
            except Exception as e:
                print(e)
                speak("unable to play")
                print("unable to play error")
        
        elif 'save it' in req:
            save_it()
        
        elif 'remembers' in req:#mainly used to remember the last conversation
            remember()
            
        elif 'exit' in req or 'quit'in req:
            speak("Exiting now")
            exit()
        