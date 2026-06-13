# в папке tests/: Если какая-то фикстура нужна только для тестов, лежащих в этой папке

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service # нужен, чтобы указать путь к драйверу Chrome (chromedriver)
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager #ChromeDriverManager — автоматически скачивает подходящую версию chromedriver для браузера и кэширует её - не нужно вручную скачивать и прописывать путь
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import BASE_URL, LOGIN, PASSWORD
from pages.login_page import LoginPage   # импорт страницы логина

@pytest.fixture # фикстура автоматом открывает и закрывает браузер для каждого теста
def driver():
    # Автоматически скачает драйвер Chrome и запустит браузер
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)    # запускает браузер
    chrome_options = Options()
    # Отключаем проверку на утекшие пароли и всплывающие окна
    chrome_options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False
    })
    chrome_options.add_argument("--disable-save-password-bubble")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.implicitly_wait(3) # ожидание для подгрузки элементов страницы
    yield driver            # отдаёт driver в тест
    driver.quit()           # после теста закрывает браузер
    
    # Есть и альтернативные варианты: полностью скрыть все всплывающие окна chrome_options.add_argument("--disable-popup-blocking") или запустить браузер в режиме инкогнито chrome_options.add_argument("--incognito")


# фикстура логина пользователя
@pytest.fixture
def logged_in_driver(driver): # Фикстура logged_in_driver принимает driver (это другая фикстура, которая просто запускает браузер)
    """Возвращает driver уже после успешного логина"""
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(LOGIN, PASSWORD)
    # Ждём, что логин успешен (появляется элемент на странице товаров)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
    )
    print("User has logged in")
    return driver   # возвращаем driver (не True) птому что в тесте нам нужен именно драйвер для дальнейших действий
