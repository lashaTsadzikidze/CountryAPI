from django.db import models

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=250)
    capital_city = models.CharField(max_length=100)
    population = models.IntegerField()
    area = models.FloatField()
    official_languages = models.CharField(max_length=300)
    continent = models.CharField(max_length=100)
    main_cities = models.TextField()
    climate = models.FloatField()
    currency = models.CharField(max_length=20)
    gdp = models.FloatField()

    def __str__(self):
        return self.name