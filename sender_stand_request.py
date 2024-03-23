import configuration
import requests


# Запрос для создания заказа c заданным телом
def create_order(order_data):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=order_data)


# Запрос на получение информации о заказе по трек-номеру
def get_order_track(track):
    return requests.get(configuration.URL_SERVICE + configuration.ORDER_INFORMATION + str(track))
