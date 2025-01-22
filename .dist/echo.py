import pyttsx3
import speech_recognition as sr
import datetime
import pyaudio
import smtplib
import wikipedia
import webbrowser
import os
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voices',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>0 and hour<12:
        speak("good morning")

    elif hour>=12 and hour<18:
        speak("good afternoon")

    else:
        speak("good evening")   

    speak(" I am echo how can i help you")            
def takeCommand():
    # it takes microphons input from the user and returns string output

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..........")
        r.pause_thresehold=1
        audio=r.listen(source)

    try:
        print("Recognizing.........")  
        query=r.recognize_google(audio,language='en-in') 
        print(f"user said : {query}\n")
               
    except Exception as e:
        # print(e) 
        print("say that again please.....")
        return "None"
    return query

def sendEmail(to,content):
    server=smtplib.SMTP('smntp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("shrutisharma110403@gmail.com","password")
    server.senmail("shrutisharma131277@gmail.com",to,content)
    server.close()
if __name__=="__main__":  
    wishMe()
    # while True:
    if 1:    
        query =takeCommand().lower()
    # logic for executing tasks based on query

        if 'wikipedia' in query:
            speak('searching wikipedia.......')
            query=query.replace("wikipedia" , "")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query :
            webbrowser.open("youtube.com")

        elif 'open youtube' in query :
            webbrowser.open("youtube.com")

        elif 'open google' in query :
            webbrowser.open("google.com")
    
        elif 'open netflix' in query :
            webbrowser.open("netflix.com")

        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir , the time is {strTime}")
                    
        elif'open code' in query:
            codePath = "C:\\Users\\a\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif'email to shruti'  in query:
            try:
                speak("what should i say?")
                content=takeCommand()
                to="shrutisharma110403@gmail.com"
                sendEmail(to,content)
                speak("email has been sent !")
            except Exception as e:
                print(e)
                speak("sorry i am not able to send this email! ")    


        