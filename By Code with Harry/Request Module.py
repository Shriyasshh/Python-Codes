import requests

respose=requests.get("https://www.google.com/")
print(respose.text)


url="https://jsonplaceholder.typicode.com/posts"
data={
    "title":"Bob",
    "body":"bro",
    "userId":1}
headers= {'Content-type': 'application/json; charset=UTF-8',}
response=requests.post(url,headers=headers,json=data)

print(response.text)


# url="https://jsonplaceholder.typicode.com/posts/1"
# r=requests.get(url)

# from bs4 import BeautifulSoup
# soup=BeautifulSoup(r.text,"html.parser")
# print(soup.title)