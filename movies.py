from bs4 import BeautifulSoup
import requests 

response = requests.get('https://www.empireonline.com/movies/features/best-movies-2/')
soup = BeautifulSoup(response.text, 'html.parser')

titles = [item.text for item in soup.select('.listicleItem_listicle-item__title__BfenH')]
titles.reverse()
for title in titles:
    print(title)