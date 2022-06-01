from django.urls import path

from mainapp.views import products, products_list
from django.conf.urls import include

app_name = 'products'

urlpatterns = [
    path('products/', include('mainapp.urls', namespace='products')),
    path('<int:pk>/', products_list, name='product_list'),
    path('auth/', include('authapp.urls', namespace='auth'))

]
