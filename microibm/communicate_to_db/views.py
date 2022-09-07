import datetime
import json

from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from django.http import HttpResponse
from . import models


# Create your views here.
class GuestConnector(View):
    def post(self, request: WSGIRequest, *args, **kwargs):
        data = json.loads(request.body)
        models.Responces(name=data.get('name'), email=data.get('email', ''),
                         comment=data.get('comment'), createdAt=data.get('createdAt', datetime.datetime.now())).save()
        print(data)
        return HttpResponse(data)

    def get(self, request, *args, **kwargs):
        return HttpResponse('12')
