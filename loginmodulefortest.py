from selenium import webdriver
from time import sleep
import pytest
from fileDataReader import DataReader

class Mytestlogin(unittest.TestCase):

    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome(executable_path="E:\\Automation project demo\\browser drive\\chromedriver.exe")
        yield
        self.driver.close()

    def test_login(self,setup):
        driver=self.driver
        try:
            driver.get("http://demo.guru99.com/v2/")
            driver.maximize_window()
        except Exception as ex:
            print (ex)
        else:
            sleep(3)
            userName,passWord=DataReader.readDataforlogin()
            driver.find_element_by_name("uid").send_keys(userName)  # entering user id
            driver.find_element_by_name("password").send_keys(passWord)  # entering Password
            sleep(5)
            driver.find_element_by_name("btnLogin").click()
            cur_url=driver.current_url
            expectedURl="http://demo.guru99.com/v2/webpages/Managerhomepage.php"
            try:
                self.assertEqual(cur_url,expectedURl,'Login failed')


            except Exception as ex:
                print("userName and Passsword is incorrect {}".format(ex))



