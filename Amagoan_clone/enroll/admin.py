from django.contrib import admin
from .models import Customer,Product,cart,orderplaced
# Register your models here.

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display=['id','user','Name','City','Pin_code','State']


@admin.register(cart)
class  cartModelAdmin(admin.ModelAdmin):
    list_dispaly=['id','user','product','Quentity']


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display=['id','title','Selling_price','Discount_price','Brand','Description','Category','Product_image']

@admin.register(orderplaced)
class orderplacedModelAdmin(admin.ModelAdmin):
    list_display=['id','user','customer','product','quentity','Order_date','Status']
