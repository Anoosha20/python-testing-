from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://www.rahulshettyacademy.com/angularpractice/")
driver.find_element_by_css_selector("input[name='name']").send_keys("rahul")
driver.find_element_by_name("email").send_keys("shetty")
#driver.find_element_by_name("name").send_keys("rahul")
driver.find_element_by_id("exampleCheck1").click()
# select class provide the methods to handle the options in dropdown, create Select object
dropdown = Select(driver.find_element_by_id("exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)
driver.find_element_by_xpath("//input[@type='submit']").click()
message = driver.find_element_by_class_name("alert-success").text
assert "success" in message
# [class*='alert-success'] - css
# //*[contains(@class,'alert-success')] - xpath