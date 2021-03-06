# Generated by Django 3.2 on 2022-01-11 14:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('City', models.CharField(max_length=100)),
                ('Pin_code', models.IntegerField()),
                ('State', models.CharField(choices=[('Bihar', 'Bihar'), ('west Bengal', 'West Bengal'), ('Utter Pradesh', 'Utter Pradesh'), ('Jharkhand', 'Jharkhand'), ('Delhi', 'Delhi'), ('Kerela', 'Kerala'), ('Maharastra', 'Maharastra'), ('Karnataka', 'Karnataka'), ('Tamil_Nandu', 'Tamil_Nandu'), ('Assam', 'Assam'), ('Manipur', 'Manipur'), ('Mizoram', 'Mizoram'), ('Madhpradesh', 'Madhpradesh')], max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('Selling_price', models.FloatField()),
                ('Discount_price', models.FloatField()),
                ('Brand', models.CharField(max_length=100)),
                ('Description', models.TextField()),
                ('Category', models.CharField(choices=[('mb', 'mobile'), ('so', 'sofa'), ('ele', 'electronice')], max_length=100)),
                ('Product_image', models.ImageField(upload_to='productimg')),
            ],
        ),
        migrations.CreateModel(
            name='orderplaced',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quentity', models.PositiveIntegerField(default=1)),
                ('Order_date', models.DateTimeField(auto_now_add=True)),
                ('Status', models.CharField(choices=[('Accepted', 'Accepted'), ('on The Way', 'on The Way'), ('Delivered', 'Delivered'), ('Cancel', 'Cancel')], default='Pending', max_length=100)),
                ('cutomer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enroll.customer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enroll.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quentity', models.PositiveIntegerField(default=1)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enroll.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
