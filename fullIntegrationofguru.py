import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver=webdriver.Chrome(executable_path="E:\\Automation project demo\\browser drive\chromedriver.exe")
driver.get("http://demo.guru99.com/v2/")
driver.find_element_by_name("uid").send_keys("mngr350488") #entering user id
driver.find_element_by_name("password").send_keys("qYdErUb") # entering Password