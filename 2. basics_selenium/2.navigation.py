from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="E:\Desktop\Python\Selenium\chromedriver.exe")

driver.get("http://newtours.demoaut.com/")
print(driver.title)

driver.get("http://www.pavantestingtools.com/")
print(driver.title)

driver.back()
print(driver.title)

driver.forward()
print(driver.title)