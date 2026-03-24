import pytest, json, allure

from generators import *
from data_file import *

class TestOrderMake: 
    
    #можно указать один из цветов — BLACK или GREY
    @allure.title('Проверить, что можно указать один из цветов — BLACK или GREY')
    @allure.description('Проверить, что код ответа 201')
    @pytest.mark.parametrize('data', ['BLACK', 'GREY'])
    def test_order_make_one_color_success_order(self, data):
        with allure.step("Указываем цвет в данных заказа."):
            order_valid_data['color'] = []
            order_valid_data['color'].append(data)
        with allure.step("Серилизуем данные заказа."):
            payload = json.dumps(order_valid_data)
        with allure.step("Отправляем запрос на создание заказа и сохраняем ответ в переменную response."):
            response = request_order_make(payload)
        with allure.step("Сохраняем track заказа."):
            track = response.json()['track']
        with allure.step("Отправляем запрос на отмену заказа."):
            request_order_cancel(track)
        with allure.step("Проверка, что код ответа равен 201."):
            assert response.status_code == 201
  
    #можно указать оба цвета
    @allure.title('Проверить, что можно указать оба цвета')
    @allure.description('Проверить, что код ответа 201')
    def test_order_make_two_color_success_order(self):
        with allure.step("Указываем оба цвета в данных заказа."):
            order_valid_data['color'] = ['BLACK', 'GREY']
        with allure.step("Серилизуем данные заказа."):
            payload = json.dumps(order_valid_data)
        with allure.step("Отправляем запрос на создание заказа и сохраняем ответ в переменную response."):
            response = request_order_make(payload)
        with allure.step("Сохраняем track заказа."):
            track = response.json()['track']
        with allure.step("Отправляем запрос на отмену заказа."):
            request_order_cancel(track)
        with allure.step("Проверка, что код ответа равен 201."):
            assert response.status_code == 201
    
    #можно совсем не указывать цвет
    @allure.title('Проверить, что можно совсем не указывать цвет')
    @allure.description('Проверить, что код ответа 201')
    def test_order_make_no_color_success_order(self):
        with allure.step("Очищаем цвет в данных заказа."):
            order_valid_data['color'] = []
        with allure.step("Серилизуем данные заказа."):
            payload = json.dumps(order_valid_data)
        with allure.step("Отправляем запрос на создание заказа и сохраняем ответ в переменную response."):
            response = request_order_make(payload)
        with allure.step("Сохраняем track заказа."):
            track = response.json()['track']
        with allure.step("Отправляем запрос на отмену заказа."):
            request_order_cancel(track)
        with allure.step("Проверка, что код ответа равен 201."):
            assert response.status_code == 201
        
    #тело ответа содержит track
    @allure.title('Проверить, что тело ответа содержит track')
    @allure.description('Проверить, что ответ содержит "track"')
    def test_order_make_valid_order_track(self):
        with allure.step("Серилизуем данные заказа."):
            payload = json.dumps(order_valid_data)
        with allure.step("Отправляем запрос на создание заказа и сохраняем ответ в переменную response."):
            response = request_order_make(payload)
        with allure.step("Сохраняем track заказа."):
            track = response.json()['track']
        with allure.step("Отправляем запрос на отмену заказа."):
            request_order_cancel(track)
        with allure.step("Проверка, что ответ содержит track."):
            assert 'track' in response.text