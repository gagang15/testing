import time
from selenium.webdriver import ActionChains
from selenium import webdriver

from selenium.webdriver.common.keys import Keys
class demoDragandDropClass():
    def dragandDrop(self):
        # driver = webdriver.Chrome(executable_path="E:\\Automation project demo\\browser drive\chromedriver.exe")
        #
        # driver.maximize_window()
        #
        # driver.get("http://demo.guru99.com/test/drag_drop.html")
        # elem1=driver.find_element_by_xpath('//*[@id="fourth"]/a')
        # elem2=driver.find_element_by_id('amt7')
        # ActionChains(driver).drag_and_drop(elem1,elem2).perform()
        # ActionChains(driver).drag_and_drop_by_offset(elem1, 520, 262).perform()
        # time.sleep(5)
        list1=[1,2,3,4,5,6]
        print(list1[-1:-6])
        print()

dd=demoDragandDropClass()
dd.dragandDrop()
