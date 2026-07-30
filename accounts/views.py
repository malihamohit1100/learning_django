from django.shortcuts import render
from accounts.forms import ResisterForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
# Create your views here.

class ResisterView(CreateView):
    form_class = ResisterForm
    template_name = 'accounts/resister.html'
    success_url = reverse_lazy('test_view')
