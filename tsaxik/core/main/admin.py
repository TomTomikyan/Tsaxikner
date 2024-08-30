# admin.py
from django.contrib import admin
from .models import UserProfile, Category, Product, CartItem, Info, Order, OrderItem, SupportMessage

# Register your models here
admin.site.register(UserProfile)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(CartItem)  # Ensure this is only registered once
admin.site.register(Info)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(SupportMessage)
