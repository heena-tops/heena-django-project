from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.

class User(models.Model):
	fname=models.CharField(max_length=100)
	lname=models.CharField(max_length=100)
	mobile=models.IntegerField()
	address=models.TextField()
	email=models.EmailField()
	password=models.CharField(max_length=100)
	usertype=models.CharField(max_length=100,default="user")

	def __str__(self):
		return self.fname+" "+self.lname 

class Product(models.Model):
	seller=models.ForeignKey(User,on_delete=models.CASCADE)
	product_name=models.CharField(max_length=100)
	product_price=models.IntegerField()
	product_qty=models.IntegerField()
	product_desc=models.TextField()
	product_image=models.ImageField(upload_to="product_image/")
	product_venue=models.TextField(default="")
	product_time=models.TimeField(blank=True,null=True)
	product_date=models.DateField(blank=True,null=True)

	def __str__(self):
		return self.seller_fname+" - "+self.product_name

class Wishlist(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	product=models.ForeignKey(Product,on_delete=models.CASCADE)
	date=models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.user.fname+" - "+self.product.product_name

class Cart(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	product=models.ForeignKey(Product,on_delete=models.CASCADE)
	date=models.DateTimeField(default=timezone.now)
	product_qty=models.IntegerField(default=1)
	product_price=models.IntegerField()
	payment_status=models.BooleanField(default=False)
	total_price=models.IntegerField(default=0)

	def __str__(self):
		return self.user.fname+" - "+self.product.product_name

class Transaction(models.Model):
    made_by = models.ForeignKey(User, related_name='transactions',on_delete=models.CASCADE)
    made_on = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField()
    order_id = models.CharField(unique=True, max_length=100, null=True, blank=True)
    checksum = models.CharField(max_length=100, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.order_id is None and self.made_on and self.id:
            self.order_id = self.made_on.strftime('PAY2ME%Y%m%dODR') + str(self.id)
        return super().save(*args, **kwargs)
