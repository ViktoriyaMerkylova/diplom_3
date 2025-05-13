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

    @allure.title('Ввод почты и клик по кнопке "Восстановить"')
    @allure.description('''Заполняем поле email в форме восстановления пароля, кликаем на кнопку "Восстановить". 
                          ОР: переход на форму сброса пароля''')
    def test_open_reset_by_recovery_button(self, driver, main_page,
                                                    login_page, password_recowery_page):
        main_page.click_sign_in_button()
        login_page.click_password_recovery_button()
        password_recowery_page.set_email()
        password_recowery_page.click_recovery_button()
        password_recowery_page.wait_save_button_clickable()
        assert password_recowery_page.get_current_url() == RESET_PASSWORD

    @allure.title('Клик по кнопке "показать/скрыть пароль" делает поле активным - подсвечивает его')
    @allure.description('''Заполняем поле email в форме восстановления пароля, кликаем на кнопку "Восстановить", 
                                в форме сброса пароля кликаем по кнопке "Скрыть/показать пароль".
                                ОР: поле "Пароль" становится активным"''')
    def test_active_password_by_password_button(self, driver, main_page, login_page,
                                                     password_recowery_page):
        main_page.click_sign_in_button()
        login_page.click_password_recovery_button()
        password_recowery_page.set_email()
        password_recowery_page.click_recovery_button()
        password_recowery_page.click_show_or_hide_password_button()
        assert password_recowery_page.check_password_field_active()