import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
list = []
list2 = []
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")
time.sleep(4)
count = len(driver.find_elements_by_xpath("//div[@class='products']/div"))
assert count == 3
buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")
for button in buttons:
    list.append(button.find_element_by_xpath("parent::div/parent::div/h4").text)
    button.click()
print(list)
driver.find_element_by_css_selector("img[alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
wait = WebDriverWait(driver, 15)
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME,"promoCode")))
veggies = driver.find_elements_by_css_selector("p.product-name")
for veggie in veggies:
    list2.append(veggie.text)
print(list2)
assert list == list2
originalAmount = driver.find_element_by_css_selector(".discountAmt").text
driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_css_selector("button.promoBtn").click()
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".promoInfo")))
discountAmount = driver.find_element_by_css_selector(".discountAmt").text
assert float(discountAmount) < float(originalAmount)
print(driver.find_element_by_css_selector(".promoInfo").text)
amounts = driver.find_elements_by_xpath("//tr/td[5]/p")
sum = 0
for amount in amounts:
    sum = sum + int(amount.text)  #48+160+180
print(sum)
ActualAmount = int(driver.find_element_by_class_name("totAmt").text)
assert sum == ActualAmount

