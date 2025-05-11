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


    @allure.title('Если кликнуть на ингридиент, появится всплывающее окно с деталями')
    def test_details_ingredient(self, driver, main_page):
        main_page.wait_main_page()
        main_page.click_ingredient_bun()
        assert main_page.check_open_popup_with_details_ingredient_bun()

    @allure.title('Всплывающее окно закрывается кликом по крестику')
    def test_close_details_ingredient(self, driver, main_page):
        main_page.wait_main_page()
        main_page.click_ingredient_bun()
        main_page.close_popup_with_ingredient_details()
        assert main_page.check_not_displaying_of_popup_details_ingredient()

    @allure.title('При добавлении ингридиента в заказ, увеличивается каунтер данного ингридиента')
    def test_increase_counter_on_add_ingredient(self, driver, main_page):
        main_page.wait_main_page()
        count_ingredient = main_page.get_count_ingredient_bun()
        main_page.move_ingredient_bun_to_constructor_burger()
        count_ingredient_after = main_page.get_count_ingredient_bun()
        assert count_ingredient_after == count_ingredient + 2

    @allure.title('Залогенный пользователь может оформить заказ')
    def test_make_order_with_sign_in(self, driver, main_page, login_page, authorized_user):
        main_page.click_sign_in_button()
        login_page.login_user(authorized_user.email, authorized_user.password)
        main_page.wait_make_order_page()
        main_page.move_ingredient_bun_to_constructor_burger()
        main_page.click_make_order_button()
        assert main_page.check_open_popup_with_order()