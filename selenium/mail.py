from selenium import webdriver
import time
import json

# Set the path to your Chrome WebDriver
driver_path = 'path/to/chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)

# Open Gmail login page
driver.get("https://www.gmail.com")

# Find and fill in the email field
email_input = driver.find_element_by_name("identifier")
email_input.send_keys("chandrabadkul26@gmail.com")

# Click the Next button
next_button = driver.find_element_by_xpath("//*[@id='identifierNext']/div/button/span")
next_button.click()

# Wait for the password input field to load
time.sleep(5)  # Wait a few seconds for the password input field to load (You might need to increase this time if necessary)

# Find and fill in the password field
password_input = driver.find_element_by_name("password")
password_input.send_keys("Chandra123")

# Click the Next button for password submission
password_next_button = driver.find_element_by_xpath("//*[@id='passwordNext']/div/button/span")
password_next_button.click()

# Wait for the inbox to load (You might need to adjust this wait time based on network speed)
time.sleep(10)

# Find and click the mail button to go to the inbox
mail_button = driver.find_element_by_xpath("//div[@class='T-I J-J5-Ji T-I-KE L3']")
mail_button.click()

# Wait for the inbox to load again
time.sleep(5)

# Get top ten emails
emails = driver.find_elements_by_xpath("//div[@class='y6']/span")
top_ten_emails = [email.text for email in emails[:10]]

# Convert emails to JSON format
emails_json = json.dumps(top_ten_emails)

# Print or use the JSON data as needed
print(emails_json)

# Close the browser
driver.quit()
