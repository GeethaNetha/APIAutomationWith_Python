import json

import requests
import jsonpath

#/**
#*
#* @author JALA Academy
#*
#*
#*
#*
#*/

#we take valid url to check
ValidUrl=' http://trainingapi.jalaacademy.com/api/users/247'
#here we are reading the content in the newly created file
file=open("C:\\Users\\geeth\\PycharmProjects\\APIAutomationwithpython\\Createuser.json",'r')
#here we are reading the file
json_input=file.read()
#here we are loading the content what we are created in the file by using json.loads
requests_json=json.loads(json_input)
#here we are printing the content
print(requests_json)
response=requests.put(ValidUrl,requests_json)

print(response)
print(response.content)
print(response.headers)
assert  response.status_code==500


#we take invalid url to check
InvalidUrl='http://trainingapi.jalaacademy.com/api/users/55'
Second_response=requests.put(InvalidUrl)
print(Second_response)
print(Second_response.content)
print(Second_response.headers)
assert  Second_response.status_code==500
