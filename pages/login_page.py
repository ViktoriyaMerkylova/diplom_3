import allure
from locators.login_locators import LoginLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    @allure.step('Загрузка страница с формой авторизации')
    def wait_login_page(self):
        self.find_and_wait_element_until_visible(LoginLocators.PASSWORD_RECOVERY_BUTTON)

    @allure.step('Кликаем по кнопке "Восстановить пароль"')
    def click_password_recovery_button(self):
        self.find_and_wait_element_until_clickable(LoginLocators.PASSWORD_RECOVERY_BUTTON)
        self.click_element(LoginLocators.PASSWORD_RECOVERY_BUTTON)

    @allure.step('Вводим текст в поле email формы авторизации')
    def set_email(self, email):
        self.find_and_wait_element_until_clickable(LoginLocators.USER_EMAIL_FIELD)
        self.set_text_to_element(LoginLocators.USER_EMAIL_FIELD, email)

    @allure.step('Вводим текст в поле "Пароль" формы авторизации')
    def set_password(self, password):
        self.find_and_wait_element_until_clickable(LoginLocators.USER_PASSWORD_FIELD)
        self.set_text_to_element(LoginLocators.USER_PASSWORD_FIELD, password)

    @allure.step('Кликаем по кнопке "Войти" в форме авторизации')
    def click_login_button(self):
        self.click_element(LoginLocators.LOGIN_BUTTON)

    @allure.step('Авторизуемся')
    def login_user(self, email, password):
        self.set_email(email)
        self.set_password(password)
        self.click_login_button()

    @allure.step('Кликаем по кнопке "Конструктор"')
    def click_constructor_button(self):
        self.find_and_wait_element_until_clickable(LoginLocators.CONSTRUCTOR_BUTTON)
        self.click_element(LoginLocators.CONSTRUCTOR_BUTTON)