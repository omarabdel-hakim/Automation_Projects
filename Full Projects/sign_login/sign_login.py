import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.service import Service
from selenium.webdriver.support.select import Select

service_obj=Service("C:/browserdrivers/chromedriver.exe")
driver =webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/client/")
driver.maximize_window()
driver.find_element(By.LINK_TEXT,"Register").click()
driver.find_element(By.CSS_SELECTOR,"#firstName").send_keys("omar")
driver.find_element(By.CSS_SELECTOR,"#lastName").send_keys("abdelhakim")
driver.find_element(By.CSS_SELECTOR,"#userEmail").send_keys("omar011@gmail.com")
driver.find_element(By.CSS_SELECTOR,"#userMobile").send_keys("1153330950")
dropdown = Select(driver.find_element(By.CSS_SELECTOR,"select"))    #driver.find_element(By.CSS_SELECTOR,"option[value='2: Student']").click()
dropdown.select_by_visible_text("Student")  #dropdown.select_by_index(2)  #dropdown.select_by_value("2: Student")


driver.find_element(By.CSS_SELECTOR,"input[value='Male']").click()
driver.find_element(By.CSS_SELECTOR,"#userPassword").send_keys("Dromar007@")
driver.find_element(By.CSS_SELECTOR,"#confirmPassword").send_keys("Dromar007@")
driver.find_element(By.CSS_SELECTOR,"input[type='checkbox']").click()
driver.find_element(By.CSS_SELECTOR,"#login").click() #driver.find_element(By.CSS_SELECTOR,"input[type='submit']").click()
time.sleep(0.5)
massege = driver.find_element(By.CSS_SELECTOR,"div[aria-label='User already exisits with this Email Id!']").text
print(massege)
assert massege
time.sleep(5)