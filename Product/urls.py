from django.urls import path
from django.conf.urls import url
from Product.views import *

urlpatterns = [
    
     path('product',ProductAPIView.as_view()),
     path('product/<pk>',ProductDetailAPIView.as_view()),
     path('products',ProductListAPIView.as_view()),
     path('products/<tribeleaderId>',TribeProductListAPIView.as_view()),
     path('products/productlist/tribelist',TribesProductListAPIView.as_view()),
     path('products/productlist/lastupdated',ProductListAPIView.as_view()),
     path('commodities/tribe/<tribeleaderId>',TribesCommodityListAPIView.as_view()),
     path('commodities/brand/<brandId>',BrandCommodityListAPIView.as_view()),


]