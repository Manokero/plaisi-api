from django.db import models
from .helpers import user_house_directory_path
from plaisi_api.bus.enums import *
from apps.proprietary.models import Proprietary
from apps.tenant.models import Tenant

cities_dr = EnumProvincesDominicanRepublic


class House(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    bedroom_number = models.SmallIntegerField(blank=True, null=True)
    bathroom_number = models.SmallIntegerField(blank=True, null=True)
    construcction_size = models.IntegerField(blank=True, null=True)
    solar_size = models.IntegerField(blank=True, null=True)
    price = models.FloatField()
    city = models.CharField(max_length=4, choices=cities_dr.as_tuple(), default=cities_dr.get_default())
    deleted = models.BooleanField(default=False)
    proprietary = models.ForeignKey(Proprietary, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title


class HouseRent(models.Model):
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    obtention_date = models.DateField()
    begin_living_date = models.DateField()
    is_active = models.BooleanField(default=False)
    # payment_amount = models.PositiveIntegerField()


class HouseImage(models.Model):
    house = models.ForeignKey(House, null=True,
            on_delete=models.DO_NOTHING)
    image = models.ImageField(upload_to=user_house_directory_path)
    description = models.TextField(blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
