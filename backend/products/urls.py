from django.urls import path
from . import views

urlpatterns=[
   # path('<int:pk>/',views.product_detail_view),
    path('<int:pk>/',views.product_ali_view),
   # path('',views.product_list_create_view),
    path('',views.product_ali_view),
    #path('list/',views.product_list_view),
]