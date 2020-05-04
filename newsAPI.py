import requests
from win32com.client import Dispatch
import json

def speak (st):
  speak = Dispatch("SAPI.SpVoice")

  speak.Speak(st)


if __name__ == '__main__':
    url="http://newsapi.org/v2/top-headlines?country=in&apiKey=dae7af9d4f1e4b64a77403386986b9e4"
    news=requests.get(url).text

    news_dic=json.loads(news)
    articles=news_dic['articles']
    print("Todays news")
    for art in articles:

        print(  "Title: "+art['title'])
        speak(art['title'])
        print("Description:",end=" ")
        print(art["description"])
        speak(art["description"])

        print("Moving on to next news")
        speak("Moving on to next news")


