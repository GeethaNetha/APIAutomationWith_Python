import json

import jsonpath
import requests

#/**
#*
#* @author JALA Academy
#*
#*
#*
#*
#*/

#api url
SignInurl=' http://trainingapi.jalaacademy.com/api/signin'
#here we are requesting to new response by using post
response=requests.post(SignInurl)
print(response)
#here we are reading the content in the newly created file
file=open("C:\\Users\\geeth\\PycharmProjects\\APIAutomationwithpython\\Createuser.json",'r')
#here we are reading the file
json_input=file.read()
#here we are loading the content what we are created in the file by using json.loads
requests_json=json.loads(json_input)
#here we are printing the content
print(requests_json)
response=requests.post(SignInurl,requests_json)
#printing the text what we are given
print(response.content)
#validating response code
assert response.status_code==404
#fetch Headers from the request
print(response.headers.get('Content-Length'))

UserUrl='http://trainingapi.jalaacademy.com/api/users'
userResponse=requests.post(UserUrl)
print(userResponse)
print(userResponse.text)