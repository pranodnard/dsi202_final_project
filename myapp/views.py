from django.shortcuts import render
from .models import *
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CreateUserForm
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.shortcuts import redirect
import datetime

# Create your views here.

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "myapp/facebook.html" 

def homey(request):
	data = Product.objects.all().order_by('id')[0:4]
	dat = Product.objects.all().order_by('id')[4:8]
	da = Product.objects.all().order_by('id')[8:12]
	categoryy = Category.objects.all()
	brands = Brand.objects.all()
	cats = Product.objects.distinct().values('category__title')


	context = {
		'data':data,
		'categoryy':categoryy,
		'brands':brands,
		'cats':cats,
		'dat':dat,
		'da':da
	}

	return render(request, 'myapp/homey.html',context)

def search(request):
	q=request.GET['q']
	data=Product.objects.filter(model__icontains=q)
	return render(request,'myapp/search.html',{'data':data})



def shoe_page(request, shoe_id,):
	if 'cart' not in request.session:
		cart = Cart.objects.create(total=0)
		request.session['cart']=cart.id

	brand = Brand.objects.all()
	shoe = Product.objects.get(id=shoe_id)
	brands = Brand.objects.all()

	


	context = {
		'shoe': Product.objects.get(id=shoe_id),
		'brand' : brand,
		'brands' : brands
	}

	return render(request, 'myapp/product.html', context)

def product_list(request,cat_id):
	category=Category.objects.get(id=cat_id)
	data=Product.objects.filter(category=category)
	brands = Brand.objects.all()
	
	categoryy = Category.objects.all()
	return render(request,'myapp/product_list.html',{
			'data':data,
			'category':category,
			'cat_id':cat_id,
			'brands':brands,
			'mode':1
			})

def product_list_type(request,type_id):
	type=Type.objects.get(id=type_id)
	data=Product.objects.filter(type=type)
	brands = Brand.objects.all()
	
	categoryy = Category.objects.all()
	return render(request,'myapp/product_list.html',{
			'data':data,
			'type_id':type_id,
			'brands':brands,
			'mode':2
			})

def product_list_cat_type(request,cat_id,type_id):
	category=Category.objects.get(id=cat_id)
	type=Type.objects.get(id=type_id)
	print(type_id)
	data=Product.objects.filter(category=category)
	data= data.filter(type=type)
	print(data)
	brands = Brand.objects.all()
	
	categoryy = Category.objects.all()
	return render(request,'myapp/product_list.html',{
			'data':data,
			'category':category,
			'cat_id':cat_id,
			'type_id':type_id,
			'brands':brands,
			'mode':3
			})

def brand_list(request,bra_id):
	brand = Brand.objects.get(id=bra_id)
	data = Product.objects.filter(brand=brand)
	brands = Brand.objects.all()
	
	return render(request, 'myapp/brand_list.html', {'data':data,'brand':brand,'brands':brands})

def new_arrival(request):
	brands = Brand.objects.all()
	context = {'brands':brands}
	return render(request, 'myapp/new_arrival.html', context)

def new_arrival01(request):
	brands = Brand.objects.all()
	context = {'brands':brands}
	return render(request, 'myapp/new_arrival01.html', context)

def new_arrival02(request):
	brands = Brand.objects.all()
	context = {'brands':brands}
	return render(request, 'myapp/new_arrival02.html', context)

def refresh_cart_total(cart):
    total = 0
    for item in cart.cart_items.all():
        total += item.quantity * item.shoe.product.price
    cart.total = total
    cart.save()


def add_to_cart(request):
	shoe = ShoeSize.objects.get(id=request.POST['size_id'])
	cart = Cart.objects.get(id=request.session['cart_id'])
	quantity = request.POST['quantity']
	cart_item = CartItem.objects.create(shoe=shoe, quantity=quantity,cart=cart)
	context = {
		'cart': Cart.objects.get(id=request.session['cart_id']),
		'shoe':shoe,
		'cart_item':cart_item
	}
	return render(request, 'myapp/cart.html', context)

	refresh_cart_total(cart)
	return redirect('/cart')


