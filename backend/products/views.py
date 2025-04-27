from rest_framework import generics

from .models import Product
from .serializers import ProductSerializer

class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class=ProductSerializer

    def perform_create(self,seralizer):
        #seralizer.save(user=self.request.user)
        print(seralizer.validated_data)
        seralizer.save()

product_create_view = ProductCreateAPIView.as_view()

class ProductDetailApiView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class=ProductSerializer

product_detail_view = ProductDetailApiView.as_view()

     