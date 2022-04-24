"""mnssby URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from enroll import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.dashboard,name='dash'),
    path('contact/', views.contact,name='contact'),
    path('feed/', views.feed,name='feed'),
    path('app/', views.app,name='app'),
    path('guide/', views.guide,name='guide'),
    path('reg/', views.user_register,name='register'),
    path('log/', views.user_login,name='login'),
    path('out/', views.user_logout,name='out'),
    path('prof/', views.user_profile,name='prof'),
    path('sub/', views.User_subsequent_details,name='sub'),
    path('re/', views.User_Repayment_details,name='re'),
    path('acc/', views.User_account_details,name='acc'),
    path('can/', views.User_loan_cancellation_details,name='can'),
    path('in/', views.User_institute_details,name='in'),
    path('cur/', views.User_current_status_details,name='cur'),
    path('ch/', views.User_change_password_details,name='ch'),
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)