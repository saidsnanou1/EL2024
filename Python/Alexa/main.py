import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
from time import sleep
import requests
from playsound import playsound



def speak(response):
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')  
    engine.setProperty('rate', rate - 60)
    engine.say(response)
    engine.runAndWait()



def get_voice_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening ...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            command = recognizer.recognize_google(audio,language='en')
            print(f"You said: {command}")
        except sr.UnknownValueError:
            print("Sorry, I could not understand your command.")
            return ""
        except sr.RequestError:
            print("Could not request results from Google Speech Recognition service.")
            return ""
        return command


def wishMe():

    hour = int(datetime.datetime.now().hour)
    sleep(1)
    if hour >= 0 and hour < 12:
        speak("Good Morning said")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon said")
    else:
        speak("Good evening said")
    sleep(1)
    speak("I am alexa, please tell me how may I help you")


def get_geo_info():
    try:
        res = requests.get("https://ipinfo.io/")
        data = res.json()
        city = data["city"]
        location = data["loc"].split(",")
        latitude = location[0]
        longitude = location[1]
        response = f"You are at {city} and latitude {latitude} and logitude {longitude}"
    except Exception as e:
        print(e)
        response = "Unable to detect your location"
    return response


def main():
    wishMe()
    while True:
        command = get_voice_command().lower()

        if "time" in command:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The current time is {current_time}.")
        elif "google" in command:
            webbrowser.open("https://www.google.com")
            speak("Opening Google.")
        elif "alarm" in command:
            playsound(r"/home/said/EL2024/Python/Alexa/alert_signal.mp3")
        elif "location" in command:
            location = get_geo_info()
            speak(location)
        elif "thank you" in command:
            speak("I am here to help,please let me know if you need anything else")
        elif "exit" in command:
            speak("Exiting the system.")
            break

        else:
            speak("I did not understand that command.")


if __name__ == "__main__":
    main()

