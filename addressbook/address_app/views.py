from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Address

from django.views.generic.edit import CreateView, DeleteView, UpdateView

# Create your views here.

def address_list(request):
    address_list = Address.objects.filter(user=request.user)
    return render(request, 'address/address_list.html', {'address_list': address_list})


class AddressCreateView(CreateView):
    model = Address
    template_name = "address/address_form.html"
    fields = ('__all__')
    success_url = reverse_lazy('address_list')


class AddressUpdateView(UpdateView):
    model = Address
    template_name = "address/address_form.html"
    fields = ('__all__')
    success_url = reverse_lazy('address_list')


class AddressDeleteView(DeleteView):
    model = Address
    template_name = "address/address_confirm_delete.html"
    success_url = reverse_lazy('address_list')

