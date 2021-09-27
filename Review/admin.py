from django.contrib import admin

# Register your models here.
from django.apps import apps
from Review.models import Review
admin.site.register(Review)
