import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.service import Service
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


from PageObjects.Homepage import HomePage
from Utilities.BaseClass import BaseClass


class TestOne(BaseClass):
    def test_do_shopping(self):
        home_page = HomePage(self.driver)

        home_page.enter_name().send_keys("omarabdelhakim")
        home_page.enter_email().send_keys("omar@gmail.com")
        home_page.enter_passowrd().send_keys("01153330950")
        home_page.enter_box()
        self.selection_Bytext(home_page.enter_gender(),"Male")
        home_page.enter_Estatus().click()
        home_page.enter_date().send_keys("2001/01/01")
        home_page.click_submit()

        checkout_page = home_page.shop_item()
        checkout_page.get_products_name("Blackberry")
        checkout_page.check_cart()

        confirm_page = checkout_page.check_out()
        confirm_page.enter_country_name("India")
        confirm_page.enter_checkbox()
        confirm_page.enter_purchase()
        time.sleep(2)
