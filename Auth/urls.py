from django.urls import path
from django.conf.urls import url
from Auth.views import *

urlpatterns = [
    
     path('signup',RegisterAPIView.as_view()),
     path('set_password', PasswordResetVerifyView.as_view()),
     path('login',LoginAPIView.as_view()),
     path('logout', LogoutView.as_view()),
     path('forget_all_devices', LogoutAllView.as_view()),
     path('change_password', PasswordchangeView.as_view()),
     path('reset_password_request', PasswordResetRequestView.as_view()),
     path('reset_password', PasswordResetVerifyView.as_view())

]