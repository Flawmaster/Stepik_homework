from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"

try:
	browser = webdriver.Chrome()
	browser.get(link)
	
	x_elem = browser.find_element_by_xpath('//span[@id="num1"]')
	x = x_elem.text
	
	y_elem = browser.find_element_by_xpath('//span[@id="num2"]')
	y = y_elem.text
	
	res = int(x) + int(y)
	
	
	select = Select(browser.find_element_by_xpath('//select[@id="dropdown"]'))
	select.select_by_value(str(res))
	
	button = browser.find_element_by_xpath('//button[@class="btn btn-default"]')
	button.click()
	
finally:
	time.sleep(30)
	browser.quit()
	