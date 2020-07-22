#change this to the Path of your address file
emails = open("C:/Users/chris/AppData/Local/Programs/Python/Python37-32/Scripts/Email Harvester/adress.txt", 'r').readlines()

emails_set = set(emails)

#change this to the Path of your address file
out = open("C:/Users/chris/AppData/Local/Programs/Python/Python37-32/Scripts/Email Harvester/adress.txt", 'w')

for email in emails_set:
    out.write(email)

out.close()
