from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from .models import studentdetails,payment,feedback
from django import forms


class feed_back(forms.ModelForm):
    class Meta:
        model=feedback
        fields=['name','email','feed_back']
#payment................................................................................................
class subsequent_payment(forms.ModelForm):
    class Meta:
        model= payment
        fields=['pdf','pdf1']


#institutedetails................................................................................................

class student(forms.ModelForm):
    class Meta:
        model = studentdetails
        fields = ['Institute_State','Institute_District','Name_of_Collage','Name_of_university','Institute_Type','Institute_City','Institute_pincode','Institute_Email_id','Institute_Mobile_No','pdf']


#signup................................................................................................

class signup(UserCreationForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
        
#edituserform................................................................................................


class edituserform(UserChangeForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']

#editadmin form................................................................................................


class edituseradminform(UserChangeForm):
    class Meta:
        model=User
        fields='__all__'
