from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

# Create your models here.
class Login(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_company = models.BooleanField(default=False)

class Customer(models.Model):
    user=models.ForeignKey(Login,on_delete=models.CASCADE,related_name='customer')
    name=models.CharField(max_length=100)
    contact_no=models.CharField(max_length=100)
    email=models.EmailField()
    address=models.TextField()

class Company(models.Model):
    user=models.ForeignKey(Login,on_delete=models.CASCADE,related_name='company')
    name = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.TextField()



class CustomerDonations(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='donations')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='company')
    customer_name = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    medicine_details = models.TextField()
    date = models.DateField(auto_now_add=True)
    company_approved = models.IntegerField(default=0)
    admin_approved = models.IntegerField(default=0)
    contact_no = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.TextField()

class Notifications(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE,related_name='notifications')
    date = models.DateTimeField(auto_now_add=True)
    message = models.CharField(max_length=255)
    read = models.BooleanField(default=False)

class Feedback(models.Model):
    user=models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='customer')
    date=models.DateField(auto_now=True)
    feedback=models.TextField(max_length=30)
    replay=models.CharField(max_length=30,null=True,blank=True)