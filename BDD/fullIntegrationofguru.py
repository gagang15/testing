import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# #login
driver=webdriver.Chrome(executable_path="E:\\Automation project demo\\browser drive\chromedriver.exe")
driver.get("http://demo.guru99.com/v2/")
driver.find_element_by_name("uid").send_keys("mngr350488") #entering user id
driver.find_element_by_name("password").send_keys("qYdErUb") # entering Password
driver.find_element_by_name("btnLogin").click()

#New Customer
driver.find_element_by_xpath("/html/body/div[3]/div/ul/li[2]/a").click()
driver.find_element_by_name("name").send_keys("Pratik Tiwari")
driver.find_element_by_name("rad1").click()
driver.find_element_by_name("dob").send_keys("12-11-1995")
driver.find_element_by_name("addr").send_keys("Nandanvan near padav collage")
driver.find_element_by_name("city").send_keys("Nagpur")
driver.find_element_by_name("state").send_keys("Maharashtra")
driver.find_element_by_name("pinno").send_keys("440009")
driver.find_element_by_name("telephoneno").send_keys("1325560845")
driver.find_element_by_name("emailid").send_keys("tdd@gmail.com")
driver.find_element_by_name("sub").click()
obj = driver.switch_to.alert
msg=obj.text
print(msg)
time.sleep(3)
arr=msg.split(":")
obj.accept()
cutid=arr[1].lstrip()



# New Account
driver.find_element_by_xpath("/html/body/div[3]/div/ul/li[5]/a").click()
driver.find_element_by_name("cusid").send_keys(cutid)
driver.find_element_by_name("inideposit").send_keys("60000")
driver.find_element_by_name("button2").click()
obj = driver.switch_to.alert
msg=obj.text
arr=msg.split(":")
time.sleep(3)
obj.accept()
accid=arr[1].lstrip()
print(msg)

#Balance Enquiry
driver.find_element_by_xpath("/html/body/div[3]/div/ul/li[8]/a").click()
driver.find_element_by_name("accountno").send_keys(accid)
driver.find_element_by_name("AccSubmit").click()
time.sleep(5)
driver.find_element_by_xpath("/html/body/table/tbody/tr/td/table/tbody/tr[21]/td/a").click()
time.sleep(5)

#mini Satatment
driver.find_element_by_xpath("/html/body/div[3]/div/ul/li[9]/a").click()
driver.find_element_by_name("accountno").send_keys(accid)
driver.find_element_by_name("AccSubmit").click()
time.sleep(5)
driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td/table/tbody/tr[3]/td/a").click()


#customised Statement
driver.find_element_by_link_text("Customised Statement").click()
driver.find_element_by_name("accountno").send_keys(accid)
driver.find_element_by_name("fdate").send_keys("01-09-2021")
driver.find_element_by_name("tdate").send_keys("02-09-2021")
driver.find_element_by_name("numtransaction").send_keys("2")
driver.find_element_by_name("AccSubmit").click()
time.sleep(5)
driver.find_element_by_link_text("Continue").click()


#Edit Account
driver.find_element_by_link_text("Edit Account").click()
driver.find_element_by_name("accountno").send_keys(accid)
driver.find_element_by_name("AccSubmit").click()
driver.find_element_by_xpath("/html/body/table/tbody/tr/td/table/tbody/tr[11]/td[2]/select").click()
driver.find_element_by_xpath("/html/body/table/tbody/tr/td/table/tbody/tr[11]/td[2]/select/option[1]").click()
time.sleep(2)
driver.find_element_by_name("AccSubmit").click()
time.sleep(2)
obj = driver.switch_to.alert
msg=obj.text
obj.accept()


#Delete Account

driver.find_element_by_xpath("/html/body/div[3]/div/ul/li[7]/a").click()
driver.find_element_by_name("accountno").send_keys(accid)
driver.find_element_by_name("AccSubmit").click()
obj = driver.switch_to.alert
time.sleep(2)
msg=obj.text
obj.accept()

#Edit customer

driver.find_element_by_xpath("/html/body/div[3]/div/ul/li[3]/a").click()
driver.find_element_by_name("cusid").send_keys(cutid)
driver.find_element_by_name("AccSubmit").click()
driver.find_element_by_name("addr").send_keys("versova near kaweri wine shop")
driver.find_element_by_name("sub").click()
obj = driver.switch_to.alert
time.sleep(3)
msg=obj.text
obj.accept()

#delete Customer
driver.find_element_by_xpath("/html/body/div[3]/div/ul/li[4]/a").click()
driver.find_element_by_name("cusid").send_keys(cutid)
driver.find_element_by_name("AccSubmit").click()
obj = driver.switch_to.alert
time.sleep(3)
msg=obj.text
obj.accept()


driver.quit()