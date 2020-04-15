import requests
import webbrowser
from bs4 import BeautifulSoup

with open('url location here') as html_code:
    soup = BeautifulSoup(html_code,'lxml')

print(soup.prettify())

tag = soup.title
print(tag)

#exact links
tags = soup.a
print(tags)
#print link
print(tags['href'])
#get all attributes
print(tags.attrs)

#exact first images
tag=soup.img
print(tag)

print(tag.attrs)

#get classes that attribute have
print(tag['class']) #will print all classes

#access comment
tag =soup.i



