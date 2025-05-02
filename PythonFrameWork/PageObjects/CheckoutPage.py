from selenium.webdriver.common.by import By

from PageObjects.ConfirmPage import ConfirmPage


class CheckoutPage:

    def __init__(self,driver):
        self.driver = driver

    products = (By.XPATH,"//div[@class='card h-100']")
    cart = (By.XPATH,"//a[contains(@class,'primary')]")
    checkout = (By.CLASS_NAME,"btn-success")
    phones_name = (By.XPATH, "div/h4")
    selected_phone = (By.XPATH, "div/button")
    def get_products_name(self,text):

        phones = self.driver.find_elements(*CheckoutPage.products)
        for phone in phones:
            if phone.find_element(*CheckoutPage.phones_name).text == text:
                phone.find_element(*CheckoutPage.selected_phone).click()
                break
    def check_cart(self):
        self.driver.find_element(*CheckoutPage.cart).click()
        self.driver.implicitly_wait(5)
    def check_out(self):
        self.driver.find_element(*CheckoutPage.checkout).click()
        confirm_page = ConfirmPage(self.driver)
        return confirm_page
