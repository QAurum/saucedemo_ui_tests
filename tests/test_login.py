import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import BASE_URL, LOGIN, PASSWORD, WRONG_LOGIN, WRONG_PASSWORD, MESSAGE_NO_USERNAME, MESSAGE_WRONG_NAME_OR_PASS
from pages.login_page import LoginPage

#--- LOGIN POSITIVE ---

def test_successful_login(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(LOGIN, PASSWORD)
    assert 'inventory' in driver.current_url
    
'''
# Расширенный вариант теста с ожиданием появления кнопки и становлением ее доступной
def test_successful_login(driver):
    login_page = LoginPage(driver)
    login_page.open()
    wait = WebDriverWait(driver, 15)
    wait.until(EC.element_to_be_clickable((By.ID, "user-name")))
    login_page.login(LOGIN, PASSWORD)
    wait.until(EC.url_contains("inventory"))
    assert "inventory" in driver.current_url
'''

#--- LOGIN NEGATIVE ---

@pytest.mark.parametrize('username, password, expected_message', [('', '', MESSAGE_NO_USERNAME), (LOGIN, PASSWORD, MESSAGE_WRONG_NAME_OR_PASS), (LOGIN, WRONG_PASSWORD, MESSAGE_WRONG_NAME_OR_PASS)])
def test_login_negative(driver, username, password, expected_message):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(username, username)
    error = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR,'[data-test="error"]')))
    assert expected_message in error.text
    
# Тесты на страницу товаров (добавление в корзину, удаление, сортировка).

# Тесты на корзину (оформление заказа, проверка суммы).

# Вынести общие части в conftest.py (например, фикстуру logged_in_driver, которая уже залогинена).
