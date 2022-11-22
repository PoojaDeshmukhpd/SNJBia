import speech_recognition as sr
import pyttsx3

import datetime

import webbrowser

import os

placementInfo="in 2021 22 placement count was 38 candidates from computer department, in 2020 21 placement count was 48 candidates from computer department "
collegeInfo="The Jain Gurukul campus has various faculties, out of which the SNJB's Late Sau Kantabai Bhavarlalji Jain College of Engineering, which is approved by the All India Council of Technical Education (AICTE)"
placementMech="in 2021 22 placement count was 27 candidates from mechanical department, in 2019 20 placement count was 40 candidates from mechanical department "


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def username():
    talk("What should i call you")
    uname = take_command()
    talk("Welcome")
    talk(uname)
    # columns = shutil.get_terminal_size().columns
    #
    # print("#####################".center(columns))
    # print("Welcome Mr.", uname.center(columns))
    # print("#####################".center(columns))

    talk("How can i Help you")



def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():

    try:
        with sr.Microphone() as source:
            print("listning")
            #listener.pause_threshold = 1
            voice = listener.listen(source)
            command = listener.recognize_google(voice, language ='en-in')
            command = command.lower()
            if 'snjbya' in command:
                command = command.replace('snjbya', '')
    except:
        print("error")
        print("Unable to Recognize your voice.")
        return "None"

    return command


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        talk("Good Morning!")

    elif hour >= 12 and hour < 18:
        talk("Good Afternoon!")

    else:
        talk("Good Evening!")

    assname = ("SNJBia")
    talk("I am your Voice Assistant SNJBYA")


if __name__ == '__main__':
    clear = lambda: os.system('cls')

    # This Function will clean any
    # command before execution of this python file
    clear()
    wishMe()
    username()

    while True:
        command = take_command().lower()
        print(command)

        if 'computer department placement ' in command:
            webbrowser.open_new_tab(
                'http://www.snjb.org/engineering/images/department/Update_Placement_Summery_Computer_Per.png')
            print(placementInfo)
            talk(placementInfo)

        elif 'mechanical department placement ' in command:
            webbrowser.open_new_tab(
                'http://www.snjb.org/engineering/images/department/ce_pd4.png')
            print(placementMech)
            talk(placementMech)

        elif command=="none":
            talk("hey i didn't heard properly come again?")

        elif 'how are you' in command:
            talk("I am fine, Thank you")
            talk("How are you, Sir")

        elif 'departments' in command:
            talk("Computer Engineering, Civil Engineering, Electronics and Telecommunication, Mechanical Engineering, Artificial Intelligence and Data Science")

        elif 'branches' in command:
            talk("Computer Engineering, Civil Engineering, Electronics and Telecommunication, Mechanical Engineering, Artificial Intelligence and Data Science")
        elif 'how many branches' in command:
            webbrowser.open_new('http://www.snjb.org/engineering/About/about_engineering#about')
            talk(collegeInfo)

        elif 'college information' in command:
            webbrowser.open_new_tab('http://www.snjb.org/engineering/About/about_engineering#about')
            talk(collegeInfo)

        elif 'DSE' in command:
            webbrowser.open_new_tab('http://www.snjb.org/engineering/Admission/fees_structure_dse')

        elif 'direct second year admission' in command:
            webbrowser.open_new_tab('http://www.snjb.org/engineering/Admission/fees_structure_dse')

        elif 'principal' in command:
            print("Dr.M.D.Kokate is Principal of SNJB's KBJ College of Engineering Chandwad")
            talk("Dr.M.D.Kokate is Principal of SNJB's KBJ College of Engineering Chandwad")
            webbrowser.open_new_tab('http://www.snjb.org/engineering/About/engineering_mba_principals_message')

        elif 'vice principal' in command:
            print("Sanghavi Sir is vice principle of SNJB's KBJ College of Engineering Chandwad")
            talk("Sanghavi Sir is vice principle of SNJB's KBJ College of Engineering Chandwad")

        elif 'account section' in command:
            webbrowser.open_new_tab('http://www.snjb.org/engineering/images/dynamic_page/Account_Section.jpg')

        elif 'vision and mission' in command:
            talk("Vision is Transform young aspirant learners towards creativity and professionalism for societal growth through quality technical education.")
            talk("Mission is To share values, ideas, beliefs by encouraging faculties and students for welfare of society.")
            webbrowser.open_new_tab('http://www.snjb.org/engineering/About/engineering_mba_mission_vision')

        elif 'college campus' in command:
            webbrowser.open_new_tab('https://youtu.be/sweoKSBXeNc')

        elif 'how many labs in computer department' in command:
            print("Total 12 Labs are available in computer department")
            talk("Total 12 Labs are available in computer department")
            webbrowser.open_new_tab('snjb.org/engineering/Computer_engineering/computer_engineering_laboratories')

        elif 'student section' in command:
            webbrowser.open_new_tab('http://www.snjb.org/engineering/images/dynamic_page/Student_Section.jpg')
            print("total 5 faculties are availabe in student section you can see the name and email id")
            talk("total 5 faculties are availabe in student section you can see the name and email id")

        elif 'account section' in command:
            webbrowser.open_new_tab('http://www.snjb.org/engineering/images/dynamic_page/Account_Section.jpg')
            print("total 3 faculties are availabe in account section you can see the name and email id")
            talk("total 3 faculties are availabe in account section you can see the name and email id")

        elif 'library section' in command:
            webbrowser.open_new_tab('http://www.snjb.org/engineering/images/dynamic_page/Account_Section.jpg')
            print("total 3 faculties are availabe in library section you can see the name and email id")
            talk("total 3 faculties are availabe in library section you can see the name and email id")


        elif 'be computer engineering result' in command:
            print("Academic Year 2021-22  100%  2018-19 96.34%")
            talk("Academic Year 2021-22  100%  2018-19 96.34%")
            webbrowser.open_new_tab('http://www.snjb.org/engineering/Computer_engineering/computer_engineering_results#r2')

        elif 'achievements of computer department' in command:
            webbrowser.open_new_tab('http://www.snjb.org/engineering/Computer_engineering/computer_engineering_achievements')
            talk(collegeInfo)

        elif 'software lab' in command:
            webbrowser.open_new_tab('http://www.snjb.org/engineering/images/department/LRM_EXPORT_20180820_211245imgFile5b7fbfc2b0165_thumb.jpg')
            print("Operating System: WINDOWS 7, UBUNTU Lab Incharge - Prof. S. B. Ambhore")
            talk("Operating System: WINDOWS 7, UBUNTU Lab Incharge - Prof. S. B. Ambhore")

        elif 'project lab' in command:
            webbrowser.open_new_tab('http://www.snjb.org/engineering/images/department/PL.JPG')
            print("Operating System:Windows 7, UBUNTU. Lab In-charge: Prof. D. S. Rajnor")
            talk("Operating System:Windows 7, UBUNTU. Lab In-charge: Prof. D. S. Rajnor")

        else:
            talk("hey i didn't heard properly come again?")





