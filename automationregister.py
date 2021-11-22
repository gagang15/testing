import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.remote.webelement import WebElement
driver=webdriver.Chrome(executable_path="E:\\Automation project demo\\browser drive\chromedriver.exe")
driver.get("http://demo.automationtesting.in/Register.html")
driver.maximize_window()

driver.find_element_by_id("imagesrc").send_keys("D:\signature.JPG")

driver.find_element_by_xpath('//*[@id="basicBootstrapForm"]/div[1]/div[1]/input').send_keys("Ashutosh")
driver.find_element_by_xpath('//*[@id="basicBootstrapForm"]/div[1]/div[2]/input').send_keys("Warade")
driver.find_element_by_xpath('//*[@id="basicBootstrapForm"]/div[2]/div/textarea').send_keys("Bhande plot")
driver.find_element_by_xpath('//*[@id="eid"]/input').send_keys("Ashutosh@gmail.com")
driver.find_element_by_xpath('//*[@id="basicBootstrapForm"]/div[4]/div/input').send_keys("9028422566")
driver.find_element_by_xpath('//*[@id="basicBootstrapForm"]/div[5]/div/label[2]/input').click()
driver.find_element_by_id('checkbox1').click()
driver.find_element_by_id('checkbox2').click()
driver.find_element_by_id('checkbox3').click()


driver.find_element_by_id('msdd').click()
html_list=driver.find_element_by_xpath('//*[@id="basicBootstrapForm"]/div[7]/div/multi-select/div[2]/ul')
items = html_list.find_elements_by_tag_name("li")
for item in items:
    if(item.text=="English" or item.text=="Czech" ):
        item.click()

listofYear=Select(driver.find_element_by_xpath('//*[@id="yearbox"]'))

print(len(listofYear.options))
for i in (listofYear.options):
    print(i.text)
listofMonth=Select(driver.find_element_by_xpath('//*[@id="basicBootstrapForm"]/div[11]/div[2]/select'))
for i in range(len(listofMonth.options)):
    print(listofMonth.options[i].text)
html_list=driver.find_element_by_xpath('//*[@id="basicBootstrapForm"]/div[7]/div/multi-select/div[2]/ul')

items=html_list.find_elements_by_tag_name("li")
userlang="English,Czech,Bulgarain,Arabic"
lang=userlang.split(",")


driver.find_element_by_xpath('//*[@id="Skills"]').send_keys("C++")
driver.find_element_by_xpath('//*[@id="countries"]').send_keys("India")

#selecting country through drop down search bar

driver.find_element_by_xpath('//*[@id="basicBootstrapForm"]/div[10]/div/span/span[1]/span/span[2]').click()
driver.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys("India")
countryList=driver.find_element_by_xpath('//*[@id="select2-country-results"]')
countryList.click()

driver.find_element_by_xpath('//*[@id="yearbox"]').send_keys("1991")
driver.find_element_by_xpath('//*[@id="basicBootstrapForm"]/div[11]/div[2]/select').send_keys("February")
driver.find_element_by_id('daybox').send_keys("14")
driver.find_element_by_id("firstpassword").send_keys("Gagan123")
driver.find_element_by_id("secondpassword").send_keys("Gagan123")

time.sleep(5)
driver.find_element_by_id("Button1").click()

driver.close()