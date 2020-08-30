# Read newspaper with python
# using two important and popular python pacakages requests and json
import requests
import json

# color settings
from colored import fg, bg, attr
reset = attr('reset')

# function for speech
def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.speak(str)

# function for India news
def india():
    print(fg('cyan') + "\n << Here is Today's India News >>" + reset)
    speak("Here is Today's news of India")
    url="http://newsapi.org/v2/top-headlines?country=in&apiKey=3e33ba1948eb4504b47af11904512730"
    news=requests.get(url).text # creating url request
    news_dict=json.loads(news) # creating python object
    contents=news_dict["articles"]
    i=1
    print('\n--------------------------------------------------------------------------------------------')
    for content in contents: # iterating the news
            print(fg('yellow') + '(',i,')',content['title'],'\n' + reset)
            speak(str(i))
            speak(content['title'])
            if(content['description']):
                print(fg('cyan')+'->',content['description']+reset)
                speak(content['description'])
            i=i+1
            print('\n----------------------------------------------------------------------------------------------')
    print(fg('cyan') + '\n********** Thank you for listening..... ***********' + reset)
    speak("thank you for listening")

# function for health news
def health():
    print(fg('cyan')+"\n << Here is Today's Health News >>"+reset)
    speak("Here is Today's health news")
    url="http://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=3e33ba1948eb4504b47af11904512730"
    news=requests.get(url).text # creating url request
    news_dict=json.loads(news) # creating python object
    contents=news_dict["articles"]
    i=1
    print('\n--------------------------------------------------------------------------------------------')
    for content in contents: # iterating the news
        print(fg(3)+'(',i,')',content['title'],'\n'+reset)
        speak(str(i))
        speak(content['title'])
        if(content['description']):
            print(fg('cyan')+'->',content['description']+reset)
            speak(content['description'])
        i=i+1
        print('\n----------------------------------------------------------------------------------------------')
    print(fg('cyan') + '\n********** Thank you for listening..... ***********' + reset)
    speak("thank you for listening")

# function for Technology news
def technology():
    print(fg('cyan')+"\n << Here is Today's Technology News >>"+reset)
    speak("Here is Today's Technology news")
    url="http://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=3e33ba1948eb4504b47af11904512730"
    news=requests.get(url).text # creating url request
    news_dict=json.loads(news) # creating python object
    contents=news_dict["articles"]
    i=1
    print('\n--------------------------------------------------------------------------------------------')
    for content in contents: # iterating the news
        print(fg(3)+'(',i,')',content['title'],'\n'+reset)
        speak(str(i))
        speak(content['title'])
        if(content['description']):
            print(fg('cyan')+'->',content['description']+reset)
            speak(content['description'])
        i=i+1
        print('\n----------------------------------------------------------------------------------------------')
    print(fg('cyan')+'\n********** Thank you for listening..... ***********'+reset)
    speak("thank you for listening")

# function for Science news
def science():
    print(fg('cyan')+"\n << Here is Today's Science News >>"+reset)
    speak("Here is Today's Science news")
    url="http://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=3e33ba1948eb4504b47af11904512730"
    news=requests.get(url).text # creating url request
    news_dict=json.loads(news) # creating python object
    contents=news_dict["articles"]
    i=1
    print('\n--------------------------------------------------------------------------------------------')
    for content in contents: # iterating the news
        print(fg(3)+'(',i,')',content['title'],'\n'+reset)
        speak(str(i))
        speak(content['title'])
        if(content['description']):
            print(fg('cyan')+'->',content['description']+reset)
            speak(content['description'])
        i=i+1
        print('\n----------------------------------------------------------------------------------------------')
    print(fg('cyan')+'\n********** Thank you for listening..... ***********'+reset)
    speak("thank you for listening")

# function for entertainment news
def entertainment():
    print(fg('cyan') + "\n << Here is Today's Entertainment News >>" + reset)
    speak("Here is Today's entertainment news")
    url="http://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=3e33ba1948eb4504b47af11904512730"
    news=requests.get(url).text # creating url request
    news_dict=json.loads(news) # creating python object
    contents=news_dict["articles"]
    i=1
    print('\n--------------------------------------------------------------------------------------------')
    for content in contents: # iterating the news
        print(fg(3)+'(',i,')',content['title'],'\n'+reset)
        speak(str(i))
        speak(content['title'])
        if(content['description']):
            print(fg('cyan')+'->',content['description']+reset)
            speak(content['description'])
        i=i+1
        print('\n----------------------------------------------------------------------------------------------')
    print(fg('cyan')+'\n********** Thank you for listening..... ***********'+reset)
    speak("thank you for listening")

# function for sports news
def sports():
    print(fg('cyan') + "\n << Here is Today's Sports News >>" + reset)
    speak("Here is Today's sports news")
    url="http://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=3e33ba1948eb4504b47af11904512730"
    news=requests.get(url).text # creating url request
    news_dict=json.loads(news) # creating python object
    contents=news_dict["articles"]
    i=1
    print('\n--------------------------------------------------------------------------------------------')
    for content in contents: # iterating the news
        print(fg(3)+'(',i,')',content['title'],'\n'+reset)
        speak(str(i))
        speak(content['title'])
        if(content['description']):
            print(fg('cyan')+'->',content['description']+reset)
            speak(content['description'])
        i=i+1
        print('\n----------------------------------------------------------------------------------------------')
    print(fg('cyan')+'\n********** Thank you for listening..... ***********'+reset)
    speak("thank you for listening")

def business():
    print(fg('cyan') + "\n << Here is Today's Business News >>" + reset)
    speak("Here is Today's business news")
    url="http://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=3e33ba1948eb4504b47af11904512730"
    news=requests.get(url).text # creating url request
    news_dict=json.loads(news) # creating python object
    contents=news_dict["articles"]
    i=1
    print('\n--------------------------------------------------------------------------------------------')
    for content in contents: # iterating the news
        print(fg(3)+'(',i,')',content['title'],'\n',reset)
        speak(str(i))
        speak(content['title'])
        if(content['description']):
            print(fg('cyan')+'->',content['description']+reset)
            speak(content['description'])
        i=i+1
        print('\n----------------------------------------------------------------------------------------------')
    print(fg('cyan')+'\n********** Thank you for listening..... ***********'+reset)
    speak("thank you for listening")
    