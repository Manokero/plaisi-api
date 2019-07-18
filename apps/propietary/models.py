from django.db import models
from django.conf import settings
from .helpers import propietary_legal_documents_path
from plaisi_api.bus.enums import EnumProvincesDominicanRepublic

cities_dr = EnumProvincesDominicanRepublic


class Propietary(models.Model):
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


class PropietaryLegalDoc(models.Model):
    propietary = models.ForeignKey(Propietary, on_delete=models.CASCADE)
    document = models.FileField(
        upload_to=propietary_legal_documents_path
    )
    name = models.CharField(max_length=50)
    description = models.TextField()
    is_deleted = models.BooleanField(default=False)