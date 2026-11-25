# Python Voice Assistant 🎙️

A simple voice-controlled personal assistant built in Python. It listens to your voice commands, understands them with speech recognition, and performs everyday tasks — telling the time and date, opening Google and YouTube, searching the web by voice, and replying with text-to-speech.

## Features

- Greets the user
- Recognizes voice commands with SpeechRecognition
- Tells the current time and date
- Opens Google and YouTube
- Searches Google using voice commands
- Responds through voice (pyttsx3 text-to-speech)
- Exits when you say "Bye" or "Stop"

## Voice Commands

| Voice Command | Action |
|---|---|
| Hello | Greets the user |
| What is the time? | Tells the current time |
| What is the date? | Tells the current date |
| Open Google | Opens Google in the browser |
| Open YouTube | Opens YouTube in the browser |
| Search ... | Searches Google for your query |
| Bye / Stop | Exits the assistant |

## Technologies Used

- Python 3
- SpeechRecognition
- pyttsx3
- PyAudio
- datetime
- webbrowser

## Installation

```bash
python -m pip install SpeechRecognition
python -m pip install pyttsx3
python -m pip install PyAudio
```

## How to Run

1. Clone or download this repository.
2. Open the project folder in Visual Studio Code.
3. Install the required libraries.
4. Connect a working microphone.
5. Run:

```bash
python assistant.py
```

6. Speak your commands when the assistant starts listening.
