from faker import Faker
import requests


BASE_URL = "https://stellarburgers.nomoreparties.site"

LOGIN = f'{BASE_URL}/login'
FORGOT_PASSWORD = f'{BASE_URL}/forgot-password'
RESET_PASSWORD = f'{BASE_URL}/reset-password'
ACCOUNT_PROFILE = f'{BASE_URL}/account/profile'
ORDER_HISTORY = f'{BASE_URL}/account/order-history'

REGISTER = f"{BASE_URL}/api/auth/register"
LOGIN_API = f"{BASE_URL}/api/auth/login"
USER = f"{BASE_URL}/api/auth/user"

BURGER = "Соберите бургер"
ORDER = "Лента заказов"


class FakeData:
    @staticmethod
    def email():
        fake = Faker()
        email = fake.ascii_free_email()
        return email

    @staticmethod
    def password():
        fake = Faker()
        password = fake.password(length=10)
        return password

    @staticmethod
    def name():
        fake = Faker()
        name = fake.first_name()
        return name


class Body:
    @staticmethod
    def build_user_body(email, password, name):
        user_body = {"email": email,
                     "password": password,
                     "name": name}
        return user_body

    @staticmethod
    def build_login_pass_body(email, password):
        login_pass_body = {"email": email,
                           "password": password}
        return login_pass_body


class Request:
    @staticmethod
    def create_user(body_user):
        return requests.post(f'{REGISTER}', json=body_user)

    @staticmethod
    def login_user(login_pass):
        return requests.post(f'{LOGIN_API}', data=login_pass)

    @staticmethod
    def delete_user(token):
        return requests.delete(f'{USER}',
                               headers={'Authorization': token})


