from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="E:\Desktop\Python\Selenium\chromedriver.exe")
driver.get("http://newtours.demoaut.com/")

userName = driver.find_element_by_name("userName")
print(userName.is_displayed())
print(userName.is_enabled())
print(userName.is_selected())

password = driver.find_element_by_name("password")
print(password.is_displayed())
print(password.is_enabled())
print(password.is_selected())

userName.send_keys("mercury")
password.send_keys("mercury")
driver.find_element_by_name("login").click()

# CSS Selector
roundtrip = driver.find_element_by_css_selector("input[value='roundtrip']")
print(roundtrip.is_selected())
