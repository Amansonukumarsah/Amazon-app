from re import template
from django.urls import path
from .forms import loginform,passwordchange,setpassword,resetpassword
from enroll import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.homeview.as_view(),name='home'),
    path('productdetails/<int:pk>', views.productdetailsview.as_view(),name='productdetails'),
    path('electro/', views.electronicview.as_view(),name='elctro'),
    path('electro/<slug:data>', views.electronicview.as_view(),name='elctrodata'), 
    path('register/', views.registrationformsview.as_view(),name='register'),  
    path('accounts/login/',auth_views.LoginView.as_view(template_name="enroll/login.html",authentication_form=loginform),name='login'), 
    path("logout/", auth_views.LogoutView.as_view(next_page='login'), name='logout') ,

    path("passwordchange/", auth_views.PasswordChangeView.as_view(template_name="enroll/changepassword.html",form_class=passwordchange), name="passwordchange"),
    path("passwordchange/done/", auth_views.PasswordChangeDoneView.as_view(template_name="enroll/passwordchangedone.html"), name="password_change_done"),
    
    path("password_reset/",auth_views.PasswordResetView.as_view(template_name="enroll/password_reset.html",form_class=resetpassword), name="password_reset"),

    path("password_reset/done/",auth_views.PasswordResetDoneView.as_view(template_name="enroll/password_reset_done.html"), name="password_reset_done"),

    path("reset/<uidb64>/<token>/",auth_views.PasswordResetConfirmView.as_view(template_name="enroll/password_reset_confirm.html",form_class=setpassword), name="password_reset_confirm"),

    path("reset/done/",auth_views.PasswordResetCompleteView.as_view(template_name="enroll/password_reset_complete.html"), name="password_reset_complete"),

    path('profile/',views.profile,name='profile'),  
    path('Adress/',views.Adress,name='adress'),  
    path('empty/',views.empty,name='empty'),  

    path('cart/', views.addtocart,name='cart'),
    path('cart1/', views.show_cart,name='show_cart'),

    path('place/', views.placeorder,name='place'),
    path('payment/', views.payment,name='payment'),


    path('od/',views.order_details,name='order'),

    path('login_cart/',views.login_cart,name='login_cart'),

] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)