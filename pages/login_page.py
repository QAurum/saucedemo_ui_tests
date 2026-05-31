# в корне проекта: Служит для глобальных фикстур, которые доступны всем тестам. Например, туда можно положить главную фикстуру, которая запускает и закрывает браузер для каждой сессии тестов.

from selenium.webdriver.common.by import By
from config import BASE_URL

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID, 'user-name')
        self.password_input = (By.ID, 'password')
        self.login_button = (By.ID, 'login-button')

    def open(self):
        self.driver.get(BASE_URL)
        
    def login(self, username, password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()
    
