from selenium import webdriver
from selenium.webdriver.common.keys import Keys
user_name = "tincho_12db@hotmail.com"
password = "41142737Noy"
driver = webdriver.Chrome()
driver.get("https://www.facebook.com")
driver.maximize_window()
element = driver.find_element_by_id("email")
element.send_keys(user_name)
element = driver.find_element_by_id("pass")
element.send_keys(password)
element.send_keys(Keys.RETURN)
element.close()
