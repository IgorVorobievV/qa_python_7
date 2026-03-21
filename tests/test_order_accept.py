import requests, json, allure

from data_file import *

class TestAcceptOrder:  

    #успешный запрос возвращает{"ok":true};
    @allure.title('Проверить, что успешный запрос возвращает "ok":true')
    @allure.description('Проверить, что текст ответа "ok":true')
    def test_accept_order_success_request_right_answer(self, courier_data_gen):
        # серилизуем данные заказа
        payload = json.dumps(order_valid_data)

        # отправляем запрос на создание заказа и сохраняем ответ в переменную response
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/orders', data=payload)
        order_track = response.json()['track']

        # отправляем запрос на получение заказа и сохраняем ответ в переменную response
        response = requests.get(f'https://qa-scooter.praktikum-services.ru/api/v1/orders/track?t={order_track}')
        order_id = response.json()['order']['id']

        # отправляем запрос на регистрацию курьера
        requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=courier_data_gen)

        # отправляем запрос на вход курьера и сохраняем ответ в переменную response
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', data=courier_data_gen)
        # получаем id созданного курьера
        courier_id = response.json()['id']

        # отправляем запрос на принятие заказа и сохраняем ответ в переменную response
        response = requests.put(f'https://qa-scooter.praktikum-services.ru/api/v1/orders/accept/{order_id}?courierId={courier_id}')

        # удаление тестовых данных (отправляем запрос на отмену заказа)
        requests.put(f'https://qa-scooter.praktikum-services.ru//api/v1/orders/cancel?track={order_track}')

        # удаление тестовых данных (отправляем запрос на удаление курьера)
        requests.delete(f'https://qa-scooter.praktikum-services.ru/api/v1/courier/{courier_id}')  

        assert response.text == '{"ok":true}'



    #если не передать id курьера, запрос вернёт ошибку;
    @allure.title('Проверить, что если не передать id курьера, запрос вернёт ошибку')
    @allure.description('Проверить, что ответ содержит "message"')
    def test_accept_order_no_courier_id_error(self):
        # серилизуем данные заказа
        payload = json.dumps(order_valid_data)
        
        # отправляем запрос на создание заказа и сохраняем ответ в переменную response
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/orders', data=payload)
        order_track = response.json()['track']

        # отправляем запрос на получение заказа и сохраняем ответ в переменную response
        response = requests.get(f'https://qa-scooter.praktikum-services.ru/api/v1/orders/track?t={order_track}')
        order_id = response.json()['order']['id']      

        # отправляем запрос на принятие заказа и сохраняем ответ в переменную response
        response = requests.put(f'https://qa-scooter.praktikum-services.ru/api/v1/orders/accept/{order_id}')

        # удаление тестовых данных (отправляем запрос на отмену заказа)
        requests.put(f'https://qa-scooter.praktikum-services.ru//api/v1/orders/cancel?track={order_track}')

        assert 'message' in response.json()

    #если передать неверный id курьера, запрос вернёт ошибку;
    @allure.title('Проверить, что если передать неверный id курьера, запрос вернёт ошибку')
    @allure.description('Проверить, что ответ содержит "message"')
    def test_accept_order_wrong_courier_id_error(self):
        # серилизуем данные заказа
        payload = json.dumps(order_valid_data)
        
        # отправляем запрос на создание заказа и сохраняем ответ в переменную response
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/orders', data=payload)
        order_track = response.json()['track']

        # отправляем запрос на получение заказа и сохраняем ответ в переменную response
        response = requests.get(f'https://qa-scooter.praktikum-services.ru/api/v1/orders/track?t={order_track}')
        order_id = response.json()['order']['id']      

        # отправляем запрос на принятие заказа и сохраняем ответ в переменную response
        response = requests.put(f'https://qa-scooter.praktikum-services.ru/api/v1/orders/accept/{order_id}?courierId=1')

        # удаление тестовых данных (отправляем запрос на отмену заказа)
        requests.put(f'https://qa-scooter.praktikum-services.ru//api/v1/orders/cancel?track={order_track}')

        assert 'message' in response.json()

    #если не передать id заказа, запрос вернёт ошибку;
    @allure.title('Проверить, что если не передать id заказа, запрос вернёт ошибку')
    @allure.description('Проверить, что ответ содержит "message"')
    def test_accept_order_no_order_id_error(self, courier_data_gen):
        # отправляем запрос на регистрацию курьера
        requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=courier_data_gen)

        # отправляем запрос на вход курьера и сохраняем ответ в переменную response
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', data=courier_data_gen)
        # получаем id созданного курьера
        courier_id = response.json()['id'] 

        # отправляем запрос на принятие заказа и сохраняем ответ в переменную response
        response = requests.put(f'https://qa-scooter.praktikum-services.ru/api/v1/orders/accept/?courierId={courier_id}')

        # удаление тестовых данных (отправляем запрос на удаление курьера)
        requests.delete(f'https://qa-scooter.praktikum-services.ru/api/v1/courier/{courier_id}') 

        assert 'message' in response.json()

    #если передать неверный id заказа, запрос вернёт ошибку.
    @allure.title('Проверить, что если передать неверный id заказа, запрос вернёт ошибку')
    @allure.description('Проверить, что ответ содержит "message"')
    def test_accept_order_wrong_order_id_error(self, courier_data_gen):
        # отправляем запрос на регистрацию курьера
        requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=courier_data_gen)

        # отправляем запрос на вход курьера и сохраняем ответ в переменную response
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', data=courier_data_gen)
        # получаем id созданного курьера
        courier_id = response.json()['id'] 

        # отправляем запрос на принятие заказа и сохраняем ответ в переменную response
        response = requests.put(f'https://qa-scooter.praktikum-services.ru/api/v1/orders/accept/1?courierId={courier_id}')

        # удаление тестовых данных (отправляем запрос на удаление курьера)
        requests.delete(f'https://qa-scooter.praktikum-services.ru/api/v1/courier/{courier_id}') 

        assert 'message' in response.json()