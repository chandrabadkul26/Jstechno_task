import time
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver_path = "C:\\Users\\Chandra\\OneDrive\\Desktop\\selenium_testing\\chromedriver-win64\\chromedriver"
driver = webdriver.Chrome(executable_path=driver_path) 

driver.get('https://mail.google.com')

email_field = driver.find_element_by_id('identifierId')
email_field.send_keys('chandrabadkul26@gmail.com')  


email_field.send_keys(Keys.RETURN)
time.sleep(2)  

password_field = driver.find_element_by_name('password')
password_field.send_keys('your_password')  
password_field.send_keys(Keys.RETURN)
time.sleep(5)  

driver.get('https://mail.google.com/mail/u/0/#inbox')
time.sleep(5) 

emails = driver.find_elements_by_css_selector('.zA[role="listitem"]')[:10]

email_data = []
for email in emails:
    sender = email.find_element_by_css_selector('.yW').text
    subject = email.find_element_by_css_selector('.bog').text
    email_data.append({'Sender': sender, 'Subject': subject})

json_data = json.dumps(email_data, indent=2)

print(json_data)

