import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.selenium.dev/selenium/web/web-form.html")

title = driver.title

driver.implicitly_wait(3)
time.sleep(5)

text_box = driver.find_element(by=By.NAME, value="my-text")
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

text_box.send_keys("Selenium")
time.sleep(5)
submit_button.click()

time.sleep(5)

message = driver.find_element(by=By.ID, value="message")
text = message.text

time.sleep(5)


driver.quit()