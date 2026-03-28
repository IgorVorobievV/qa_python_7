import allure

from generators import *

class TestCreateCourier:
    #курьера можно создать и запрос возвращает правильный код ответа 201 и текст {"ok":true}
    @allure.title('Проверить, что курьера можно создатьи запрос возвращает правильный код ответа 201 и текст "ok":true')
    @allure.description('Проверить, что код ответа 201 и текст "ok":true')   
    def test_create_courier_original_data_success_create(self, courier_create_and_delete):

        with allure.step('Получаем тело запроса из фикстуры и копируем в переменную payload.'):
            payload = courier_create_and_delete.copy()

        with allure.step('Отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response.'):
            response = request_courier_create(payload)

        with allure.step('Проверка, что код ответа равен 201 и текст - "ok":true.'):
            assert response.status_code == 201 and response.text == '{"ok":true}'

    #нельзя создать двух одинаковых курьеров
    @allure.title('Проверить, нельзя создать двух одинаковых курьеров')
    @allure.description('Проверка, что код ответа равен 409 и сообщение - "Этот логин уже используется. Попробуйте другой.".')
    def test_create_courier_double_data_no_create(self):

        with allure.step('Генерируем тело запроса и сохраняем в переменную payload.'):
            payload = generate_courier_data_and_return_payload().copy()

        with allure.step('Отправляем запрос на регистрацию курьера.'):
            request_courier_create(payload)

        with allure.step('Отправляем еще один запрос на регистрацию курьера с теми же данными и сохраняем ответ в переменную response.'):
            response = request_courier_create(payload)

        with allure.step('Проверка, что код ответа равен 409 и сообщение - "Этот логин уже используется. Попробуйте другой.".'):
            assert response.text == '{"code":409,"message":"Этот логин уже используется. Попробуйте другой."}'

    #чтобы создать курьера, нужно передать в ручку все обязательные поля
    @allure.title('Проверить, чтобы создать курьера, нужно передать в ручку все обязательные поля')
    @allure.description('Проверить, что код ответа 201 и текст "ok":true')
    def test_create_courier_required_data_success_create(self, courier_create_and_delete):

        with allure.step('Получаем тело запроса из фикстуры и копируем в переменную payload.'):
            payload = courier_create_and_delete.copy()

        with allure.step('Удаляем из сгенерированных данных имя курьера.'):
            payload.pop("firstName")

        with allure.step('Отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response.'):
            response = request_courier_create(payload)

        with allure.step('Проверка, что код ответа равен 201.'):
            assert response.status_code == 201 and response.text == '{"ok":true}'

    #если одного из полей нет, запрос возвращает ошибку с правильным кодом 400
    @allure.title('Проверить, что запрос возвращает ошибку и правильный код ответа 400')
    @allure.description('Проверить, что возвращается ошибка и код ответа 400')
    def test_create_courier_without_password_code_400(self):

        with allure.step('Генерируем тело запроса и сохраняем в переменную payload.'):
            payload = generate_courier_data_and_return_payload().copy()

        with allure.step('Удаляем из сгенерированных данных пароль.'):
            payload.pop("password")

        with allure.step('Отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response.'):
            response = request_courier_create(payload)

        with allure.step('Проверка, что возвращается ошибка и код ответа равен 400.'):
            assert response.text == '{"code":400,"message":"Недостаточно данных для создания учетной записи"}'

    #если создать пользователя с логином, который уже есть, возвращается ошибка с правильным кодом 409;
    @allure.title('Проверить, что запрос возвращает ошибку и правильный код ответа 409')
    @allure.description('Проверить, что возвращается ошибка и код ответа 409')
    def test_create_courier_double_data_code_409(self):

        with allure.step('Генерируем тело запроса и сохраняем в переменную payload.'):
            payload = generate_courier_data_and_return_payload().copy()

        with allure.step('Отправляем запрос на регистрацию курьера.'):
            request_courier_create(payload)

        with allure.step('Заменяем имя на логин в теле запроса.'):
            payload["firstName"] = payload["login"]

        with allure.step('Отправляем еще один запрос на регистрацию курьера с измененным именем, но тем же логином, и сохраняем ответ в переменную response.'):
            response = request_courier_create(payload)

        with allure.step('Проверка, что возвращается ошибка и код ответа равен 409.'):
            assert response.text == '{"code":409,"message":"Этот логин уже используется. Попробуйте другой."}'