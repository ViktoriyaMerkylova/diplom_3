import allure
from data import *


@allure.feature("Востановление пароля")
class TestPasswordRecovery:
    @allure.title('Переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_password_recovery_button(self, driver, main_page,
                                      login_page, password_recowery_page):
        main_page.click_sign_in_button()
        login_page.click_password_recovery_button()
        password_recowery_page.wait_password_forgot_page()
        assert password_recowery_page.get_current_url() == FORGOT_PASSWORD