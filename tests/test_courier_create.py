import requests, pytest, allure

class TestCreateCourier:  

    #курьера можно создать;
    @allure.title('Проверить, что курьера можно создать')
    @allure.description('Проверить, что код ответа 201')   
    def test_create_courier_original_data_success_create(self, courier_data_gen):
        # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=courier_data_gen)

        # удаление тестовых данных (отправляем запрос на вход курьера и сохраняем ответ в переменную response2)
        response2 = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', data=courier_data_gen)
        # удаление тестовых данных (получаем id созданного курьера)
        id = response2.json()['id']
        # удаление тестовых данных (отправляем запрос на удаление курьера)
        requests.delete(f'https://qa-scooter.praktikum-services.ru/api/v1/courier/{id}')

        assert response.status_code == 201

    #нельзя создать двух одинаковых курьеров;
    @allure.title('Проверить, нельзя создать двух одинаковых курьеров')
    @allure.description('Проверить, что код ответа не 201')
    def test_create_courier_double_data_no_create(self, courier_data_gen):
        # отправляем запрос на регистрацию курьера
        requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=courier_data_gen)
        # отправляем еще один запрос на регистрацию курьера с теми же данными и сохраняем ответ в переменную response
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=courier_data_gen)

        assert response.status_code != 201

    #чтобы создать курьера, нужно передать в ручку все обязательные поля;
    @allure.title('Проверить, чтобы создать курьера, нужно передать в ручку все обязательные поля')
    @allure.description('Проверить, что код ответа 201')
    def test_create_courier_required_data_success_create(self, courier_data_gen):
        # удаляем из сгенерированных данных имя курьера
        courier_data_gen.pop("firstName")

        # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=courier_data_gen)
        
        # удаление тестовых данных (отправляем запрос на вход курьера и сохраняем ответ в переменную response2)
        response2 = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', data=courier_data_gen)
        # удаление тестовых данных (получаем id созданного курьера)
        id = response2.json()['id']
        # удаление тестовых данных (отправляем запрос на удаление курьера)
        requests.delete(f'https://qa-scooter.praktikum-services.ru/api/v1/courier/{id}')

        assert response.status_code == 201
    
    #запрос возвращает правильный код ответа 400;
    @allure.title('Проверить, что запрос возвращает правильный код ответа 400')
    @allure.description('Проверить, что код ответа 400')
    def test_create_courier_without_password_code_400(self, courier_data_gen):
        # удаляем из сгенерированных данных пароль
        courier_data_gen.pop("password")

        # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=courier_data_gen)

        assert response.status_code == 400

    #запрос возвращает правильный код ответа 409;
    @allure.title('Проверить, что запрос возвращает правильный код ответа 409')
    @allure.description('Проверить, что код ответа 409')
    def test_create_courier_double_data_code_409(self, courier_data_gen):
        # отправляем запрос на регистрацию курьера
        requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=courier_data_gen)
        # отправляем еще один запрос на регистрацию курьера с теми же данными и сохраняем ответ в переменную response
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=courier_data_gen)

        assert response.status_code == 409

    #запрос возвращает правильный код ответа 201;
    @allure.title('Проверить, что запрос возвращает правильный код ответа 201')
    @allure.description('Проверить, что код ответа 201')
    def test_create_courier_original_data_code_201(self, courier_data_gen):
        # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=courier_data_gen)

        # удаление тестовых данных (отправляем запрос на вход курьера и сохраняем ответ в переменную response2)
        response2 = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', data=courier_data_gen)
        # удаление тестовых данных (получаем id созданного курьера)
        id = response2.json()['id']
        # удаление тестовых данных (отправляем запрос на удаление курьера)
        requests.delete(f'https://qa-scooter.praktikum-services.ru/api/v1/courier/{id}')

        assert response.status_code == 201


    #успешный запрос возвращает {"ok":true};
    @allure.title('Проверить, что успешный запрос возвращает "ok":true')
    @allure.description('Проверить, что текст ответа "ok":true')
    def test_create_courier_original_data_right_text(self, courier_data_gen):
        # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=courier_data_gen)

        # удаление тестовых данных (отправляем запрос на вход курьера и сохраняем ответ в переменную response2)
        response2 = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', data=courier_data_gen)
        # удаление тестовых данных (получаем id созданного курьера)
        id = response2.json()['id']
        # удаление тестовых данных (отправляем запрос на удаление курьера)
        requests.delete(f'https://qa-scooter.praktikum-services.ru/api/v1/courier/{id}')

        assert response.text == '{"ok":true}'

    #если одного из полей нет, запрос возвращает ошибку;
    @allure.title('Проверить, что если одного из полей нет, запрос возвращает ошибку')
    @allure.description('Проверить, что текст ответа содержит "code":400')
    @pytest.mark.parametrize('data', ['only_login', 'only_password'])
    def test_create_courier_without_required_data_error(self, data, courier_data_gen):
        if data == 'only_login':
            # удаляем из сгенерированных данных пароль
            courier_data_gen.pop("password")
        if data == 'only_password':
            # удаляем из сгенерированных данных логин
            courier_data_gen.pop("login")

        # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=courier_data_gen)

        assert '"code":400' in response.text

    #если создать пользователя с логином, который уже есть, возвращается ошибка.
    @allure.title('Проверить, что если создать пользователя с логином, который уже есть, возвращается ошибка')
    @allure.description('Проверить, что текст ответа содержит "code":409')
    def test_create_courier_double_data_error(self, courier_data_gen):
        # отправляем запрос на регистрацию курьера
        requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=courier_data_gen)
        # отправляем еще один запрос на регистрацию курьера с теми же данными и сохраняем ответ в переменную response
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=courier_data_gen)

        assert '"code":409' in response.text