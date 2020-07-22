import tldextract
from difflib import SequenceMatcher

domain = input("Enter your Domain: ")
domain = tldextract.extract(domain)
#Output of extract: tupel with subdomain, domain and suffix, access via .Operator
domain_raw = domain.domain
tld = domain.suffix

created_domains = set() 
#save all created domains here

similar_tlds = set()
available_domains = set()

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
#but with several functions the User has more controll over the Output
    
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
    print("Press e to exit")
    words = []
    user_input = 0
    
    while 1:
        user_input = input()
        if user_input == "e":
            break
        else:
            words.append(user_input)
        
    for word in words:
        created_domains.add(word+domain_raw)
        created_domains.add(word+"-"+domain_raw)
        created_domains.add(domain_raw+word)
        created_domains.add(domain_raw+"-"+word)        
    return


def add_original_tld():
    for domain in created_domains:
        domain = domain + "." + tld
        available_domains.add(domain)
    return

def add_other_tlds():
    for tld in similar_tlds:
        for domain in created_domains:
            domain = domain + "." +tld
            available_domains.add(domain)
    return

      
def print_info_screen():
    print("Welcome to Domain Phisher")
    print("Run program with one or more of the following arguments: ")
    print("Enter c to generate customer Domains...")
    print("E.g. customerservice-domain.tld")
    print("Enter i to generate IT Domains...")
    print("E.g. domain-support.tld")
    print("Enter b to generate Billing Domains...")
    print("E.g. invoice-domain.tld")
    print("Enter n to generate Number Domains...")
    print("E.g. domain24.tld")
    print("Enter f to genrate fake TLDs...")
    print("E.g. domain-com.tld")
    print("Enter d to double chars of the Domain...")
    print("E.g. doomain.tld")
    print("Enter r to replace chars of the Domain...")
    print("E.g. d0main.tld")
    print("Enter u for your own userinput...")
    print("E.g. append domains with custom words relevant to your industy")
    return input("Enter your choice here: ").lower()


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

print("A total of",len(created_domains), "new Domains was created") 

print("Checking similar TLDs...")
create_tlds()
print("Appending TLDs to Domains...")
add_original_tld()
add_other_tlds()


for i in available_domains:
    print(i)
print(len(available_domains))

#ascii art: https://www.devdungeon.com/content/create-ascii-art-text-banners-python 
