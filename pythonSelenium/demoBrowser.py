from selenium import webdriver
# browser exposes an executable file
# through selenium test we need to invoke the executable file which will then invoke actual browser
driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/#/index")
print(driver.title)
print(driver.current_url)
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
driver.minimize_window()
driver.back()
driver.refresh()
driver.close()