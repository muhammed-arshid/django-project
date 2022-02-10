# from itertools import product
# import re   
# from urllib import response
from django.http import JsonResponse
# from django.views.generic.detail import DetailView
# from django.views.generic.list import ListView
from .models import Manufacture,Producet


def producet_list(request):

    producets = Producet.objects.all()
    data = {"producet":list(producets.values())}
    responce = JsonResponse(data)
    return responce




def producet_deatail(request,pk):
    try:
        producet = Producet.objects.get(pk=pk)

        data = {"producet":{
            "name" : producet.name,
            "manufracturer":producet.manufacture.name,
            "description":producet.description,
            "photo": producet.photo.url,
            "price":producet.price,
            "shipping_cost":producet.shipping_cost,
            "quantity":producet.quantity,
            }}
        response = JsonResponse(data)
    except Producet.DoesNotExist:
        response = JsonResponse({
            "error":{
                    "code": 404,
                    "message":"Producet Does Not exist...!",
                    }},status= 404)
    return response
# class producetDeatails(DetailView):
#     model = Producet
#     template_name = 'producet\prodect_deatils.html'


# class productlist(ListView):
#     model = Producet
#     template_name = 'producet\product_list.html'


def manufractures_deatails(request,pk):
    man =  Manufacture.objects.get(pk=pk)
    data  = {"deatails":{
        "name":man.name,
        "location":man.location,
        "products":list(k['name'] for k in Producet.objects.filter(manufacture=pk).values("name"))
    } }
    response = JsonResponse(data)
    return response

def active_manufracture(request):
    data = {"active_manufractures":list(k["name"]  for k in  Manufacture.objects.filter(active=True).values("name"))}
    return JsonResponse(data)
    








