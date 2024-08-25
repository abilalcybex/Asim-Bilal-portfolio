from django.contrib import admin
from .models import Supplier, Product, Inventory, Customer, Order, Production

admin.site.register(Supplier)
admin.site.register(Product)
admin.site.register(Inventory)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Production)
