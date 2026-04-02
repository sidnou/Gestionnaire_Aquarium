from django.db import models

from aquariums.models import Aquarium


# Create your models here.
class Appareil(models.Model):
    nom_appreil = models.CharField(max_length=100)
    type_appareil = models.CharField(max_length=100)
    aquarium = models.ForeignKey(Aquarium,on_delete=models.CASCADE)
    adresse_ip = models.GenericIPAddressField(null=True,blank=True)
    date_ajout = models.DateField(null=True,blank=True)
    active = models.BooleanField(default=True)


class ConfigurationAppareil(models.Model):
    appareil = models.ForeignKey(Appareil,on_delete=models.CASCADE)
    version_configuration = models.CharField(max_length=20)
    fichier_configuration = models.FileField(upload_to='confg_appareil/')
