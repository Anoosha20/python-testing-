from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://login.salesforce.com/?locale=eu")
driver.find_element_by_css_selector("#username").send_keys("rahul")
driver.find_element_by_css_selector(".password").send_keys("shetty")
driver.find_element_by_css_selector(".password").clear()
driver.find_element_by_link_text("Forgot Your Password?").click()
#//tagname[text()='aaa']
driver.find_element_by_xpath("//a[text()='Cancel']").click()
#parent child
# xpath - //div[@id='usernamegroup']/label , //form[@name='login']/div[1]/label
# css - div[id='usernamegroup'] label
print(driver.find_element_by_xpath("//form[@name='login']/div[1]/label").text)
print(driver.find_element_by_css_selector("form[name='login'] label:nth-child(4)").text)