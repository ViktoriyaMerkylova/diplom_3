import allure
from pages.base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators


class OrderFeedPage(BasePage):
    @allure.step('Загрузка страницы')
    def wait_list_orders_page(self):
        self.find_and_wait_element_until_visible(OrderFeedLocators.ORDERS_FOR_ALL_TIME)

    @allure.step('Получаем текст заголовка "Лента заказов"')
    def get_list_orders_header_text(self):
        self.wait_list_orders_page()
        return self.get_element_text(OrderFeedLocators.LIST_ORDERS_HEADER)

    @allure.step('Клик на верхний заказ в ленте заказов')
    def click_first_order_in_list(self):
        self.find_and_wait_element_until_visible(OrderFeedLocators.FIRST_ORDER_IN_LIST)
        return self.click_element(OrderFeedLocators.FIRST_ORDER_IN_LIST)

    @allure.step('Количество заказов')
    def get_count_orders(self, locator):
        self.wait_list_orders_page()
        self.find_and_wait_element_until_visible(locator)
        return self.get_element_text(locator)

    @allure.step('Кликаем по кнопке "Конструктор"')
    def click_constructor_button(self):
        self.find_and_wait_element_until_clickable(OrderFeedLocators.CONSTRUCTOR_BUTTON)
        self.click_element(OrderFeedLocators.CONSTRUCTOR_BUTTON)

    @allure.step('Получаем id заказ, который в разделе "В работе"')
    def get_id_order_in_processing(self):
        self.find_and_wait_element_until_visible(OrderFeedLocators.ORDER_IN_PROCESSING)
        return self.get_element_text(OrderFeedLocators.ORDER_IN_PROCESSING)

    @allure.step('Появление всплывающего окна с деталями заказа')
    def check_open_popup_with_details_order(self):
        self.find_and_wait_element_until_visible(OrderFeedLocators.ORDER_POPUP_DETAILS)
        return self.check_displaying_of_element(OrderFeedLocators.ORDER_POPUP_DETAILS)

    @allure.step('Проверяем, что заказ пользовталя есть в "Ленте заказов"')
    def check_id_order_user_in_list_orders(self, id_order):
        order_locator = OrderFeedLocators.search_order_by_id(id_order)
        self.find_and_wait_element_until_visible(order_locator)
        return self.check_displaying_of_element(order_locator)