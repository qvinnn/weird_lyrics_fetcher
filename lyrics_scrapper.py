import requests

from bs4 import BeautifulSoup

#ask user for a musixmatch link
user_input = input("insert musixmatch URL:\n")

#Setting up requests-HTML and Soup 
page = requests.get(
    user_input,
    headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    
)
soup = BeautifulSoup(page.content,'html.parser', from_encoding="utf-8")

#pretty sure this can be improved lol
lyrics = soup.find_all(class_="mxm-lyrics__content")
for text in lyrics:
    print(text.text)
