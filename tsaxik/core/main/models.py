from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='profile_pics/', null=True, blank=True)

class Category(models.Model):
    name = models.CharField('Cat name', max_length=25)

    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    name = models.CharField('Prod name', max_length=50)
    img = models.ImageField('Prod img', upload_to='products/')
    price = models.DecimalField('Price', max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return self.name
    
class Info(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='info')
    img = models.ImageField('Img info', upload_to='info/')
    name = models.CharField('Name info', max_length=50)
    text = models.TextField('Text info')
    price = models.DecimalField('Price', max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return self.name


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product.name} ({self.quantity})"
    
    @property
    def total_price(self):
        return self.quantity * self.product.price

    def __str__(self):
        return f"{self.quantity} of {self.product.name}"

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cart')

    @property
    def total_sum(self):
        return sum(item.total_price for item in self.cart_items.all())

    def __str__(self):
        return f"Cart of {self.user.username}"

class SupportMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject
    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"Order {self.id} by {self.user.username}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"