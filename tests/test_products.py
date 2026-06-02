import pytest
from selenium.webdriver.common.by import By
from pages.products_page import ProductsPage

# Список товаров для тестирования
PRODUCTS = [
    "Sauce Labs Backpack",
    "Sauce Labs Bike Light",
    "Sauce Labs Bolt T-Shirt"
]

#--- POSITIVE ---

@pytest.mark.parametrize("product_name", PRODUCTS)
def test_add_product_to_cart(logged_in_driver, product_name): # logged_in_driver - после логина эта фикстура логина возвращает драйвер с открытой страницей инвентаря
    driver = logged_in_driver
    products_page = ProductsPage(driver)
    products_page.add_to_cart(product_name)
    
    assert products_page.get_cart_badge_count() >= 1
    assert products_page.get_button_text(product_name) == 'Remove'
    
    #print(driver.page_source[:1000])  #Первые 1000 символов HTML-кода текущей страницы в виде одной огромной строки для отладки

@pytest.mark.parametrize("product_name", PRODUCTS)
def test_remove_product_from_cart(logged_in_driver, product_name):
    driver = logged_in_driver
    products_page = ProductsPage(driver)
    products_page.add_to_cart(product_name)
    # Проверим, что кнопка стала "Remove"
    assert products_page.get_button_text(product_name) == 'Remove'
    
    products_page.remove_from_cart(product_name)
    # Проверим, что кнопка вернулась в "Add to cart"
    assert products_page.get_button_text(product_name) == 'Add to cart'
    assert products_page.get_cart_badge_count() == 0
