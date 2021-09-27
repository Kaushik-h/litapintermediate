from django.contrib import admin
from django.urls import path,include,re_path
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/authservice/', include('Auth.urls')),
    path('api/profileservice/', include('Profile.urls')),
    path('api/brandservice/', include('Brand.urls')),
    path('api/reviewservice/', include('Review.urls')),
    path('api/productservice/', include('Product.urls')),
    path('api/endorsementservice/', include('Endorsement.urls')),
    path('api/feedservice/', include('Feed.urls')),
    path('api/orderservice/', include('Order.urls')),
    path('api/eventservice/', include('Event.urls')),
    path('api/locationservice/', include('Location.urls')),
    path('api/mediaservice/', include('Media.urls')),
    path('api/mediacollectionservice/', include('MediaCollection.urls')),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT})]