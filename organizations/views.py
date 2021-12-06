from django.db.models import query
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from rest_framework.decorators import permission_classes
from drivers.models import Driver
from organizations.serializers import DriverSerializer

# Create your views here.
def homeview(request):
    template = "index.html"
    context = {
        "drivers":Driver.objects.all()
    }
    return render(request, template, context)
def CreateDriver(request):
    if request.method == "POST":
        name = request.POST.get('name', None)
        Driver.objects.create(name=name)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

class DriverViewSet(ModelViewSet):
    serializer_class = DriverSerializer
    queryset = Driver.objects.all()
    permission_classes=[AllowAny,]