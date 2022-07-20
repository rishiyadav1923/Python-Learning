# Python Requests head() Method

# Example
# Make a HEAD request to a web page, and return the HTTP headers:

import requests

x = requests.head('https://www.w3schools.com/python/demopage.php')

print(x.headers)

# Definition and Usage
# The head() method sends a HEAD request to the specified url.
# HEAD requests are done when you do not need the content of the file, but only the status_code or HTTP headers.

# Syntax
# requests.head(url, args)
# args means zero or more of the named arguments in the parameter table below. Example:
# requests.head(url, timeout=2.50)

# Parameter Values
# Parameter		                        Description
# url		                            Required. The url of the request

import requests

#the required first parameter of the 'head' method is the 'url':
x = requests.head('https://www.w3schools.com/python/demopage.php')

#print the response headers (the HTTP headers of the requested file):
print(x.headers)

# allow_redirects                       Optional. A Boolean to enable/disable redirection.
#                                       Default False (not allowing redirects)

import requests

url = 'https://w3schools.com/python/demopage.php'

x = requests.head(url, allow_redirects=True)

#The server will redirect this url to 'https://w3schools.com/python/demopage.php'
#and since the head method by default do not allow redirects, we must use allow_redirects=True.

print(x.status_code)

import requests

url = 'https://w3schools.com/python/demopage.php'

x = requests.head(url)

#Since the server will redirect this url to 'https://w3schools.com/python/demopage.php'
#AND the head method by default do not allow redirects, we will get an 301 status code.

print(x.status_code)

# auth		                            Optional. A tuple to enable a certain HTTP authentication.
#                                       Default None

import requests

url = 'https://www.w3schools.com/python/demopage.php'

#use the 'auth' parameter to send requests with HTTP Basic Auth:
x = requests.head(url, auth = ('user', 'pass'))

print(x.status_code)

# cert		                            Optional. A String or Tuple specifying a cert file or key.
#                                       Default None

import requests

url = 'https://www.w3schools.com/python/demopage.htm'

#specify a cert to use as a client side certificate by setting the 'cert' parameter:
x = requests.head(url, cert='folder/myclient.cert')

print(x.status_code)

# cookies		                        Optional. A dictionary of cookies to send to the specified url.
#                                       Default None

import requests

url = 'https://www.w3schools.com/python/demopage.php'

#use the 'cookies' parameter to send cookies to the server:
x = requests.head(url, cookies = {"favcolor": "Red"})

print(x.status_code)

# headers		                        Optional. A dictionary of HTTP headers to send to the specified url.
#                                       Default None

import requests

url = 'https://www.w3schools.com/python/demopage.asp'

#use the 'headers' parameter to set the HTTP headers:
x = requests.head(url, headers = {"HTTP_HOST": "MyVeryOwnHost"})

print(x.status_code)

# proxies		                        Optional. A dictionary of the protocol to the proxy url.
#                                       Default None

import requests

url = 'https://www.w3schools.com/python/demopage.php'

#find a free proxy address and send your request via that proxy:
x = requests.head(url, proxies = { "https" : "https://1.1.0.1:80"})

print(x.status_code)

# stream		                        Optional. A Boolean indication if the response should be immediately downloaded (False) or streamed (True).
#                                       Default False

import requests

url = 'https://www.w3schools.com/images/pulpit.jpg'

#allow the response to be streamed by setting the 'stream' parameter to True:
x = requests.head(url, stream=True)

print(x.status_code)

# timeout		                        Optional. A number, or a tuple, indicating how many seconds to wait for the client to make a connection and/or send a response.
#                                       Default None which means the request will continue until the connection is closed

import requests

url = 'https://w3schools.com/python/demopage.php'

#to demonstrate the 'timeout' parameter, we set the timeout to 0.001 to guarantee that the connection will be timed out:
x = requests.head(url, timeout=0.001)

print(x.status_code)

# verify		                        Optional. A Boolean or a String indication to verify the servers TLS certificate or not.
#                                       Default True

import requests

url = 'https://www.w3schools.com/python/demopage.php'

#make the request with the path to a TLS certificate:
x = requests.head(url, verify='folder/tlscertificate')

print(x.status_code)

# Return Value
# The head() method returns a requests.Response object.


