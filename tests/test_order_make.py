import requests, pytest, json, allure

from data_file import *

class TestOrderMake: 
    
    #можно указать один из цветов — BLACK или GREY;
    @allure.title('Проверить, что можно указать один из цветов — BLACK или GREY')
    @allure.description('Проверить, что код ответа 201')
    @pytest.mark.parametrize('data', ['BLACK', 'GREY'])
    def test_order_make_one_color_success_order(self, data):
        # указываем цвет в данных заказа
        order_valid_data['color'] = []
        order_valid_data['color'].append(data)
        # серилизуем данные заказа
        payload = json.dumps(order_valid_data)

        # отправляем запрос на создание заказа и сохраняем ответ в переменную response
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/orders', data=payload)
        order_track = response.json()['track']

        # удаление тестовых данных (отправляем запрос на отмену заказа)
        requests.put(f'https://qa-scooter.praktikum-services.ru//api/v1/orders/cancel?track={order_track}')

        assert response.status_code == 201
  
    #можно указать оба цвета;
    @allure.title('Проверить, что можно указать оба цвета')
    @allure.description('Проверить, что код ответа 201')
    def test_order_make_two_color_success_order(self):
        # указываем оба цвета в данных заказа
        order_valid_data['color'] = ['BLACK', 'GREY']
        # серилизуем данные заказа
        payload = json.dumps(order_valid_data)

        # отправляем запрос на создание заказа и сохраняем ответ в переменную response
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/orders', data=payload)
        order_track = response.json()['track']

        # удаление тестовых данных (отправляем запрос на отмену заказа)
        requests.put(f'https://qa-scooter.praktikum-services.ru//api/v1/orders/cancel?track={order_track}')

        assert response.status_code == 201
    
    #можно совсем не указывать цвет;
    @allure.title('Проверить, что можно совсем не указывать цвет')
    @allure.description('Проверить, что код ответа 201')
    def test_order_make_no_color_success_order(self):
        # передаем данные заказа без цвета
        order_valid_data['color'] = []
        # серилизуем данные заказа
        payload = json.dumps(order_valid_data)

        # отправляем запрос на создание заказа и сохраняем ответ в переменную response
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/orders', data=payload)
        order_track = response.json()['track']

        # удаление тестовых данных (отправляем запрос на отмену заказа)
        requests.put(f'https://qa-scooter.praktikum-services.ru//api/v1/orders/cancel?track={order_track}')

        assert response.status_code == 201
        
    #тело ответа содержит track.
    @allure.title('Проверить, что тело ответа содержит track')
    @allure.description('Проверить, что ответ содержит "track"')
    def test_order_make_valid_order_track(self):
        # серилизуем данные заказа
        payload = json.dumps(order_valid_data)

        # отправляем запрос на создание заказа и сохраняем ответ в переменную response
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/orders', data=payload)
        order_track = response.json()['track']

        # удаление тестовых данных (отправляем запрос на отмену заказа)
        requests.put(f'https://qa-scooter.praktikum-services.ru//api/v1/orders/cancel?track={order_track}')

        assert 'track' in response.text