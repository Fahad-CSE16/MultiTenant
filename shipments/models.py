from django.db import models

# Create your models here.
from locations.models import Location
from drivers.models import Driver

class Shipment(models.Model):
     origin = models.ForeignKey(Location, on_delete=models.CASCADE,related_name="shipments")
     destination = models.ForeignKey(Location, on_delete=models.CASCADE)
     driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
     completion = models.DateTimeField()