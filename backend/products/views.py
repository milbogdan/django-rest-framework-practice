from rest_framework import generics

from .models import Product
from .serializers import ProductSerializer

class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class=ProductSerializer

    def perform_create(self,seralizer):
        #seralizer.save(user=self.request.user)
        print(seralizer.validated_data)
        seralizer.save()

product_list_create_view = ProductListCreateAPIView.as_view()

class ProductDetailApiView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class=ProductSerializer

product_detail_view = ProductDetailApiView.as_view()


class ProductListApiView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class=ProductSerializer

product_list_view = ProductListApiView.as_view()

     