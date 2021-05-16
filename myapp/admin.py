from django.contrib import admin
from .models import *
# Register your models here.
class BrandAdmin(admin.ModelAdmin):
    list_display=['name']
    

admin.site.register(Brand,BrandAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display=['id','title']

admin.site.register(Category,CategoryAdmin)


class TypeAdmin(admin.ModelAdmin):
    list_display=['type']

admin.site.register(Type,TypeAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display=['id','model','brand','price','type','category','seller','is_feature']
    list_editable=['price','model','seller','is_feature']
    list_filter=['brand','type','category']

admin.site.register(Product,ProductAdmin)

class SizeAdmin(admin.ModelAdmin):
    list_display=['size']



admin.site.register(Size,SizeAdmin)


class ProductAttributeAdmin(admin.ModelAdmin):
    list_display=['id','product','brand','size','type','price']

admin.site.register(ProductAttribute,ProductAttributeAdmin)

class ShoeSizeAdmin(admin.ModelAdmin):
    list_display=['size','inventory','quantity_sold','product']
    list_editable=['inventory','quantity_sold']

admin.site.register(ShoeSize,ShoeSizeAdmin)

class CartAdmin(admin.ModelAdmin):
    list_display=['total','created_at','updated_at']

admin.site.register(Cart,CartAdmin)

class CartItemAdmin(admin.ModelAdmin):
    list_display=['shoe','quantity','cart','created_at','updated_at']

admin.site.register(CartItem,CartItemAdmin)

class AddressAdmin(admin.ModelAdmin):
    list_display=['address','address2','city','state','zipcode','created_at','updated_at']

admin.site.register(Address,AddressAdmin)

class UserAdmin(admin.ModelAdmin):
    list_display=['first_name','last_name','email','created_at','updated_at']

admin.site.register(User,UserAdmin)

class CreditCartAdmin(admin.ModelAdmin):
    list_display=['number','first_name','last_name','user','created_at','updated_at']

admin.site.register(CreditCard,CreditCartAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display=['status','cart','user','credit_card','created_at','updated_at']

admin.site.register(Order,OrderAdmin)
