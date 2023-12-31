import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()

# Login first
driver.get("http://localhost:8080")

# Enter staff id
staff_id = driver.find_element(By.ID, "staffId")
staff_id.clear()
staff_id.send_keys(140002)

# Enter password
password = driver.find_element(By.ID, "password")
password.clear()
password.send_keys("susan")

# Click login button
driver.find_element(By.ID, "login").click()

# Go to role listing page
text = driver.find_element(By.ID, "role_listings").click()

# Wait for 3 seconds (for the page to load)
time.sleep(3)

# Open the first modal 
element = driver.find_element(By.ID, "role_listing_card").click()

# Wait for 3 seconds (for the page to load)
time.sleep(3)

driver.find_element(By.ID, "apply_role").click()
time.sleep(1)

text = driver.find_element(By.ID, "apply_success_alert").text

print(text)

assert "You have successfully applied for the role" in text

print("TEST PASSED : Apply Role")

print("Application title ", driver.title)
print("Application url is ", driver.current_url)
driver.quit()