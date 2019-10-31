from django.shortcuts import HttpResponse, get_object_or_404
from flutter_django_test.models import Card
from django.core import serializers


# Create your views here.
def all(request):
    return HttpResponse(serializers.serialize('json', Card.objects.all()))


def spec(request, id: int):
    return HttpResponse(serializers.serialize('json', [Card.objects.get(['id', id])]))
