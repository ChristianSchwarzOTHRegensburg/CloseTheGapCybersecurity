import requests
import re
from bs4 import BeautifulSoup
import sys

start_url = input("Enter Website: ")
start_url = "http://" + start_url

website_list = []
website_list.append(start_url)
used_websites = []
email_list = []
#change this to the Path of your address file
adress_file = open("C:/Users/chris/AppData/Local/Programs/Python/Python37-32/Scripts/Email Harvester/adress.txt","a")

for website in website_list:
    if(website in used_websites):
        continue
    else:
        try:
            response = requests.get(website)
            converted_response = str(response.content)
            used_websites.append(website)
        except:
            used_websites.append(website) 
            continue

        soup = BeautifulSoup(converted_response, "lxml")
        for tag in soup.findAll('a', href=True):
            website_list.append(tag['href'])

        stripped_response = re.sub("[<,>,:,/,&,\",\\,},\,,;,#]", " ", converted_response)
        #more advanced regex
        emails = re.findall("[A-Za-z0-9_-]+[A-Za-z0-9]+\@[A-Za-z0-9_-]+\.[a-zA-Z]+", stripped_response)

        for email in emails:
            if(email in email_list):
                continue
            else: 
                #comment this out if you don´t want the mails on your terminal
                print(email)
                email_list.append(email)
                adress_file.write(email + "\n")
                if(len(email_list) > 5):
                    adress_file.close()
                    sys.exit()


    

        
