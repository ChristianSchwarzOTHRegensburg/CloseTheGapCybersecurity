import requests
import re
from bs4 import BeautifulSoup
import sys

start_url = input("Enter Website: ")
start_url = "http://" + start_url
domain_name = start_url.replace("http://","").replace("https://","").replace("www.","")

#user can choose betwenn examining only one site are run the programm through the entire Internet (until manuel stop!)
internal_or_external = input("Only internal Links? Y/N ").lower()
if(internal_or_external == "n"):
    #exit condition
    email_counter = int(input("Enter Number of Emails you want to collect: "))

website_list = []
website_list.append(start_url)
used_websites = set()
email_list = set()
#change this to the path of your address file
adress_file = open("C:/Users/chris/AppData/Local/Programs/Python/Python37-32/Scripts/Email Harvester/adress.txt","a")

def internal_only(str):
    if(domain_name in tag['href']):
        website_list.append(tag['href'])
        return
    else:
        return

#if the exit condition is met
def counter_reached():
    if(len(email_list) >= email_counter):
        for email in email_list:
            adress_file.write(email + "\n")
        adress_file.close()
        sys.exit()
    else:
        return

    
for website in website_list:  
    if(website in used_websites):
        continue
    else:
        try:
            response = requests.get(website)
            converted_response = str(response.content)
            used_websites.add(website)
        except:
            used_websites.add(website) 
            continue

        soup = BeautifulSoup(converted_response, "lxml")
        
        for tag in soup.findAll('a', href=True):
            if(internal_or_external == "y"):
                internal_only(tag['href'])
            else:
                website_list.append(tag['href'])

        stripped_response = re.sub("[<,>,:,/,&,\",\\,},\,,;,#]", " ", converted_response)
        emails = re.findall("[.A-Za-z0-9_-]+[A-Za-z0-9]+\@[A-Za-z0-9_-]+\.[a-zA-Z]+", stripped_response)
        email_list.update(emails)
                
        if(internal_or_external == "n"):        
            counter_reached()

for email in email_list:
    adress_file.write(email + "\n")
    
adress_file.close()
