from django.contrib import admin
from Product.models import Product,CustomizationType,Commodity,Dimension
# Register your models here.
admin.site.register(Product)
admin.site.register(Commodity)
admin.site.register(Dimension)
admin.site.register(CustomizationType)