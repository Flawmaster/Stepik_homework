from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

link ='http://suninjuly.github.io/explicit_wait2.html'

try:
	browser = webdriver.Chrome()
	browser.get(link)
	
	# ждем, пока не будет цена 100
	WebDriverWait(browser, 14).until(EC.text_to_be_present_in_element((By.XPATH,'//h5[@id="price"]'),'100'))
	
	# бронируем дом
	buttonBook = browser.find_element(By.XPATH, '//button[@id="book"]')
	buttonBook.click()
	
	# скроллим до самого нижнего элемента на странице(кнопка submit)
	buttonSubmit = browser.find_element_by_xpath('//button[@id="solve"]')
	browser.execute_script('arguments[0].scrollIntoView(true)', buttonSubmit)
	
	# ждем появления х и считаем формулу от х
	x_elem = WebDriverWait(browser, 1).until(EC.element_to_be_clickable((By.XPATH, '//span[@id="input_value"]')))
	x = int(x_elem.text)
	res = calc(x)
	
	# заполняем input с ответом
	input = browser.find_element(By.XPATH, '//input[@id="answer"]')
	input.send_keys(res)
	
	# кликаем кнопку submit
	buttonSubmit.click()
	
	
	
finally:
	# ждем 10 секунд
	time.sleep(10)
	# закрываем браузер после всех манипуляций
	browser.quit()
	# не забываем оставить пустую строку в конце файла