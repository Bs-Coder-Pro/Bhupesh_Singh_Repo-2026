import speech_recognition as sr
import commands
from speech_recognition import Recognizer
from speech_recognition import audio, audioop, AudioData, AudioFile, AudioSource


def text_to_speech():
    recognizer = Recognizer()
    return recognizer


def jarvis_audio():
    Audio = (audio, audioop, AudioData, AudioFile, AudioSource)

    return Audio

while True:
    try:
        commands.clear_screen()
        text_to_speech.recognizer()
        jarvis_audio()
        if text_to_speech.recognizer:
            pass
    except:
        pass
