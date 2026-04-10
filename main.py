import datetime
import pyaudio
import speech_recognition as sr
import pyttsx3
import pywhatkit
import os
import webbrowser
import wikipedia 

listener= sr.Recognizer() 
engine = pyttsx3.init()
voices= engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
        engine.say(audio)
        engine.runAndWait()

#It wishes according to the time 
def wishme():
        hour = int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
            print('Good Morning, sir..!')
            speak('Good Morning sir..!')
        elif hour>=12 and hour<17:
            print('Good Afternoon, sir..!')
            speak('Good Afternoon sir..!')
        else:
            print('Good evening, sir..!')
            speak('Good evening sir..!')
        speak('I am your voice assistant, how can i help you?')

#Take commands as queries through voice
def takeCommand():
    command=''
    try:
        with sr.Microphone() as source:
            print('\nlistening...')
            listener.pause_threshold = 1
            listener.energy_threshold = 500
            audio = listener.listen(source)
            command = listener.recognize_google(audio)
            command=command.lower()
    except Exception as e:
        print('Can you say once again sir.')
        speak('Can you say once again sir.')
    return command 

#
def initial():
    while True:
        query=takeCommand()
        print('User said: '+query)
    
        
        if 'open google' in query:
            speak('Opening google')
            webbrowser.open('google.com')
            break
        elif 'search in google' in query:
            query=query.replace('search in google about','').strip()
            speak('Searching in google for '+query)
            webbrowser.open(f'https://www.google.com/search?q={query}')
            break
        elif 'play' and 'youtube' in query:
            query=query.replace('play','')
            speak('playing'+query)
            pywhatkit.playonyt(query)
            break
        elif 'wikipedia' in query:
            speak('Searching on wikipedia...')
            query =query.replace('according to wikipedia','').strip()
            result=wikipedia.summary(query,sentences=2)
            print(result)
            speak(result)
            break
        elif 'open' and 'file explorer' in query:
            print('Opening file explorer')
            speak('Opening file explorer')
            os.system('explorer')
            break
        elif 'open' and 'calculator' in query:
            speak('Opening Calculator')
            os.system('calc.exe')
            break
        elif 'time' in query:
            time=datetime.datetime.now()
            print('\n',time.strftime('%I:%M:%p'))
            speak('Sir,today is '+time.strftime('%d')+ 'of' +time.strftime('%B')+ 'and the time is '+time.strftime('%I')+' '+time.strftime('%M')+time.strftime('%p'))
            break
        elif 'open notepad' in query:
            speak('Opening notepad')
            notepad=os.system('notepad')
            break
        elif 'open' and 'camera' in query:
            speak('Opening camera')
            Settings=os.system('start microsoft.windows.camera:')
            break
        elif 'shutdown' in query:
            speak('Shutting down the system')
            os.system('shutdown /s /t 1')
        elif 'restart' in query:
            speak('Restarting the system')
            os.system('shutdown /r /t 1')
        elif 'bye' in query:
            speak('Bye sir, meet you later')
            break
        elif 'hai' or 'hi' in query:
            speak('Nice to meet you sir')
                
                

# Our code begins from here
# Take command to activate the code.
# If it takes the correct command, our code will start execution from initial
command=''
try:
    with sr.Microphone() as source:
        print('Listening...')
        listener.pause_threshold = 1
        listener.energy_threshold = 500
        audio= listener.listen(source)
        command= listener.recognize_google(audio)
        command=command.lower()
except:
        pass
    
if 'hello assistant' in command:
    command=command.replace('hello assistant','')
    if len(command)==0:
        wishme()
else:
    print(command,' is not me')
    speak(command,' is not me')
    
x=True
while(x):
    
    initial()
    y=int(input('\nWould you like to repeat : 1. yes 2. no'))
    if y==1:
        x=True
    elif y==2:
        x=False
    else:
        print('Invalid input.. Please enter valid input.')
print('voice assitant closed')