from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="E:\Desktop\Python\Selenium\chromedriver.exe")

driver.get("http://newtours.demoaut.com/")

title = driver.title
print(title)

driver.close()