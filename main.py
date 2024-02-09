from bs4 import BeautifulSoup
import requests

response = requests.get('https://news.ycombinator.com/')
page = response.text

soup = BeautifulSoup(page, 'html.parser')
titles = [item.text for item in soup.select('.titleline a:not(.sitebit.comhead a)')]

