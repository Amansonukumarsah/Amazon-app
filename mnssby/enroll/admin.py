from django.contrib import admin
from .models import payment, studentdetails,feedback
# Register your models here.
admin.site.register(studentdetails)
admin.site.register(payment)
admin.site.register(feedback)


