from selenium import webdriver

driver = webdriver.Chrome(executable_path="E:\Desktop\Python\Selenium\chromedriver.exe")
driver.get("http://newtours.demoaut.com/")
# Действует на весь код
driver.implicitly_wait(10)

assert "Welcome: Mercury Tous" in driver.title

userName = driver.find_element_by_name("userName").send_keys("mercury")
password = driver.find_element_by_name("password").send_keys("mercury")
driver.find_element_by_name("login").click()