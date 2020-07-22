from selenium import webdriver

driver = webdriver.Chrome(executable_path = r"D:\Downloads\chromedriver_win32\chromedriver.exe")
driver.get('http://[yourfancydomainname]wp-login')

user_input = driver.find_element_by_id("user_login")
user_input.send_keys('admin')

password_input = driver.find_element_by_id('user_pass')
password_input.send_keys('admin')

login_button = driver.find_element_by_id('wp-submit')
login_button.click()

