from django.db import models
from django.contrib.auth.models import User
# 
# contact
# 

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    number = models.CharField(max_length=255)
    message = models.TextField()


class Contact_address(models.Model):
    link = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.EmailField()
    work_day = models.CharField(max_length=255)

# 
# CONTACT INFO
# 

class Contact_info(models.Model):
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.EmailField()
    work_day = models.CharField(max_length=255)

# 
# All Items
# 

class All_Items(models.Model):
    logo = models.ImageField()
    number = models.CharField(max_length=255)

#
# FEATURED PRODUCTS
# 


class New_Arrivals(models.Model):
    img1 = models.ImageField(upload_to='image')
    img2 = models.ImageField(upload_to='image')
    img3 = models.ImageField(upload_to='image')
    img4 = models.ImageField(upload_to='image')
    name = models.CharField(max_length=255)
    catergory_name = models.CharField(max_length=255)
    narx = models.IntegerField()
    reting = models.IntegerField()
    discriptions = models.TextField()
    productId = models.IntegerField()
    delivery = models.CharField(max_length=255)


class Category(models.Model):
    img = models.ImageField(upload_to='image')
    name = models.CharField(max_length=255)
    narx = models.IntegerField()

class Browse_Catergory(models.Model):
    img = models.ImageField(upload_to='image')
    name = models.CharField(max_length=255)


class Brend(models.Model):
    img = models.ImageField(upload_to='image')
    link = models.CharField(max_length=255)


class Best_Selling_Product(models.Model):
    img = models.ImageField(upload_to='image')
    name = models.CharField(max_length=255)
    narx = models.IntegerField()


class Featured_Products(models.Model):
    img = models.ImageField(upload_to='image')
    name = models.CharField(max_length=255)
    narx = models.IntegerField() 

class New_Arivals(models.Model):
    img = models.ImageField(upload_to='image')
    name = models.CharField(max_length=255)
    narx = models.IntegerField()

class Top_Rated_Products(models.Model):
    img = models.ImageField(upload_to='image')
    name = models.CharField(max_length=255)
    narx = models.IntegerField()

class Blog(models.Model):
    img = models.ImageField(upload_to='image')
    name = models.CharField(max_length=255)
    text = models.TextField()


class Single_Sms(models.Model):
    comment = models.TextField()
    name = models.CharField(max_length=255)
    email = models.EmailField()
    number = models.CharField(max_length=255)

class About(models.Model):
    our = models.CharField(max_length=255)
    story = models.TextField() 



class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)   
    newarrivals = models.ForeignKey(New_Arrivals, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

class Сustomer(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    email = models.EmailField()
    number = models.CharField(max_length=255)    
    state = models.CharField(max_length=255)   
    country = models.CharField(max_length=255)
    address1=models.CharField(max_length=255)
    address2=models.CharField(max_length=255)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)    
    date = models.DateField(auto_now_add=True)
    total_prise = models.IntegerField()


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)    
    newarrivals = models.ForeignKey(New_Arrivals, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.IntegerField()


