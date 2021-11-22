# import pytest
# import unittest
# from selenium import webdriver
#
# def testfnlogin():
#     userName='mngr34646'
#     passWord='hahamyz'
#     driver = webdriver.Chrome(executable_path="E:\\Automation project demo\\browser drive\\chromedriver.exe")
#     driver.get("http://demo.guru99.com/v2/")
#     assert driver.find_element_by_name("uid").is_displayed()==True ,"userid filed is not visible "
#     assert driver.find_element_by_name("uid").is_enabled(),"userid filed is not enable "
#     driver.find_element_by_name("uid").send_keys(userName)  # entering user id
#     driver.find_element_by_name("password").send_keys(passWord)  # entering Password
#     driver.find_element_by_name("btnLogin").click()
#     # driver.find_element_by_xpath("/html/body/div[3]/div/ul/li[2]/a").click()
#     error = "Welcome To Manager's Page of Guru99 Bank"
#     msg=driver.find_element_by_xpath('/html/body/table/tbody/tr/td/table/tbody/tr[2]/td/marquee').text
#     print(msg)
#     unittest.TestCase.assertNotEqual(msg, error,"Login failed")
#
# def testfuncton1():
#     x=1
#     y=6
#     assert x==y,"test failed"
a=[1,2,3,4,5,6]
print(a[-1:-3])
