from django.contrib import admin

# Register your models here.
from Order.models import *
admin.site.register(OrderProducts)
admin.site.register(Order)
admin.site.register(Cart)
admin.site.register(CartProducts)
