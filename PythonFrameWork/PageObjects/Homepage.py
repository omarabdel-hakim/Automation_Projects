from selenium.webdriver.common.by import By

from PageObjects.CheckoutPage import CheckoutPage


class HomePage:

    def __init__(self,driver):
        self.driver = driver
    shop = (By.CSS_SELECTOR,"a[href*='shop']")
    name = (By.NAME,"name")
    email = (By.NAME,"email")
    passowrd = (By.ID,"exampleInputPassword1")
    box = (By.CSS_SELECTOR,"#exampleCheck1")
    gender = (By.ID, "exampleFormControlSelect1")
    emplymentStatus = (By.CSS_SELECTOR,"#inlineRadio1")
    date = (By.NAME,"bday")
    submit = (By.CSS_SELECTOR, "input[type='submit']")
    sumbitMessage = (By.CSS_SELECTOR,".alert-success")

    def enter_name(self):
        return self.driver.find_element(*HomePage.name)
    def enter_email(self):
        return self.driver.find_element(*HomePage.email)
    def enter_passowrd(self):
        return self.driver.find_element(*HomePage.passowrd)
    def enter_box(self):
        self.driver.find_element(*HomePage.box).click()
    def enter_gender(self):
        return self.driver.find_element(*HomePage.gender)
    def enter_Estatus(self):
        return self.driver.find_element(*HomePage.emplymentStatus) #driver.find_element(By.XPATH,"//input[@id='inlineRadio1']").click()
                                                                   #driver.find_element(By.CSS_SELECTOR,"input[id='inlineRadio1']").click()
    def enter_date(self):
        return self.driver.find_element(*HomePage.date)
    def click_submit(self):
        self.driver.find_element(*HomePage.submit).click()
        message = self.driver.find_element(*HomePage.sumbitMessage).text  # driver.find_element(By.CLASS_NAME,"alert").text
        assert "submitted successfully" in message

    def shop_item(self):
        self.driver.find_element(*HomePage.shop).click() #driver.find_element(By.XPATH,"//a[contains(@href,'shop')]").click()
        self.driver.implicitly_wait(5)
        checkout_page = CheckoutPage(self.driver)
        return checkout_page
