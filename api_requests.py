import requests
from data import *


class ApiRequest:
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

