import pytest, allure, requests, json

from generators import *
from curl import *
from data_file import *

@pytest.fixture # фикстура, которая генерирует данные курьера и удаляет курьера после теста
def courier_create_and_delete():

    with allure.step("Генерируем логин, пароль и имя курьера."):
        payload = generate_courier_data_and_return_payload()

    with allure.step("Передаем тело запроса в тест."): 
        yield payload

    try:
        with allure.step("Отпраляем запрос на авторизацию курьера и извлекаем id."):
            id = request_courier_login(payload).json()['id']

        with allure.step("Отпраляем запрос на удаление курьера."):
            request_courier_delete(id)

    except Exception as e:
        print(f"Ошибка при очистке тестовых данных: {e}")


@pytest.fixture # 
def order_accept_and_delete():

    with allure.step("Создаем пустой словарь для передачи данных в тест."):
        result = dict()

    with allure.step("Серилизуем данные заказа."):
        payload = json.dumps(order_valid_data)
        
    with allure.step("Отправляем запрос на создание заказа и сохраняем ответ в переменную response."):
        response = request_order_make(payload)

    with allure.step("Сохраняем track заказа."):
        order_track = response.json()['track']
        
    with allure.step("Отправляем запрос на получение заказа и сохраняем ответ в переменную response."):
        response = requests.get(f'{ORDER_URL}/track?t={order_track}')

    with allure.step("Сохраняем id заказа."):
        result['id'] = response.json()['order']['id']
    
    with allure.step("Генерируем логин, пароль и имя курьера."):
        payload = generate_courier_data_and_return_payload()

    with allure.step("Отправляем запрос на регистрацию курьера."):
        requests.post(COURIER_URL, data=payload)   
        
    with allure.step("Отправляем запрос на вход курьера и сохраняем ответ в переменную response."):
        response = request_courier_login(payload)
        
    # получаем id созданного курьера
    with allure.step("Сохраняем id курьера."):
        result['courierId'] = response.json()['id']

    with allure.step(f"Передаем result {result} в тест."):
        yield result

    try:
        with allure.step("Отправляем запрос на отмену заказа."):
            request_order_cancel(result['id'])

        with allure.step("Отпраляем запрос на удаление курьера."):
            request_courier_delete(result['courierId'])

    except Exception as e:
        print(f"Ошибка при очистке тестовых данных: {e}")