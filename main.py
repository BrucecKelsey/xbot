from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time 

usernameInfo = "Markubased"
passwordInfo = "MMas2269"

options = webdriver.ChromeOptions()

driver = webdriver.Chrome(options=options)

driver.get("https://www.x.com/")

SignIn = driver.find_element(By.XPATH, "//span[contains(@class, 'css-1jxf684') and text()='Sign in']").click()

time.sleep(5)

username = driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input')
username.send_keys(usernameInfo)

usernameClick = driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]/div/span/span').click()

time.sleep(5)

password = driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
password.send_keys(passwordInfo)
password.send_keys(Keys.RETURN)

time.sleep(10000)

driver.quit()