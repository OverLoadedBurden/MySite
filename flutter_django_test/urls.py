from django.urls import path
from flutter_django_test.views import spec, all

urlpatterns = [
    path(r'', all),
    path(r'^/%d$/', spec)
]
