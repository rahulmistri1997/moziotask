from django.contrib.gis.db import models

# Create your models here.


class Provider(models.Model):
    """ Model for Provider """
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=100)
    language = models.CharField(max_length=120, default='EN')
    currency = models.CharField(max_length=120, default='INR')

    def __str__(self):
        return self.name


class ServiceArea(models.Model):
    """ Model for ServiceArea """
    provider = models.ForeignKey(Provider,related_name='service_areas',
                                 on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    area = models.PolygonField()

    def __str__(self):
        return f"{self.provider} : {self.name}"
