import tldextract

domain = input("Enter your Domain: ")
domain = tldextract.extract(domain)
#Output of extract: tupel with subdomain, domain and suffix, access via .Operator
domain_raw = domain.domain
tld = domain.suffix
original_domain = domain_raw + tld

tld_list = set() 

#save all created domains here
created_domains = set() 

def create_tlds():
    #change to Path of your Domain_Extensions File
    domain_list = open("C:/Users/chris/AppData/Local/Programs/Python/Python37-32/Scripts/Domain Phisher/Domain_Extensions.txt", "r")
    #List of domain Extensions from: https://data.iana.org/TLD/tlds-alpha-by-domain.txt
    tld_counter = 0
    for i in domain_list:
        possible_domain = domain_raw + "." + i.lower()
        #domains in File are Uppercase, therefore lower()
        print(possible_domain)
        tld_list.add(possible_domain)
        tld_counter += 1
    print(tld_counter, "new Domains")
    #To do: next Versions: only add Domains that are similiar to the Input Domain

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
    #To do: User can enter his own transformations
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
        

append_customer()
append_it()
append_customer()
append_billing()
append_numbers()
append_fake_tld()
double_char()
replace_char()

append_userinput()
#first create variations, then add TLDs


print(created_domains)
print(len(created_domains))

#NEXT VERSIONS
#-Check Availability --> V3
#-whois + refactor + User Input --> V4
