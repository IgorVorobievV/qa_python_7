import requests, allure

class TestOrderGetList:
  
    #Проверь, что в тело ответа возвращается список заказов.
    @allure.title('Проверить, что в тело ответа возвращается список заказов')
    @allure.description('Проверить, что ответа содержит "orders"')
    def test_order_get_list_valid_order_list_order(self): 
        # отправляем запрос на список заказов с лимитом выдачи 3 и сохраняем ответ в переменную response
        response = requests.get(f'https://qa-scooter.praktikum-services.ru/api/v1/orders?limit=3')

        assert 'orders' in response.json()
        