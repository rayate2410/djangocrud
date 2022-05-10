from django.contrib import admin

from .models import Address

# Register your models here.
class AddressAdmin(admin.ModelAdmin):
    list_display = ('user', 'full_name', 'address_first_line', 'address_second_line', 'landmark', 'pincode', 'town_or_city', 'state', 'address_type')

admin.site.register(Address, AddressAdmin)