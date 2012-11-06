from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse
from django.core import serializers
from mizzou.apps.dispatch.models import Dispatch, Type


def map_api(request):
    return render_to_response('points.json', {'points': Dispatch.objects.all()}, mimetype="application/json")
