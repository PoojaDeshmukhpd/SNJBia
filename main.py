import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import urllib.request
import webbrowser
import re

collegeInfo="The Jain Gurukul campus has various faculties, out of which the SNJB's Late Sau Kantabai Bhavarlalji Jain College of Engineering, which is approved by the All India Council of Technical Education (AICTE)"
placementInfo="in 2021 22 placement count was 38 candidates from computer department, in 2020 21 placement count was 48 candidates from computer department "
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():

    try:
        with sr.Microphone() as source:
            print("listning")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'snjbya' in command:
                command = command.replace('snjbya', '')
    except:
        print("error")

    return command

def run_snjbya():
    command = take_command()
    print(command)

    if  'placement' in command:
        webbrowser.open_new_tab('http://www.snjb.org/engineering/Computer_engineering/computer_engineering_placements_statistics')
        talk(placementInfo)

    elif 'college information' or 'about college' or 'information about college' in command:
        webbrowser.open_new_tab('http://www.snjb.org/engineering/About/about_engineering#about')
        talk(collegeInfo)
    elif 'DSE' or 'direct second year admission' in command:
        webbrowser.open_new_tab('http://www.snjb.org/engineering/Admission/fees_structure_dse')
    elif 'about college' in command:
        time =datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('current time is'+ time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk("sorry, I have a headache")
    elif 'are you single' in command:
        talk("I am in a relationship with wifi")
    elif 'i love you' in command:
        talk("Thank you, i am also love to spend time with you")
    elif 'joke' in command:
        talk(pyjokes.get_joke())

    else:
        talk("hey i didn't heard properly come again?")


while True:
    run_snjbya()