from rest_framework import generics,mixins,permissions,authentication
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import AllowAny,IsAdminUser

from django.shortcuts import get_object_or_404

from .models import Product
from .serializers import ProductSerializer

from api.mixins import (StaffEditorPermissionMixin,UserQuerySetMixin)

class ProductListCreateAPIView(UserQuerySetMixin,StaffEditorPermissionMixin,generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class=ProductSerializer
    allow_staff_view = False
    def perform_create(self,serializer):
        #seralizer.save(user=self.request.user)
        #print(seralizer.validated_data)
        title=serializer.validated_data.get('title')
        content=serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(user=self.request.user,content=content)

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAdminUser()]
        return [AllowAny()]

    # def get_queryset(self,*args,**kwargs):
    #     qs=super().get_queryset(*args,**kwargs)
    #     request=self.request
    #     user = request.user
    #     if not user.is_authenticated:
    #         return Product.objects.none()
    #     print(request.user)
    #     return qs.filter(user=request.user)

product_list_create_view = ProductListCreateAPIView.as_view()



class ProductDetailApiView(UserQuerySetMixin,StaffEditorPermissionMixin,generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class=ProductSerializer

product_detail_view = ProductDetailApiView.as_view()


class ProductUpdateApiView(UserQuerySetMixin,StaffEditorPermissionMixin,generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class=ProductSerializer
    lookup_field='pk'

    def perform_update(self, serializer):
        instance=serializer.save()
        if not instance.content:
            instance.content=instance.title
    
product_update_view = ProductUpdateApiView.as_view()



class ProductDestroyAPIView(StaffEditorPermissionMixin,generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class=ProductSerializer
    lookup_field='pk'

    def perform_destroy(self, instance):
        super().perform_destroy(instance)
    
product_destroy_view = ProductDestroyAPIView.as_view()


# class ProductListApiView(generics.ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class=ProductSerializer

# product_list_view = ProductListApiView.as_view()



# @api_view(['GET','POST'])
# def product_ali_view(request, pk=None, *args, **kwargs):
#     method = request.method

#     if method == "GET":
#         if pk is not None:
#             #detail view
#             obj = get_object_or_404(Product,pk=pk)
#             data=ProductSerializer(obj,many=False).data
#             return Response(data)
#         else:
#             #list view
#             queryset = Product.objects.all()
#             data= ProductSerializer(queryset,many=True).data
#             return Response(data)

#     if method == "POST":
#         serializer = ProductSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             title=serializer.validated_data.get('title')
#             content=serializer.validated_data.get('content') or None
#             if content is None:
#                 content = title
#             serializer.save(content=content)
#             return Response(serializer.data)
#         return Response(serializer.data)




# class ProductMixinView(mixins.CreateModelMixin,mixins.ListModelMixin,mixins.RetrieveModelMixin,generics.GenericAPIView):
#     queryset= Product.objects.all()
#     serializer_class=ProductSerializer
#     lookup_field='pk'


#     def get(self,request,*args,**kwargs):
#         pk=kwargs.get("pk")
#         if pk is not None:
#             return self.retrieve(request,*args,**kwargs)
#         return self.list(request,*args,**kwargs)


#     def post(self,request,*args,**kwargs):
#         return self.create(request,*args,**kwargs)

# product_mixin_view = ProductMixinView.as_view()