# в корне проекта: Служит для глобальных фикстур, которые доступны всем тестам. Например, туда можно положить главную фикстуру, которая запускает и закрывает браузер для каждой сессии тестов.

#Фикстуры и хуки для pytest. Этот файл pytest подхватывает автоматически: Фикстуры (например, soup, driver, db_connection), Плагины, Переопределение поведения pytest

# saucedemo_ui_tests/conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

#chrome_options.add_argument('--headless') # позволяет запускать тесты в фоне без графического интерфейса. Это ускоряет парсинг сайтов и автоматизацию тестирования на серверах, экономя ресурсы.
# options.add_argument("--window-position=-2400,-2400") #для использования на версии хрома 29,30. Так как в селениуме открывается просто пустое окно, если хедлесс не указать без второй строчки

