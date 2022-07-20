# Python Requests delete() Method

# Example
# Make a DELETE request to a web page, and return the response text:

import requests

x = requests.delete('https://w3schools.com/python/demopage.php')

print(x.text)

# Definition and Usage
# The delete() method sends a DELETE request to the specified url.
# DELETE requests are made for deleting the specified resource (file, record etc).

# Syntax
# requests.delete(url, args)
# args means zero or more of the named arguments in the parameter table below. Example:
# requests.delete(url, timeout=2.50)

# Parameter Values
# Parameter		        Description
# url		            Required. The url of the request

import requests

#the required first parameter of the 'delete' method is the 'url':
x = requests.delete('https://w3schools.com/python/demopage.php')

#print the response text (the content of the requested file):
print(x.text)

# allow_redirects		Optional. A Boolean to enable/disable redirection.
#                       Default True (allowing redirects)

import requests

url = 'https://w3schools.com/python/demopage.php'

#Sometimes the server redirects a request, could be if the file does not exist etc., set the 'allow_redirects' parameter to False to deny redirects:

x = requests.delete(url, allow_redirects=False)

#print the response text (the content of the requested file):
print(x.text)

# auth		            Optional. A tuple to enable a certain HTTP authentication.
#                       Default None

import requests

url = 'https://w3schools.com/python/demopage.php'

#use the 'auth' parameter to send requests with HTTP Basic Auth:
x = requests.delete(url, auth = ('user', 'pass'))

print(x.status_code)

# cert		            Optional. A String or Tuple specifying a cert file or key.
#                       Default None

import requests

url = 'https://w3schools.com/python/demopage.htm'

#specify a cert to use as a client side certificate by setting the 'cert' parameter:
x = requests.delete(url, cert='folder/myclient.cert')

print(x.status_code)

# cookies		        Optional. A dictionary of cookies to send to the specified url.
#                       Default None

import requests

url = 'https://w3schools.com/python/demopage2.php'

#use the 'cookies' parameter to send cookies to the server:
x = requests.delete(url, cookies = {"favcolor": "Red"})

print(x.status_code)

# headers		        Optional. A dictionary of HTTP headers to send to the specified url.
#                       Default None

import requests

url = 'https://w3schools.com/python/demopage.asp'

#use the 'headers' parameter to set the HTTP headers:
x = requests.delete(url, headers = {"HTTP_HOST": "MyVeryOwnHost"})

print(x.status_code)

# proxies		        Optional. A dictionary of the protocol to the proxy url.
#                       Default None

import requests

url = 'https://w3schools.com/python/demopage.php'

#find a free proxy address and send your request via that proxy:
x = requests.delete(url, proxies = { "https" : "https://1.1.0.1:80"})

print(x.status_code)

# stream		        Optional. A Boolean indication if the response should be immediately downloaded (False) or streamed (True).
#                       Default False


import requests

url = 'https://w3schools.com/images/pulpit.jpg'

#allow the response to be streamed by setting the 'stream' parameter to True:
x = requests.delete(url, stream=True)

print(x.status_code)

# timeout		        Optional. A number, or a tuple, indicating how many seconds to wait for the client to make a connection and/or send a response.
#                       Default None which means the request will continue until the connection is closed

import requests

url = 'https://w3schools.com/python/demopage.php'

#to demonstrate the 'timeout' parameter, we set the timeout to 0.001 to guarantee that the connection will be timed out:
x = requests.delete(url, timeout=0.001)

print(x.text)

# verify	            Optional. A Boolean or a String indication to verify the servers TLS certificate or not.
#                       Default True

import requests

url = 'https://w3schools.com/python/demopage.php'

#make the request with the path to a TLS certificate:
x = requests.delete(url, verify='folder/tlscertificate')

print(x.status_code)

import requests

url = 'https://w3schools.com/python/demopage.php'

#make the request and specify that there will be no verifying:
x = requests.delete(url, verify=False)

print(x.status_code)

# Return Value
# The delete() method returns a requests.Response object.


