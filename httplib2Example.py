import webbrowser
import httplib2
from pprint import pprint

bin_url = 'https://httpbin.org/'
#open link in default browser
# webbrowser.open(bin_url)

http = httplib2.Http()
# get headers and data from link and assign them to two variables
resp,data = http.request(bin_url)
#print header data
#pprint(resp)

#get type and lenght 
print(type(resp))
print(len(resp))
#print responce status
print(resp.status)
#print responce reason
print(resp.reason)
#print responce version
print(resp.version)
#print original url that we requested that will not print anything when site not redirect our url
print(resp.previous)
#print responce data
pprint(data)
#print type and length of data
print(type(data),len(data)) #the type of data is bytes we can convert type as below

html = data.decode('UTF-8')
print(type(data))
#print html page
pprint(html)

#request what operations(GET,POST,...) support for relevent url
resp,data = http.request(bin_url,method='OPTION')
pprint(resp) # we can check operations from access-control-allow-methods

#when we need only get header 
resp,data = http.request(bin_url,method='HEAD')
pprint(resp)

#specipy method
resp,data = http.request(bin_url,method='GET')
pprint(resp)

#how to make post request
post_data = '{"name":"Alice","college":"SAC"}'
resp,data = http.request('http://httpbin.org/post',method='POST',body=post_data,headers={'content-type':'application/json'})
pprint(resp)

#set http follow redirects for GET request
http.follow_redirects

#set http follow redirect for other operations such as POST,PUT but this is not recommond
http.follow_redirects

#set http not follow redirects for GET request
http.follow_redirects = False



