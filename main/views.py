from ast import Or
from itertools import count, product
from multiprocessing import context
from statistics import quantiles
from django.shortcuts import render,redirect
from .models import *

def Search(request):
    if request.method == 'POST':
        search = request.POST.get('search')
        new_arrivals = New_Arrivals.objects.filter(name=search)
        print(len(new_arrivals))
        context = {
            'new_arrivals':new_arrivals,
        }

        return render(request, 'search.html', context )

    return render(request, 'search.html', )

def Home(request,):
    info = Contact_info.objects.last()
    all = All_Items.objects.last()
    address = Contact_address.objects.last()
    new_arrivals = New_Arrivals.objects.all().order_by('-id')[0:9]
    category = Category.objects.all().order_by('-id')[0:3]
    browse_catergory = Browse_Catergory.objects.all().order_by('-id')
    brend = Brend.objects.all().order_by('-id')
    best_selling_product = Best_Selling_Product.objects.all().order_by('-id')[0:4]
    featured_products = Featured_Products.objects.all().order_by('-id')[0:4]
    new_arivals = New_Arivals.objects.all().order_by('-id')[0:4]
    top_rated_products = Top_Rated_Products.objects.all().order_by('-id')[0:4]

    context = {
        'info':info,
        'all':all,
        'new_arrivals':new_arrivals,
        'category':category,
        'browse_catergory':browse_catergory,
        'brend':brend,
        'best_selling_product':best_selling_product,
        'featured_products':featured_products,
        'new_arivals':new_arivals,
        'top_rated_products':top_rated_products,
        'address':address
    }
    return render(request, 'index.html', context)

def BlogViews(request):

    blog = Blog.objects.all().order_by('-id')[0:3]
    info = Contact_info.objects.last()
    all = All_Items.objects.last()
    new_arrivals = New_Arrivals.objects.all().order_by('-id')[0:6]
    category = Category.objects.all().order_by('-id')[0:3]
    browse_catergory = Browse_Catergory.objects.all().order_by('-id')
    brend = Brend.objects.all().order_by('-id')
    best_selling_product = Best_Selling_Product.objects.all().order_by('-id')[0:4]
    featured_products = Featured_Products.objects.all().order_by('-id')[0:4]
    new_arivals = New_Arivals.objects.all().order_by('-id')[0:4]
    top_rated_products = Top_Rated_Products.objects.all().order_by('-id')[0:4]

    context = {
        'blog':blog,
        'info':info,
        'all':all,
        'new_arrivals':new_arrivals,
        'category':category,
        'browse_catergory':browse_catergory,
        'brend':brend,
        'best_selling_product':best_selling_product,
        'featured_products':featured_products,
        'new_arivals':new_arivals,
        'top_rated_products':top_rated_products
    }

    return render(request, 'blog.html', context)

def Single(request,pk):
    blog = Blog.objects.get(id=pk)
    info = Contact_info.objects.last()
    all = All_Items.objects.last()
    new_arrivals = New_Arrivals.objects.all().order_by('-id')[0:6]
    category = Category.objects.all().order_by('-id')[0:3]
    browse_catergory = Browse_Catergory.objects.all().order_by('-id')
    brend = Brend.objects.all().order_by('-id')
    best_selling_product = Best_Selling_Product.objects.all().order_by('-id')[0:4]
    featured_products = Featured_Products.objects.all().order_by('-id')[0:4]
    new_arivals = New_Arivals.objects.all().order_by('-id')[0:4]
    top_rated_products = Top_Rated_Products.objects.all().order_by('-id')[0:4]
    context = {
        'blog':blog,
        'info':info,
        'all':all,
        'new_arrivals':new_arrivals,
        'category':category,
        'browse_catergory':browse_catergory,
        'brend':brend,
        'best_selling_product':best_selling_product,
        'featured_products':featured_products,
        'new_arivals':new_arivals,
        'top_rated_products':top_rated_products
    }


    return render(request, 'single.html', context)

