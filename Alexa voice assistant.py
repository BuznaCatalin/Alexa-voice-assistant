import speech_recognition as sr
import time
from time import ctime
import webbrowser
import os
import playsound
from gtts import gTTS
from datetime import datetime as dt
import datetime
import calendar
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
option = Options()


def speak(voice_data):
    tts = gTTS(text=voice_data, lang="en")
    date_string = dt.now().strftime("%d%m%Y%H%M%S")
    filename = "voice" + date_string + ".mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)


def record_audio(ask = True):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        if ask:
            print(ask)
    voice_data = ''
    try:
        voice_data = r.recognize_google(audio)
        print(voice_data)
    except sr.UnknownValueError:
        speak("Sorry, I did not get that")
    return voice_data

def response(voice_data):
    inputs = ['hi', 'hey', 'hola', 'greetings', 'hello']
    for phrase in inputs:
        if phrase in voice_data:
            speak("Hi")
    inputs2 = ["what's up", 'how are you', 'how is your day']
    for phrase in inputs2:
        if phrase in voice_data:
            speak("I'm fine, thank you, how about you")
    if 'name' in voice_data:
        speak("My name is Alexa")
    if 'what time is it' in voice_data:
        now = datetime.datetime.now()
        my_date = datetime.datetime.today()
        weekday = calendar.day_name[my_date.weekday()] 
        monthNum = now.month
        dayNum = now.day
        # A list of months
        month_names = ['January', 'February', 'March', ' April', 'May', 'June', 'July', 'August', 'September', ' October',
                       'November', 'December']

        # A list of ordinal Numbers
        ordinalNumbers = ['1st', '2nd', '3rd', ' 4th', '5th', '6th', '7th', '8th', '9th', '10th', '11th', '12th', '13th',
                          '14th', '15th', '16th',
                          '17th', '18th', '19th', '20th', '21st', '22nd', '23rd', '24rd', '25th', '26th', '27th', '28th',
                          '29th', '30th', '31st']

        speak('Today is ' + weekday + ' ' + month_names[monthNum - 1] + ' the ' + ordinalNumbers[dayNum - 1] + ' .')

    if 'search' in voice_data:
        speak('What do you want to search for?')
        search = record_audio('What do you want to search for?')
        url = "https://google.com/search?q=" + search
        webbrowser.get().open(url)
        speak("Here is what I found for" + search)
    if 'location' in voice_data:
        speak("What is the location?")
        location = record_audio('What is the location?')
        url = "https://google.nl/maps/place/" + location + "/&amp;"
        webbrowser.get().open(url)
        speak("Here is location of" + location)
    if 'your desire program from your computer' in voice_data:
        os.startfile(r'The path to your .exe program')
        speak("this is what i can open")
    if 'Facebook' in voice_data:
        option.add_argument("--disable-infobars")
        option.add_argument("start-maximized")
        option.add_argument("--disable-extensions")

        option.add_experimental_option("prefs", {
            "profile.default_content_setting_values.notifications": 1
        })

        driver = webdriver.Chrome(options=option, executable_path='C:\Chromedriver\chromedriver.exe')
        driver.get('https://www.facebook.com')

        id = driver.find_element_by_name("email")
        psw = driver.find_element_by_name("pass")

        id.send_keys("your fb id")
        psw.send_keys("your fb password")

        driver.find_element_by_xpath("//*[@id='u_0_d']").click()
    if 'exit' in voice_data:
        speak("ok, bye")
        exit()


speak("Hello, how can i help you?")

voice_data = record_audio()
response(voice_data)

time.sleep(1)
while 1:
    voice_data = record_audio()
    response(voice_data)

