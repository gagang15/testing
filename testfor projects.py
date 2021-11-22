import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome(executable_path="E:\\Automation project demo\\browser drive\chromedriver.exe")
def fnNewCustomer(**newcustomer):
    try:
        driver.get("http://demo.guru99.com/v2/")
        if driver.find_element_by_name("uid").is_displayed():
            if driver.find_element_by_name("uid").is_enabled():
                driver.find_element_by_name("uid").send_keys(newcustomer["userName"])  # entering user id
            else:
                print("user name is disabled")
                return
        else:

            print("user name is not displyed ")
            return
        if driver.find_element_by_name("password").is_displayed():
            if driver.find_element_by_name("password").is_enabled():
                driver.find_element_by_name("password").send_keys(newcustomer['password'])  # entering user id
            else:
                print("Password  is disabled")
                return
        else:

            print("Password is not displyed ")
            return
        driver.find_element_by_name("btnLogin").click()
    except:
        print("Login failed")



    try:
        driver.find_element_by_xpath("/html/body/div[3]/div/ul/li[2]/a").click()
        if driver.find_element_by_name("name").is_displayed():
            if driver.find_element_by_name("name").is_enabled():
                driver.find_element_by_name("name").send_keys(newcustomer["name"])  # entering user id
            else:
                print(" name is disabled")
                return
        else:

            print(" name is not displyed ")
            return

        driver.find_element_by_name("rad1").click()
        if driver.find_element_by_name("dob").is_displayed():
            if driver.find_element_by_name("dob").is_enabled():
                driver.find_element_by_name("dob").send_keys(newcustomer["dob"])  # entering user id
            else:
                print(" dob is disabled")
                return
        else:

            print(" dob is not displyed ")
            return
        if driver.find_element_by_name("addr").is_displayed():
            if driver.find_element_by_name("addr").is_enabled():
                driver.find_element_by_name("addr").send_keys(newcustomer["addres"])  # entering user id
            else:
                print(" addres is disabled")
                return
        else:

            print(" addres is not displyed ")
            return
        if driver.find_element_by_name("city").is_displayed():
            if driver.find_element_by_name("city").is_enabled():
                driver.find_element_by_name("city").send_keys(newcustomer["city"])  # entering user id
            else:
                print(" city is disabled")
                return
        else:

            print(" city is not displyed ")
            return
        if driver.find_element_by_name("state").is_displayed():
            if driver.find_element_by_name("state").is_enabled():
                driver.find_element_by_name("state").send_keys(newcustomer["state"])  # entering user id
            else:
                print(" state is disabled")
                return
        else:

            print(" state is not displyed ")
            return
        if driver.find_element_by_name("pinno").is_displayed():
            if driver.find_element_by_name("pinno").is_enabled():
                driver.find_element_by_name("pinno").send_keys(newcustomer["pin"])  # entering user id
            else:
                print(" pin is disabled")
                return
        else:

            print(" pin is not displyed ")
            return
        if driver.find_element_by_name("telephoneno").is_displayed():
            if driver.find_element_by_name("telephoneno").is_enabled():
                driver.find_element_by_name("telephoneno").send_keys(newcustomer["mobileNo"])  # entering user id
            else:
                print(" pin is disabled")
                return
        else:

            print(" pin is not displyed ")
            return
        if driver.find_element_by_name("emailid").is_displayed():
            if driver.find_element_by_name("emailid").is_enabled():
                driver.find_element_by_name("emailid").send_keys(newcustomer["email"])  # entering user id
            else:
                print(" email is disabled")
                return
        else:

            print(" email is not displyed ")
            return

        driver.find_element_by_name("sub").click()
        obj = driver.switch_to.alert
        msg = obj.text

    except:
        print("New Customer error")






newcustomer={
    "userName":"mngr354103",
    "password":"anErYgU",
    "name":"Pratik Tiwari",
    "dob":"12-11-1995",
    "addres":"Nandanvan near padav collage",
    "city":"nagpur",
    "state":"Maharashtra",
    "pin":"440009",
    "mobileNo":"7502311121",
    "email":"prtik@gmail.com"
}
fnNewCustomer(**newcustomer)