import webbrowser
import time
import speech_recognition as sr
import datetime
import content
import string
import os

# color settings
from colored import fg, bg, attr
reset = attr('reset')

# function for speaking
def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.speak(str)

# menu of application
menu=['\n  1. --> INDIA News', '  2. --> HEALTH News', '  3. --> TECHNOLOGY News',
      '  4. --> SCIENCE News', '  5. --> ENTERTAINMENT News', '  6. --> SPORTS News',
      '  7. --> BUSINESSS News', '  8. --> Open YouTube', '  9. --> Give Location',
      ' 10. --> Web-Search\n']

print(fg('yellow') + '\n [ WELCOME TO NEWS-FEEDER ]\n' + reset)

speak('WELCOME TO NEWS-FEEDER')
time.sleep(1)

# looping the main menu
while 1:
    os.system('cls')
    print(fg('yellow') + '\n [ WELCOME TO NEWS-FEEDER ]\n\n' + reset)
    # prints todays date and time
    now = datetime.datetime.now()
    print(fg(1) + ' DATE:'f'{now:%d-%m-%Y | %H:%M }' + reset)
    
    print(fg(5) + '\n\n    ( MAIN MENU )' + reset)
    for row in menu:
        print(fg('green')+ row + reset)
    print(fg(45)+' -> Tell me, What you want to do today?'+reset)
    speak('Tell me what you want to do today')
    r=sr.Recognizer()
    with sr.Microphone() as source:
        audio=r.listen(source)
    try:
        voice_data=r.recognize_google(audio)
        print('    You selected - ' +fg(5)+ voice_data+reset)
        time.sleep(3)
        os.system('cls')
        if 'India news' in voice_data:
            speak('You selected'+'India news')
            content.india()
            time.sleep(5)
        elif 'health news' in voice_data:
            speak('You selected'+'health news')
            content.health()
            time.sleep(5)
        elif 'technology news' in voice_data:
            speak('You selected'+'technology news')
            content.technology()
            time.sleep(5)
        elif 'science news' in voice_data:
            speak('You selected'+'science news')
            content.science()
            time.sleep(5)
        elif 'entertainment news' in voice_data:
            speak('You selected'+'entertainment news')
            content.entertainment()
            time.sleep(5)
        elif 'sports news' in voice_data:
            speak('You selected'+'sports news')
            content.sports()
            time.sleep(5)
        elif 'business news' in voice_data:
            speak('You selected business news')
            content.business()
            time.sleep(5)
        elif 'YouTube' in voice_data:
            speak('You selected open YouTube')
            time.sleep(1)
            speak('opening your youtube page..')
            url='https://www.youtube.com'
            webbrowser.get().open(url)
            time.sleep(2)
        elif 'location' in voice_data:
            speak('You selected give location')
            print(fg('cyan')+'\n\t\t-> Which place to locate:',end=' '+reset)
            speak('Which place to locate')
            with sr.Microphone() as source:
                audio=r.listen(source)
                try:
                    place=r.recognize_google(audio)
                    print(fg('red')+place+reset)
                    url='https://google.nl/maps/place/'+place+'/&amp'
                    webbrowser.get().open(url)
                    speak('giving location of'+place)
                except sr.UnknownValueError:
                    print(fg('green') + '\n\n\t\t Sorry, i didnt hear you, Try again..')
                    speak(' Sorry, i didnt hear you, try again')
                    pass
                except sr.RequestError:
                    print(fg('green') + '\n\n\t\t Sorry, my speech service is down, Try later..')
                    speak('Sorry, my speech service is down, try later')
                    pass
            time.sleep(2)
        elif 'search' in voice_data:
            speak('You selected web search')
            print(fg('cyan')+'\n\t\t-> What you want to search:',end=' '+reset)
            speak('What you want to search')
            with sr.Microphone() as source:
                audio=r.listen(source)
                try:
                    thing=r.recognize_google(audio)
                    print(fg('red')+thing+reset)
                    url='https://google.com/search?q='+thing
                    webbrowser.get().open(url)
                    speak('giving search result for '+ thing)
                except sr.UnknownValueError:
                    print(fg('green') + '\n\n\t\t Sorry, i didnt hear you, Try again..')
                    speak(' Sorry, i didnt hear you, try again')
                    pass
                except sr.RequestError:
                    print(fg('green') + '\n\n\t\t Sorry, my speech service is down, Try later..')
                    speak('Sorry, my speech service is down, try later')
                    pass
            time.sleep(2)
        elif 'exit' in voice_data:
            speak('Good Bye')
            exit()
        else:
            print(fg('green') + '\n\n\t\tSorry - Invalid Command - Try again..')
            speak('Sorry, Invalid command, try again')
            continue         
    except sr.UnknownValueError:
        print(fg('green') + '\n\n Sorry, i didnt hear you, Try again..')
        speak(' Sorry, i didnt hear you, try again')
    except sr.RequestError:
        print(fg('green') + '\n\n Sorry, my speech service is down, Try later..')
        speak('Sorry, my speech service is down, try later')

                                    # COPYRIGHT (C) SANJAY KUMAR #
