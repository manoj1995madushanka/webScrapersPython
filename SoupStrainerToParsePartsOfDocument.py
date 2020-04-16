import re
from bs4 import SoupStrainer,BeautifulSoup

simple_html = """
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


#get only div tags in website
div_tags = SoupStrainer("div")
soup = BeautifulSoup(simple_html,"lxml",parse_only=div_tags)
print(soup.prettify())

#get link tags only
link_tags=SoupStrainer("a")
soup = BeautifulSoup(simple_html,"lxml",parse_only=link_tags)
print(soup.prettify())

#get all image tags
image_tags = SoupStrainer("img")
soup = BeautifulSoup(simple_html,"lxml",parse_only=image_tags)
print(soup.prettify())


# get all alt attributes
alt_attr = SoupStrainer(alt="creator_image")
soup = BeautifulSoup(simple_html,"lxml",parse_only=alt_attr)
print(soup.prettify())

#get with regular expression which contain link in each id
id_attr = SoupStrainer(id = re.compile("link"))
print(soup.prettify())




