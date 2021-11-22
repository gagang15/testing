import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#TC_to_check_correct_Data
driver=webdriver.Chrome(executable_path="E:\\Automation project demo\\browser drive\chromedriver.exe")
driver.get("http://demo.guru99.com/v2/")
driver.find_element_by_name("uid").send_keys("mngr346462") #entering user id
driver.find_element_by_name("password").send_keys("hahamyz") # entering Password
driver.find_element_by_name("btnLogin").click()
driver.find_element_by_xpath("/html/body/div[3]/div/ul/li[5]/a").click()
driver.find_element_by_name("cusid").send_keys("35102")
driver.find_element_by_name("inideposit").send_keys("60000")
driver.find_element_by_name("button2").click()
time.sleep(5)
driver.close()

#######################################################################
#TC_to_check_incorrect_customer_ID
driver=webdriver.Chrome(executable_path="E:\\Automation project demo\\browser drive\chromedriver.exe")
driver.get("http://demo.guru99.com/v2/")
driver.find_element_by_name("uid").send_keys("mngr346462") #entering user id
driver.find_element_by_name("password").send_keys("hahamyz") # entering Password
driver.find_element_by_name("btnLogin").click()
driver.find_element_by_xpath("/html/body/div[3]/div/ul/li[5]/a").click()
driver.find_element_by_name("cusid").send_keys("12345")
driver.find_element_by_name("inideposit").send_keys("60000")
driver.find_element_by_name("button2").click()
time.sleep(5)
driver.close()

#######################################################################
#TC_to_check_submit_button_with_Blank_field
driver=webdriver.Chrome(executable_path="E:\\Automation project demo\\browser drive\chromedriver.exe")
driver.get("http://demo.guru99.com/v2/")
driver.find_element_by_name("uid").send_keys("mngr346462") #entering user id
driver.find_element_by_name("password").send_keys("hahamyz") # entering Password
driver.find_element_by_name("btnLogin").click()
driver.find_element_by_xpath("/html/body/div[3]/div/ul/li[5]/a").click()
driver.find_element_by_name("cusid").send_keys("")
driver.find_element_by_name("inideposit").send_keys("60000")
driver.find_element_by_name("button2").click()
time.sleep(5)
driver.close()

######################################################################
#TC_to_check_reset_button
driver=webdriver.Chrome(executable_path="E:\\Automation project demo\\browser drive\chromedriver.exe")
driver.get("http://demo.guru99.com/v2/")
driver.find_element_by_name("uid").send_keys("mngr346462") #entering user id
driver.find_element_by_name("password").send_keys("hahamyz") # entering Password
driver.find_element_by_name("btnLogin").click()
driver.find_element_by_xpath("/html/body/div[3]/div/ul/li[5]/a").click()
driver.find_element_by_name("cusid").send_keys("12345")
driver.find_element_by_name("inideposit").send_keys("60000")
driver.find_element_by_name("reset").click()
time.sleep(5)
driver.close()


######################################################################
#TC_to_check_reset_button
driver=webdriver.Chrome(executable_path="E:\\Automation project demo\\browser drive\chromedriver.exe")
driver.get("http://demo.guru99.com/v2/")
driver.find_element_by_name("uid").send_keys("mngr346462") #entering user id
driver.find_element_by_name("password").send_keys("hahamyz") # entering Password
driver.find_element_by_name("btnLogin").click()
driver.find_element_by_xpath("/html/body/div[3]/div/ul/li[5]/a").click()
driver.find_element_by_name("cusid").send_keys("12345")
driver.find_element_by_name("inideposit").send_keys("60000")
time.sleep(3)
driver.close()
driver=webdriver.Chrome(executable_path="E:\\Automation project demo\\browser drive\chromedriver.exe")
driver.get("http://demo.guru99.com/v2/")
driver.find_element_by_name("uid").send_keys("mngr346462") #entering user id
driver.find_element_by_name("password").send_keys("hahamyz") # entering Password
driver.find_element_by_name("btnLogin").click()
driver.find_element_by_xpath("/html/body/div[3]/div/ul/li[5]/a").click()
#####################################################################3
#function to Add new Account
def fnNewAccount(Usrnm, pswd, cusid, inidop):
    river = webdriver.Chrome(executable_path="E:\\Automation project demo\\browser drive\chromedriver.exe")
    driver.get("http://demo.guru99.com/v2/")
    driver.find_element_by_name("uid").send_keys(Usrnm)  # entering user id
    driver.find_element_by_name("password").send_keys(pswd)  # entering Password
    driver.find_element_by_name("btnLogin").click()
    driver.find_element_by_xpath("/html/body/div[3]/div/ul/li[5]/a").click()
    driver.find_element_by_name("cusid").send_keys(cusid)
    driver.find_element_by_name("inideposit").send_keys(inidop)
    driver.find_element_by_name("button2").click()
    time.sleep(5)


fnNewAccount("mngr346462", "hahamyz", "35102", "60000")