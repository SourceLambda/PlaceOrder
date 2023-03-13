import json
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework import status
from app.models import Bill
from app.serializers import BillSerializer



# Create your views here.
@csrf_exempt
def billApi(request,id=0):
    if request.method=='GET':
        if id!=0:
            bills = Bill.objects.get(idBill=id)
            bills_serializer = BillSerializer(bills)
            temp=json.loads(json.dumps(bills_serializer.data))
            products=json.loads(temp['products'])
            temp['products']=products
        else:
            bills = Bill.objects.all()
            bills_serializer = BillSerializer(bills,many=True)

            temp=json.loads(json.dumps(bills_serializer.data))
            for bill in temp:
                products=json.loads(bill['products'])
                bill['products']=products
        return JsonResponse(temp,safe=False)
    elif request.method=='POST':
        bill_data=JSONParser().parse(request)
        total=Calculatetotal(bill_data['products'])
        bill_data['total']=total
        bill_serializer=BillSerializer(data=bill_data)
        if bill_serializer.is_valid():
            bill_serializer.save()
            return JsonResponse("Added Successfully!!",safe=False)
        message = bill_serializer.errors
        print(message)
        return JsonResponse("Failed to Add.",safe=False)
    elif request.method=='PUT':
        bill_data=JSONParser().parse(request)
        bill=Bill.objects.get(_id=bill_data['idBill'])
        bill_serializer=BillSerializer(bill,data=bill_data)
        if bill_serializer.is_valid():
            bill_serializer.save()
            return JsonResponse("Updated Successfully!!",safe=False)
        return JsonResponse("Failed to Update.",safe=False)
    elif request.method=='DELETE':
        bill=Bill.objects.get(_id=id)
        bill.delete()
        return JsonResponse("Deleted Succefully!!",safe=False)
    
def Calculatetotal(products):
    total=0
    for product in products:
        total=total+product['price']*product['quantity']
    return total
    