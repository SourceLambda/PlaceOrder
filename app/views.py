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
        if id!=0: # se trae todas las facturas
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
        bill_data["idBill"]=Bill.objects.count()+1
        bill_serializer=BillSerializer(data=bill_data)
        if bill_serializer.is_valid():
            bill_serializer.save()
            temp=json.loads(json.dumps(bill_serializer.data))
            products=json.loads(temp['products'])
            temp['products']=products
            return JsonResponse(temp,safe=False)
        message = bill_serializer.errors
        print(message)
        return JsonResponse("Failed to Add.",safe=False)
    
    elif request.method=='PUT':
        bill_data=JSONParser().parse(request)
        bill=Bill.objects.get(idBill=bill_data['idBill'])
        try:
            for field in bill_data:
                setattr(bill,field,bill_data[field])
            bill.save()
        except Exception as e:
            print(e)
            pass
        #Retornar la factura actualizada
        bill_serializer=BillSerializer(bill)
        temp=json.loads(json.dumps(bill_serializer.data))
        products=json.loads(temp['products'])
        temp['products']=products
        return JsonResponse(temp,safe=False)
    

    elif request.method=='DELETE':
        bill=Bill.objects.get(idBill=id)
        bill.delete()
        str1="Deleted Succefully!, IdBill: !"+str(id)
        return JsonResponse(str1 ,safe=False)
    
def historyApi(request,id):
    if request.method=='GET':
        history = Bill.objects.filter(idCliente=id)
        history_serializer = BillSerializer(history,many=True)
        temp=json.loads(json.dumps(history_serializer.data))
        for bill in temp:
            products=json.loads(bill['products'])
            bill['products']=products
        return JsonResponse(temp,safe=False)
def Calculatetotal(products):
    total=0
    for product in products:
        total=total+product['price']*product['quantity']
    return total

def StrToJSON(str):
    return json.loads(str)
    