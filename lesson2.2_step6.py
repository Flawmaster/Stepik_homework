from selenium import webdriver
import time
import math

link = "http://SunInJuly.github.io/execute_script.html"

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

try:
	browser = webdriver.Chrome()
	browser.get(link)
	
	x_elem = browser.find_element_by_xpath('//span[@id="input_value"]')
	x = x_elem.text
	res = calc(int(x))
	
	input = browser.find_element_by_xpath('//input[@id="answer"]')
	input.send_keys(res)
	
	button = browser.find_element_by_xpath('//button[@class="btn btn-primary"]')
	browser.execute_script('arguments[0].scrollIntoView(true)', button)
	
	checkbox = browser.find_element_by_xpath('//input[@id="robotCheckbox"]')
	checkbox.click()
	
	radiobutton = browser.find_element_by_xpath('//input[@id="robotsRule"]')
	radiobutton.click()
	
	button.click()
	
	
	
finally:
	time.sleep(15)
	browser.quit()