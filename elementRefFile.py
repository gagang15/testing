import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys #importing drivers for Chrome and web browser
from selenium.webdriver.support.ui import Select #importing select for dropwdown elements
#assign chrome driver to driver varible throgh chrome driver path
driver=webdriver.Chrome(executable_path="E:\\Automation project demo\\browser drive\chromedriver.exe")

#############################################################################################################
#for opeing any sites

driver.get("http://demo.guru99.com/v2/")

#############################################################################################################
#To Maximize Any window

driver.maximize_window()

#############################################################################################################
#to Click on any button or element
# We can do this opration by id or by name or by xpath

driver.find_element_by_id('id of that element').click()

#############################################################################################################
#to pass value to any element / " we can directly pass the value to the dropdown

driver.find_element_by_name("Name of that tag").send_keys("value which we want psss")

#############################################################################################################

#Switch the control to the Alert window
obj = driver.switch_to.alert

#Retrieve the message on the Alert window
msg=obj.text
print ("Alert shows following message: "+ msg )

#use the accept() method to accept the alert
obj.accept()

##use the dismiss() method to cancel  accept the alert
obj.dismiss()

##################################################################################################################

#for Ui and li multiple item selection code
# We have to import following WebElement
from selenium.webdriver.remote.webelement import WebElement

#now we have to select parent tag for whole value which ui(unordered list)

html_list=driver.find_element_by_xpath('//*[@id="basicBootstrapForm"]/div[7]/div/multi-select/div[2]/ul')

#now we have whole data in html_list so we have to convert it into list through li tag
items=html_list.find_elements_by_tag_name("li")

#we have whole list in items and now we have to compair and select li item

for item in items:
    if(item.text=="list item" or item.text=="list item" ):
        item.click()

########################################################################################
#for Ui and li multiple item selection code with search bar
#selecting item in drop down of list item with search bar
#click on that field
driver.find_element_by_xpath('//*[@id="basicBootstrapForm"]/div[10]/div/span/span[1]/span/span[2]').click()
#send the search value the search bar element
driver.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys("India")

#now coolect parent element "ui " data in varible
countryList=driver.find_element_by_xpath('//*[@id="select2-country-results"]')
#now get the single item from list to click and then click it
countryList.click()

##########################################################################################################
#we can directly send values to Select tag dropdown by send keys using x path
driver.find_element_by_xpath('//*[@id="yearbox"]').send_keys("value")

#we can also print whole select drop down item by Select for that we have to import Select
from selenium.webdriver.support.ui import Select

#now we can transfer whole select list in single varibale to itrrate
listofYear=Select(driver.find_element_by_xpath('//*[@id="yearbox"]'))

#now we can directly print every item using for and option
for i in (listofYear.options):
    print(i.text)

#another way of writing for loop for same case

for i in range(len(listofYear.options)):
    print(listofYear.options[i].text)

###########################################################
#suppose there are more than 2 tabs, to switch between 2 tabs use following code
#to swicth to second tab
driver.switch_to.window(driver.window_handles[1])
#to swtich to 3rd tab
driver.switch_to.window(driver.window_handles[2])
#to swicth to fisrt tab
driver.switch_to.window(driver.window_handles[0])

#to close perticuler tab use close() but dont forget to switch driver to another tab
driver.close()
######################################################################################
#code for disabled date picker
driver.get("http://demo.automationtesting.in/Datepicker.html")
driver.find_element_by_xpath('//*[@id="datepicker1"]').click()

while driver.find_element_by_class_name('ui-datepicker-title').text != "February 1991":
    driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/div/a[1]/span').click()

date=driver.find_elements_by_class_name('ui-state-default')
for i in date:
    if(i.text=="15"):
        i.click()
        break

#####################################################################################
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