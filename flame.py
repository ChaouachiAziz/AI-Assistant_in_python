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
import json
import urllib.request
import wolframalpha
import tkinter as tk
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
    
    
    
def welcome(username):
    hour = datetime.datetime.now().hour
    if (hour >= 6 and hour < 12):
        speak(f"good morning {username}")
    elif (hour >= 12 and hour < 18):
        speak(f"good afternoon {username}")
    elif (hour >= 18 and hour < 24):
        speak(f"good night {username}")
    else:
        speak(f"good night {username}")
    speak("How may I be of service today, sir")


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
    speak("what are your commands sir")
    com = commandInput().lower()
    if 'restart os' in com:
        os.system('shutdown /r')
    elif 'shutdown os' in com:
        os.system('shutdown')
    elif 'log out' in com:
        os.system('shutdown -l')

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

def get_news():
    api_url = urllib.request('https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=API_KEY')
    news = json.load(api_url)
    for piece in news['article']:
        print(piece['title']+"\n")
        speak(piece['title'])

def get_location():
    speak("which place")
    find = commandInput().lower()
    speak("locating")
    wb.open('https://www.google.com/maps/place/' + find)
    
def calculate():
    cli = wolframalpha.Client(app_id='5EUX97-ER7HVLT9R6')
    speak("what should i calculate")
    req = commandInput().lower()
    res = cli.query(req)
    ans = next(res).text
    speak("the answer is")
    speak(ans)    
    
def explain(req):
    cli = wolframalpha.Client(app_id='5EUX97-ER7HVLT9R6')
    speak("explaining")
    res = cli.query(req)
    print(next(res).text)
    speak(next(res).text) 

def stop_listening():
    speak("for how long should i stop")
    ans = commandInput().lower()
    print(ans)
    speak(f"stopping for {ans} seconds")
    time.sleep(int(ans))

    
if __name__ == "__main__":
    # Ask for the username using tkinter form
    def on_button_click():
        global username
        username = entry_username.get()
        window.destroy()
        # Call the welcome function with the provided username
        welcome(username)

    window = tk.Tk()

    window.geometry("500x400")
    window.configure(bg="#121212")  # Adjust the background color

    label_username = tk.Label(
        text="NAME",
        bg="#121212",  # Background color of the label
        fg="white",  # Text color of the label
        font=("Montserrat-Bold", 16)  # Fix the font name
    )
    label_username.place(
        x=200,
        y=80,
        width=100,
        height=40.0
    )

    # Add an entry widget to take the username
    entry_username = tk.Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000000",
        highlightthickness=0
    )
    entry_username.place(
        x=51.25,
        y=120.0,
        width=400.0,
        height=38.0
    )

    button_username = tk.Button(
        text="Submit",
        command=on_button_click,
        bg="#FFFFFF",
        fg="#000000",
        font=("MontserratRoman Bold", 16)
    )
    button_username.place(
        x=200,
        y=170,
        width=100,
        height=38.0
    )

    window.mainloop()
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
                
        elif 'terminal' in req or 'commands' in req:
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
        
        #elif 'remembers' in req:#mainly used to remember the last conversation
            #remember()
        
        elif 'news' in req:
            try:
                get_news()
            except Exception as e:
                print(e)        
                
        elif 'location' in req:
            get_location()
        
        #elif 'calculate' in req:
         #   try:
          #      calculate()
           # except Exception as e:
            #    print(e)
             #   print("could not calculate")
        elif 'explain' in req or 'what is' in req :
            try:
                explain(req)
            except Exception as e:
                print(e)
                speak("could not understand")
        
        elif 'stop' in req:
            stop_listening()    

        
        elif 'exit' in req or 'quit'in req:
            speak("Exiting now")
            exit()
    
