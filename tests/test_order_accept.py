import allure

from generators import *

class TestAcceptOrder:  

    #успешный запрос возвращает{"ok":true}
    @allure.title('Проверить, что успешный запрос возвращает "ok":true')
    @allure.description('Проверить, что текст ответа "ok":true')
    def test_accept_order_success_request_right_answer(self, order_accept_and_delete):
        
        with allure.step("Получаем данные из фикстуры order_accept_and_delete"):
            id = order_accept_and_delete['id']
            courierId = order_accept_and_delete['courierId']

        with allure.step("Отправляем запрос на принятие заказа и сохраняем ответ в переменную response."):
            response = request_order_accept(id, courierId)
        
        with allure.step('Проверка, что текст ответа {"ok":true}.'):
            assert response.text == '{"ok":true}' and response.status_code == 200

    #если не передать id курьера, запрос вернёт ошибку
    @allure.title('Проверить, что если не передать id курьера, запрос вернёт ошибку')
    @allure.description('Проверить, что ответ содержит "message"')
    def test_accept_order_no_courier_id_error(self, order_accept_and_delete):
        
        with allure.step("Получаем данные из фикстуры order_accept_and_delete"):
            id = order_accept_and_delete['id']
            courierId = ''

        with allure.step("Отправляем запрос на принятие заказа без id курьера и сохраняем ответ в переменную response."):
            response = request_order_accept(id, courierId)
        
        with allure.step('Проверка, что возвращается ошибка.'):
            assert response.text == '{"code":400,"message":"Недостаточно данных для поиска"}'

    #если передать неверный id курьера, запрос вернёт ошибку
    @allure.title('Проверить, что если передать неверный id курьера, запрос вернёт ошибку')
    @allure.description('Проверить, что ответ содержит "message"')
    def test_accept_order_wrong_courier_id_error(self, order_accept_and_delete):
        
        with allure.step("Получаем данные из фикстуры order_accept_and_delete"):
            id = order_accept_and_delete['id']
            courierId = 1

        with allure.step("Отправляем запрос на принятие заказа c неверным id курьера и сохраняем ответ в переменную response."):
            response = request_order_accept(id, courierId)
        
        with allure.step('Проверка, что возвращается ошибка.'):
            assert response.text == '{"code":404,"message":"Курьера с таким id не существует"}'

    #если не передать id заказа, запрос вернёт ошибку
    @allure.title('Проверить, что если не передать id заказа, запрос вернёт ошибку')
    @allure.description('Проверить, что ответ содержит "message"')
    def test_accept_order_no_order_id_error(self, order_accept_and_delete):
        
        with allure.step("Получаем данные из фикстуры order_accept_and_delete"):
            id = ''
            courierId = order_accept_and_delete['courierId']

        with allure.step("Отправляем запрос на принятие заказа без id и сохраняем ответ в переменную response."):
            response = request_order_accept(id, courierId)
        
        with allure.step('Проверка, что возвращается ошибка.'):
            assert response.text == '{"code":404,"message":"Not Found."}'

    #если передать неверный id заказа, запрос вернёт ошибку
    @allure.title('Проверить, что если передать неверный id заказа, запрос вернёт ошибку')
    @allure.description('Проверить, что ответ содержит "message"')
    def test_accept_order_wrong_order_id_error(self, order_accept_and_delete):
        
        with allure.step("Получаем данные из фикстуры order_accept_and_delete"):
            id = 1
            courierId = order_accept_and_delete['courierId']

        with allure.step("Отправляем запрос на принятие заказа с неверным id заказа и сохраняем ответ в переменную response."):
            response = request_order_accept(id, courierId)
        
        with allure.step('Проверка, что возвращается ошибка.'):
            assert response.text == '{"code":404,"message":"Заказа с таким id не существует"}'