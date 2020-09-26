from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="E:\Desktop\Python\Selenium\chromedriver.exe")
driver.get("https://fs11.formsite.com/ZiepuM/bb3ik5fiep/index.html?1591040394939")

## How many inputboxes

input_boxes = driver.find_elements(By.CLASS_NAME, 'text_field')
print(len(input_boxes))

## Provide value to the inputbox

driver.find_element(By.ID, 'RESULT_TextField-2').send_keys("Padavan")
driver.find_element(By.ID, 'RESULT_TextField-3').send_keys("Yuniy")
driver.find_element(By.ID, 'RESULT_TextField-4').send_keys("Ala")
driver.find_element(By.ID, 'RESULT_TextField-5').send_keys("Maty")
driver.find_element(By.ID, 'RESULT_TextField-6').send_keys("MatyAla")