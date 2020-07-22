import requests
import re

#change this to whatever site you want to harvest
response = requests.get("http://www.somesiteidontknowjustthinkofsomething.com")
converted_response = str(response.content)

#strip some chars from the response to break up the text
stripped_response = re.sub("[<,>,:]", " ", converted_response)

#use the regex to find all valid email addresses inside the sides content
emails = re.findall("\S+\@\S+\.\S+", stripped_response)

for i in emails:
     print(i)
        
