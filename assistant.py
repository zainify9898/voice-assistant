
import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
from urllib.parse import quote_plus

# Initialize voice assistant
engine = pyttsx3.init()
recognizer = sr.Recognizer()

# Voice response function
def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

# Take voice command
def take_command():
    try:
        with sr.Microphone() as source:
            print("\nListening...")
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=7)

        print("Recognizing...")
        command = recognizer.recognize_google(audio)
        command = command.lower()

        print("You:", command)
        return command

    except sr.WaitTimeoutError:
        speak("I did not hear anything.")
        return ""

    except sr.UnknownValueError:
        speak("Sorry, I could not understand.")
        return ""

    except sr.RequestError:
        speak("Internet connection problem.")
        return ""

    except OSError:
        speak("Microphone is not available.")
        return ""

# Welcome message
speak("Hello! Welcome to your Python Voice Assistant.")
speak("How can I help you?")

# Main program
while True:

    command = take_command()

    if "hello" in command or "hi" in command:
        speak("Hello! How are you?")

    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak("The current time is " + current_time)

    elif "date" in command:
        current_date = datetime.datetime.now().strftime("%d %B %Y")
        speak("Today's date is " + current_date)

    elif "open google" in command:
        webbrowser.open("https://www.google.com")
        speak("Opening Google.")

    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube.")

    elif command.startswith("search for "):
        query = command.replace("search for ", "", 1)
        webbrowser.open(
            "https://www.google.com/search?q=" + quote_plus(query)
        )
        speak("Here are the search results.")

    elif "exit" in command or "stop" in command or "bye" in command:
        speak("Goodbye! Have a nice day.")
        break

    elif command == "":
        continue

    else:
        speak("Sorry, this command is not available.")
