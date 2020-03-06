from selenium import webdriver
import time
import math

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/math.html"

try:
	browser = webdriver.Chrome()
	browser.get(link)
	
	x_element = browser.find_element_by_xpath('//span[@id="input_value"]')
	x = x_element.text
	y = calc(x)
	
	input = browser.find_element_by_xpath('//input[@id="answer" and @required]')
	input.send_keys(y)
	
	checkbox = browser.find_element_by_xpath('//input[@id="robotCheckbox" and @required]')
	checkbox.click()
	
	radiobutton = browser.find_element_by_xpath('//input[@value="robots" and @id="robotsRule"]')
	radiobutton.click()
	
	button = browser.find_element_by_xpath('//button[@type="submit" and contains(@class,"btn")]')
	button.click()
	
	

finally:
	# ждем 30 секунд
	time.sleep(30)
	# закрываем браузер после всех манипуляций
	browser.quit()
	
	# не забываем оставить пустую строку в конце файла
