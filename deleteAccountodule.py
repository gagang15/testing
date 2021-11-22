import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#TC_to_check_submit_button_with_Correct_Account_number
driver=webdriver.Chrome(executable_path="E:\\Automation project demo\\browser drive\chromedriver.exe")
driver.get("http://demo.guru99.com/v2/")
driver.find_element_by_name("uid").send_keys("mngr346462") #entering user id
driver.find_element_by_name("password").send_keys("hahamyz") # entering Password
driver.find_element_by_name("btnLogin").click()
driver.find_element_by_xpath("/html/body/div[3]/div/ul/li[7]/a").click()
driver.find_element_by_name("accountno").send_keys("35102")
driver.find_element_by_name("AccSubmit").click()
time.sleep(5)
driver.close()

##################################################################
#TC_to_check_submit_button_with_incorrect_Account_number
driver=webdriver.Chrome(executable_path="E:\\Automation project demo\\browser drive\chromedriver.exe")
driver.get("http://demo.guru99.com/v2/")
driver.find_element_by_name("uid").send_keys("mngr346462") #entering user id
driver.find_element_by_name("password").send_keys("hahamyz") # entering Password
driver.find_element_by_name("btnLogin").click()
driver.find_element_by_xpath("/html/body/div[3]/div/ul/li[7]/a").click()
driver.find_element_by_name("accountno").send_keys("35102")
driver.find_element_by_name("AccSubmit").click()
time.sleep(5)
driver.close()

##################################################################
#TC_to_check_submit_button_with_Blank_Customer_ID
driver=webdriver.Chrome(executable_path="E:\\Automation project demo\\browser drive\chromedriver.exe")
driver.get("http://demo.guru99.com/v2/")
driver.find_element_by_name("uid").send_keys("mngr346462") #entering user id
driver.find_element_by_name("password").send_keys("hahamyz") # entering Password
driver.find_element_by_name("btnLogin").click()
driver.find_element_by_xpath("/html/body/div[3]/div/ul/li[7]/a").click()
driver.find_element_by_name("accountno").send_keys("")
driver.find_element_by_name("AccSubmit").click()
time.sleep(5)
driver.close()

##################################################################
#TC_to_check_reset
driver=webdriver.Chrome(executable_path="E:\\Automation project demo\\browser drive\chromedriver.exe")
driver.get("http://demo.guru99.com/v2/")
driver.find_element_by_name("uid").send_keys("mngr346462") #entering user id
driver.find_element_by_name("password").send_keys("hahamyz") # entering Password
driver.find_element_by_name("btnLogin").click()
driver.find_element_by_xpath("/html/body/div[3]/div/ul/li[7]/a").click()
driver.find_element_by_name("accountno").send_keys("35102")
driver.find_element_by_name("res").click()
time.sleep(5)
driver.close()
##################################################################
#TC_to_check_reset
driver=webdriver.Chrome(executable_path="E:\\Automation project demo\\browser drive\chromedriver.exe")
driver.get("http://demo.guru99.com/v2/")
driver.find_element_by_name("uid").send_keys("mngr346462") #entering user id
driver.find_element_by_name("password").send_keys("hahamyz") # entering Password
driver.find_element_by_name("btnLogin").click()
driver.find_element_by_xpath("/html/body/div[3]/div/ul/li[7]/a").click()
driver.find_element_by_name("accountno").send_keys("35102")
time.sleep(5)
driver.close()
driver=webdriver.Chrome(executable_path="E:\\Automation project demo\\browser drive\chromedriver.exe")
driver.get("http://demo.guru99.com/v2/")
driver.find_element_by_name("uid").send_keys("mngr346462") #entering user id
driver.find_element_by_name("password").send_keys("hahamyz") # entering Password
driver.find_element_by_name("btnLogin").click()
driver.find_element_by_xpath("/html/body/div[3]/div/ul/li[7]/a").click()