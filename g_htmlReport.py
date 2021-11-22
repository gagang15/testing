import unittest
from selenium import webdriver
import time
import HTMLTestRunner
class Mytestsuit(unittest.TestCase):
    def setUp(self):
        self.driver= webdriver.Chrome(executable_path="E:\\Automation project demo\\browser drive\chromedriver.exe")
    def test_get_title(self):
        driver=self.driver
        try:
            driver.get('http://www.ui5cn.com')
        except Exception as ex:
            print(ex)
        else:
            time.sleep(10)
            my_title='UI5CN'
            self.assertEqual(driver.title,my_title,'Not Matching ')
    def tearDown(self):
        self.driver.quit()

if __name__=="__main__":
    HTMLTestRunner.main()