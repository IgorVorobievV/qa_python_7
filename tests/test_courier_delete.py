import pytest, allure

from generators import *

class TestDeleteCourier:  

    #неуспешный запрос возвращает соответствующую ошибку
    @allure.title('Проверить, что неуспешный запрос возвращает соответствующую ошибку')
    @allure.description('Проверить, что код ответа 400 при отсутствующем id курьера и 404 при несуществующим id курьера')
    @pytest.mark.parametrize('id, code', [['', 400],[1, 404]])
    def test_delete_courier_wrong_data_right_error(self, id, code):

        with allure.step("Отправляем запрос на удаление курьера и сохраняем ответ в переменную response."):
            response = request_courier_delete(id)

        with allure.step(f"Проверка, что ответ с соответствующим кодом {code}."):
            assert response.status_code == code
        
    #успешный запрос возвращает {"ok":true}
    @allure.title('Проверить, что успешный запрос возвращает "ok":true')
    @allure.description('Проверить, что текст ответа содержит "ok":true')
    def test_delete_courier_success_request_right_answer(self):
        
        with allure.step("Генерируем логин, пароль и имя курьера."):
            payload = generate_courier_data_and_return_payload()

        with allure.step("Отправляем запрос на регистрацию курьера."):
            request_courier_create(payload)
        
        with allure.step("Отправляем запрос на авторизацию созданного курьера и сохраняем id."):
            id = request_courier_login(payload).json()['id']

        with allure.step("Отправляем запрос на удаление курьера и сохраняем ответ в переменную response."):
            response = request_courier_delete(id)

        with allure.step('Проверяем, что текст ответа {"ok":true}'):
            assert response.text == '{"ok":true}'

    #если отправить запрос без id, вернётся ошибка
    @allure.title('Проверить, что если отправить запрос без id, вернётся ошибка')
    @allure.description('Проверить, что ответ содержит "message"')
    def test_delete_courier_without_id_error(self):

        with allure.step("Отправляем запрос на удаление курьера без id и сохраняем ответ в переменную response."):
            response = request_courier_delete('')

        with allure.step("Проверка, что ответ содержит message."):
            assert 'message' in response.json()

    #если отправить запрос с несуществующим id, вернётся ошибка
    @allure.title('Проверить, что если отправить запрос с несуществующим id, вернётся ошибка')
    @allure.description('Проверить, что ответ содержит "message"')
    def test_delete_courier_nonexistent_id_error(self):

        with allure.step("Отправляем запрос на удаление курьера с id=1 и сохраняем ответ в переменную response."):
            response = request_courier_delete(1)

        with allure.step("Проверка, что ответ содержит message."):
            assert 'message' in response.json()