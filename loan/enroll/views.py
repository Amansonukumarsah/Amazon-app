from django import urls
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import signup,subsequent_payment
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import student
from django.contrib import messages

#HOME PAGE OF WEBSITE

def dashboard(request):
    return render(request,'enroll/dashboard.html')

#contact

def contact(request):
    return render(request,'enroll/contact.html')

#FEED
#@login_required(urls='/')
def feed(request):
    return render(request,'enroll/feed.html')

#GUIDE

def guide(request):
    return render(request,'enroll/guide.html')

#app

def app(request):
    return render(request,'enroll/app.html')


#AUTHINTICATED PAGES

def user_register(request):
    if request.method=="POST":
        form=signup(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Congratulations: your account have been sucessfully created')
    else:
        form=signup()
    return render(request,'enroll/register.html',{'fm':form})

#user_login:-

def user_login(request):
    if not request.user.is_authenticated:
        if request.method=="POST":
            form=AuthenticationForm(request=request,data=request.POST)
            if form.is_valid():
                uname=form.cleaned_data['username']
                upass=form.cleaned_data['password']
                user=authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    return HttpResponseRedirect('/prof/')
        else:
            form=AuthenticationForm()
        return render(request,'enroll/login.html',{'fm':form})
    else:
        return HttpResponseRedirect('/prof/')

#user_logout:-

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/log/')


#PROFILE OF WEBSITE AND INSIDE IT ALL APPLICATION:-

def user_profile(request):
    if request.user.is_authenticated:
        return render(request,'enroll/profile.html')
    else:
        return HttpResponseRedirect('/log/')
    

#another page which is inside the profile page

def User_subsequent_details(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            fm=subsequent_payment(request.POST,request.FILES)
            if fm.is_valid():
                fm.save()
        else:
            fm=subsequent_payment()
        return render(request,'enroll/subsequent.html',{'form':fm})
    else:
        return HttpResponseRedirect('/log/')

#user_repayment

def User_Repayment_details(request):
    if request.user.is_authenticated:
        return render(request,'enroll/repayment.html')
    else:
        return HttpResponseRedirect('/log/')

#user_account_details

def User_account_details(request):
    if request.user.is_authenticated:
        return render(request,'enroll/update_bankacc.html')
    else:
        return HttpResponseRedirect('/log/')

#user_loan_cancellation

def User_loan_cancellation_details(request):
    if request.user.is_authenticated:
        return render(request,'enroll/loan_cancellation.html')
    else:
        return HttpResponseRedirect('/log/')

#user_instittute_details

def User_institute_details(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            fm=student(request.POST,request.FILES)
            if fm.is_valid():
                fm.save()
        else:
            fm=student()
        return render(request,'enroll/institute_details.html',{'form':fm})
    else:
        return HttpResponseRedirect('/log/')
        
#user_current_status_details

def User_current_status_details(request):
    if request.user.is_authenticated:
        return render(request,'enroll/current_status.html')
    else:
        return HttpResponseRedirect('/log/')

#user_change_passowrd_details

def User_change_password_details(request):
    if request.user.is_authenticated:
        return render(request,'enroll/change_password.html')
    else:
        return HttpResponseRedirect('/log/')


