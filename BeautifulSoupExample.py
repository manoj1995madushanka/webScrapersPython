#pip installBeautifulSoup4
#pip install lxml
#pip install html5lib

import requests
import webbrowser
from bs4 import BeautifulSoup

very_simple_html = """
<html lang="en">
<head>
  <meta charset="utf-8">

  <title>The HTML5 Herald</title>
  <meta name="description" content="The HTML5 Herald">
  <meta name="author" content="SitePoint">

  <link rel="stylesheet" href="css/styles.css?v=1.0">

</head>

<body>
  <script src="js/scripts.js"></script>
</body>
</html>
"""

soup = BeautifulSoup(very_simple_html)
print(soup.prettify())

soup.title
soup.body


soup.body.name
soup.body.parent.name

soup.p

#return first a tag
soup.a

#print parser
html = """<h1><a><b><th></h1>"""
soup = BeautifulSoup(html)
print(soup.prettify())

soup = BeautifulSoup(html,'lxml')
print(soup.prettify())


#parse as a xml
soup = BeautifulSoup(html,'xml')
print(soup.prettify())

#use lxml
soup = BeautifulSoup(html,'lxml xml')
print(soup.prettify())