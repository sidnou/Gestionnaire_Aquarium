from django.db import models



# Create your models here.
class Capteur(models.Model):
    TYPE_CAPTEUR = [
        ("temperature",'Température'),
        ("ph","pH"),
        ("tds","TDS"),
        ("lumiere","Lumière")

    ]

    aquarium = models.ForeignKey('aquariums.Aquarium',on_delete=models.CASCADE)
    type_capteur = models.CharField(max_length=25,choices=TYPE_CAPTEUR)
    esp_id = models.CharField(max_length=100)
    est_active = models.BooleanField(default=True)
