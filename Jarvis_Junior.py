import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

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
    speak("I am Jarvis Junior. I am at your service. Please tell me how may I help you?")

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
        elif 'play music' in query:
            music_dir='C:\\Users\\Akanksha Rajwar\\Desktop\\TIME PASS\\SONGS\\audios'
            songs=os.listdir(music_dir)
            print(songs)
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
        elif ('thank you' in query) or ('thanks' in query) :
            speak("I am all yours.It is always my pleasure")
        elif('shukriya' in query) or('dhanyavad' in query):
            speak("Anything for you my friend. Namaste")
        elif 'quit' in query:
            speak("This is Jarvis signing off")
            exit()
