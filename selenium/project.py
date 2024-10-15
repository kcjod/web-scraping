from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

file = 1
query = "laptops"
files_limit = 100

for i in range(1,11):
    if file<=files_limit:
        driver.get(f"https://www.amazon.in/s?k={query}&page={i}")
        elems = driver.find_elements(By.CLASS_NAME, "puis-card-container")
        for elem in elems:
            data = elem.get_attribute("outerHTML")
            with open(f"data/{query}-{file}.html","w",encoding="utf-8") as f:
                f.write(data)
            file+=1

            if file>files_limit:
                break
    else:
        break

driver.close()