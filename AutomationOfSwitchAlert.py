import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.remote.webelement import WebElement
driver=webdriver.Chrome(executable_path="E:\\Automation project demo\\browser drive\chromedriver.exe")
driver.get("http://demo.automationtesting.in/Alerts.html")
driver.maximize_window()

driver.find_element_by_xpath('//*[@id="OKTab"]/button').click()



#Switch the control to the Alert window
obj = driver.switch_to.alert

#Retrieve the message on the Alert window
msg=obj.text
print ("Alert shows following message: "+ msg )
time.sleep(2)
#use the accept() method to accept the alert
obj.accept()

driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/ul/li[2]/a').click()
driver.find_element_by_xpath('//*[@id="CancelTab"]/button').click()
time.sleep(3)
obj.dismiss()

driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/ul/li[3]/a').click()
driver.find_element_by_id("Textbox").click()
obj.send_keys("gagan")
time.sleep(2)
obj.accept()
print(driver.find_element_by_id('demo1').text)