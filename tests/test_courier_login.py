import pytest, allure

from generators import *
from data_file import *

class TestCreateLogin:  
    
    #курьер может авторизоваться и успешный запрос возвращает id
    @allure.title('Проверить, что курьер может авторизоваться и возвращается id')
    @allure.description('Проверить, что код ответа 200 и возвращается id')
    def test_login_courier_valid_data_success(self):
        
        with allure.step("Копируем тело запроса из данных"):
            payload = courier_valid_data.copy()

        with allure.step("Отправляем запрос на авторизацию курьера и сохраняем ответ в переменную response."):
            response = request_courier_login(payload)

        with allure.step("Проверка, что код ответа равен 200 и возвращается id."):
            assert response.status_code == 200 and 'id' in response.text

    #для авторизации нужно передать все обязательные поля
    @allure.title('Проверить, что для авторизации нужно передать все обязательные поля')
    @allure.description('Проверить, что код ответа 200')
    def test_login_courier_only_login_error(self):

        with allure.step("Копируем тело запроса из данных"):
            payload = courier_valid_data.copy()

        with allure.step("Удаляем из данных имя курьера"):
            payload.pop("firstName")

        with allure.step("Отправляем запрос на авторизацию курьера и сохраняем ответ в переменную response."):
            response = request_courier_login(payload)

        with allure.step("Проверка, что код ответа равен 200."):
            assert response.status_code == 200

    #система вернёт ошибку, если неправильно указать логин или пароль
    @allure.title('Проверить, что система вернёт ошибку, если неправильно указать логин или пароль')
    @allure.description('Проверить, что код ответа 404')
    @pytest.mark.parametrize('data', [courier_valid_data['login'], courier_valid_data['password']])
    def test_login_courier_wrong_data_error(self, data):

        with allure.step("Копируем тело запроса из данных"):
            payload = courier_valid_data.copy()

        with allure.step("Меняем логин в теле запроса"):
            payload['login'] = data

        with allure.step("Меняем пароль в теле запроса"):
            payload['password'] = data

        with allure.step("Отправляем запрос на авторизацию курьера и сохраняем ответ в переменную response."):
            response = request_courier_login(payload)

        with allure.step("Проверка, что возвращается ошибка и код ответа равен 404."):
            assert response.status_code == 404 and 'message' in response.text

    #если какого-то поля нет, запрос возвращает ошибку
    @allure.title('Проверить, что если какого-то поля нет, запрос возвращает ошибку')
    @allure.description('Проверить, что код ответа 400')
    def test_login_courier_only_password_error(self):
        with allure.step("Копируем тело запроса из данных"):
            payload = courier_valid_data.copy()

        with allure.step("Удаляем из данных логин"):
            payload.pop("login")

        with allure.step("Отправляем запрос на авторизацию курьера и сохраняем ответ в переменную response."):
            response = request_courier_login(payload)

        with allure.step("Проверка, что возвращается ошибка и код ответа равен 400."):
            assert response.status_code == 400 and 'message' in response.text

    #если авторизоваться под несуществующим пользователем, запрос возвращает ошибку
    @allure.title('Проверить, что если авторизоваться под несуществующим пользователем, запрос возвращает ошибку')
    @allure.description('Проверить, что код ответа 404')
    def test_login_courier_nonexistent_login_error(self):

        with allure.step("Копируем тело запроса из данных"):
            payload = courier_valid_data.copy()

        with allure.step("Заменяем логин паролем"):
            payload['login'] = courier_valid_data['password']

        with allure.step("Отправляем запрос на авторизацию курьера и сохраняем ответ в переменную response."):
            response = request_courier_login(payload)

        with allure.step("Проверка, что возвращается ошибка и код ответа равен 404."):
            assert response.status_code == 404 and 'message' in response.text