'''from newsapi import NewsApiClient

# Init
newsapi =NewsApiClient(api_key='0e09c5d153d14644ad04b5bbe4184548')

# /v2/top-headlines
# top_headlines = newsapi.get_top_headlines(q='bitcoin',
#                                         sources='bbc-news,the-verge',
#                                         category='business',
#                                         language='en',)
top_headlines = newsapi.get_top_headlines(q='Python',
                                        category='technology',
                                        language='en')


sources=newsapi.get_sources()
print(sources)
'''


import requests
import json

query=input("Enter the topic you want to search: ")

url=f"https://newsapi.org/v2/everything?q={query}&apiKey=0e09c5d153d14644ad04b5bbe4184548"
r=requests.get(url)
news=json.loads(r.text)
# print(news,type(news))

for i in news['articles']:
    # print(i['title'])
    # print(i['description'])
    # # print(i['url'])
    # print("-----------------\n-----------------")

    print("Title:", i['title'])
    print("Description:", i['description'])
    print("Published At:", i['publishedAt'])  # Displaying the date of upload
    print("-----------------\n-----------------")