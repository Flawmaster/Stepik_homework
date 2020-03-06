from selenium import webdriver
import time

link = "http://suninjuly.github.io/registration2.html"

try:
	browser = webdriver.Chrome()
	browser.get(link)
	
	#заполняем имя
	firstName = browser.find_element_by_css_selector('div.first_block>div.first_class>input')
	firstName.send_keys("John")

	#заполняем фамилию
	lastName = browser.find_element_by_css_selector('div.first_block>div.second_class>input')
	lastName.send_keys("Smith")

	#заполняем е-мэйл
	email = browser.find_element_by_css_selector('div.first_block>div.third_class>input')
	email.send_keys('test@mail.com')

	#кликаем кнопку submit
	button = browser.find_element_by_css_selector("button.btn")
	#ждем для визуальной проверки верности заполнения полей
	time.sleep(5)
	button.click()
	
	# Проверяем, что смогли зарегистрироваться
	# ждем загрузки страницы
	time.sleep(1)
	
	# находим элемент, содержащий текст
	welcome_text_elt = browser.find_element_by_tag_name("h1")
	# записываем в переменную welcome_text текст из элемента welcome_text_elt
	welcome_text = welcome_text_elt.text
	
	# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
	assert "Congratulations! You have successfully registered!" == welcome_text


finally:
	# ждем 30 секунд
	time.sleep(10)
	# закрываем браузер после всех манипуляций
	browser.quit()
	# не забываем оставить пустую строку в конце файла