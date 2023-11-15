import requests

from bs4 import BeautifulSoup

#Setting up requests-HTML and Soup 
page = requests.get(
    "https://www.musixmatch.com/lyrics/jaz-22/why-is-it-so-loud-in-here-Jaycie-Rhetorical",
    headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    
)
soup = BeautifulSoup(page.content,'html.parser', from_encoding="utf-8")

#pretty sure this can be improved lol
lyrics = soup.find_all(class_="mxm-lyrics__content")
for text in lyrics:
    print(text.text)
