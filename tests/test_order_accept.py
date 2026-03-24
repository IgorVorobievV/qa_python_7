import allure

from generators import *

class TestAcceptOrder:  

    #успешный запрос возвращает{"ok":true}
    @allure.title('Проверить, что успешный запрос возвращает "ok":true')
    @allure.description('Проверить, что текст ответа "ok":true')
    def test_accept_order_success_request_right_answer(self, order_accept_and_delete):
        
        with allure.step("Получаем данные из фикстуры order_accept_and_delete"):
            id = order_accept_and_delete['id']
            print(f'id {id}')
            courierId = order_accept_and_delete['courierId']
            print(f'courierId {courierId}')

        with allure.step("Отправляем запрос на принятие заказа и сохраняем ответ в переменную response."):
            response = request_order_accept(id, courierId)
        
        with allure.step('Проверка, что текст ответа {"ok":true}.'):
            assert response.text == '{"ok":true}'

    #если не передать id курьера, запрос вернёт ошибку
    @allure.title('Проверить, что если не передать id курьера, запрос вернёт ошибку')
    @allure.description('Проверить, что ответ содержит "message"')
    def test_accept_order_no_courier_id_error(self, order_accept_and_delete):
        
        with allure.step("Получаем данные из фикстуры order_accept_and_delete"):
            id = order_accept_and_delete['id']
            print(f'id {id}')
            courierId = ''
            print(f'courierId {courierId}')

        with allure.step("Отправляем запрос на принятие заказа без id курьера и сохраняем ответ в переменную response."):
            response = request_order_accept(id, courierId)

        with allure.step('Проверка, что возвращается ошибка.'):
            assert 'message' in response.json()

    #если передать неверный id курьера, запрос вернёт ошибку
    @allure.title('Проверить, что если передать неверный id курьера, запрос вернёт ошибку')
    @allure.description('Проверить, что ответ содержит "message"')
    def test_accept_order_wrong_courier_id_error(self, order_accept_and_delete):
        
        with allure.step("Получаем данные из фикстуры order_accept_and_delete"):
            id = order_accept_and_delete['id']
            print(f'id {id}')
            courierId = 1
            print(f'courierId {courierId}')

        with allure.step("Отправляем запрос на принятие заказа c неверным id курьера и сохраняем ответ в переменную response."):
            response = request_order_accept(id, courierId)

        with allure.step('Проверка, что возвращается ошибка.'):
            assert 'message' in response.json()

    #если не передать id заказа, запрос вернёт ошибку
    @allure.title('Проверить, что если не передать id заказа, запрос вернёт ошибку')
    @allure.description('Проверить, что ответ содержит "message"')
    def test_accept_order_no_order_id_error(self, order_accept_and_delete):
        
        with allure.step("Получаем данные из фикстуры order_accept_and_delete"):
            id = ''
            print(f'id {id}')
            courierId = order_accept_and_delete['courierId']
            print(f'courierId {courierId}')

        with allure.step("Отправляем запрос на принятие заказа без id и сохраняем ответ в переменную response."):
            response = request_order_accept(id, courierId)

        with allure.step('Проверка, что возвращается ошибка.'):
            assert 'message' in response.json()

    #если передать неверный id заказа, запрос вернёт ошибку
    @allure.title('Проверить, что если передать неверный id заказа, запрос вернёт ошибку')
    @allure.description('Проверить, что ответ содержит "message"')
    def test_accept_order_wrong_order_id_error(self, order_accept_and_delete):
        
        with allure.step("Получаем данные из фикстуры order_accept_and_delete"):
            id = 1
            print(f'id {id}')
            courierId = order_accept_and_delete['courierId']
            print(f'courierId {courierId}')

        with allure.step("Отправляем запрос на принятие заказа с неверным id заказа и сохраняем ответ в переменную response."):
            response = request_order_accept(id, courierId)

        with allure.step('Проверка, что возвращается ошибка.'):
            assert 'message' in response.json()