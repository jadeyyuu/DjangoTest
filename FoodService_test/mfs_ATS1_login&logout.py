import unittest
import time
from selenium import webdriver

from selenium.webdriver.common.keys import Keys

class mfs_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_mfs(self):
        user = "instructor"
        pwd = "instructor1a"
        driver = self.driver
        driver.maximize_window()
        driver.get("http://jadeyyuu.pythonanywhere.com/admin")
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        time.sleep(2)
        elem.send_keys(Keys.RETURN)
        time.sleep(2)
        driver.get("http://jadeyyuu.pythonanywhere.com/admin")
        assert "Logged In"
        time.sleep(3)

        elem = driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/a[3]").click()
        assert "Logged Out"
        time.sleep(3)

    def tearDown(self):
        self.driver.close()

    if __name__ == "__main__":
        unittest.main()
