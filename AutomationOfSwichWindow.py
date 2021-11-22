import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.remote.webelement import WebElement
driver=webdriver.Chrome(executable_path="E:\\Automation project demo\\browser drive\chromedriver.exe")
driver.get("http://demo.automationtesting.in/Windows.html")
driver.maximize_window()


driver.find_element_by_xpath('//*[@id="Tabbed"]/a/button').click()
driver.switch_to.window(driver.window_handles[1])

driver.find_element_by_xpath('//a[@class="analystic"]').send_keys("gagan")
driver.close()
driver.switch_to.window(driver.window_handles[0])
driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/ul/li[2]/a').click()
driver.find_element_by_xpath('//*[@id="Seperate"]/button').click()
driver.switch_to.window(driver.window_handles[1])
driver.maximize_window()
driver.close()
driver.switch_to.window(driver.window_handles[0])
driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/ul/li[3]/a').click()
driver.find_element_by_xpath('//*[@id="Multiple"]/button').click()
driver.switch_to.window(driver.window_handles[2])
driver.close()
driver.switch_to.window(driver.window_handles[1])
driver.close()
driver.switch_to.window(driver.window_handles[0])
driver.quit()


