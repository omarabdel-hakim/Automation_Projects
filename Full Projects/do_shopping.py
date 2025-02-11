import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.service import Service
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

#C:\browserdrivers\msedgedriver.exe
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
service_object=Service("C:/browserdrivers/chromedriver.exe")
driver=webdriver.Chrome(service=service_object,options=chrome_options)
driver.get("https://rahulshettyacademy.com/angularpractice/")

#########################   ID,NAME,Xpath,CSSSelector,Classname,LikeText    #########################
#########################   Xpath >>>>>> //tagname[@attribute,"value"] ,,,, //tagname[@attribute,"value"][1]   #########################
#########################   CSS_SELECTOR >>>>>> tagname[attribute,"value"] ,,,, #id ,,,, .classname    #########################
driver.find_element(By.NAME,"name").send_keys("omarabdelhakim")
driver.find_element(By.NAME,"email").send_keys("omar@gmail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("01153330950")
driver.find_element(By.CSS_SELECTOR,"#exampleCheck1").click()

driver.find_element(By.CSS_SELECTOR,"input[type='submit']").click()
drobdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
drobdown.select_by_index(0)
#driver.find_element(By.XPATH,"//input[@id='inlineRadio1']").click()
#driver.find_element(By.CSS_SELECTOR,"input[id='inlineRadio1']").click()
driver.find_element(By.CSS_SELECTOR,"#inlineRadio1").click()
driver.find_element(By.NAME,"bday").send_keys("2001/01/01")
massege= driver.find_element(By.CSS_SELECTOR,".alert-success").text     #driver.find_element(By.CLASS_NAME,"alert").text
print(massege)
assert "Success" in massege
#driver.find_element(By.XPATH,"//a[contains(@href,'shop')]").click()
driver.find_element(By.CSS_SELECTOR,"a[href*='shop']").click()
driver.implicitly_wait(5)
phones = driver.find_elements(By.XPATH,"//div[@class='card h-100']")
for phone in phones:
    if phone.find_element(By.XPATH,"div/h4").text == "Blackberry":
        phone.find_element(By.XPATH,"div/button").click()
        break
driver.find_element(By.XPATH,"//a[contains(@class,'primary')]").click()
driver.implicitly_wait(5)
driver.find_element(By.CLASS_NAME,"btn-success").click()
driver.find_element(By.ID,"country").send_keys("in")
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))
driver.find_element(By.LINK_TEXT,"India").click()
driver.find_element(By.CLASS_NAME,"checkbox-primary").click()
driver.find_element(By.CLASS_NAME,"btn-success").click()
massege = driver.find_element(By.CLASS_NAME,"alert-success").text
assert "Success!" in massege


time.sleep(2)
