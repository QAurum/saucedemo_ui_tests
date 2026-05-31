# в корне проекта: Служит для глобальных фикстур, которые доступны всем тестам. Например, туда можно положить главную фикстуру, которая запускает и закрывает браузер для каждой сессии тестов.

'''
Хорошей практикой является разделение:
config.py — настройки окружения (URL, таймауты, опции браузера).
test_data.py — тестовые данные (логины, пароли, сообщения об ошибках).
locators.py — локаторы элементов (по страницам).
'''

BASE_URL = 'https://www.saucedemo.com/'
LOGIN = 'standard_user'
PASSWORD = 'secret_sauce'

WRONG_LOGIN = 'tandard_use'
WRONG_PASSWORD = 'ecret_sauc'

MESSAGE_NO_USERNAME = 'Username is required'
MESSAGE_WRONG_NAME_OR_PASS = 'Username and password do not match'
