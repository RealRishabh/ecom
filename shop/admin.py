from django.contrib import admin
from django.contrib.admin.decorators import display
from .models import products, order
# Register your models here.

admin.site.site_header = 'Dukaan'
admin.site.site_title = '24/7 Dukaan'
admin.site.index_title = 'Manage Dukaan'

class ProductsManage(admin.ModelAdmin):
    list_display = ('title','price','discount_price','category')
    search_fields = ('title','category')
    list_editable = ('price','discount_price')

class OrderManage(admin.ModelAdmin):
    list_display = ('name','items','total')
    search_fields = ('name','email','items')
    

admin.site.register(products,ProductsManage)
admin.site.register(order,OrderManage)