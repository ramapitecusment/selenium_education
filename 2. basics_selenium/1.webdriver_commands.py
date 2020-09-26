from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="E:\Desktop\Python\Selenium\chromedriver.exe")
driver.get("http://demo.automationtesting.in/Windows.html")

title = driver.title
url = driver.current_url

print(title)
print(url)

driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()

time.sleep(5)

#closes currently focussed url
#driver.close()

driver.quit()