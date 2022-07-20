# Python Requests get() Method

# Example
# Make a request to a web page, and return the status code:

import requests

x = requests.get('https://w3schools.com')
print(x.status_code)

# Definition and Usage
# The get() method sends a GET request to the specified url.

# Syntax
# requests.get(url, params={key: value}, args)
# args means zero or more of the named arguments in the parameter table below. Example:
# requests.get(url, timeout=2.50)

# Parameter Values
# Parameter		            Description
# url		                Required. The url of the request

import requests

#the required first parameter of the 'get' method is the 'url':
x = requests.get('https://w3schools.com/python/demopage.htm')

#print the response text (the content of the requested file):
print(x.text)

# params		            Optional. A dictionary, list of tuples or bytes to send as a query string.
#                           Default None

import requests

url = 'https://w3schools.com/python/demopage.php'

#demonstrate how to use the 'params' parameter:
x = requests.get(url, params = {"model": "Mustang"})

#print the response (the content of the requested file):
print(x.text)

#the file 'demopage.php' looks for a 'model' query string and prints its value.

# allow_redirects		    Optional. A Boolean to enable/disable redirection.
#                           Default True (allowing redirects)

import requests

#to demonstrate the 'allow_redirects' parameter we use 'http' instead of 'https', w3schools.com automatically redirects http requests to https:
url = 'http://w3schools.com/python/demopage.htm'

#first, make a request without setting the 'allow_redirects' parameter to False:
x = requests.get(url)
print(x.text)

print("----------------")

#then, make a request with the 'allow_redirects' parameter set to False:
x = requests.get(url, allow_redirects=False)
print(x.text)

# auth		                Optional. A tuple to enable a certain HTTP authentication.
#                           Default None

import requests

url = 'https://w3schools.com/python/demopage.php'

#use the 'auth' parameter to send requests with HTTP Basic Auth:
x = requests.get(url, auth = ('user', 'pass'))

print(x.status_code)


# cert		                Optional. A String or Tuple specifying a cert file or key.
#                           Default None

import requests

url = 'https://w3schools.com/python/demopage.htm'

#specify a cert to use as a client side certificate by setting the 'cert' parameter:
x = requests.get(url, cert='folder/myclient.cert')

print(x.status_code)

# cookies		            Optional. A dictionary of cookies to send to the specified url.
#                           Default None

import requests

url = 'https://w3schools.com/python/demopage2.php'

#use the 'cookies' parameter to send cookies to the server:
x = requests.get(url, cookies = {"favcolor": "Red"})

print(x.text)

#the 'demopage2.php' prints the value of the 'favcolor' cookie.

# headers		            Optional. A dictionary of HTTP headers to send to the specified url.
#                           Default None

import requests

url = 'https://w3schools.com/python/demopage.asp'

#use the 'headers' parameter to set the HTTP headers:
x = requests.get(url, headers = {"HTTP_HOST": "MyVeryOwnHost"})

print(x.text)

#the 'demopage.asp' prints all HTTP Headers

# proxies		            Optional. A dictionary of the protocol to the proxy url.
#                           Default None

import requests

url = 'https://w3schools.com/python/demopage.php'

#find a free proxy address and send your request via that proxy:
x = requests.get(url, proxies = { "https" : "https://1.1.0.1:80"})

#'demopage.php' will print the ip address of the proxy instead of your ip:
print(x.text)

# stream		            Optional. A Boolean indication if the response should be immediately downloaded (False) or streamed (True).
#                           Default False

import requests

url = 'https://w3schools.com/images/pulpit.jpg'

#allow the response to be streamed by setting the 'stream' parameter to True:
x = requests.get(url, stream=True)

print(x.status_code)

# timeout		            Optional. A number, or a tuple, indicating how many seconds to wait for the client to make a connection and/or send a response.
#                           Default None which means the request will continue until the connection is closed

import requests

url = 'https://w3schools.com/python/demopage.php'

#to demonstrate the 'timeout' parameter, we set the timeout to 0.001 to guarantee that the connection will be timed out:
x = requests.get(url, timeout=0.001)

print(x.text)

# verify	                Optional. A Boolean or a String indication to verify the servers TLS certificate or not.
#                           Default True

import requests

url = 'https://w3schools.com/python/demopage.php'

#make the request with the path to a TLS certificate:
x = requests.get(url, verify='folder/tlscertificate')

print(x.status_code)

import requests

url = 'https://w3schools.com/python/demopage.php'

#make the request and specify that there will be no verifying:
x = requests.get(url, verify=False)

print(x.status_code)

# Return Value
# The get() method returns a requests.Response object.


