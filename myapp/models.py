from django.db import models
from django.urls import reverse

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=45)

    def __str__(self):
        return self.name

class Category(models.Model):
    title = models.CharField(max_length=45)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('product:product_by_category', args=[self.title])


class Type(models.Model):
    type = models.CharField(max_length=30)


    def __str__(self):
        return self.type


class Product(models.Model):
    model = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    brand = models.ForeignKey(Brand, related_name="models", on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, related_name="types", on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image_1 = models.ImageField(null=True, blank=True ,upload_to="product/1")
    image_2 = models.ImageField(null=True, blank=True ,upload_to="product/2")
    image_3 = models.ImageField(null=True, blank=True ,upload_to="product/3")
    image_4 = models.ImageField(null=True, blank=True ,upload_to="product/4")
    is_feature = models.BooleanField(default=False)
    seller = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.model
    
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('product', arg[str(self.id)])
        
class Size(models.Model):
    size = models.DecimalField(max_digits=3, decimal_places=1)

    def __str__(self):
        return '%s' %(self.size)

class ProductAttribute(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
    size = models.ForeignKey(Size,on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    

    def __str__(self):
        return self.product.model

class ShoeSize(models.Model):
    size = models.DecimalField(max_digits=3, decimal_places=1)
    inventory = models.IntegerField(default=0)
    quantity_sold = models.IntegerField(default=0)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return '%s' %(self.size)

class Cart(models.Model):
    total = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class CartItem(models.Model):
    shoe = models.ForeignKey(ShoeSize, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    cart = models.ForeignKey(Cart,related_name="cart_items",on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now=True)




class Address(models.Model):
    address = models.CharField(max_length=45)
    address2 = models.CharField(max_length=45)
    city = models.CharField(max_length=45)
    state = models.CharField(max_length=2)
    zipcode = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)

class CreditCard(models.Model):
    number = models.IntegerField()
    security_code = models.IntegerField()
    expiration_date = models.DateField()
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    address = models.ForeignKey(Address, related_name="card", on_delete = models.CASCADE)
    user = models.ForeignKey(User, related_name="credit_cards", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)

class Order(models.Model):
    status = models.CharField(max_length=45)
    cart = models.OneToOneField(
        Cart,
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(User,related_name="orders", on_delete=models.CASCADE)
    credit_card = models.ForeignKey(CreditCard,related_name="orders", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)