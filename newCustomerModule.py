import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome(executable_path="E:\\Automation project demo\\browser drive\chromedriver.exe")


#TC_to_check_correct_data_entered
driver.get("http://demo.guru99.com/v2/")
try:
    driver.find_element_by_name("uid").send_keys("mngr346462") #entering user id
    driver.find_element_by_name("password").send_keys("hahamyz") # entering Password
    driver.find_element_by_name("btnLogin").click()
    driver.find_element_by_xpath("/html/body/div[3]/div/ul/li[2]/a").click()
    driver.find_element_by_name("name").send_keys("Pratik Tiwari")
    driver.find_element_by_name("rad1").click()
    driver.find_element_by_name("dob").send_keys("12-11-1995")
    driver.find_element_by_name("addr").send_keys("Nandanvan near padav collage")
    driver.find_element_by_name("city").send_keys("Nagpur")
    driver.find_element_by_name("state").send_keys("Maharashtra")
    driver.find_element_by_name("pinno").send_keys("440009")
    driver.find_element_by_name("telephoneno").send_keys("7506311121")
    driver.find_element_by_name("emailid").send_keys("pratik@gmail.com")
    driver.find_element_by_name("sub").click()
    time.sleep(3)
except:
    print("Email Address Already Exist ")
finally:
    driver.close()

#######################################################
#TC_to_Check_only_Requied_filed
driver=webdriver.Chrome(executable_path="E:\\Automation project demo\\browser drive\chromedriver.exe")
driver.get("http://demo.guru99.com/v2/")
driver.find_element_by_name("uid").send_keys("mngr346462") #entering user id
driver.find_element_by_name("password").send_keys("hahamyz") # entering Password
driver.find_element_by_name("btnLogin").click()
driver.find_element_by_xpath("/html/body/div[3]/div/ul/li[2]/a").click()
driver.find_element_by_name("name").send_keys("Pratik Tiwari")
driver.find_element_by_name("rad1").click()
driver.find_element_by_name("dob").send_keys("12-11-1995")
driver.find_element_by_name("addr").send_keys("Nandanvan near padav collage")
driver.find_element_by_name("city").send_keys("Nagpur")
driver.find_element_by_name("state").send_keys("Maharashtra")
driver.find_element_by_name("pinno").send_keys("440009")
driver.find_element_by_name("telephoneno").send_keys("")
driver.find_element_by_name("emailid").send_keys("pratik@123gmail.com")
driver.find_element_by_name("sub").click()
time.sleep(3)
driver.close()

#######################################################
#TC_to_Check_only_Non_required_filed
driver=webdriver.Chrome(executable_path="E:\\Automation project demo\\browser drive\chromedriver.exe")
driver.get("http://demo.guru99.com/v2/")
driver.find_element_by_name("uid").send_keys("mngr346462") #entering user id
driver.find_element_by_name("password").send_keys("hahamyz") # entering Password
driver.find_element_by_name("btnLogin").click()
driver.find_element_by_xpath("/html/body/div[3]/div/ul/li[2]/a").click()
driver.find_element_by_name("name").send_keys("")
driver.find_element_by_name("rad1").click()
driver.find_element_by_name("dob").send_keys("")
driver.find_element_by_name("addr").send_keys("")
driver.find_element_by_name("city").send_keys("")
driver.find_element_by_name("state").send_keys("")
driver.find_element_by_name("pinno").send_keys("")
driver.find_element_by_name("telephoneno").send_keys("9028422595")
driver.find_element_by_name("emailid").send_keys("")
driver.find_element_by_name("sub").click()
time.sleep(3)
driver.close()

###############################################################
#TC_to_check_blank_field
driver=webdriver.Chrome(executable_path="E:\\Automation project demo\\browser drive\chromedriver.exe")
driver.get("http://demo.guru99.com/v2/")
driver.find_element_by_name("uid").send_keys("mngr346462") #entering user id
driver.find_element_by_name("password").send_keys("hahamyz") # entering Password
driver.find_element_by_name("btnLogin").click()
driver.find_element_by_xpath("/html/body/div[3]/div/ul/li[2]/a").click()
driver.find_element_by_name("name").send_keys("")
driver.find_element_by_name("rad1").click()
driver.find_element_by_name("dob").send_keys("")
driver.find_element_by_name("addr").send_keys("")
driver.find_element_by_name("city").send_keys("")
driver.find_element_by_name("state").send_keys("")
driver.find_element_by_name("pinno").send_keys("")
driver.find_element_by_name("telephoneno").send_keys("")
driver.find_element_by_name("emailid").send_keys("")
driver.find_element_by_name("sub").click()
time.sleep(3)
driver.close()

