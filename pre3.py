import time
import os
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

#キャプチャ保存ファイル生成
filename = os.path.join(os.path.dirname(os.path.abspath(__file__)),"image/screen.png")

driver = webdriver.Chrome()
driver.get("https://www.selenium.dev/selenium/web/web-form.html")
title = driver.title
driver.implicitly_wait(5)

time.sleep(3)

#要素を選択?
text_box = driver.find_element(by=By.NAME, value="my-text")
my_pass = driver.find_element(By.NAME,value="my-password")
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

#アクション実行
#RPAと関連付けて学ぶ
text_box.send_keys("Selenium")
my_pass.send_keys("TEST_test")
time.sleep(3)
submit_button.click()

#直前に要素の宣言?をしないとうまく動かない
message = driver.find_element(by=By.ID, value="message")
text = message.text

#キャプチャ取得ページの高さと幅を取得
#w = driver.execute_script("return document.Body.scrollWidth;")
#h = driver.execute_script("return document.Body.scrollHight;")

#キャプチャのサイズをセット
#driver.set_window_size(w,h)

#キャプチャ取得
driver.save_screenshot(filename)

time.sleep(3)

print(text)
print(title)

driver.quit()
