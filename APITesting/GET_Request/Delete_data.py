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

ValidUrl="http://trainingapi.jalaacademy.com/api/users/247"
response=requests.delete(ValidUrl)
#fetch response code
print(response)
assert response.status_code==500

#invalid url
InvalidUrl='http://trainingapi.jalaacademy.com/api/users/49'
Url_response=requests.delete(InvalidUrl)
print(Url_response)

