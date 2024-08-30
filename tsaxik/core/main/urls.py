# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='Login'),
    path('register/', views.register, name='Register'),
    path('home/', views.home, name='Home'),
    path('home/product/', views.product_list, name='Product'),
    path('home/product/<int:id>/', views.product_detail, name='ProductDetail'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='AddToCart'),
    path('cart/', views.view_cart, name='Cart'),
    path('checkout/', views.checkout, name='Checkout'),
    path('profile/', views.profile, name='Profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('info/<int:id>/', views.info_view, name='ProductInfo'),
    path('support/', views.support, name='Support'),
    path('support/success/', views.support_success, name='SupportSuccess'),
    path('order/success/', views.order_success, name='OrderSuccess'), 
]
