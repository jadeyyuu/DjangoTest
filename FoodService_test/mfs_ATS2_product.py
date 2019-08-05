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

        elem = driver.find_element_by_xpath("/html/body/div/div/div/div/div/div/div/div/div[3]/div/div/p[2]/a").click()

        elem = driver.find_element_by_xpath("/html/body/div/div/div/div[3]/div/a/span").click()
        elem = driver.find_element_by_id("id_cust_name")
        elem = driver.find_element_by_xpath("/html/body/div/div/div/form/div[1]/div/select/option[2]").click()
        elem = driver.find_element_by_id("id_product")
        elem.send_keys("test of selenium")
        elem = driver.find_element_by_id("id_p_description")
        elem.send_keys("Description for selenium")
        elem = driver.find_element_by_id("id_quantity")
        elem.send_keys("1")
        elem = driver.find_element_by_id("id_charge")
        elem.send_keys("32")
        time.sleep(2)
        elem = driver.find_element_by_xpath("/html/body/div/div/div/form/button").click()

        driver.get("http://jadeyyuu.pythonanywhere.com/product_list")
        time.sleep(5)
        assert "Add new Product"

        elem = driver.find_element_by_xpath("/html/body/div/div/div/div[3]/table/tbody/tr[5]/td[7]/a").click()
        elem = driver.find_element_by_id("id_product")
        elem.send_keys("Edit")
        elem = driver.find_element_by_id("id_p_description")
        elem.send_keys("Edit Description")
        time.sleep(2)
        elem = driver.find_element_by_xpath("/html/body/div/div/div/form/button").click()
        driver.get("http://jadeyyuu.pythonanywhere.com/product_list")
        time.sleep(5)
        assert "Edit Product"

        elem = driver.find_element_by_xpath("/html/body/div/div/div/div[3]/table/tbody/tr[5]/td[8]/a").click()
        alert = driver.switch_to.alert
        time.sleep(1)
        alert.accept()
        driver.get("http://jadeyyuu.pythonanywhere.com/product_list")
        time.sleep(5)
        assert "Delete Product"


    def tearDown(self):
        self.driver.close()

    if __name__ == "__main__":
        unittest.main()