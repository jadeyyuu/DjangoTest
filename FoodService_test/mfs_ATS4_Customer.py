import unittest
import time
from selenium import webdriver

from selenium.webdriver.common.keys import Keys

class Blog_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_blog(self):
        user = "instructor"
        pwd = "instructor1a"
        driver = self.driver
        driver.maximize_window()
        driver.get("http://jadeyyuu.pythonanywhere.com/")
        elem = driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul[2]/li/a").click()
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        time.sleep(1)
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        driver.get("http://jadeyyuu.pythonanywhere.com/")
        assert "Logged In"

        driver.get("http://jadeyyuu.pythonanywhere.com/customer_list")
        time.sleep(2)
        elem = driver.find_element_by_xpath("/html/body/div[3]/table/tbody/tr[4]/td[12]/a").click()
        elem = driver.find_element_by_id("id_address")
        elem.send_keys("Edit address")
        time.sleep(2)
        elem = driver.find_element_by_xpath("/html/body/form/button").click()
        driver.get("http://jadeyyuu.pythonanywhere.com/customer_list")
        time.sleep(5)
        assert "Edit Customer"

        elem = driver.find_element_by_xpath("/html/body/div[3]/table/tbody/tr[4]/td[13]/a").click()
        alert = driver.switch_to.alert
        time.sleep(1)
        alert.accept()
        driver.get("http://jadeyyuu.pythonanywhere.com/customer_list")
        time.sleep(5)
        assert "Delete Customer"

        elem = driver.find_element_by_xpath("/html/body/div[3]/table/tbody/tr[1]/td[14]/a").click()
        time.sleep(5)
        assert "Summary Customer"


    def tearDown(self):
        self.driver.close()

    if __name__ == "__main__":
        unittest.main()