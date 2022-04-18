# Create your views here.

from django.shortcuts import render
from django.views import generic
from ..Services.models import Services


class HomeView(generic.ListView):
    template_name = 'authentication/home.html'
    context_object_name = 'sevices_list'

    def get_queryset(self):
        return Services.objects.order_by('-create_time')[:3]
