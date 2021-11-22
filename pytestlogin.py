import pytest
import mysql.connector
from selenium import webdriver

from fileDataReader import DataReader
import unittest
#command to Generate html reprt " pytest -v -s --html=report.html pytestlogin.py"
class Testlogin():

    @pytest.fixture()
    def setup(self):
        self.driver=webdriver.Chrome(executable_path="E:\\Automation project demo\\browser drive\\chromedriver.exe")
        self.driver.maximize_window()
        yield
        self.driver.close()

    def test_loginwithDb(self,setup):
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="demodb")
        try:
            mycusor = mydb.cursor()
            mycusor.execute("select * from demo")
            result=mycusor.fetchall()
            for i in result:
                if i[1]=="tc_004":
                    userName=i[2]
                    passWord=i[3]
        except Exception as ex:
            print(ex)
        else:
            driver = self.driver
            driver.get("http://demo.guru99.com/v2/")
            driver.find_element_by_name("uid").send_keys(userName)
            driver.find_element_by_name("password").send_keys(passWord)
            driver.find_element_by_name("btnLogin").click()
            expURl="http://demo.guru99.com/v2/webpages/Managerhomepage.php"
            curUrl=driver.current_url
            assert expURl==curUrl

    def test_loginwithExcel(self,setup):

        userName, passWord = DataReader.readDataforlogin()
        driver=self.driver
        driver.get("http://demo.guru99.com/v2/")
        driver.find_element_by_name("uid").send_keys(userName)
        driver.find_element_by_name("password").send_keys(passWord)
        driver.find_element_by_name("btnLogin").click()
        expURl="http://demo.guru99.com/v2/webpages/Managerhomepage.php"
        curUrl=driver.current_url
        assert expURl==curUrl

