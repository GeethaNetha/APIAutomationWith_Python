import requests
import json
import jsonpath

#/**
#*
#* @author JALA Academy
#*
#*
#*
#*
#*/

#API URL
url=' http://trainingapi.jalaacademy.com/api/users?search=&page=1'
#send get request
response=requests.get(url)
#if we have to know the response content what we arev getting by the .text command
print(response)
assert response.status_code==500
#print(response.text)
#print(response.text)
#print(response.content)
print(response.content)
#print(response.headers)
print(response.headers)

InValidUrl='http://trainingapi.jalaacademy.com/api/users?search=&page='
Url_response=requests.get(url)
#if we have to know the response content what we arev getting by the .text command
print(Url_response)
assert Url_response.status_code==500
#print(response.text)
#print(response.text)
#print(response.content)
print(Url_response.content)
#print(response.headers)
print(Url_response.headers)
