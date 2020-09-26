# Working with Selenium

Selenium requires a driver to interface with the chosen browser. Firefox, for example, requires 
geckodriver, which needs to be installed before the below examples can be run. Make sure it’s in 
your PATH.

To build Selenium Python from the source code, clone the official repository. It contains the source 
code for all official Selenium flavors, like Python, Java, Ruby and others. The Python code resides 
in the /py directory.

If you have installed Selenium Python bindings, you can start using it from Python like this.
```
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

//The instance of Firefox WebDriver is created.
driver = webdriver.Firefox()

driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()
```