from selenium import webdriver
import time
import math

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))
	
link = "http://suninjuly.github.io/redirect_accept.html"

try:
	browser = webdriver.Chrome()
	browser.get(link)
	
	# кликаем кнопку
	button1 = browser.find_element_by_xpath('//button[@type="submit"]')
	button1.click()
	
	# переключаем вкладку
	newWindow = browser.window_handles[1]
	browser.switch_to.window(newWindow)
	
	# получаем х и считаем результат
	xElem = browser.find_element_by_xpath('//span[@id="input_value"]')
	x = int(xElem.text)
	result = calc(x)
	
	# заполняем ответ в input
	input = browser.find_element_by_xpath('//input[@id="answer"]')
	input.send_keys(result)
	
	# кликаем по кнопке submit
	button = browser.find_element_by_xpath('//button[@type="submit"]')
	button.click()

finally:
	# ждем 10 секунд
	time.sleep(10)
	# закрываем браузер после всех манипуляций
	browser.quit()
	# не забываем оставить пустую строку в конце файла
	