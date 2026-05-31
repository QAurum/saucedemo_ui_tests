import sys
print('sys.path', sys.path)
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from selenium.webdriver.common.by import By

from pages.login_page import LoginPage
from config import LOGIN, PASSWORD

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

'''
def test_successful_login(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(LOGIN, PASSWORD)
    assert 'inventory' in driver.current_url
    
'''

def test_successful_login(driver):
    login_page = LoginPage(driver)
    login_page.open()
    # Ждём, пока поле username станет доступным
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "user-name"))
    )
    login_page.login(LOGIN, PASSWORD)
    assert "inventory" in driver.current_url
