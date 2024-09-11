from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField()
    location = models.CharField(max_length=255)

class Ticket(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True)
    barcode = models.ImageField(upload_to='barcodes/', blank=True)