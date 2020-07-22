import tldextract
from difflib import SequenceMatcher
import pyfiglet
from time import sleep
import whois #pip install python-whois, windows: install whois in system32

domain = input("Enter your Domain: ")
domain = tldextract.extract(domain)
#Output of extract: tupel with subdomain, domain and suffix, access via .Operator
domain_raw = domain.domain
tld = domain.suffix

created_domains = set() 
similar_tlds = set()
available_domains = set() 
registered_domains = set()
unregistered_domains = set()

def create_tlds():
    #change to Path of your Domain_Extensions File
    domain_list = open("C:/Users/chris/AppData/Local/Programs/Python/Python37-32/Scripts/Domain Phisher/Domain_Extensions.txt", "r")
    #List of domain Extensions from: https://data.iana.org/TLD/tlds-alpha-by-domain.txt
    for domain in domain_list:
        new_domain = domain.lower()
        s = SequenceMatcher(None, tld, new_domain)
        similarity = s.ratio()
        #For Testing: 0.6 as Similarity Level, change according to your needs or make it editable by the User
        if similarity > 0.6:
            similar_tlds.add(new_domain)

def replace_char():
    if "o" in domain_raw:
        replaced_o = domain_raw.replace("o", "0")
        created_domains.add(replaced_o)  
    if "l" in domain_raw:
        replaced_l = domain_raw.replace("l", "1")
        created_domains.add(replaced_l)  
    if "d" in domain_raw:
        replaced_d = domain_raw.replace("d", "cl")
        created_domains.add(replaced_d)
    return

def double_char():
    chars_to_double = ["o", "l", "e" ]
    for char in chars_to_double:
        doubled_char = char + char
        if char in domain_raw:
            domain_doubled = domain_raw.replace(char, doubled_char, 1)
            created_domains.add(domain_doubled)
        else:
            pass
    return

#append Functions could be refactored to one function
#less code, better to read
#but with several functions the User has more controll over the Outpu
    
def append_it():
    it_list = ["it", "servicedesk", "helpdesk", "support", "admin"]
    for word in it_list:
        created_domains.add(word+domain_raw)
        created_domains.add(word+"-"+domain_raw)
        created_domains.add(domain_raw+word)
        created_domains.add(domain_raw+"-"+word)
    return

def append_customer():
    customer_list = ["customer", "customerservice", "help", "info", "client", "consumer"]
    for word in customer_list:
        created_domains.add(word+domain_raw)
        created_domains.add(word+"-"+domain_raw)
        created_domains.add(domain_raw+word)
        created_domains.add(domain_raw+"-"+word)
    return

def append_billing():
    billing_list = ["bill", "billing", "invoice", "account", "check", "note", "report"]
    for word in billing_list:
        created_domains.add(word+domain_raw)
        created_domains.add(word+"-"+domain_raw)
        created_domains.add(domain_raw+word)
        created_domains.add(domain_raw+"-"+word)
    return

def append_numbers():
    #1 and 11 are personal choices, 24 is often used as part of domains (e.g. scout24.de, immoscout24.de)
    #247 indicates that Website is reachable 24 hours, 7 days a week
    #365 indicates that Website is reachable 365 days a year
    number_list = ["1","11","24","247","365"]
    for word in number_list:
        created_domains.add(word+domain_raw)
        created_domains.add(word+"-"+domain_raw)
        created_domains.add(domain_raw+word)
        created_domains.add(domain_raw+"-"+word)
    return

def append_fake_tld():
    fake_tld_list = ["com", "org", "net", "info", "gov", "io", "us"]
    for word in fake_tld_list:
        created_domains.add(domain_raw+"-"+word)
    #append tld inside domain (www.google-com.net, serious domains only)
    #with - because . in domain not allowed
    return

def append_userinput():
    print("Enter the words you want to add to the domain")
    print("Press enter after each word")
    print("Press e to exit")
    words = set()
    user_input = 0
    
    while 1:
        user_input = input().lower()
        if user_input == "e":
            break
        else:
            words.add(user_input)
        
    for word in words:
        created_domains.add(word+domain_raw)
        created_domains.add(word+"-"+domain_raw)
        created_domains.add(domain_raw+word)
        created_domains.add(domain_raw+"-"+word)        
    return

def add_tld():
    for tld in similar_tlds:
        for domain in created_domains:
            domain = domain + "." +tld
            available_domains.add(domain)
    return
              
def print_info_screen():
    print(pyfiglet.figlet_format("Domain Phisher"))
    print("Welcome to Domain Phisher \n")
    print("Run program with one or more of the following arguments: \n")
    print("==> c to generate customer Domains...")
    print("E.g. customerservice-"+domain_raw+".tld \n")
    print("==> i to generate IT Domains...")
    print("E.g. "+domain_raw+"-support.tld \n")
    print("==> b to generate Billing Domains...")
    print("E.g. invoice"+domain_raw+".tld \n")
    print("==> n to generate Number Domains...")
    print("E.g. "+domain_raw+"24.tld \n")
    print("==> f to genrate fake TLDs...")
    print("E.g. "+domain_raw+"-com.tld \n")
    print("==> d to double chars of the Domain...")
    print("E.g. doomain.tld \n")
    print("==> r to replace chars of the Domain...")
    print("E.g. d0main.tld \n")
    print("==> u for your own userinput...")
    print("E.g. append domains with custom words relevant to your industy \n")
    return input("Enter your choice here: ").lower()

def whois_lookup():
    for domain in available_domains:
        try:
            availability_check = whois.whois(domain)
            if availability_check.domain_name == None: #not "null" or NULL
                print("Domain: ", domain, "is unregistered")
                unregistered_domains.add(domain)
            else:
                print("Domain: ", domain, "is registered, see Information below")
                print(availability_check)
                registered_domains.add(domain)
        except (whois.parser.PywhoisError, socket.gaierror) as e:
            print("Unable to process Domain: ", domain)  
        sleep(0.5)
        #wait half a second, so the server doesn´t get to many requests
    return

def print_result_screen():
    print("-----RESULT-----")
    print("Generated",len(created_domains),"unique Domains")
    print("Found", len(similar_tlds), "similar TLDs")
    print("This means", len(similar_tlds)*len(created_domains), "possible Domains for Phishers")
    print(len(unregistered_domains), "of them are not registered")
    print(len(registered_domains), "of them are registered")
    return

selected_preferences = print_info_screen()

if "c" in selected_preferences:
    append_customer()
if "i" in selected_preferences:
    append_it()
if "b" in selected_preferences:
    append_billing()
if "n" in selected_preferences:
    append_numbers()
if "f" in selected_preferences:
    append_fake_tld()
if "d" in selected_preferences:
    double_char()
if "r" in selected_preferences:
    replace_char()
if "u" in selected_preferences:
    append_userinput()

create_tlds()
add_tld()

for i in available_domains:
    print(i)

whois_lookup()
print_result_screen()
