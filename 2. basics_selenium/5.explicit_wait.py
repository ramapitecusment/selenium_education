from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome(executable_path="E:\Desktop\Python\Selenium\chromedriver.exe")
driver.implicitly_wait(5)

driver.maximize_window()
driver.get("https://www.expedia.com/")

# driver.find_element_by_id("tab-flight-tab-hp").click()
driver.find_element(By.ID, "tab-flight-tab-hp").click()

# driver.find_element_by_xpath("//label[@id=wizard-flight-pwa]/span").click()

time.sleep(2)
driver.find_element(By.ID, "flight-origin-hp-flight").send_keys("ALA")
driver.find_element(By.ID, "flight-destination-hp-flight").send_keys("TSE")
driver.find_element(By.ID, "flight-departing-hp-flight").clear()
driver.find_element(By.ID, "flight-departing-hp-flight").send_keys("05/26/2020")
time.sleep(2)
driver.find_element(By.ID, "flight-returning-hp-flight").clear()
driver.find_element(By.ID, "flight-returning-hp-flight").send_keys(Keys.CONTROL, "a")
driver.find_element(By.ID, "flight-returning-hp-flight").send_keys("06/06/2020")
driver.find_element_by_xpath("//*[@id='gcw-flights-form-hp-flight']/div[8]/label/button").click()

# Explicit wait
wait = WebDriverWait(driver, 10)

element = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='stopFilter_stops-0']")))
element.click()
time.sleep(3)