def Single_Sms_Views(request):
    if request.method == 'POST':

        comment = request.POST.get('comment')
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')

        Single_Sms.objects.create(comment=comment, name=name, email=email, number=number)
        
    return redirect('blog')

def ContactViews(request):
    info = Contact_info.objects.last()
    all = All_Items.objects.last()
    new_arrivals = New_Arrivals.objects.all().order_by('-id')[0:6]
    category = Category.objects.all().order_by('-id')[0:3]
    browse_catergory = Browse_Catergory.objects.all().order_by('-id')
    brend = Brend.objects.all().order_by('-id')
    best_selling_product = Best_Selling_Product.objects.all().order_by('-id')[0:4]
    featured_products = Featured_Products.objects.all().order_by('-id')[0:4]
    new_arivals = New_Arivals.objects.all().order_by('-id')[0:4]
    top_rated_products = Top_Rated_Products.objects.all().order_by('-id')[0:4]
    contact = Contact_address.objects.last()
    context = {
        'contact':contact,
        'info':info,
        'all':all,
        'new_arrivals':new_arrivals,
        'category':category,
        'browse_catergory':browse_catergory,
        'brend':brend,
        'best_selling_product':best_selling_product,
        'featured_products':featured_products,
        'new_arivals':new_arivals,
        'top_rated_products':top_rated_products
    }
    
    return render(request, 'contact.html', context)

def AddContact(request):
    if request.method == 'POST':

        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        message = request.POST.get('message')
    
        Contact.objects.create(name=name, email=email, number=number, message=message, )
    return redirect('contact')

def AboutViews(request):
    about = About.objects.last()
    brend = Brend.objects.all().order_by('-id')
    info = Contact_info.objects.last()
    all = All_Items.objects.last()
    new_arrivals = New_Arrivals.objects.all().order_by('-id')[0:6]
    category = Category.objects.all().order_by('-id')[0:3]
    browse_catergory = Browse_Catergory.objects.all().order_by('-id')
    brend = Brend.objects.all().order_by('-id')
    best_selling_product = Best_Selling_Product.objects.all().order_by('-id')[0:4]
    featured_products = Featured_Products.objects.all().order_by('-id')[0:4]
    new_arivals = New_Arivals.objects.all().order_by('-id')[0:4]
    top_rated_products = Top_Rated_Products.objects.all().order_by('-id')[0:4]

    context = {
        'about':about,
        'brend':brend,
        'info':info,
        'all':all,
        'new_arrivals':new_arrivals,
        'category':category,
        'browse_catergory':browse_catergory,
        'brend':brend,
        'best_selling_product':best_selling_product,
        'featured_products':featured_products,
        'new_arivals':new_arivals,
        'top_rated_products':top_rated_products
    }

    return render(request, 'about.html', context)


def OurStore(request):
    info = Contact_info.objects.last()
    all = All_Items.objects.last()
    new_arrivals = New_Arrivals.objects.all().order_by('-id')[0:6]
    category = Category.objects.all().order_by('-id')[0:3]
    browse_catergory = Browse_Catergory.objects.all().order_by('-id')
    brend = Brend.objects.all().order_by('-id')
    best_selling_product = Best_Selling_Product.objects.all().order_by('-id')[0:4]
    featured_products = Featured_Products.objects.all().order_by('-id')[0:4]
    new_arivals = New_Arivals.objects.all().order_by('-id')[0:4]
    top_rated_products = Top_Rated_Products.objects.all().order_by('-id')[0:4]

    context = {
        'info':info,
        'all':all,
        'new_arrivals':new_arrivals,
        'category':category,
        'browse_catergory':browse_catergory,
        'brend':brend,
        'best_selling_product':best_selling_product,
        'featured_products':featured_products,
        'new_arivals':new_arivals,
        'top_rated_products':top_rated_products
    }


    return render(request, 'our_store.html', context)



def ShopCategories(request):

    return render(request, 'shop-categories.html')


