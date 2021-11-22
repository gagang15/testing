import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome(executable_path="E:\\Automation project demo\\browser drive\chromedriver.exe")


#TC_to_check_correct_username_and_password
driver.get("http://demo.guru99.com/v2/")
driver.find_element_by_name("uid").send_keys("mngr346462") #entering user id
driver.find_element_by_name("password").send_keys("hahamyz") # entering Password
driver.find_element_by_name("btnLogin").click()
#driver.find_element_by_xpath("/html/body/div[3]/div/ul/li[2]/a").click()
time.sleep(2)
########################################################################################################
#TC_to_check_incorrect_username_and_incorrect_password
driver.get("http://demo.guru99.com/v2/")
driver.find_element_by_name("uid").send_keys("mngr") #entering user id
driver.find_element_by_name("password").send_keys("rEz") # entering Password
driver.find_element_by_name("btnLogin").click()
time.sleep(2)

########################################################################################################
#TC_to_check_incorrect_username_and_Correct_password
driver.get("http://demo.guru99.com/v2/")
driver.find_element_by_name("uid").send_keys("mngr") #entering user id
driver.find_element_by_name("password").send_keys("hahamyz") # entering Password
driver.find_element_by_name("btnLogin").click()

time.sleep(2)

########################################################################################################
#TC_to_check_correct_username_and_incorrect_password
driver.get("http://demo.guru99.com/v2/")
driver.find_element_by_name("uid").send_keys("mngr341681") #entering user id
driver.find_element_by_name("password").send_keys("rEz") # entering Password
driver.find_element_by_name("btnLogin").click()

time.sleep(2)

########################################################################################################
#TC_to_check_blank_username_and_password
driver.get("http://demo.guru99.com/v2/")
driver.find_element_by_name("uid").send_keys("") #entering user id
driver.find_element_by_name("password").send_keys("") # entering Password
driver.find_element_by_name("btnLogin").click()

time.sleep(2)

########################################################################################################
#TC_to_check_blank_username_and_filled_password
driver.get("http://demo.guru99.com/v2/")
driver.find_element_by_name("uid").send_keys("") #entering user id
driver.find_element_by_name("password").send_keys("rEzdsd") # entering Password
driver.find_element_by_name("btnLogin").click()

time.sleep(2)

########################################################################################################
#TC_to_check_filled_username_and_blank_password
driver.get("http://demo.guru99.com/v2/")
driver.find_element_by_name("uid").send_keys("mngr341681") #entering user id
driver.find_element_by_name("password").send_keys("rEz") # entering Password
driver.find_element_by_name("btnLogin").click()
time.sleep(2)

########################################################################################################
#TC_to_check_reset_button
driver.get("http://demo.guru99.com/v2/")
driver.find_element_by_name("uid").send_keys("mngr341681") #entering user id
driver.find_element_by_name("password").send_keys("rEz") # entering Password
driver.find_element_by_name("btnReset").click()
time.sleep(2)

########################################################################################################
#TC_to_check_reset_button
driver.get("http://demo.guru99.com/v2/")
driver.find_element_by_name("uid").send_keys("mngr346462") #entering user id
driver.find_element_by_name("password").send_keys("hahamyz") # entering Password
driver.close()
driver=webdriver.Chrome(executable_path="E:\\Automation project demo\\browser drive\chromedriver.exe")
driver.get("http://demo.guru99.com/v2/")


#####################################################################################################
def fnlogin(userName, passWord):
    driver = webdriver.Chrome(executable_path="E:\\Automation project demo\\browser drive\chromedriver.exe")
    driver.get("http://demo.guru99.com/v2/")
    if driver.find_element_by_name("uid").is_displayed():
        if driver.find_element_by_name("uid").is_enabled():
            driver.find_element_by_name("uid").send_keys(userName)  # entering user id
        else:
            print("user name is disabled")
            return
    else:

        print("user name is not displyed ")
        return
    driver.find_element_by_name("password").send_keys(passWord)  # entering Password
    driver.find_element_by_name("btnLogin").click()
    # driver.find_element_by_xpath("/html/body/div[3]/div/ul/li[2]/a").click()
    error = "Welcome To Manager's Page of Guru99 Bank"
    if (driver.find_element_by_xpath('/html/body/table/tbody/tr/td/table/tbody/tr[2]/td/marquee').text) == error:
        print("login successfull")
    else:
        print("login failed")


fnlogin("mngr346462", "hahamyz")