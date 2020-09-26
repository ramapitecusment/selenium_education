from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

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
driver.find_element(By.ID, 'RESULT_TextField-8').send_keys("MatyAla")
driver.find_element(By.ID, 'RESULT_TextField-9').send_keys("MatyAla")
driver.find_element(By.ID, 'RESULT_TextField-11').send_keys("MatyAla")

## Drop-down mwnu
driver.find_element(By.XPATH, '//*[@id="RESULT_RadioButton-7"]/option[text()="Georgia"]').click()
element = driver.find_element(By.ID, 'RESULT_RadioButton-7')
drp = Select(element)
drp.select_by_index(2)
drp.select_by_visible_text('Georgia')
drp.select_by_value("Radio-8")

## Count options
print(len(drp.options))

## Capture all the options and print
all_options = drp.options
for option in all_options:
    print(option.text)

## ACTION CHAINS
# actions = ActionChains(driver)
# actions.move_to_element(menu)
# actions.click(hidden_submenu)
# actions.perform()

## Radio Button
element_RadioButton = driver.find_element(By.ID, 'RESULT_RadioButton-10_0')
ActionChains(driver).move_to_element(element_RadioButton).click().perform()
# driver.find_element_by_xpath('//*[@id="q13"]/table/tbody/tr[1]/td/label').click()
status_choiceA = driver.find_element(By.ID, 'RESULT_RadioButton-10_0').is_selected()
print(status_choiceA)

## CheckBox
element_CheckBox = driver.find_element_by_id('RESULT_CheckBox-12_0')
ActionChains(driver).move_to_element(element_CheckBox).click().perform()
status_yes_checkBox = driver.find_element(By.ID, 'RESULT_CheckBox-12_0').is_selected()
print(status_yes_checkBox)
