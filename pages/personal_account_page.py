import allure
from pages.base_page import BasePage
from locators.personal_account_locators import PersonalAccountLocators


class PersonalAccount(BasePage):
    @allure.step('Загрузка личного кабинета пользователя')
    def wait_user_account_page(self):
        self.find_and_wait_element_until_visible(PersonalAccountLocators.SAVE_BUTTON)

    @allure.step('Кликаем по кнопке "История заказов"')
    def click_order_history_button(self):
        self.find_and_wait_element_until_visible(PersonalAccountLocators.ORDER_HISTORY_BUTTON)
        self.click_element(PersonalAccountLocators.ORDER_HISTORY_BUTTON)

    @allure.step('Кликаем по кнопке "Выход" ')
    def click_logout_button(self):
        self.find_and_wait_element_until_visible(PersonalAccountLocators.LOGOUT_BUTTON)
        self.click_element(PersonalAccountLocators.LOGOUT_BUTTON)

    @allure.step('Получаем id последнего заказа пользователя')
    def get_id_last_order(self):
        self.find_and_wait_element_until_visible(PersonalAccountLocators.ID_LAST_ORDER_IN_HISTORY)
        return self.get_element_text(PersonalAccountLocators.ID_LAST_ORDER_IN_HISTORY)

    @allure.step('Кликаем по кнопке "Лента заказов"')
    def click_list_order_button(self):
        self.find_and_wait_element_until_visible(PersonalAccountLocators.LIST_ORDER_BUTTON)
        self.click_element(PersonalAccountLocators.LIST_ORDER_BUTTON)