from django.db import models
from django.contrib.auth.models import User
from localflavor.in_.models import INStateField

# Create your models here.

ADDRESS_TYPE_CHOICES = (
    ('home', 'Home'),
    ('work', 'Office/Commercial'),
)

class Address(models.Model):
    """Model class for Address"""
    user = models.ForeignKey(User, blank=False, null=False, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=512, help_text="Full name")
    address_first_line = models.CharField(max_length=512, help_text="Flat, House no., Building, Company, Apartment", null=False, blank=False)
    address_second_line = models.CharField(max_length=512, help_text="Area, Street, Sector, Village", null=True, blank=True)
    landmark = models.CharField(max_length=512, help_text="Landmark", null=True, blank=True)
    pincode = models.IntegerField(help_text="Pin code", null=False, blank=False)
    town_or_city = models.CharField(max_length=512, help_text="Town or City", null=True, blank=True)
    state = INStateField(help_text="State")
    address_type = models.CharField(max_length=10, choices=ADDRESS_TYPE_CHOICES, default='home')