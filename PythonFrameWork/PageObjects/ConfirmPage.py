import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Utilities.BaseClass import BaseClass


class ConfirmPage(BaseClass):
    def __init__(self, driver):
        self.driver = driver

    country = (By.ID,"country")
    term = (By.CLASS_NAME,"checkbox-primary")
    purchase = (By.CLASS_NAME,"btn-success")
    success_message = (By.CLASS_NAME, "alert-success")
    def enter_country_name(self,country_name):
        self.driver.find_element(*ConfirmPage.country).send_keys(country_name)
        self.verify_link_presence(country_name)
        self.driver.find_element(By.LINK_TEXT,country_name).click()
    def enter_checkbox(self):
        self.driver.find_element(*ConfirmPage.term).click()
    def enter_purchase(self):
        self.driver.find_element(*ConfirmPage.purchase).click()
        message = self.driver.find_element(*ConfirmPage.success_message).text
        time.sleep(1)
        assert "Success!" in message



