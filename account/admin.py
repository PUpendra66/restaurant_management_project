from django.contrib import admin

# Register your models here.
from .models import Menu,Order
@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display=('name','price')
    search_fields=('name',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display=('id','customer','status','total_amount','created_at')
    list_filter=('status',)
    search_fields=('customer__username',)
    filter_horizontal=('items',)
