# в корне проекта: Служит для глобальных фикстур, которые доступны всем тестам. Например, туда можно положить главную фикстуру, которая запускает и закрывает браузер для каждой сессии тестов.

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class ProductsPage:
#  __init__ сохраняет драйвер внутри объекта, чтобы другие методы могли им пользоваться. Методы описывают действия, которые можно совершить на странице.
    def __init__(self, driver):
        self.driver = driver


    def _get_product_container(self, product_name):
        '''Нахоидт контейнер по названию товара'''
        # normalize-space() - удаляет рпобелы в начале, конце, наменяет несколько на один
        xpath = f"//div[contains(@class, 'inventory_item_name') and contains(normalize-space(), '{product_name}')]/ancestor::div[contains(@class, 'inventory_item')]"
        return self.driver.find_element(By.XPATH, xpath)
        # // в начале XPath означает поиск от корня документа (всего HTML).
    
    
    def _get_button(self, product_name):
        '''Находит кнопку с опр текстом анутри контейнера товара'''
        container = self._get_product_container(product_name)
        # Ищем кнопку с классом btn_inventory внутри контейнера
        xpath = ".//button[contains(@class, 'btn_inventory')]"
        # .// означает поиск относительно текущего элемента (в данном случае — внутри контейнера товара)
        
        return container.find_element(By.XPATH, xpath)
        # вызов метода find_element у объекта container (который является веб-элементом). Он ищет внутри этого элемента (не во всей странице) по указанному XPath.
    
# ----------------------------------------------

    def get_button_text(self, product_name):
        button = self._get_button(product_name)
        return button.text
    
    def add_to_cart(self, product_name):
        button = self._get_button(product_name)
        button.click()

    def remove_from_cart(self, product_name):
        button = self._get_button(product_name)
        button.click()

    ''' Добавление товаров по конкретному ID
    def add_to_cart(self, product_id):
        #Добавляет товар в корзину по его ID (например, add-to-cart-sauce-labs-backpack)
        add_button = (By.ID, product_id)
        self.driver.find_element(*add_button).click()
        
    def remove_from_cart(self, product_id):
        #Удаляет товар из корзины по его ID (например, 'remove-sauce-labs-backpack')
        remove_button = (By.ID, product_id)
        self.driver.find_element(*remove_button).click()
        
    '''

    def get_cart_badge_count(self):
        try:
            badge = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
            )
            return int(badge.text)
        except TimeoutException:
            return 0
