from .base_page import BasePage
from .locators import BasketPageLocators
from selenium.webdriver.common.by import By



class BasketPage(BasePage):
    """Реализация методов
       1 Ожидаем, что в корзине нет товаров
       2 Ожидаем, что есть текст о том что корзина пуста """

    def should_be_no_goods_in_basket(self):
        """Проверяем, что в корзине нет товаров"""
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "Basket isnt empty"


    def should_be_text_in_basket_that_basket_is_empty(self):
        """Проверяем, что есть текст, что корзина пуста"""
        #Проверяем, что такой элемент есть
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY), \
            "No element basket present"
        #Сравниваем текст, что корзина пуста
        basket_message = self.browser.find_element(*BasketPageLocators.BASKET_EMPTY).text
        assert "Your basket is empty." in basket_message, "Basket has no text 'Your basket is empty'"