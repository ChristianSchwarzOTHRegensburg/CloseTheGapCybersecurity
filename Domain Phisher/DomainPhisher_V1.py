import tldextract

domain = input("Enter your Domain: ")
domain = tldextract.extract(domain)
#Output of extract: tupel with subdomain, domain and suffix, access via .Operator

domain_raw = domain.domain
tld = domain.suffix

print(domain_raw)
print(tld)

