  
# Implementations.
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import pyaudio
import re
import pyowm

# Starting.
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

print("\n   <!!! ONLINE !!!> \n")
print("\n   I am SARA! Your Digital Assistant.\n")
engine.say('Hello. I am Sara, Your Digital Assistant! Please Enter Your Name Below')
engine.runAndWait()
name = input('Name:- ')
engine.say('Okay! Now, Your City.')
engine.runAndWait()
city = input("City:- ")
engine.say('Next! Your Email Address.')
engine.runAndWait()
emailadd = input('Email:- ')
engine.say("Make Sure That You Have Enabled Less Secured App Access In Your Gmail Account or You Won't Be Able To Send Emails through Gmail. Finally enter your Password")
engine.runAndWait()
print("\n   !Enable Less Secure App Access In Your Gmail!\n")
pword = input('Password:- ')

engine.say(f'Okay, So You are {name}')
engine.runAndWait()

# Comments About the Name.
if len(name) < 3:
    engine.say("Don't Mind, But the Name Is Too Short.")
elif len(name) > 20:
    engine.say("Don't Mind, But the Name Is Too Long.")
else:
    engine.say("Nice Name.")

# Bades With The Time.
hour = int(datetime.datetime.now().hour)
if hour>=3 and hour<6:
    engine.say(f'Good Day,{name}')
    engine.runAndWait()
elif hour>=6 and hour<12:
    engine.say(f'Good Morning,{name}')
    engine.runAndWait()
elif hour>=12 and hour<18:
    engine.say(f'Good Afternoon,{name}')
    engine.runAndWait()
else:
    engine.say(f'Good Evening,{name}')
    engine.runAndWait()
engine.say("Now, We are Ready to Go.")
engine.runAndWait()


# Speaks The Audio.
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Hears The Voice.
def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\n   Listening...\n")
        speak("Listening")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("   Recognizing...\n") 
        speak("Recognizing")
        query = r.recognize_google(audio, language='en-in')
        print(f"{name} said:-  {query}\n")

    except Exception as e: 
        print("   Did Not Get It...\n")  
        return "None"
    return query

# Hears The Voice Also.
def takeCommandSt():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\n   Say Something...\n")
        speak("Hearing!")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("   Getting...\n") 
        speak("understanding")
        query = r.recognize_google(audio, language='en-in')
        print(f"{name} said:-  {query}\n")

    except Exception as e: 
        print("   Say that again please...\n")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(emailadd, pword)
    server.sendmail(emailadd, to, content)
    server.close()

if __name__ == "__main__":

    # The Querys.
    while True:
        query = takeCommandSt().lower()

        if 'wiki' in query:
            speak('Searching Wikipedia')
            query = query.replace("wikipedia", "")
            wikiResults = wikipedia.summary(query, sentences=5)
            speak("Wikipedia Says")
            print(f"   {wikiResults}\n")
            speak(results)

        elif 'open an app' in query:
            try:
                speak("Which Application Should I Open?")
                app = takeCommand()
                os.startfile(app)
                speak(f"opening {app}")
            except Exception as e:
                speak(f"couldnot open Application called {app}")

        elif 'start' in query:
                os.system('explorer C:\\{}'.format(query.replace('launch ','')))
                desired = ("{}".format(query.replace('launch ','')))
                speak(f"Launching {desired}")

        elif 'send email' in query:
            try:
                speak("whom to send?")
                to = input("Email To:- ")
                speak("What to say?")
                content = takeCommand()
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                speak("Something Went Wrong! Email Was Not Sent!")

        elif "open a website" in query:
            try:
                speak("which website should I open?")
                dweb = takeCommand()
                webbrowser.open(f'www.{dweb}')
                speak(f"opening {dweb}")
            except Exception as e:
                speak(f"Unable to Open {dweb}")

        elif 'say' in query:
            copy = query.replace("say", "")
            speak(copy)

        elif 'hello' in query:
            speak(f'HI {name}! How Can I Help You?')

        elif 'how are you' in query:
            speak("I am Fine, Thank You for asking!")

        elif 'who am i' in query:
            speak(f"You Are, {name} and currently is in {city}")
            print(f"   Your Name Is {name}, Your Email Address is {emailadd} and You are from {city}")

        elif 'who are you' in query:
            speak("I am Sara Your Voice Assistant Made By Shahzeb Ali in Python.")
            speak("plaese go and Checkout Shahzeb Ali on Social Media!")
            print("   Shahzeb Ali")
            print("     Email:- shahzebchannel@gmail.com")
            print("     Youtube:- Shahzeb Ali   Subscribe! ")
            print("     Github:- Shahzeb-A   Follow! \n")
                 
        elif 'exit' in query:
            speak(f"ThankYou {name} For Giving Me Your Valueable Time, BYE! Have a Good Day!")
            print("   <!!! OFFLINE !!!>")
            exit()

        else:
            speak("Sorry! Didn't Get It!\n")
