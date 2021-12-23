import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import datetime
import os
from gnewsclient import gnewsclient
from wikipedia import exceptions 
import smtplib

engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[1].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir")
    elif hour>=12 and hour<=18:
        speak("Good Afternoon Sir")
    else:
        speak("Good Evening Sir")
    speak("Please tell me How may i help you.")


def takeCommand():
    #it takes microphone input and returns into string
    r =sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please.....")
        speak("Say that again please.....")
        takeCommand()
    return query

def sendMail(to,cont_mail):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('users email address','users password')
    server.sendmail('users email address',to,cont_mail)
    server.close()

def mail_add_str(raw): #to convert the reciever's email address from raw microphone input to a meaningful email address
    str1=raw.replace(" ","")
    if 'attherate' in str1:
        str2= str1.replace("attherate","@")
    elif 'at' in str1:
        str2= str1.replace("at","@")
    return str2



if __name__=="__main__":
    wishMe()
    while True:
        #if 1:
        query = takeCommand().lower() #converting query into lowercase
        #Logic for executing task based on query
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query=query.replace("wikipedia","")
            result = wikipedia.summary(query,)
            print(result)
            speak(result)
        elif 'latest news' in query:
            speak("Fetching today's news.....")
            client=gnewsclient.NewsClient(language='english',location='india',max_results=5)
            news_list=client.get_news()
            tt=news_list[0]
            speak(tt)
        elif 'send email' in query:
            try:
                print("Speak the content sir.")
                speak("Speak the content sir.")
                cont_mail=takeCommand()
                print("to who should i send this sir?")
                speak("to who should i send this sir?")
                raw=takeCommand()
                to=mail_add_str(raw)
                sendMail(to,cont_mail)
                speak("sir, the email has been sent.")
            except Exception as e:
                print(e)
                speak("Sir, I apologies the mail has not been sent.")
        elif 'Charlie' in query:
            print("Sir?")
            speak("Sir?")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'brave' in query:
                brave_dir="C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
                os.startfile(brave_dir)
        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        elif 'open code' in query:
            codePath="C:\\Users\\shiva\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'play' in query:
            music_dir='D:\Music\Eng'
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif 'who are you' in query:
            speak("I am Donny, I am a voice assistant programmed by Shivam, I can hear you, but i can't hear the noise")
        elif 'goodbye' in query:
            print("GoodBye sir")
            speak("GoodBye sir.")
            break
        else:
            print("Say that again please.....")
            speak("Say that again please.....")
            takeCommand()


        
