import requests
import re
from bs4 import BeautifulSoup

start_url = input("Enter Website: ")
start_url = "http://" + start_url

website_list = []
website_list.append(start_url)
used_websites = []
email_list = []


for website in website_list:

    if(website in used_websites):
        continue
    else:
        #use a try/catch block in case this fails
        try:
            response = requests.get(website)
            converted_response = str(response.content)
            used_websites.append(website)
        except:
            #if it fails save the website in used_websites and continue
            used_websites.append(website) 
            continue

        #search for links on the site and add them to our list of Websites
        soup = BeautifulSoup(converted_response, "lxml")
        for tag in soup.findAll('a', href=True):
            website_list.append(tag['href'])

        
        #could also be done with bs4 html parser
        stripped_response = re.sub("[<,>,:]", " ", converted_response)
        emails = re.findall("\S+\@\S+\.\S+", stripped_response)

        for email in emails:
            if(email in email_list):
                #if we allready know the email, do nothing
                continue
            elif(len(email) < 30):
                #to large email addresses where often mismatches during tests, quick and dirty way to sort them out is to check for length
                print(email)
                email_list.append(email)
