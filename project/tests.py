from rest_framework.test import APIRequestFactory
import json

factory = APIRequestFactory()

def test_get_orders_api(request):
    data = {"user": 3 }  
    request = factory.post('/get_orders/', json.dumps(data), content_type='application/json')
    print(request)


def test_define_order(request):
    data = { "user": 3, "foodName": "Döner", "categoryName": "Döner/Kebap", "restaurant":"Süper Dönerci" }
    request = factory.post('/define_order/', json.dumps(data), content_type='application/json')
    print(request)

def test_approve_order(request):
    data = { }
    request = factory.post('/approve_order/', json.dumps(data), content_type='application/json')
    print(request)