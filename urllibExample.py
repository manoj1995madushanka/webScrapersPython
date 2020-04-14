import urllib.request
import webbrowser
from pprint import pprint

bin_url = 'http://httpbin.org/'

#open url from browsre
#webbrowser.open(bin_url)

#download content makin GET
resp = urllib.request.urlopen(bin_url)

#print status code
resp.getcode()

#access header data
print(resp.info())

#print html data
data = resp.read()
pprint(data.decode('UTF-8'))

#retrive all options that website supports
req = urllib.request.Request(bin_url,method='OPTIONS')
resp = urllib.request.urlopen(req)
print(resp.info())

#how to post data using urllib in urllib unencoded data can not post
post_data = urllib.parse.urlencode({"name":"Alice","college":"SAC"}).encode('ascii')
#this header indicates to the server this request is made using fireox browser
req = urllib.request.Request('https://httpbin.org/post',method='POST',data=post_data,headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'})
resp = urllib.request.urlopen(req)
print(resp.info())

#now decode and read our resp data
data = resp.read().decode("UTF-8")
pprint(data)

#use with block
with urllib.request.urlopen('https://www.google.com/search?q=pluralsight') as resp:
    pprint(resp.read().decode('ISO-8859-1'))

#when above with block return a exception we need to handle that as below
from urllib.error import URLError, HTTPError
try:
    with urllib.request.urlopen('https://www.google.com/search?q=pluralsight') as resp:
        pprint(resp.read().decode('ISO-8859-1'))
except HTTPError as e:
    print(e.reason,e.code)


#devide url into parts
parsed_data = urllib.parse.urlparse('http://www.loonycon.in:80/language/python.html')




