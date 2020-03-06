from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
	browser = webdriver.Chrome()
	browser.get(link)
	
	# заполняем имя
	firstName = browser.find_element_by_xpath('//input[@name="firstname"]')
	firstName.send_keys('John')
	
	# заполняем фамилию
	lastName = browser.find_element_by_xpath('//input[@name="lastname"]')
	lastName.send_keys('Smith')
	
	# заполняем почту
	email = browser.find_element_by_xpath('//input[@name="email"]')
	email.send_keys('test@mail.com')
	
	# получаем путь
	currentDir = os.path.abspath(os.path.dirname(__file__))
	fileDir = currentDir + '\\attach\\test.txt'
	
	# отправляем файл по полученному пути
	fileInput = browser.find_element_by_xpath('//input[@name="file"]')
	fileInput.send_keys(fileDir)
	#time.sleep(5)
	
	#кликаем на кнопку
	button = browser.find_element_by_xpath('//button[@type="submit"]')
	button.click()
	
finally:
	time.sleep(10)
	# закрываем браузер после всех манипуляций
	browser.quit()
	# не забываем оставить пустую строку в конце файла