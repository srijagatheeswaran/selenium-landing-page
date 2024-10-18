from selenium import webdriver
from selenium.webdriver.common.by import By
import time  

driver = webdriver.Chrome()

# Open the landing page
driver.get("https://ck.hdm3.in/lp.php?sid=085aaaf6&txnid={uniqueid}")

name_field = driver.find_element("name", "lead_data[name]") 
name_field.send_keys("John Doe")
name_field = driver.find_element("name", "lead_data[email]") 
name_field.send_keys("JohnDoe@gmail.com")
name_field = driver.find_element("name", "lead_data[contact_no]") 
name_field.send_keys("1234567890")

submit_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-dark.btn-lg.mt-2.shadow-lg")
submit_button.click()


# time.sleep(30) 

