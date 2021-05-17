from . import views
from django.contrib import admin
from django.urls import path, include,re_path
from django.conf.urls import url
from myapp import views

urlpatterns = [
    path('', views.homey, name ="homey"),
	path('product/<int:shoe_id>', views.shoe_page, name="productt"),
    path('search', views.search,name="search"),
    path('product_list/<int:cat_id>', views.product_list,name="product_list"),
    path('product_list_type/<int:type_id>', views.product_list_type,name="product_list_type"),
    path('product_list_cat_type/<int:cat_id>/<int:type_id>', views.product_list_cat_type,name="product_list_cat_type"),
    path('brand_list/<int:bra_id>', views.brand_list,name="brand_list"),
    path('checkout/', views.checkout, name="checkout"),
    path('confirm/', views.confirm, name="confirm"),
    path('cart/', views.cart, name="cart"),
    path('add_to_cart/', views.add_to_cart, name="add_to_cart"),    
   
    path('about/', views.about, name="about"),
    path('help/', views.help, name="help"),
    path('sell/', views.sell, name="sell"),

    path('NewArrival/', views.new_arrival, name="NewArrival"),
    path('NewArrival_01/', views.new_arrival01, name="new_arrival01"),
    path('NewArrival_02/', views.new_arrival02, name="new_arrival02"),

    path('checkout_process_guest', views.checkout_process_guest),

    path('oauth/', include('social_django.urls', namespace='social')),
]

