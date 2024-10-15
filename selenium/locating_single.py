from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.amazon.in/s?k=laptops")

elem = driver.find_element(By.CLASS_NAME, "a-size-mini")
print(elem.text)

driver.close()