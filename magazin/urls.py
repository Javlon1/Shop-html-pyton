from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from main.views import *
urlpatterns = [

    path('admin/', admin.site.urls),
    path('', Home , name='home'),
    path('search/', Search , name='search'),
    path('blog/', BlogViews , name='blog'),
    path('add-cart/', AddCart , name='add-cart'),
    path('single/<int:pk>', Single , name='single'),
    path('single_sms_views', Single_Sms_Views , name='single_sms_views'),
    path('contact/', ContactViews , name='contact'),
    path('addcontact/', AddContact , name='addcontact'),
    path('about/', AboutViews , name='about'),
    path('our_store/', OurStore , name='our_store'),
    path('order-tracking/', OrderTracking , name='order-tracking'),
    path('shopcategories/', ShopCategories , name='shopcategories'),
    path('shopgridrightsidebar/', ShopGridRightSidebar , name='shopgridrightsidebar'),
    path('shopcart/', ShopCart , name='shopcart'),
    path('createorder', CreateOrder, name='createorder'),
    path('shopcategories/', ShopCategories , name='shopcategories'),
    path('checkoutdetails/', CheckoutDetails , name='checkoutdetails'),
    # path('customerviews/', СustomerViews , name='customerviews'),
    path('checkoutshipping/', CheckoutShipping , name='checkoutshipping'),
    path('checkoutpayment/', CheckoutPayment , name='checkoutpayment'),
    path('checkoutreview/', CheckoutReview , name='checkoutreview'),
    path('checkoutcomplete/', CheckoutComplete , name='checkoutcomplete'),
    path('ordertracking/', OrderTracking , name='ordertracking'),
    path('productcomparison/', ProductComparison , name='productcomparison'),
    path('authenticationsignin/', AuthenticationSignin , name='authenticationsignin'),
    path('authenticationsignup/', AuthenticationSignup , name='authenticationsignup'),
    path('productdetails/<int:pk>/', ProductDetails , name='productdetails'),
    path('authenticationforgotpassword/', AuthenticationForgotPassword , name='authenticationforgotpassword'),

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)