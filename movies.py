from bs4 import BeautifulSoup
import requests 
URL = 'https://www.empireonline.com/movies/features/best-movies-2/'
response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')

titles = [item.text for item in soup.select('.listicleItem_listicle-item__title__BfenH')]
titles.reverse()
with open('movies.txt', 'w') as f:
    for title in titles:
        f.write(f"{title}\n")

