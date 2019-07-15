from django.db import models
from .helpers import user_house_directory_path

# Create your models here.

# TODO: Add Enums in a diferrent file
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
    bedroom_number = models.SmallIntegerField(blank=True, null=True)
    bathroom_number = models.SmallIntegerField(blank=True, null=True)
    construcction_size = models.IntegerField(blank=True, null=True)
    solar_size = models.IntegerField(blank=True, null=True)
    price = models.FloatField()
    city = models.CharField(max_length=4, choices=CITIES_DOMINICAN_REPUBLIC, default=SD)
    deleted = models.BooleanField(default=False)
    # propietary = models.ForeignKey(null=False)
    
    def __str__(self):
        return self.title

class HouseImage(models.Model):
    property_id = models.ForeignKey(HouseRent, null=False, 
        default=1, on_delete=models.DO_NOTHING)
    image = models.ImageField(upload_to=user_house_directory_path)
    uploaded_at = models.DateTimeField(auto_now_add=True)
