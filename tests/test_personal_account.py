import allure
from data import *


@allure.feature("Личный кабинет")
class TestPersonalAccount:
    @allure.title('Переход по клику на "Личный кабинет"')
    def test_open_personal_account(self, driver, main_page, login_page, personal_account_page, authorized_user):
        main_page.click_sign_in_button()
        login_page.login_user(authorized_user.email, authorized_user.password)
        main_page.wait_make_order_page()
        main_page.click_user_account_button()
        personal_account_page.wait_user_account_page()
        assert personal_account_page.get_current_url() == ACCOUNT_PROFILE

    @allure.title('Переход в раздел "История заказов"')
    def test_open_history_order(self, driver, main_page, login_page, personal_account_page, authorized_user):
        main_page.click_sign_in_button()
        login_page.login_user(authorized_user.email, authorized_user.password)
        main_page.wait_make_order_page()
        main_page.click_user_account_button()
        personal_account_page.wait_user_account_page()
        personal_account_page.click_order_history_button()
        assert personal_account_page.get_current_url() == ORDER_HISTORY

    @allure.title('Выход из аккаунта')
    def test_logout(self, driver, main_page, login_page, personal_account_page, authorized_user):
        main_page.click_sign_in_button()
        login_page.login_user(authorized_user.email, authorized_user.password)
        main_page.wait_make_order_page()
        main_page.click_user_account_button()
        personal_account_page.wait_user_account_page()
        personal_account_page.click_logout_button()
        login_page.wait_login_page()
        assert login_page.get_current_url() == LOGIN
