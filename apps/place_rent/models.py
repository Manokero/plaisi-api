from django.db import models

# Create your models here.
SD = 'SD'
SC = 'SC'
SA = 'SA'

CITIES_DOMINICAN_REPUBLIC = [
    (SD, 'Santo Domingo'),
    (SC, 'San Cristobal'),
    (SA, 'Santiago'),
]

class HouseRent(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    bedroom_number = models.SmallIntegerField()
    bathroom_number = models.SmallIntegerField()
    construcction_size = models.IntegerField()
    solar_size = models.IntegerField()
    price = models.FloatField()
    city = models.CharField(max_length=4, choices=YEAR_IN_SCHOOL_CHOICES, default=FRESHMAN)
    # photos
    