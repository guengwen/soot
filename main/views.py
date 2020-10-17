from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.http import Http404
from django.views.generic import View, TemplateView
from django.http import HttpResponse
from .forms import CustomerForm
from datetime import datetime
from django import forms
from .forms import *
from .models import *

# Create your views here.
class MainIndexView(View):
	def get (self, request):
		return render(request, 'index.html')

	def post (self, request):
		return render(request, 'signUp.html')

class dashboardView(View):
	def get(self,request):
		return render(request, 'dashboard.html')

class SignIndexView(View):
	def get (self, request):
		return render(request, 'signUp.html')

	def post(self, request):
		form = CustomerForm(request.POST)

		if form.is_valid():

			d = datetime.now()
			phone = request.POST.get ("f1-mobile")
			profile = request.POST.get("profpic")
			fname = request.POST.get ("firstname")
			mname = request.POST.get ("f1-middle-name")
			lname = request.POST.get ("lastname")
			gender = request.POST.get ("f1-gender")
			bdate = request.POST.get ("f1-birthday")
			stat = request.POST.get ("f1-status")
			weight = request.POST.get ("f1-weight")
			height = request.POST.get ("f1-height")
			religion = request.POST.get ("f1-religion")
			spouse = request.POST.get ("f1-spouse")
			spouseOccupation = request.POST.get ("f1-spouseOc")
			noOfChildren = request.POST.get ("f1-no")
			mother = request.POST.get ("f1-mother")
			motherOccupation = request.POST.get ("f1-motherOc")
			father = request.POST.get ("f1-father")
			fatherOccupation = request.POST.get ("f1-fatherOc")
			street = request.POST.get ("f1-street")
			brgy = request.POST.get ("f1-brgy")
			city = request.POST.get ("f1-city")
			province = request.POST.get ("f1-province")
			ZIP = request.POST.get ("f1-zip")
			country = request.POST.get ("f1-country")
			email = request.POST.get ("f1-email")
			form = Customer(firstname = fname, middlename = mname, lastname = lname, gender = gender, birthdate = bdate,
				status = stat, weight = weight, height = height, religion = religion, spouseName = spouse, 
				spouseOccupation = spouseOccupation, noOfChil = noOfChildren, motherName = mother, motherOccupation = motherOccupation, 
				fatherName = father, fatherOccupation = fatherOccupation, street = street, brgy = brgy, city = city, province = province, ZIP = ZIP, country = country,
				dateRegistered = d,mobile = phone, email = email, profile = profile)

			form.save()

			return redirect('main:tablescustom_view')

		else:
			return HttpResponse ('Not Valid!')

class ProductTablesView1(View):
	def get(self, request):
		return render(request, 'tablesproduct.html')

