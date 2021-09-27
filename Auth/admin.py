from django.contrib import admin
from django.apps import apps
from Auth.models import User,CallbackToken

admin.site.register(User)
admin.site.register(CallbackToken)
