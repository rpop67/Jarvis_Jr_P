import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import json
from bs4 import  BeautifulSoup as Soup
import urllib.request
from urllib.request import  urlopen

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def TakeCommand():
    #It takes microphone input from user and returns string output

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening... ")
        r.pause_threshold=0.8 #waiting time fir the phase completion of non speaking
        audio=r.listen(source)

    try:

        print("Recognizing.. ")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e) #only when error needs to be displayed
        print("Couldnot catch your words.Say that again please.")
        return("None")
    return query

def WishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Hey, Good Morning fella!")
    elif hour>=12 and hour<17:
        speak("Hey, Good Afternoon fella! ")
    else:
        speak("Hey, Good Evening fella !")
    #speak("I am Jarvis Junior. I am at your service. Please tell me how may I help you?")

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)#587 is port
    server.ehlo()
    server.starttls()
    server.login('myemailhere','mypasswordhere') #from which email needs to be sent
    server.sendmail('myemailhere',to,content)
    server.close()


if __name__ =="__main__":
    WishMe()
    MailMap = {
        "akanksha": "rajwar101@gmail.com",
        "yashvi": "yashvipatel2903@gmail.com",
        "mansi": "mansidhingra007@gmail.com",
        "smrity": "smritychaudhary01@gmail.com"
    }
    while True:
        query=TakeCommand().lower();

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak('According to wikipedia...')
            speak(results)
        elif 'hey jarvis' in query:
            speak('Hi Anshu. What can I do for you today?')
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
        elif 'open google' in query:
            speak('hope you find what you are about to google')
            webbrowser.open('google.com')
        elif 'open stackoverflow' in query:
            speak('Hope all your coding doubts get cleared')
            webbrowser.open('stackoverflow.com')
        elif 'open facebook' in query:
            speak("Let's get your social life on board")
            webbrowser.open('facebook.com')
        elif 'open geeksforgeeks' in query:
            webbrowser.open('geeksforgeeks.org')
        elif 'lift' in query and 'mood' in query :
            lift_dir='C:\\Users\\Akanksha Rajwar\\Desktop\\TIME PASS\\SONGS\\liftMood'
            liftSong=os.listdir(lift_dir)
            print(f"Playing {liftSong} for you, Anshu")
            speak("Don't feel so down Anshu. I have got you covered with some mood lifters. Now get up and show me some moves")
            os.startfile(os.path.join(lift_dir,liftSong[0]))
        elif ('sad' in query  or 'fight' in query)and 'song' in query:

            sad_dir='C:\\Users\\Akanksha Rajwar\\Desktop\\TIME PASS\\SONGS\\sadSongs'
            sadSong=os.listdir(sad_dir)
            print(f"Playing {sadSong} for you, Anshu")
            speak("Let me console you with some sad songs.")
            os.startfile(os.path.join(sad_dir,sadSong[0]))
        elif 'korean' in query and 'song' in query:
            sad_dir='C:\\Users\\Akanksha Rajwar\\Desktop\\TIME PASS\\SONGS\\koreanSongs'
            sadSong=os.listdir(sad_dir)
            print(sadSong)
            os.startfile(os.path.join(sad_dir,sadSong[0]))
        elif 'taylor' in query and 'song' in query:
            sad_dir='C:\\Users\\Akanksha Rajwar\\Desktop\\TIME PASS\\SONGS\\taylorSwift'
            sadSong=os.listdir(sad_dir)
            print(sadSong)
            os.startfile(os.path.join(sad_dir,sadSong[0]))
        elif ('maroon' in query and '5' in query ) or ('marron5' in query) and 'song' in query:
            sad_dir='C:\\Users\\Akanksha Rajwar\\Desktop\\TIME PASS\\SONGS\\Maroon5'
            sadSong=os.listdir(sad_dir)
            print(sadSong)
            os.startfile(os.path.join(sad_dir,sadSong[0]))
        elif 'play music' in query:
            music_dir='C:\\Users\\Akanksha Rajwar\\Desktop\\TIME PASS\\SONGS\\audios'
            songs=os.listdir(music_dir)
            print(f"Playing {songs} for you, Anshu")
            os.startfile(os.path.join(music_dir,songs[0]))
        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is{strTime}")
        elif ('send email' in query) or ('send mail' in query):
            try:
                speak('Whom would you like to mail?')
                name=TakeCommand().lower()
                to=MailMap[name]
                speak("What would you like to mail?")
                content=TakeCommand()
                sendEmail(to,content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry buddy, I could not send the mail. Would you like to try again?")
        elif 'news' in query and ('read' in query or 'tell' in query or 'update' in query):
            try:
                news_url="https://news.google.com/news/rss"
                #with urllib.request.urlopen(news_url) as response:
                #htmlSource = response.read()
                Client=urlopen(news_url)
                xml_page=Client.read()
                Client.close()
                soup_page=Soup(xml_page,"xml")


                news_list=soup_page.findAll("item")
                for news in news_list[:15]:
                    newsTitle=news.title.text
                    newsTitle=newsTitle.replace("-"," as quoted by ")
                    print(newsTitle)
                    speak(newsTitle)

            except Exception as e:
                print(e)

        elif ('thank you' in query) or ('thanks' in query) :
            speak("It is always my pleasure")
        elif('shukriya' in query) or('dhanyavad' in query):
            speak("Anything for you my friend. Namaste")
        elif 'quit' in query:
            speak("This is Jarvis signing off")
            exit()