class CustomerTablesView(View):
	def get(self, request):
		customer = Customer.objects.exclude(isDelete = 0)
		products = Product.objects.all()
		orders = Order.objects.all()
		context = {
        	'customers' : customer,
        	'products': products,
        	'orders': orders
        }
		return render(request,'tablescustomer.html', context)

	def post(self, request):
		if request.method == 'POST':
			if 'updateBtn' in request.POST:
				pid = request.POST.get("idno")
				pfirst = request.POST.get("firstname")
				pmiddle = request.POST.get("middlename")
				plast = request.POST.get("lastname")
				pgender = request.POST.get("gender")
				pbdate = request.POST.get("birthdate")
				pstatus = request.POST.get("status")
				pweight = request.POST.get("weight")
				pheight = request.POST.get("height")
				preligion = request.POST.get("religion")
				pmobile = request.POST.get("mobile")
				pStreet = request.POST.get("Street")
				pbrgy = request.POST.get("brgy")
				pcity = request.POST.get("city")
				pprovince = request.POST.get("province")
				pZIP = request.POST.get("ZIP")
				pcountry = request.POST.get("country")
				pspouseName = request.POST.get("spouseName")
				pspouseOc = request.POST.get("spouseOc")
				pnoOfChil = request.POST.get("noOfChil")
				pmother = request.POST.get("mother")
				pmotherOc = request.POST.get("motherOc")
				pfather = request.POST.get("father")
				pfatherOc = request.POST.get("fatherOc")
				update_customer = Customer.objects.filter(person_ptr_id = pid).update(firstname = pfirst, middlename = pmiddle,
					lastname = plast, gender = pgender, birthdate = pbdate, status = pstatus, weight = pweight, height = pheight,
					religion = preligion, mobile = pmobile, street = pStreet, brgy = pbrgy, city = pcity, province = pprovince,
					ZIP = pZIP, country = pcountry, spouseName = pspouseName, spouseOccupation = pspouseOc, noOfChil = pnoOfChil,
					motherName = pmother, motherOccupation = pmotherOc, fatherName = pfather, fatherOccupation = pfatherOc)
				print('Profile Updated!')
			elif 'deleteBtn' in request.POST:
				pstat = request.POST.get("idno")
				#pers = Person.objects.filter(id = pid).delete()
				#cust = Customer.objects.filter(person_ptr_id = pid).delete()
				#pid = request.POST.get("idno")
				#pers = Person.objects.filter(id = pid).delete()
				#cust = Customer.objects.filter(person_ptr_id = pid).delete()
				pers = Customer.objects.filter(id = pstat).update(isDelete = 0)

			elif 'orderBtn' in request.POST:
				customerId = request.POST.get("idno")
				customer = Customer.objects.filter(pk=customerId).get()
				orderItem = request.POST.getlist('check')
				quantityItem = request.POST.getlist('quantity')
				for order1  in orderItem:
					product = Product.objects.filter(id=order1).get()
					if(quantityItem[orderItem.index(order1)] is not ""):
						quantity = quantityItem[orderItem.index(order1)]
					else:
						quantity=0
					Product.objects.filter(id=order1).update(stocks = product.stocks-int(quantity))
					product_info_dict={
						'customer': customer, 'product':product, 'quantity':quantity
					}
					Order.objects.create(**product_info_dict)

			elif 'btnSearch' in request.POST: #kani gwen
				if request.POST.get("from_date") and request.POST.get("to_date"):
					_from = request.POST.get("from_date")
					_to = request.POST.get("to_date")
					customers = Customer.objects.filter(
						dateRegistered__range = (_from, _to))
					context = {
						'customers': customers,
						'from_date': _from,
						'to_date': _to
					}
					return render(request, "tablescustomer.html", context)

		customer = Customer.objects.all()
		products = Product.objects.all()
		orders = Order.objects.all()
		context = {
			'customers': customer,
			'products': products,
			'orders': orders
		}
		return redirect('main:tablescustom_view')


class ProductView(View):
	def get(self, request):
		products = Product.objects.exclude(isDelete = 0)
		context = {
			'products' : products
		}
		return render(request, 'tablesproduct.html', context)

	def post(self,request):
		if request.method == 'POST':
			if 'updateBtn' in request.POST:
				print('Update Profile Button Clicked')
				pid = request.POST.get("idno")
				pcat = request.POST.get("category")
				pbrand = request.POST.get("brand")
				pname = request.POST.get("name")
				pprice = request.POST.get("price")
				pstocks = request.POST.get("stocks")
				psize = request.POST.get("size")
				update_product = Product.objects.filter(id = pid).update(name = pname,
					price = pprice)
				print(update_product)
				print('Profile Updated!')
			elif 'deleteBtn' in request.POST:
				pid = request.POST.get("idno")
				prod = Product.objects.filter(id = pid).update(isDelete = 0)
			elif 'btnSearch' in request.POST: #kani gwen
				if request.POST.get("from_date") and request.POST.get("to_date"):
					_from = request.POST.get("from_date")
					_to = request.POST.get("to_date")
					products = Product.objects.filter(
						dateRegistered__range = (_from, _to))
					context = {
						'products': products,
						'from_date': _from,
						'to_date': _to
					}
					return render(request, "tablesproduct.html", context)
		return redirect('main:tables_view')


class regProductView(View):

	def get(self, request):
		return render(request, 'ProductRegistration1.html')

	def post(self, request):
		form = ProductForm(request.POST)
		form.errors

		if form.is_valid():
			sku = datetime.now()
			date = datetime.now()
			name = request.POST.get("productname")
			cat = request.POST.get("category")
			brand = request.POST.get("brand")
			color = request.POST.get("color")
			size = request.POST.get("size")
			price = request.POST.get("price")
			stock = request.POST.get("stock")
			image = request.POST.get("file-input")

			form = Product(dateRegistered = date, sku = sku, name = name, category = cat, brand = brand, 
				color = color, size = size, price = price, stocks = stock, image = image)
			form.save()

			return redirect('main:tables_view')
		else:
			print(form.errors)
			return HttpResponse('Not Valid!')