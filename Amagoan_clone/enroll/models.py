from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxLengthValidator,MinLengthValidator
State_choice=(
    ('Bihar','Bihar'),
    ('west Bengal','West Bengal'),
    ('Utter Pradesh','Utter Pradesh'),
    ('Jharkhand','Jharkhand'),
    ('Delhi','Delhi'),
    ('Kerela','Kerala'),
    ('Maharastra','Maharastra'),
    ('Karnataka','Karnataka'),
    ('Tamil_Nandu','Tamil_Nandu'),
    ('Assam','Assam'),
    ('Manipur','Manipur'),
    ('Mizoram','Mizoram'),
    ('Madhpradesh','Madhpradesh'),
)

class Customer(models.Model):
    user =models.ForeignKey(User, on_delete=models.CASCADE)
    Name=models.CharField(max_length=100)
    City = models.CharField(max_length=100)
    Pin_code=models.IntegerField()
    State = models.CharField(choices=State_choice,max_length=100)

def __str__(self):
    return str(self.id)

Catecory_Choice=(
    ('mb','mobile'),
    ('so','sofa'),
    ('ele','electronice'),
    ('Ts','T-Shirt')
)

class Product(models.Model):
    title=models.CharField(max_length=100)
    Selling_price = models.FloatField()
    Discount_price = models.FloatField()
    Brand = models.CharField(max_length=100)
    Description = models.TextField()
    Category = models.CharField(choices=Catecory_Choice,max_length=100)
    Product_image = models.ImageField(upload_to="productimg")
 
def __str__(self):
    return str(self.id)

class cart(models.Model):
    user =models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quentity = models.PositiveIntegerField(default=1)

def __str__(self):
    return str(self.id)

Status_Choice=(
    ('Accepted','Accepted'),
    ('on The Way','on The Way'),
    ('Delivered','Delivered'),
    ('Cancel','Cancel')
)

class orderplaced(models.Model):
    user = models.ForeignKey( User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quentity = models.PositiveIntegerField(default=1)
    Order_date = models.DateTimeField(auto_now_add=True)
    Status = models.CharField(choices=Status_Choice,max_length=100,default='Pending')