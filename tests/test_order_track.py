import requests, json, allure

from data_file import *

class TestTrackOrder:  

    # успешный запрос возвращает объект с заказом;
    @allure.title('Проверить, что успешный запрос возвращает объект с заказом')
    @allure.description('Проверить, что ответ содержит "order"')
    def test_track_order_success_request_order(self):
        # серилизуем данные заказа
        with allure.step("Серилизуем данные заказа."):
            payload = json.dumps(order_valid_data)

        # отправляем запрос на создание заказа и сохраняем ответ в переменную response
        with allure.step("Отправляем запрос на создание заказа и сохраняем ответ в переменную response."):
            response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/orders', data=payload)
        with allure.step("Сохраняем track заказа."):
            order_track = response.json()['track']

        # отправляем запрос на получение заказа и сохраняем ответ в переменную response
        with allure.step("Отправляем запрос на получение заказа и сохраняем ответ в переменную response."):
            response = requests.get(f'https://qa-scooter.praktikum-services.ru/api/v1/orders/track?t={order_track}')

        # удаление тестовых данных (отправляем запрос на отмену заказа)
        with allure.step("Отправляем запрос на отмену заказа."):
            requests.put(f'https://qa-scooter.praktikum-services.ru//api/v1/orders/cancel?track={order_track}')
        with allure.step('Проверка, что в ответе есть order.'):
            assert 'order' in response.json()

    # запрос без номера заказа возвращает ошибку;
    @allure.title('Проверить, что запрос без номера заказа возвращает ошибку')
    @allure.description('Проверить, что ответ содержит "message"')
    def test_track_order_without_track_error(self):
        # отправляем запрос на получение заказа и сохраняем ответ в переменную response
        with allure.step("Отправляем запрос на получение заказа без трека и сохраняем ответ в переменную response."):
            response = requests.get(f'https://qa-scooter.praktikum-services.ru/api/v1/orders/track?t=')
        with allure.step('Проверка, что возвращается ошибка.'):
            assert 'message' in response.json()

    # запрос с несуществующим заказом возвращает ошибку.
    @allure.title('Проверить, что запрос с несуществующим заказом возвращает ошибку')
    @allure.description('Проверить, что ответ содержит "message"')
    def test_track_order_wrong_track_error(self):
        # отправляем запрос на получение заказа и сохраняем ответ в переменную response
        with allure.step("Отправляем запрос на получение заказа с треком 1 и сохраняем ответ в переменную response."):
            response = requests.get(f'https://qa-scooter.praktikum-services.ru/api/v1/orders/track?t=1')
        with allure.step('Проверка, что возвращается ошибка.'):
            assert 'message' in response.json()