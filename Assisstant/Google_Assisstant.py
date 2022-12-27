from googletrans import Translator
import speech_recognition as sr
from playsound import playsound
from gtts import gTTS
import pywhatkit
import datetime
import pyttsx3
import wikipedia
import pyjokes
import os

engine = pyttsx3.init()
translator = Translator()


voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate',160)
engine.setProperty('volume',1)

langu = 'en'

def speka(text):
    engine.say(text)
    engine.runAndWait()

        
def talk(text,lang=langu):
    tr = translator.translate(text,dest=lang)
    print(tr.text)
    speak = gTTS(text=tr.text, lang=lang, slow=False)
    speak.save("captured_voice.mp3")
    playsound("captured_voice.mp3")
    os.remove('captured_voice.mp3')
    return 
    

def language():
    speka('Select the language for Your Alexa...')
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("listening.....")
            r.pause_threshold = 1
            audio = r.listen(source)
            
        print("Recognizing.....")
        comm = r.recognize_google(audio, language=langu)
        abc = f"you have selected the {comm} language for your Alexa\n"
        print(abc)
        speka(abc)
        
    except Exception as e:
        print("say that again please.....")
        return "None"
    
    return comm

def transl(langu):
    comm = language()
    print(comm)
    text = 'mein aapake lie kya kar sakatee hu'
    
    if 'Hindi' in comm:
        langu = 'hi'
        talk(text,langu)
        
    elif 'Kannada' in comm:
        langu = 'kn'
        talk(text,langu)
        
    elif 'English' in comm:
        langu = 'en'
        talk(text,langu)
        
    else:
        talk('Please Select Other language...')
        
    return langu

transl(langu)
print(langu)
