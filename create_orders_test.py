import sender_stand_request
import data


# Михаил Евсеев, 14 когорта, Авто-Тест на создание заказа и получение заказа по треку с помощью API Яндекс Самокат.
def test_get_order_track():
    track = sender_stand_request.create_order(data.order_data).json()['track']
    response = sender_stand_request.get_order_track(track)
    assert response.status_code == 200
