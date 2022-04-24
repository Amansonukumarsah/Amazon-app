from itertools import product
from sre_parse import State
from xml.etree.ElementTree import QName
from django import views
from django.shortcuts import redirect, render
from .models import Customer,Product,orderplaced,cart
from django.views import View
from .forms import registrationforms,Adressform
from django.contrib import messages
from django.db.models import Q



class homeview(View):
    def get(self, request):
        sofa = Product.objects.filter(Category='so')
        electronic = Product.objects.filter(Category='ele')
        T_shirt = Product.objects.filter(Category='Ts')
        return render(request,'enroll/home.html',{'sofa':sofa,'electronic':electronic,'T_shirt':T_shirt})


class productdetailsview(View):
    def get(self,request,pk):
        product= Product.objects.get(pk=pk)
        item_already_in_cart=False
        item_already_in_cart=cart.objects.filter(Q(product=product.id)& Q(user=request.user)).exists()
        return render(request,'enroll/productdetails.html',{'product':product,'item_already_in_cart':item_already_in_cart})


class electronicview(View):
    def get(self,request,data=None):
        if data==None:
            electronic = Product.objects.filter(Category='ele')
        elif data=='below':
            electronic = Product.objects.filter(Category='ele').filter(Selling_price__lte=30000)
        elif data=='above':
            electronic = Product.objects.filter(Category='ele').filter(Selling_price__gte=30000)
        return render(request,'enroll/electronic.html',{'electronic':electronic})


class registrationformsview(View):
    def get(self,request):
        form = registrationforms()
        return render(request,'enroll/register.html',{'form':form})
    def post(self,request):
        form = registrationforms(request.POST)
        if form.is_valid():
            messages.success(request,'Registration Successfully')
            form.save()
        return render(request,'enroll/register.html',{'form':form})


def profile(request):
    if request.method=="POST":
        form=Adressform(request.POST)
        if form.is_valid():
            user=request.user
            name=form.cleaned_data['Name']
            city=form.cleaned_data['City']
            pincode=form.cleaned_data['Pin_code']
            State=form.cleaned_data['State']
            reg=Customer(user=user,Name=name,City=city,Pin_code=pincode,State=State)
            reg.save()     
    else:
        form=Adressform()
    return render(request,'enroll/profile.html',{'form':form,'active':'btn-primary'})


def Adress(request):
    user=request.user
    customer=Customer.objects.filter(user=user)
    return render(request,'enroll/Adress.html',{'customer':customer,'active':'btn-primary'})


def addtocart(request):
    user =request.user
    product_id= request.GET.get('prod_id')
    product =Product.objects.get(id=product_id)
    cart(user=user,product=product).save()
    return redirect('/cart1')


def show_cart(request):
    if request.user.is_authenticated:
        user=request.user
        carts=cart.objects.filter(user=user)
        amount=0.0
        ship=30.0
        totalamount=0.0
        pamount=0
        cart_product=[p for p in cart.objects.all() if p.user==user]
        if carts:
            for p in cart_product:
                pamount=(p.quentity * p.product.Discount_price)
                amount=amount+pamount
            totalamount=amount+ship
            return render(request,'enroll/Addcart.html',{'cart':carts,'totalamount':totalamount,'amount':amount})
        else:
            return render(request,'enroll/empty.html')

def empty(request):
    return render(request,'enroll/empty.html')


def placeorder(request):
    user=request.user
    add=Customer.objects.filter(user=user)
    cart_item=cart.objects.filter(user=user)
    return render(request,'enroll/placeorder.html',{'add':add,'cart_item':cart_item})


def payment(request):
    user=request.user
    custid=request.GET.get("custid")
    customer=Customer.objects.get(id=custid)
    Cart=cart.objects.filter(user=user)
    for c in Cart:
        orderplaced(user=user,customer=customer,product=c.product,quentity=c.quentity).save()
        c.delete()
    return redirect("order")



def login_cart(request):
    return render(request,'enroll/login_cart.html')

    
def order_details(request):
    user=request.user
    order=orderplaced.objects.filter(user=user)
    return render(request,'enroll/orders_details.html',{'order':order})