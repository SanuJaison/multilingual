import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
from playsound import playsound
import os

#sppech to text function
def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("PLEASE SAY SOMETHING...")
        recognizer.adjust_for_ambient_noise(source) #to handle bg noises
        audio = recognizer.listen(source)
    try:
        print("RECOGNIZING...")
        text = recognizer.recognize_google(audio)
        print(f"YOU SAID:{text}")
        return text
    except sr.RequestError as e:
        print(f"ERROR WITH GOOGLE SPEECH RECOGNITION SERVICD:(e)")
        return None

#text translation function
def translate_text(text,dest_language = 'es'):
    translator = Translator()
    try:
        translated = translator.translate(text,dst = dest_language)
        print(f"TRANSLATED TEXT: (translated.text)")
        return translated.text
    except Exception as e:
        print(f"TRANSLATION FAILED: (e)")
        return None
    
#text to speech function
def text_to_speech(text,lang = 'en'):
    try:
        tts = gTTS(text = text,lang = lang)
        filename = "output.mp3"
        tts.save(filename)
        playsound(filename)
        os.remove(filename)
    except Exception as e:
        print(f"TEXT TO SPEECH CONVERSATION FAILD: (e)")

#complete multilingual speech translation system
def multilingual_speech_translation():
#step1: covert speech to text
    while True:
        text = speech_to_text()
        if text is None:
            continue

#exit
        if text.lower() == "exit":
            print("EXITING THE PROGRAM.GOODBYE!")
            break

#step2: translate text
        translated_text = translate_text(text,dest_language = 'mal')
        if translated_text is None:
            continue

#step3: convert translated text to speech
        text_to_speech(translated_text,lang = 'ml')
if __name__ == "__main__":
    multilingual_speech_translation()              