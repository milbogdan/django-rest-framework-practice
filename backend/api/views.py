from django.shortcuts import render
from django.http import JsonResponse
import json
from products.models import Product
from django.forms.models import model_to_dict

from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializers import ProductSerializer
# Create your views here.




@api_view(['POST'])
def api_home(request, *args, **kwargs):

    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        instance=serializer.save()
        print(serializer.data)
        return Response(serializer.data)






# @api_view(["GET"])
# def api_home(request, *args, **kwargs):
#     instance = Product.objects.all().order_by("?").first()
#     data={}
#     if instance:
#         # data['id']=model_data.id
#         # data['title']=model_data.title
#         # data['content']=model_data.content
#         # data['price']=model_data.price

#         #serialization
#         #data=model_to_dict(instance,fields=['id','title','price','sale_price'])
#         data=ProductSerializer(instance).data
#     return JsonResponse(data)







# def api_home(request, *args, **kwargs):
#     print(request.GET) #print url query parameters
#     body = request.body #byte string of json data
#     data = {}
#     try:
#         data=json.loads(body) #string of json data to python dictionary
#     except:
#         pass
#     print(data)
#     data['parms']=dict(request.GET)
#     data['headers']=dict(request.headers)
#     data['content_type']=request.content_type
#     return JsonResponse(data)

