from django.db import models
from datetime import datetime

# Create your models here.

class Person (models.Model):
	firstname = models.CharField(max_length = 100)
	middlename = models.CharField(max_length = 100)
	lastname = models.CharField(max_length = 100)
	gender = models.CharField(max_length = 50)
	birthdate = models.DateField(blank=True, null=True)
	status = models.CharField(max_length = 50)
	weight = models.CharField(max_length = 5)
	height = models.CharField(max_length = 5)
	religion = models.CharField(max_length = 50)
	spouseName = models.CharField(max_length = 100)
	spouseOccupation = models.CharField(max_length = 100)
	noOfChil = models.CharField(max_length = 50)
	motherName = models.CharField(max_length = 100)
	motherOccupation = models.CharField(max_length = 100)
	fatherName = models.CharField(max_length = 100)
	fatherOccupation = models.CharField(max_length = 100)
	street = models.CharField(max_length = 100)
	brgy = models.CharField(max_length = 100)
	city = models.CharField(max_length = 100)
	province = models.CharField(max_length = 100)
	ZIP = models.CharField(max_length = 5)
	country = models.CharField(max_length = 100)
	class Meta:
		db_table = "Person"
	
class Customer (Person):
	dateRegistered = models.DateField(default=datetime.now())
	mobile = models.CharField (max_length = 11)
	email = models.CharField(max_length = 100)
	profile = models.ImageField(upload_to="media", null = True, blank = True)

	class Meta:
		db_table = "Customer"

class Product(models.Model):
 	sku = models.DateField(default = datetime.now())
 	dateRegistered = models.DateField(default = datetime.now())
 	name = models.CharField(max_length = 100)
 	category = models.CharField(max_length = 100)
 	brand = models.CharField(max_length = 100)
 	color = models.CharField(max_length = 100)
 	size = models.CharField(max_length = 50)
 	price = models.FloatField()
 	stocks = models.IntegerField()
 	image = models.ImageField(upload_to = "image", null = True)

 	class Meta:
 		db_table = "Product"

class Order(models.Model):
	customer = models.ForeignKey(Customer, null = False, blank = False, on_delete = models.CASCADE)
	product = models.ForeignKey(Product, null = False, blank = False, on_delete = models.CASCADE)
	quantity = models.CharField(max_length = 5)
	date_Ordered = models.DateField(default = datetime.now())

	class Meta:
		db_table = "Order"


