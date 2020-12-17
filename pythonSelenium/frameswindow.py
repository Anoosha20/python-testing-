from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://the-internet.herokuapp.com/iframe")
#frame id or frame name or index value
driver.switch_to.frame("mce_0_ifr")
driver.find_element_by_xpath("//body[@id='tinymce']/p").clear()
driver.find_element_by_xpath("//body[@id='tinymce']/p").send_keys(" iam able to automate")
driver.switch_to.default_content()
print(driver.find_element_by_tag_name("h3").text)