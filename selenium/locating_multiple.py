from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.amazon.in/s?k=laptops")

elems = driver.find_elements(By.CLASS_NAME, "a-size-mini")
print(f"{len(elems)} elements found.")

for elem in elems:
    print(elem.text)

driver.close()