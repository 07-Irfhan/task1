import speech_recognition as sr
import  os
import  datetime
import wikipedia
import pyttsx3
import webbrowser
import pyjokes

engine = pyttsx3.init()

def speak(text):
    print(f"Assistant: {text}")
    try:
        engine.say(text)
        engine.runAndWait()
    except:
        print("Speech output not supported.")

def greet():
    hour = int(datetime.datetime.now().hour)
    if hour < 12:
        speak("Good Morning!")
    elif hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am your voice assistant How can I help you today?")

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        r.adjust_for_ambient_noise(source, duration=1)

    try:
        query = r.recognize_google(audio)
        print(f"You said: {query}")
        return query.lower()
    except:
        speak("Sorry, I didn't here you speak loudly")
        return ""
    
def run_assist():
    greet()
    while True:
        query=take_command()

        if 'wikipedia' in query:
            speak("searching wikipedia...")
            query=query.replace("wikipedia","")
            try:
                result=wikipedia.summary(query,sentences=5)
                speak("according to wikipedia:")
                speak(result)
            except:
                speak("sorry result not found")

        elif 'open spotify' in query:
                speak("opening spotify...")
                webbrowser.open("https://www.spotify.com")
        elif 'open google' in query:
                speak("Opening Google...")
                webbrowser.open("https://www.google.com")
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The current time is {strTime}")
        elif 'joke' in query:
            joke = pyjokes.get_joke()
            speak(joke)
        
        elif 'exit'  in query:
            speak("Goodbye! Have a nice day!")
            break

        else:
            speak("please Try again.")
            break

run_assist()


    



