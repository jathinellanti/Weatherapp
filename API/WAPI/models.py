from django.db import models

class City(models.Model):
    objects = None
    name = models.CharField(max_length=100)
    temperature = models.DecimalField(max_digits=5, decimal_places=2,null=True)
    humidity = models.DecimalField(max_digits=5, decimal_places=2,null=True)
    weather_condition = models.CharField(max_length=100)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self): #show the actual city name on the dashboard
        return self.name


    class Meta: #show the plural of city as cities instead of citys
        verbose_name_plural = 'cities'
