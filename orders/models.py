from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Menu(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField(blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return self.name
class Order(models.Model):
    STATUS_CHOICES=[('PENDING','pending'),
    ('PROCESSING','processing'),('COMPLETED','completed'),('CANCELLED','cancelled'),]
    customer=models.ForeignKey(User,on_delete=models.CASCADE,related_name='orders')
    total_amount=models.DecimalField(max_digits=10,decimal_places=2)
    status=models.CharField(max_length=100,choices=STATUS_CHOICES,default='pending')
    created_at=models.DataTimeField(auto_now_add=True)
  


    def __str__(self):
        return f"Order# {self.id} By {self.customer.username}"


class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE,related_name='items')
    menu_item=models.ForeignKey(Menu,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    price=models.DecimalField(max_digits=10,decimal_places=2)


    def __str__(self):
        return f"{self.quantity} X {self.menu_item.name} "


    def get_total_amount(self):
        return self.quantity * self.menu_item.price

