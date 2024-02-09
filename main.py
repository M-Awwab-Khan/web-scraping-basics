from bs4 import BeautifulSoup
import requests

response = requests.get('https://news.ycombinator.com/')
page = response.text

soup = BeautifulSoup(page, 'html.parser')
titles = [item.text for item in soup.select('.titleline a:not(.sitebit.comhead a)')]
upvotes = [item.text for item in soup.select('.subline .score')]


for i in range(0, len(titles)+1):
    print(f"{i+1}. {titles[i]} : {upvotes[i]}")