from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Orders
from .serializers import OrderSerializer
import json, midtransclient, hashlib

# Create your views here.
def midtrans(data_order):
    snap = midtransclient.Snap(
        is_production=False,
        server_key=settings.MIDTRANS_SERVER_KEY,
        client_key=settings.MIDTRANS_CLIENT_KEY
    )

    param = {
        "transaction_details": {
            "order_id": f"{data_order['order_id']}",
            "gross_amount": data_order['price']
        }, 
        "item_details": [{
            "price": data_order['price'],
            "quantity": data_order['qty'],
            "name": f"{data_order['product']}",
        }],
        "customer_details": {
            "name": f"{data_order['customer_name']}",
            "email": f"{data_order['email']}",
            "billing_address": {
                "address": f"{data_order['address']}",
            }   
        },
    }

    # create transaction
    transaction = snap.create_transaction(param)

    # transaction redirect url
    transaction_redirect_url = transaction['redirect_url']
    return transaction_redirect_url

@api_view(['POST'])
def orders(request):
    if request.method == 'POST':
        response = json.loads(request.body)
        serializer = OrderSerializer(data=response)
        if serializer.is_valid():
            order = serializer.save()

            data_serializer = OrderSerializer(order).data
            url_midtrans = midtrans(data_serializer)
            response_data = data_serializer
            response_data['url_midtrans'] = url_midtrans

            return Response(response_data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def midtrans_notification(request):
    response = json.loads(request.body)
    order = Orders.objects.get(order_id=response['order_id'])

    # -------------------------------------------------------------------------------
    # Cek Signature
    credential = f"{response['order_id']}{response['status_code']}{response['gross_amount']}{settings.MIDTRANS_SERVER_KEY}"
    sha512 = hashlib.sha512()
    sha512.update(credential.encode('utf-8'))
    signature = sha512.hexdigest()
    # -------------------------------------------------------------------------------


    # -------------------------------------------------------------------------------
    def update_status(order, status_payment):
        status_update = {'status': f'{status_payment}'}
        serializer = OrderSerializer(order, data=status_update, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    # -------------------------------------------------------------------------------


    # -------------------------------------------------------------------------------
    if(response['signature_key'] == signature):
        if(response['transaction_status'] == 'settlement' or response['transaction_status'] == 'capture'):
            if(response['fraud_status'] == 'accept'):
                update_status(order, 'PAID')
    
    # -------------------------------------------------------------------------------
    return HttpResponse()

