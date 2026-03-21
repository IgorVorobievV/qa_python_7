import requests, pytest, allure

class TestDeleteCourier:  

    #неуспешный запрос возвращает соответствующую ошибку;
    @allure.title('Проверить, что неуспешный запрос возвращает соответствующую ошибку')
    @allure.description('Проверить, что текст ответа содержит "Недостаточно данных для удаления курьера." при отсутствующем id курьера и "Курьера с таким id нет." при несуществующим id курьера')
    @pytest.mark.parametrize('id, error', [['', 'Недостаточно данных для удаления курьера.'],[1, 'Курьера с таким id нет.']])
    def test_delete_courier_wrong_data_right_error(self, id, error):

        # отправляем запрос на удаление курьера и сохраняем ответ в переменную response
        response = requests.delete(f'https://qa-scooter.praktikum-services.ru/api/v1/courier/{id}')

        assert response.json()['message'] == error
        
    #успешный запрос возвращает {"ok":true};
    @allure.title('Проверить, что успешный запрос возвращает "ok":true')
    @allure.description('Проверить, что текст ответа содержит "ok":true')
    def test_delete_courier_success_request_right_answer(self, courier_data_gen):
        
        # отправляем запрос на регистрацию курьера
        requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=courier_data_gen)

        # отправляем запрос на вход курьера и сохраняем ответ в переменную response
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', data=courier_data_gen)

        # получаем id созданного курьера
        id = response.json()['id']

        # отправляем запрос на удаление курьера и сохраняем ответ в переменную response2
        response2 = requests.delete(f'https://qa-scooter.praktikum-services.ru/api/v1/courier/{id}')

        assert response2.text == '{"ok":true}'

    #если отправить запрос без id, вернётся ошибка;
    @allure.title('Проверить, что если отправить запрос без id, вернётся ошибка')
    @allure.description('Проверить, что ответ содержит "message"')
    def test_delete_courier_without_id_error(self):
        # отправляем запрос на удаление курьера и сохраняем ответ в переменную response
        response = requests.delete(f'https://qa-scooter.praktikum-services.ru/api/v1/courier/')

        assert 'message' in response.json()

    #если отправить запрос с несуществующим id, вернётся ошибка.
    @allure.title('Проверить, что если отправить запрос с несуществующим id, вернётся ошибка')
    @allure.description('Проверить, что ответ содержит "message"')
    def test_delete_courier_nonexistent_id_error(self):
        # отправляем запрос на удаление курьера и сохраняем ответ в переменную response
        response = requests.delete(f'https://qa-scooter.praktikum-services.ru/api/v1/courier/1')

        assert 'message' in response.json()