###############################################################
#TC_to_check_reset_button
driver=webdriver.Chrome(executable_path="E:\\Automation project demo\\browser drive\chromedriver.exe")
driver.get("http://demo.guru99.com/v2/")
driver.find_element_by_name("uid").send_keys("mngr346462") #entering user id
driver.find_element_by_name("password").send_keys("hahamyz") # entering Password
driver.find_element_by_name("btnLogin").click()
driver.find_element_by_xpath("/html/body/div[3]/div/ul/li[2]/a").click()
driver.find_element_by_name("name").send_keys("Pratik Tiwari")
driver.find_element_by_name("rad1").click()
driver.find_element_by_name("dob").send_keys("12-11-1995")
driver.find_element_by_name("addr").send_keys("Nandanvan near padav collage")
driver.find_element_by_name("city").send_keys("Nagpur")
driver.find_element_by_name("state").send_keys("Maharashtra")
driver.find_element_by_name("pinno").send_keys("440009")
driver.find_element_by_name("telephoneno").send_keys("7506311121")
driver.find_element_by_name("emailid").send_keys("pratik@gmail.com")
driver.find_element_by_name("res").click()
time.sleep(3)
driver.close()


###############################################################
#TC_to_check_fileds_for_closing_windows
driver.get("http://demo.guru99.com/v2/")
driver.find_element_by_name("uid").send_keys("mngr346462") #entering user id
driver.find_element_by_name("password").send_keys("hahamyz") # entering Password
driver.find_element_by_name("btnLogin").click()
driver.find_element_by_xpath("/html/body/div[3]/div/ul/li[2]/a").click()
driver.find_element_by_name("name").send_keys("Pratik Tiwari")
driver.find_element_by_name("rad1").click()
driver.find_element_by_name("dob").send_keys("12-11-1995")
driver.find_element_by_name("addr").send_keys("Nandanvan near padav collage")
driver.find_element_by_name("city").send_keys("Nagpur")
driver.find_element_by_name("state").send_keys("Maharashtra")
driver.find_element_by_name("pinno").send_keys("440009")
driver.find_element_by_name("telephoneno").send_keys("7506311121")
driver.find_element_by_name("emailid").send_keys("pratik@gmail.com")
driver.close()
driver=webdriver.Chrome(executable_path="E:\\Automation project demo\\browser drive\chromedriver.exe")
driver.get("http://demo.guru99.com/v2/")
driver.find_element_by_name("uid").send_keys("mngr346462") #entering user id
driver.find_element_by_name("password").send_keys("hahamyz") # entering Password
driver.find_element_by_name("btnLogin").click()
driver.find_element_by_xpath("/html/body/div[3]/div/ul/li[2]/a").click()

#####################################################################################
#function to Add new Customer
def fnNewCustomer(usrnm,pswd,name,dob,addr,city,stat,pin,telno,email):
    driver.get("http://demo.guru99.com/v2/")
    driver.find_element_by_name("uid").send_keys(usrnm) #entering user id
    driver.find_element_by_name("password").send_keys(pswd) # entering Password
    driver.find_element_by_name("btnLogin").click()
    driver.find_element_by_xpath("/html/body/div[3]/div/ul/li[2]/a").click()
    driver.find_element_by_name("name").send_keys(name)
    driver.find_element_by_name("rad1").click()
    driver.find_element_by_name("dob").send_keys(dob)
    driver.find_element_by_name("addr").send_keys(addr)
    driver.find_element_by_name("city").send_keys(city)
    driver.find_element_by_name("state").send_keys(stat)
    driver.find_element_by_name("pinno").send_keys(pin)
    driver.find_element_by_name("telephoneno").send_keys(telno)
    driver.find_element_by_name("emailid").send_keys(email)
    driver.find_element_by_name("sub").click()
    driver.close()
fnNewCustomer("mngr346462","hahamyz","Pratik Tiwari","12-11-1995","Nandanvan near padav collage","Nagpur","Maharashtra","440009",
              "7506311121","pratik@gmail.com")
###################################################################################################################
#by passing dictonry
def fnNewCustomer(**newcustomer):
    driver.get("http://demo.guru99.com/v2/")
    driver.find_element_by_name("uid").send_keys(newcustomer["userName"]) #entering user id
    driver.find_element_by_name("password").send_keys(newcustomer['password']) # entering Password
    driver.find_element_by_name("btnLogin").click()
    driver.find_element_by_xpath("/html/body/div[3]/div/ul/li[2]/a").click()
    driver.find_element_by_name("name").send_keys(newcustomer['name'])
    driver.find_element_by_name("rad1").click()
    driver.find_element_by_name("dob").send_keys(newcustomer['dob'])
    driver.find_element_by_name("addr").send_keys(newcustomer['addres'])
    driver.find_element_by_name("city").send_keys(newcustomer['city'])
    driver.find_element_by_name("state").send_keys(newcustomer['state'])
    driver.find_element_by_name("pinno").send_keys(newcustomer['pin'])
    driver.find_element_by_name("telephoneno").send_keys(newcustomer['mobileNo'])
    driver.find_element_by_name("emailid").send_keys(newcustomer['email'])
    driver.find_element_by_name("sub").click()



newcustomer={
    "userName":"mngr346462",
    "password":"hahamyz",
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

######################################################
#conditional
def fnNewCustomer(**newcustomer):
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



newcustomer={
    "userName":"mngr346462",
    "password":"hahamyz",
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