from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://google.com')

id_box = driver.find_element_by_name('username')