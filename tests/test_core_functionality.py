import allure
from data import *


@allure.feature("Проверка основного функционала")
class TestCoreFunctionality:
    @allure.title('Переход по клику на "Конструктор"')
    def test_open_constructor(self, driver, main_page, login_page):
        main_page.click_sign_in_button()
        login_page.wait_login_page()
        login_page.click_constructor_button()
        assert main_page.get_make_burger_text() == BURGER

    @allure.title('Переход по клику на "Лента Заказов"')
    def test_open_list_orders(self, driver, main_page, order_feed_page):
        main_page.wait_main_page()
        main_page.click_list_order_button()
        assert order_feed_page.get_list_orders_header_text() == ORDER

