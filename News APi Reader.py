            #Read newspaper
            # read news api from different site it will be just like alexa,it will pronounce the news
# #FOR  latest news you have to parse JSON.Use JSON module and request module to make a newspaper. IF WE WIll name our
# def speak(str):
#     from win32com.client import Dispatch
#
#     speak = Dispatch("SAPI.SpVoice")
#
#     speak.Speak(str)
#
# if __name__ == '__main__':
#     speak("how are you my friend")



#Reading newspaper
import requests
import json

def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

if __name__ == '__main__':
    speak("News for today.. Lets begin")
    url = "https://newsapi.org/v2/everything?q=tesla&from=2021-07-21&sortBy=publishedAt&apiKey=dfe0abf93efb4d11bf10b0b09ad25144" #this url should be copied from any news api sites
    news = requests.get(url).text
    news_dict = json.loads(news)
    arts = news_dict['articles']
    for article in arts:
        speak(article['title'])
        print(article['title'])
        speak("Moving on to the next news..")

    speak("Thanks for listening...")


