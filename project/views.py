from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import status
from .models import Order
from .serializers import OrderSerializer
import redis
import json

#define redis client
redis_client = redis.Redis(host='localhost', port=6379)

#This api gets user id and filters this users orders
#Type = POST
'''
    Requiered Data(s):
      User Id
'''
@api_view(['POST'])
def order_list(request):
    try:
        data = JSONParser().parse(request)
        selectedUser = data['user']
        order = Order.objects.filter(user = selectedUser)
        serializer = OrderSerializer(order, many=True)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)
    except:
        return JsonResponse({"error":"An error occured"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

#This api publishes order to pub/sub server
#Type = POST
'''
    Requiered Data(s):
        User Id
        Food Name
        Category Name
        Restaurant
'''
@api_view(['POST'])
@csrf_exempt
def define_order(request):
    try:
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            redis_client.publish('order', json.dumps(serializer.data))
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        else:
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except:
        return JsonResponse({"error":"An error occured"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

#This api gets order from pub/sub server and write order to database for approve order operation
#Type = POST
'''
    This api doesn't need any data
'''
@api_view(['POST'])
@csrf_exempt
def approve_order(request):
    p = redis_client.pubsub()
    p.subscribe('order')
    while True:
        message = p.get_message()
        if message and not message['data'] == 1:
            message = message['data'].decode('utf-8')
            try:
                serializer = OrderSerializer(data=message)
                if serializer.is_valid():
                    serializer.save()
                    return JsonResponse(serializer.data, status=status.HTTP_200_OK)
                else:
                    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            except:
                return JsonResponse({"error":"An error occured"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
