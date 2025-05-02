import time

import pytest

from PageObjects.Homepage import HomePage
from TestData.HomePageData import HomePageData
from Utilities.BaseClass import BaseClass


class TestHomePage(BaseClass,HomePageData):
    def test_formSubmission(self,get_data):
        log = self.get_logger()
        home_page = HomePage(self.driver)
        home_page.enter_name().send_keys(get_data["Name"])
        log.info("Name is " + get_data["Name"] )
        home_page.enter_email().send_keys(get_data["Email"])
        log.info("Email is " + get_data["Email"])
        home_page.enter_passowrd().send_keys(get_data["Password"])
        log.info("Password is " + get_data["Password"])
        home_page.enter_box()
        self.selection_Bytext(home_page.enter_gender(), get_data["Gender"])
        log.info("Gender is " + get_data["Gender"])
        home_page.enter_Estatus().click()
        home_page.enter_date().send_keys(get_data["Date"])
        log.info("Date is " + get_data["Date"])
        time.sleep(2)
        self.driver.refresh()
        #home_page.click_submit()
    @pytest.fixture(params=HomePageData.getTestData("omar abdelhakim")) ## From Excel
  # @pytest.fixture(params=HomePageData.test_HomePage_data)             ## From Manual Data
    def get_data(self,request):
        return request.param
