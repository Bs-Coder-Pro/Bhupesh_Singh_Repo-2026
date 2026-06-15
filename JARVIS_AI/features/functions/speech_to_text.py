import os
import speech_recognition as sr
# from main.features.commands.


def say(text):
    return os.system(f"say: {text}").strip()


def user_voice_commands():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)
        try:
            query = recognizer.recognize_amazon(audio, language="en-in")
            return f"user_said: {query}"
        except Exception as e:
            raise "Error Occurred: [ Sorry from JARVIS ]"