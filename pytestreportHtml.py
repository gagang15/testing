from selenium import webdriver
import pytest

import time

class Test_login_aplliction():

    @pytest.fixture()
    def setup(self):#follwoing code will excute before every test bcz of fixture
        self.driver= webdriver.Chrome(executable_path="E:\\Automation project demo\\browser drive\\chromedriver.exe")
        self.driver.maximize_window()
        yield # this code will execute after every test
        self.driver.close()


    def test_get_title(self,setup):
        driver=self.driver
        try:
            driver.get('http://www.ui5cn.com')
        except Exception as ex:
            print(ex)
        else:
            my_title='UI5N'
            assert driver.title==my_title,'Not Matching '


