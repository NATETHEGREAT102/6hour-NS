import os
import time
import webbrowser
import speech_recognition as sr
import pyttsx3
from openai import OpenAI

# 1. Initialize OpenAI Brain (Replace with your actual API key)
# It's best practice to use os.environ.get("OPENAI_API_KEY")
client = OpenAI(api_key="YOUR_OPENAI_API_KEY")

# 2. Initialize Voice Engine (Speaking)
engine = pyttsx3.init('sapi5')  # 'sapi5' is standard for Windows. Use 'nsss' for Mac.
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # 0 for Male (Jarvis), 1 for Female (Friday)
engine.setProperty('rate', 175)  # Adjust speaking speed


def speak(text):
    """Makes the assistant speak out loud."""
    print(f"J.A.R.V.I.S.: {text}")
    engine.say(text)
    engine.runAndWait()


def listen_command():
    """Listens to the microphone and converts audio to text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening...")
        recognizer.pause_threshold = 1.0
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-US')
        print(f"You said: {query}")
        return query.lower()
    except Exception:
        return ""


def ask_jarvis_brain(user_input):
    """Sends the speech text to OpenAI configured with a Jarvis persona."""
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # Fast and cost-efficient
            messages=[
                {"role": "system",
                 "content": "You are J.A.R.V.I.S., Tony Stark's brilliant, slightly sarcastic, ultra-helpful AI butler. Keep responses concise and conversational."},
                {"role": "user", "content": user_input}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Sir, I encountered an issue connecting to my core servers. {e}"


# 3. Main Execution Loop
if __name__ == "__main__":
    speak("Initialization complete. Systems are online, Sir. How can I assist you today?")

    while True:
        query = listen_command()

        if not query:
            continue

        # Hardcoded Local Automation Commands
        if "goodbye jarvis" in query or "go to sleep" in query:
            speak("Understood, Sir. Powering down systems. Goodbye.")
            break

        elif "open youtube" in query:
            speak("Opening YouTube, Sir.")
            webbrowser.open("https://youtube.com")

        elif ('open google' in query):
            speak("Navigating to Google.")
            webbrowser.open("https://google.com")

            # Contextual Brain Queries (LLM)
else:
            ai_response = ask_jarvis_brain(query)
            speak(ai_response)


def mic_input():
    """
    Takes input from the microphone and returns it as a string
    :return: (string) input from the microphone, (boolean) False if failure
    """
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.energy_threshold = 4000
            audio = r.listen(source, timeout=30, phrase_time_limit=20)

        try:
            print("Recognizing...")
            command = r.recognize_google(audio, language='en-in').lower()
            print(f"User said: {command}\n")
        except Exception:
            print("Say that again please...")
            command = mic_input()
        return command
    except Exception as ex:
        print(ex)
        return False


def tts(text):
    """
    Text to speech function
    :param text: (string) text to be spoken
    :return: (boolean) True if successful, False if failure
    """
    try:
        engine.say(text)
        engine.runAndWait()
        engine.setProperty('rate', 175)
        return True
    except Exception as ex:
        print(ex)
        return False

