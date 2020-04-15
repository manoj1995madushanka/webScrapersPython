import re
from bs4 import BeautifulSoup

with open('file location') as html_code:
    soup = BeautifulSoup(html_code,'lxml')

print(soup.prettify())

#access first paragraph
soup.p

#get first paragraph
soup.find('p')

#get all paragraphs
soup.findAll('p')

soup.findAll(src='cat.jpg')

#get irst tag starts with a
soup.findAll(re.compile("^a"))

#get all tags starts with a
for tag in soup.findAll(re.compile("^a")):
    print(tag)

#pring all tags name starts with a
for tag in soup.findAll(re.compile("^a")):
    print(tag.name)


#get all tags starts wth a and have class which starts with cre
soup.findAll('a',attrs={'class':re.compile("^a")})


#get tags that have i in word
for tag in soup.findAll(re.compile("i")):
    print(tag.name)


#get href attribute that pointed to wikipedia
for tag in soup.findAll(href=re.compile("wikipedia")):
    print(tag)

#add multiple attributes
soup.findAll(['a','img'])

#get all of the html element tag names
for tag in soup.findAll(True):
    print(tag.name)


#write conditions in functions
def has_src_but_no_href(tag):
    return tag.has_attr('src') and not tag.has_attr('href')

soup.findAll(has_src_but_no_href)


def has_no_tom(href):
    return href and not re.compile("Tom_Cat").search(href)

soup.findAll(href=has_no_tom)




