import allure

from generators import *

class TestCreateCourier:
    #курьера можно создать и запрос возвращает правильный код ответа 201 и текст {"ok":true}
    @allure.title('Проверить, что курьера можно создатьи запрос возвращает правильный код ответа 201 и текст "ok":true')
    @allure.description('Проверить, что код ответа 201 и текст "ok":true')   
    def test_create_courier_original_data_success_create(self, courier_create_and_delete):

        with allure.step("Отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response."):
            response = request_courier_create(courier_create_and_delete)

        with allure.step('Проверка, что код ответа равен 201 и текст - "ok":true.'):
            assert response.status_code == 201 and response.text == '{"ok":true}'

    #нельзя создать двух одинаковых курьеров
    @allure.title('Проверить, нельзя создать двух одинаковых курьеров')
    @allure.description('Проверить, что код ответа не 201')
    def test_create_courier_double_data_no_create(self, courier_create_and_delete):

        with allure.step("Отправляем запрос на регистрацию курьера."):
            request_courier_create(courier_create_and_delete)

        with allure.step("Отправляем еще один запрос на регистрацию курьера с теми же данными и сохраняем ответ в переменную response."):
            response = request_courier_create(courier_create_and_delete)

        with allure.step("Проверка, что код ответа не равен 201."):
            assert response.status_code != 201 and response.text != '{"ok":true}'

    #чтобы создать курьера, нужно передать в ручку все обязательные поля
    @allure.title('Проверить, чтобы создать курьера, нужно передать в ручку все обязательные поля')
    @allure.description('Проверить, что код ответа 201')
    def test_create_courier_required_data_success_create(self, courier_create_and_delete):

        with allure.step("Удаляем из сгенерированных данных имя курьера."):
            courier_create_and_delete.pop("firstName")

        with allure.step("Отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response."):
            response = request_courier_create(courier_create_and_delete)

        with allure.step("Проверка, что код ответа равен 201."):
            assert response.status_code == 201

    #если одного из полей нет, запрос возвращает ошибку с правильным кодом 400
    @allure.title('Проверить, что запрос возвращает ошибку и правильный код ответа 400')
    @allure.description('Проверить, что возвращается ошибка и код ответа 400')
    def test_create_courier_without_password_code_400(self, courier_create_and_delete):

        with allure.step("Удаляем из сгенерированных данных пароль."):
            courier_create_and_delete.pop("password")

        with allure.step("Отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response."):
            response = request_courier_create(courier_create_and_delete)

        with allure.step("Проверка, что возвращается ошибка и код ответа равен 400."):
            assert response.text == '{"code":400,"message":"Недостаточно данных для создания учетной записи"}'

    #если создать пользователя с логином, который уже есть, возвращается ошибка с правильным кодом 409;
    @allure.title('Проверить, что запрос возвращает ошибку и правильный код ответа 409')
    @allure.description('Проверить, что возвращается ошибка и код ответа 409')
    def test_create_courier_double_data_code_409(self, courier_create_and_delete):

        with allure.step("Отправляем запрос на регистрацию курьера."):
            request_courier_create(courier_create_and_delete)

        with allure.step("Отправляем еще один запрос на регистрацию курьера с теми же данными и сохраняем ответ в переменную response."):
            response = request_courier_create(courier_create_and_delete)

        with allure.step("Проверка, что возвращается ошибка и код ответа равен 409."):
            assert response.text == '{"code":409,"message":"Этот логин уже используется. Попробуйте другой."}'