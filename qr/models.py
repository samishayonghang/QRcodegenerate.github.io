from django.db import models

# Create your models here.
class QRcode(models.Model):
    text=models.CharField(max_length=800)
    fileurl=models.URLField(max_length=100)

