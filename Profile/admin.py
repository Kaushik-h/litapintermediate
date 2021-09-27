from django.contrib import admin

# Register your models here.
from django.apps import apps
from Profile.models import Tribe,KYC,Bio

admin.site.register(Tribe)
admin.site.register(KYC)
admin.site.register(Bio)