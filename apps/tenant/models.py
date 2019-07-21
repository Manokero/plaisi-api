from django.db import models
from django.conf import settings
from plaisi_api.bus.enums import EnumProvincesDominicanRepublic

cities_dr = EnumProvincesDominicanRepublic
# Create your models here.

class Tenant(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    phone = models.CharField(max_length=20)
    address = models.TextField(blank=True, null=True)
    province = models.CharField(
        choices=cities_dr.as_tuple(),
        default=cities_dr.get_default(),
        max_length=4
    )

    def __str__(self):
        return self.user.username



