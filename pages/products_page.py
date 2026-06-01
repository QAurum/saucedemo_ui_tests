# в корне проекта: Служит для глобальных фикстур, которые доступны всем тестам. Например, туда можно положить главную фикстуру, которая запускает и закрывает браузер для каждой сессии тестов.

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductsPage:
#  __init__ сохраняет драйвер внутри объекта, чтобы другие методы могли им пользоваться. Методы описывают действия, которые можно совершить на странице.
    def __init__(self, driver):
        self.driver = driver
        
    def add_to_card(self, product_id):
        '''Добавляет товар в корзину по его ID (например, add-to-cart-sauce-labs-backpack)'''
        add_button = (By.ID, product_id)
        self.driver.find_element(*add_button).click()
        
    def remove_from_cart(self, product_id):
        '''Удаляет товар из корзины по его ID (например, 'remove-sauce-labs-backpack')'''
        remove_button = (By.ID, product_id)
        self.driver.find_element(*remove_button).click()

    def get_cart_badge_count(self):
        try:
            badge = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
            )
            return int(badge.text)
        except:
            return 0
