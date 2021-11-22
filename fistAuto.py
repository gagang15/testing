import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome(executable_path="E:\\Automation project demo\\browser drive\chromedriver.exe")
driver.get("https://www.google.com/") # to go perticuler URL
driver.get("https://www.facebook.com/")
driver.back() #to backword
time.sleep(5)
driver.forward()
time.sleep(5)
print(driver.title) #to show title of the page
print(driver.current_url) #to show the current URL
print(driver.page_source) # will show the page source
driver.close()
