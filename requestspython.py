#!/usr/bin/python
import requests

#r = requests.get('https://github.com/timeline.json')
#r = requests.get('https://www.google.com.mx/?gws_rd=ssl')
r = requests.get('https://www.youtube.com/')
#r = requests.post("http://httpbin.org/post")

#r = requests.put("http://httpbin.org/put")

#print (r.url)

print (r.text)