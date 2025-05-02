import selenium
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
import inspect
import logging

@pytest.mark.usefixtures("setup")
class BaseClass:
    def verify_link_presence(self,text):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,text)))

    def selection_Bytext(self,locator,text):
        element = Select(locator)
        element.select_by_visible_text(text)
    def get_logger(self):
        loggername = inspect.stack()[1][3]
        logger = logging.getLogger(loggername)
        fileHandler = logging.FileHandler("Base_file.log")
        formatter = logging.Formatter("{%(asctime)s} ,%(name)s ,%(levelname)s ,%(message)s",
                                      datefmt="%D-%B-->%H:%M:%S")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.DEBUG)
        return logger