import requests, random, string, allure

from curl import *

# метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string

# метод отправки запроса на создание курьера
def request_courier_create(payload):
    with allure.step("Отправляем запрос на регистрацию курьера и возвращаем ответ."):
        return requests.post(COURIER_URL, data=payload)
    
# метод отправки запроса на авторизацию курьера
def request_courier_login(payload):
    with allure.step("Отправляем запрос на авторизацию курьера и возвращаем ответ."):
        return requests.post(f'{COURIER_URL}/login', data=payload)
    
# метод отправки запроса на удаление курьера
def request_courier_delete(id):
    with allure.step("Отправляем запрос на удаление курьера и возвращаем ответ."):
        return requests.delete(f'{COURIER_URL}/{id}')

# метод отправки запроса на создание заказа
def request_order_make(payload):
    with allure.step("Отправляем запрос на создание заказа и возвращаем ответ."):
        return requests.post(ORDER_URL, data=payload)
    
# метод отправки запроса на отмену заказа
def request_order_cancel(track):
    with allure.step("Отправляем запрос на отмену заказа и возвращаем ответ."):
        return requests.put(f'{ORDER_URL}/cancel?track={track}')

# метод отправки запроса на получение списка заказов
def request_order_get_list(id=''):
    with allure.step("Отправляем запрос на получение списка заказов и возвращаем ответ."):
        return requests.get(f'{ORDER_URL}?courierId={id}')
    
# метод отправки запроса на принятие заказа
def request_order_accept(id, courierId):
    with allure.step("Отправляем запрос на принятие заказа и возвращаем ответ."):
        return  requests.put(f'{ORDER_URL}/accept/{id}?courierId={courierId}')




# метод генерации данных курьера возвращает запрос с логином, паролем и именем
def generate_courier_data_and_return_payload():

    with allure.step("Генерируем логин, пароль и имя курьера."):
        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)

    with allure.step("Собираем тело запроса."):
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

    print(payload)
    with allure.step("Возвращаем тело запроса."):
        return payload