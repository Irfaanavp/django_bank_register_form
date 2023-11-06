from django.db import models

# Create your models here.

class Userform(models.Model):
    name = models.CharField(max_length=100)
    username=models.CharField(max_length=100)
    dob = models.DateField()
    gender = models.CharField(max_length=10, choices=(('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')))
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    district = models.CharField(max_length=50)
    branch = models.CharField(max_length=50)
    account_type = models.CharField(max_length=20, choices=(('Savings Account', 'Savings Account'), ('Current Account', 'Current Account')))
    # materials_provide = models.ManyToManyField(Material, blank=True)
    class Meta:
        app_label = 'bankapp'