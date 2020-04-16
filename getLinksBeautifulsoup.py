import requests
import re
import webbrowser
from bs4 import BeautifulSoup

url = 'https://pypi.org/project/httplib2/'
resp = requests.get(url)
soup = BeautifulSoup(resp.text,'lxml')
print(soup)

#get all links in that webpage
soup.find_all("a",attrs={'hre':re.compile("^https")})


for link in soup.find_all("a",attrs={'hre':re.compile("^https")}):
    print(link['href'])


for link in soup.find_all("a",attrs={'hre':re.compile("^https|http")}):
    print(link['href'])

for link in soup.findAll("a",hre=True):
    print(link['href'])


for link in soup.findAll('a',href=True):
    if not link['href'].startwith('http'):
        link = url+link['href'].strip('/')
    else:
        link=link['href']
    print(link)


