from django.db import models

# Create your models here.
class Aquarium(models.Model):
    nom = models.CharField(max_length=25)
    volume_eau = models.IntegerField()
    date_mise_en_service = models.DateField()
    commentaire = models.TextField()
    def __str__(self):
        return self.nom
class Analyse(models.Model):
    aquarium = models.ForeignKey(Aquarium,on_delete=models.CASCADE)
    date_analyse = models.DateField()
    no2 = models.FloatField(max_length=5)
    no3 = models.FloatField(max_length=5)
    ph = models.FloatField(max_length=5)
    nh4 = models.FloatField(max_length=5)
    kh = models.FloatField(max_length=5)
    gh = models.FloatField(max_length=5)
    sio2 = models.FloatField(max_length=5)
    po4 = models.FloatField(max_length=5)
    mg = models.FloatField(max_length=5)
    fe = models.FloatField(max_length=5)
    cu = models.FloatField(max_length=5)
    tds = models.IntegerField()
    observation = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.aquarium} {self.no2} "


class ChangeEau(models.Model):
    aquarium = models.ForeignKey(Aquarium,on_delete=models.CASCADE)
    date_change_eau  = models.DateField()
    quantite_litre = models.IntegerField()
    osmose_pourcentage = models.IntegerField()
    robinet_pourcentage = models.IntegerField()

class Traitement(models.Model):
    aquarium = models.ForeignKey(Aquarium,on_delete=models.CASCADE)
    nom_produit = models.CharField(max_length=25)
    quantite = models.IntegerField( help_text="en ml")
    date_traitement = models.DateField()

class Espece(models.Model):
        # Choix de dureté de l'eau
    DURTEE_CHOIX = [
            ("TRES_DOUCE", "Très douce (0-4 °dGH)"),
            ("DOUCE", "Douce (4-8 °dGH)"),
            ("MOYENNEMENT_DURE", "Moyennement dure (8-12 °dGH)"),
            ("LEGEREMENT_DURE", "Légèrement dure (12-18 °dGH)"),
            ("DURE", "Dure (18-25 °dGH)"),
            ("TRES_DURE", "Très dure (>25 °dGH)"),
    ]

    aquarium = models.ForeignKey(Aquarium,on_delete=models.CASCADE)
    nom_espece = models.CharField(max_length=25)
    type_espece = models.CharField(max_length=25)
    nombre_espece = models.IntegerField()
    paramettre_min_ph = models.FloatField()
    paramettre_max_ph = models.FloatField()
    paramettre_eau = models.CharField(max_length=25)
class Plante(models.Model):
    EMPLACEMENT_CHOIX = [
        ("ARRIERE PLAN","Arrière Plan"),
        ("MILIEU PLAN", "Milieu Plan"),
        ("PREMIER PLAN", "Premier Plan"),
        ("SUR OBJET","Sur Objet"),
        ("FLOTANTE","Flottante"),
        ("N'IMPORTE OU","N'importe où"),
    ]
    aquarium = models.ForeignKey(Aquarium,on_delete=models.CASCADE)
    nom_plante = models.CharField(max_length=25)
    emplacement_aquarium = models.CharField(max_length=25,choices=EMPLACEMENT_CHOIX)
    paramettre_min_ph = models.FloatField()
    paramettre_max_ph = models.FloatField()
    paramettre_min_co2 = models.FloatField()
    paramettre_max_co2 = models.FloatField()



class Equipement(models.Model):
    aquarium = models.ForeignKey(Aquarium,on_delete=models.CASCADE)
    type_equipement = models.CharField(max_length=100)
    nom_equipement = models.CharField(max_length=100)
    date_installation = models.DateField()
    carateristique = models.TextField(null=True, blank=True)
    commentaire = models.TextField(null=True, blank=True)    
