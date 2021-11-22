import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


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
    obj = driver.switch_to.alert
    if obj =='':

        if (driver.find_element_by_xpath('/html/body/table/tbody/tr/td/table/tbody/tr[2]/td/marquee').text) == error:
            print("login successfull")
    else:
        print("login failed")


fnlogin("mngr346462", "hahamyz")