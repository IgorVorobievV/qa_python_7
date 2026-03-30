import allure

from generators import *
class TestOrderGetList:
  
    #Проверь, что в тело ответа возвращается список заказов
    @allure.title('Проверить, что в тело ответа возвращается список заказов')
    @allure.description('Проверить, что ответа содержит "orders"')
    def test_order_get_list_valid_order_list_order(self): 

        with allure.step("Отправляем запрос на список заказов и сохраняем ответ в переменную response."):
            response = request_order_get_list()

        with allure.step("Проверка, что ответ содержит orders и имеет код 200."):
            assert response.status_code == 200 and 'orders' in response.text
        