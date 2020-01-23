from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome("C:/Users/User/PycharmProjects/untitled2/venv/Scripts/chromedriver.exe")
driver.get('https://github.com/login')
driver.find_element_by_id('login_field').send_keys("Mariam-hub")
driver.find_element_by_id('password').send_keys('mariam2001hub')
driver.find_element_by_name('commit').click()
time.sleep(5)
driver.quit()