def ShopGridRightSidebar(request):
    info = Contact_info.objects.last()
    all = All_Items.objects.last()
    new_arrivals = New_Arrivals.objects.all().order_by('-id')[0:6]
    category = Category.objects.all().order_by('-id')[0:3]
    browse_catergory = Browse_Catergory.objects.all().order_by('-id')
    brend = Brend.objects.all().order_by('-id')
    best_selling_product = Best_Selling_Product.objects.all().order_by('-id')[0:4]
    featured_products = Featured_Products.objects.all().order_by('-id')[0:4]
    new_arivals = New_Arivals.objects.all().order_by('-id')[0:4]
    top_rated_products = Top_Rated_Products.objects.all().order_by('-id')[0:4]

    context = {
        'info':info,
        'all':all,
        'new_arrivals':new_arrivals,
        'category':category,
        'browse_catergory':browse_catergory,
        'brend':brend,
        'best_selling_product':best_selling_product,
        'featured_products':featured_products,
        'new_arivals':new_arivals,
        'top_rated_products':top_rated_products
    }


    return render(request, 'shop-grid-right-sidebar.html', context)

# def СustomerViews(request):
#     if request.method == 'POST':
    
#         name = request.POST.get('name')
#         surname = request.POST.get('surname')
#         email = request.POST.get('email')
#         number = request.POST.get('number')
#         state = request.POST.get('state')
#         country = request.POST.get('country')
#         address1 = request.POST.get('address1')
#         address2 = request.POST.get('address2')

#         Сustomer.objects.create(name=name, surname=surname, email=email, number=number, state=state, country=country, address1=address1, address2=address2)
      
#     return redirect('checkoutdetails')


def CreateOrder(request):
        
    if request.method == 'POST':

        user = request.user
        cart = Cart.objects.filter(user=user)
        total = 0
        if cart:
            for i in cart:
                total += int(i.newarrivals.narx) * int(i.quantity)
            order = Order.objects.create(user=user, total_prise=total)  
            for i in cart:
                OrderItem.objects.create(order=order, newarrivals=i.newarrivals, quantity=i.quantity, price=i.newarrivals.narx)  
            for i in cart:
                i.delete()
        else:
            pass    
    return redirect('checkoutdetails')

def AddCart(request):
    if request.method == 'POST':
        user = request.user
        newarrivals = request.POST.get('newarrivals')
        Cart.objects.create(user=user, newarrivals_id=newarrivals)
    return redirect('home')


def ShopCart(request):
    user = request.user
    cart = Cart.objects.filter(user=user)
    context = {
        'cart':cart
    }
    return render(request, 'shop-cart.html', context)


def ShopCategories(request):

    return render(request, 'shop-categories.html')

def CheckoutDetails(request):
    user = request.user
    cart = Cart.objects.filter(user=user)
    context = {
        'cart':cart
    }
    if request.method == 'POST':
    
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        email = request.POST.get('email')
        number = request.POST.get('number')
        state = request.POST.get('state')
        country = request.POST.get('country')
        address1 = request.POST.get('address1')
        address2 = request.POST.get('address2')

        Сustomer.objects.create(name=name, surname=surname, email=email, number=number, state=state, country=country, address1=address1, address2=address2)
 
    return render(request, 'checkout-details.html', context)

def CheckoutShipping(request):
    return render(request, 'checkout-shipping.html')

def CheckoutPayment(request):

    return render(request, 'checkout-payment.html')

def CheckoutReview(request):

    return render(request, 'checkout-review.html')

def CheckoutComplete(request):

    return render(request, 'checkout-complete.html')

def OrderTracking(request):

    return render(request, 'order-tracking.html')

def ProductComparison(request):

    return render(request, 'product-comparison.html')

def AuthenticationSignin(request):

    return render(request, 'authentication-signin.html')

def AuthenticationSignup(request):

    return render(request, 'authentication-signup.html')

def AuthenticationForgotPassword(request):

    return render(request, 'authentication-forgot-password.html')



def ProductDetails(request, pk):
    new_arrivals = New_Arrivals.objects.get(id=pk)

    context = {
        'new_arrivals':new_arrivals
    }


    return render(request, 'product-details.html', context)


