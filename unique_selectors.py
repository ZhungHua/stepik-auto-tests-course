"""
Просто запустить скрипт
"""

from selenium import webdriver
import time


succsessfull_test_link = "https://suninjuly.github.io/registration1.html"
bugged_test_link = 'http://suninjuly.github.io/registration2.html'

credentials = {
    'first_name': 'John',
    'last_name': 'Doe',
    'email': 'john.doe@eg.net',
    'phone': '111-111-111',
    'address': 'Dull State 5'
}

locators = {
    # schema: block - subclass
    'first_name': ['first', 'first'],
    'last_name': ['first', 'second'],
    'email': ['first', 'third'],
    'phone': ['second', 'first'],
    'address': ['second', 'second']
}

locator_template = '.{}_block .{}'


def test_registration(url, locators, locator_template, credentials):
    """
    Check registration form fields
    """
    try:
        browser = webdriver.Chrome()
        browser.get(url)

        # Заполняем поля ввода
        for key, selector in locators.items():
            inputx = browser.find_element_by_css_selector(
                locator_template.format(*selector))
            inputx.send_keys(credentials.get(key))

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
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
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()


# run
for link in [succsessfull_test_link, bugged_test_link]:
	test_registration(link, locators, credentials)