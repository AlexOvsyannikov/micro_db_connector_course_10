from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse


# Create your views here.
class GuestConnector(View):
    def get(self):
        return HttpResponse('21')

