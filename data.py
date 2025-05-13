from faker import Faker


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





