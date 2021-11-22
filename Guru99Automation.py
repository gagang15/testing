import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver=webdriver.Chrome(executable_path="E:\\Automation project demo\\browser drive\chromedriver.exe")
driver.get("http://demo.guru99.com/v2/")
driver.find_element_by_name("uid").send_keys("mngr346462") #entering user id
driver.find_element_by_name("password").send_keys("hahamyz") # entering Password
driver.find_element_by_name("btnLogin").click()
driver.find_element_by_xpath("/html/body/div[3]/div/ul/li[3]/a").click()
driver.find_element_by_name("cusid").send_keys("12334")
time.sleep(5)
driver.find_element_by_name("res").click()
time.sleep(5)
assertE
driver.close()