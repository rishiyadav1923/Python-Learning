# Python Requests post() Method

# Example
# Make a POST request to a web page, and return the response text:

import requests

url = 'https://www.w3schools.com/python/demopage.php'
myobj = {'somekey': 'somevalue'}

x = requests.post(url, json = myobj)

print(x.text)

# Definition and Usage
# The post() method sends a POST request to the specified url.
# The post() method is used when you want to send some data to the server.

# Syntax
# requests.post(url, data={key: value}, json={key: value}, args)
# args means zero or more of the named arguments in the parameter table below. Example:
# requests.post(url, data = myobj, timeout=2.50)

# Parameter Values
# Parameter		                        Description
# url		                            Required. The url of the request

import requests

url = 'https://www.w3schools.com/python/demopage.php'

x = requests.post(url)

#print the response text (the content of the requested file):

print(x.text)

# data		                            Optional. A dictionary, list of tuples, bytes or a file object to send to the specified url

import requests

url = 'https://www.w3schools.com/python/demopage.php'
myobj = {'somekey': 'somevalue'}

x = requests.post(url, json = myobj)

#print the response text (the content of the requested file):

print(x.text)

# json		                            Optional. A JSON object to send to the specified url

import requests

url = 'https://www.w3schools.com/python/demopage.php'
myjson = {'somekey': 'somevalue'}

x = requests.post(url, json = myjson)

#print the response text (the content of the requested file):

print(x.text)

# files		                            Optional. A dictionary of files to send to the specified url

import requests

url = 'https://www.w3schools.com/python/demopage.php'
myfiles = {'file': open('myfirstreact.png' ,'rb')}

x = requests.post(url, files = myfiles)

#print the response text (the content of the requested file):

print(x.text)

# allow_redirects		                Optional. A Boolean to enable/disable redirection.
#                                       Default True (allowing redirects)

import requests

#to demonstrate the 'allow_redirects' parameter we use 'http' instead of 'https', w3schools.com automatically redirects http requests to https:
url = 'http://w3schools.com/python/demopage.htm'
myobj = {'somekey': 'somevalue'}

#first, make a request without setting the 'allow_redirects' parameter to False:
x = requests.post(url, data = myobj)
print(x.text)

print("----------------")

#then, make a request with the 'allow_redirects' parameter set to False:
x = requests.post(url, data = myobj, allow_redirects=False)
print(x.text)

# auth		                            Optional. A tuple to enable a certain HTTP authentication.
#                                       Default None

import requests

url = 'https://w3schools.com/python/demopage.php'
myobj = {'somekey': 'somevalue'}

#use the 'auth' parameter to send requests with HTTP Basic Auth:
x = requests.post(url, data = myobj, auth = ('user', 'pass'))

print(x.status_code)


# cert		                            Optional. A String or Tuple specifying a cert file or key.
#                                       Default None

import requests

url = 'https://w3schools.com/python/demopage.php'
myobj = {'somekey': 'somevalue'}

#specify a cert to use as a client side certificate by setting the 'cert' parameter:
x = requests.post(url, data = myobj, cert='folder/myclient.cert')

print(x.status_code)

# cookies		                        Optional. A dictionary of cookies to send to the specified url.
#                                       Default None

import requests

url = 'https://w3schools.com/python/demopage2.php'
myobj = {'somekey': 'somevalue'}

#use the 'cookies' parameter to send cookies to the server:
x = requests.post(url, data = myobj, cookies = {"favcolor": "Red"})

print(x.text)

#the 'demopage2.php' prints the value of the 'favcolor' cookie.


# headers		                        Optional. A dictionary of HTTP headers to send to the specified url.
#                                       Default None

import requests

url = 'https://w3schools.com/python/demopage.asp'
myobj = {'somekey': 'somevalue'}

#use the 'headers' parameter to set the HTTP headers:
x = requests.post(url, data = myobj, headers = {"HTTP_HOST": "MyVeryOwnHost"})

print(x.text)

#the 'demopage.asp' prints all HTTP Headers


# proxies		                        Optional. A dictionary of the protocol to the proxy url.
#                                       Default None

import requests

url = 'https://w3schools.com/python/demopage.php'
myobj = {'somekey': 'somevalue'}

#find a free proxy address and send your request via that proxy:
x = requests.post(url, data = myobj, proxies = { "https" : "https://1.1.0.1:80"})

#'demopage.php' will print the ip address of the proxy instead of your ip:
print(x.text)

# stream		                        Optional. A Boolean indication if the response should be immediately downloaded (False) or streamed (True).
#                                       Default False

import requests

url = 'https://w3schools.com/python/demopage.php'
myobj = {'somekey': 'somevalue'}

#allow the response to be streamed by setting the 'stream' parameter to True:
x = requests.post(url, data = myobj, stream=True)

print(x.status_code)

# timeout		                        Optional. A number, or a tuple, indicating how many seconds to wait for the client to make a connection and/or send a response.
#                                       Default None which means the request will continue until the connection is closed

import requests

url = 'https://w3schools.com/python/demopage.php'
myobj = {'somekey': 'somevalue'}

#to demonstrate the 'timeout' parameter, we set the timeout to 0.001 to guarantee that the connection will be timed out:
x = requests.post(url, data = myobj, timeout=0.001)

print(x.text)

# verify	                            Optional. A Boolean or a String indication to verify the servers TLS certificate or not.
#                                       Default True

import requests

url = 'https://w3schools.com/python/demopage.php'
myobj = {'somekey': 'somevalue'}

#make the request with the path to a TLS certificate:
x = requests.post(url, data = myobj, verify='folder/tlscertificate')

print(x.status_code)

import requests

url = 'https://w3schools.com/python/demopage.php'
myobj = {'somekey': 'somevalue'}

#make the request and specify that there will be no verifying:
x = requests.post(url, data = myobj, verify=False)

print(x.status_code)

# Return Value
# A requests.Response object.


