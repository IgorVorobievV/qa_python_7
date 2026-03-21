import requests, pytest, allure

from data_file import *

class TestCreateLogin:  
    
    #курьер может авторизоваться;
    @allure.title('Проверить, что курьер может авторизоваться')
    @allure.description('Проверить, что код ответа 200')
    def test_login_courier_valid_data_success(self):
        payload = courier_valid_data.copy()
        # отправляем запрос на авторизацию курьера и сохраняем ответ в переменную response
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', data=payload)
        assert response.status_code == 200

    #для авторизации нужно передать все обязательные поля;
    @allure.title('Проверить, что для авторизации нужно передать все обязательные поля')
    @allure.description('Проверить, что код ответа 200')
    def test_login_courier_only_login_error(self):
        payload = courier_valid_data.copy()
        # удаляем из данных имя курьера
        payload.pop("firstName")
        # отправляем запрос на авторизацию курьера и сохраняем ответ в переменную response
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', data=payload)

        assert response.status_code == 200

    #система вернёт ошибку, если неправильно указать логин или пароль;
    @allure.title('Проверить, что система вернёт ошибку, если неправильно указать логин или пароль')
    @allure.description('Проверить, что код ответа 404')
    @pytest.mark.parametrize('data', [courier_valid_data['login'], courier_valid_data['password']])
    def test_login_courier_wrong_data_error(self, data):
        payload = courier_valid_data.copy()
        payload['login'] = data
        payload['password'] = data
        # отправляем запрос на авторизацию курьера и сохраняем ответ в переменную response
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', data=payload)

        assert response.status_code == 404

    #если какого-то поля нет, запрос возвращает ошибку;
    @allure.title('Проверить, что если какого-то поля нет, запрос возвращает ошибку')
    @allure.description('Проверить, что код ответа 400')
    def test_login_courier_only_password_error(self):
        payload = courier_valid_data.copy()
        # удаляем из данных login курьера
        payload.pop("login")
        # отправляем запрос на авторизацию курьера и сохраняем ответ в переменную response
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', data=payload)

        assert response.status_code == 400

    #если авторизоваться под несуществующим пользователем, запрос возвращает ошибку;
    @allure.title('Проверить, что если авторизоваться под несуществующим пользователем, запрос возвращает ошибку')
    @allure.description('Проверить, что код ответа 404')
    def test_login_courier_nonexistent_login_error(self):
        payload = courier_valid_data.copy()
        # заменяем логин паролем
        payload['login'] = courier_valid_data['password']
        # отправляем запрос на авторизацию курьера и сохраняем ответ в переменную response
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', data=payload)

        assert response.status_code == 404

    #успешный запрос возвращает id.
    @allure.title('Проверить, что успешный запрос возвращает id')
    @allure.description('Проверить, что ответа содержит id')
    def test_login_courier_valid_data_id(self):
        payload = courier_valid_data.copy()
        # отправляем запрос на авторизацию курьера и сохраняем ответ в переменную response
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', data=payload)
        
        assert 'id' in response.text