def cart(request):
	if 'card_id' not in request.session:
		cart = Cart.objects.create(total=1)
		request.session['cart_id']=cart.id
	context = {
		'cart': Cart.objects.get(id=request.session['cart_id'])
	}
	return render(request, 'myapp/cart.html', context)

def checkout(request):
	if 'cart_id' not in request.session:
		return redirect("/")

	cart = Cart.objects.get(id=request.session['cart_id'])


	
	context = {
		'cart' : Cart.objects.get(id=request.session["cart_id"])
	}

	return render(request, 'myapp/checkout.html', context)

def checkout_process_guest(request):
	shipping_address = Address.objects.create(
		address = request.POST['address'],
		address2 = request.POST['address2'],
		city = request.POST['city'],
		state = request.POST['state'],
		zipcode = request.POST['zipcode'],
	)

	if 'same_address' in request.POST:
		billing_address = shipping_address
		cc_first_name = request.POST['first_name']
		cc_last_name = request.POST['last_name']
	else :
		billing_address = Address.objects.create(
			address = request.POST['cc_address'],
			address2 = request.POST['cc_address2'],
			city = request.POST['cc_city'],
			state = request.POST['cc_state'],
			zipcode = request.POST['cc_zipcode'],
		)
	cc_first_name = request.POST['cc_first_name']
	cc_last_name = request.POST['cc_last_name']

	guest_user = User.objects.create(
		first_name = request.POST['first_name'],
		last_name = request.POST['last_name'],
		email = request.POST['email'],
		password = "",
		
	)

	expiration_date = datetime.date(int(request.POST['expireYYYY']),int(request.POST['expireM']),1)

	credit_card = CreditCard.objects.create(
		number = request.POST['cc_number'],
		security_code = request.POST['cc_security_code'],
		expiration_date = expiration_date,
		first_name = cc_first_name,
		last_name = cc_last_name,
		address = billing_address,
		user = guest_user,
	)

	cart = Cart.objects.get(id=request.session['cart_id'])
	new_order = Order.objects.create(
		status = "Processing",
		cart = cart,
		user = guest_user,
		credit_card = credit_card,
	)

	for item in cart.cart_items.all():
		shoe = item.shoe
		shoe.inventory = shoe.inventory-item.quantity
		shoe.quantity_sold = shoe.quantity_sold+item.quantity
		shoe.save()

	request.session['order_id'] = new_order.id

	request.session.pop("cart_id")

	return redirect('confirm')


def confirm(request):
    # Retrieves order from session.
    current_order = Order.objects.get(id = request.session['order_id'])

    # Formats credit card number to just show last digits.
    # This may be a security vulnerability. Not sure.
    cc_last_digits = current_order.credit_card.number % 10000

    # Because credit card expiration date is stored as a date with the first of the month,
    # this reformats it as a MM/YY
    cc_expiration_date = current_order.credit_card.expiration_date.strftime('%m/%y')

    context = {
        'order': current_order,
        'cc_last_digits': cc_last_digits,
        'cc_expiration_date': cc_expiration_date
    }
    return render(request, 'myapp/confirm.html', context)

def about(request):
	brands = Brand.objects.all()
	context = {'brands':brands}
	return render(request, 'myapp/about.html', context)

def help(request):
	brands = Brand.objects.all()
	context = {'brands':brands}
	return render(request, 'myapp/help.html', context)

def sell(request):
	brands = Brand.objects.all()
	context = {'brands':brands}
	return render(request, 'myapp/sell.html', context)

#login-regis

from .forms import CreateUserForm

def registerPage(request):
	if request.user.is_authenticated:
		context = {}
		return render(request, 'myapp/signup.html', context)
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('login')

		context = {'form':form}
		return render(request, 'myapp/signup.html', context)

def loginPage(request):
	if request.user.is_authenticated:
		context = {}
		return render(request, 'myapp/login.html', context)
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('homey')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'myapp/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')

@login_required(login_url='login')
def home(request):
	return render(request, 'myapp/homey.html', context)