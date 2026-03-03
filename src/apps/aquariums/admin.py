from django.contrib import admin
from .models import Aquarium, Analyse, ChangeEau, Traitement, Espece, Plante


# Register your models here.

@admin.register(Aquarium)
class AquariumAdmin(admin.ModelAdmin):
    list_display = ["nom", "volume_eau", "date_mise_en_service", "commentaire"]


@admin.register(Analyse)
class AnalyseAdmin(admin.ModelAdmin):
    list_display = ["aquarium","no2", "no3", "nh4", "ph", "po4", "kh", "gh", "mg", "fe", "cu", "tds", "observation"]


@admin.register(ChangeEau)
class ChangeEauAdmin(admin.ModelAdmin):
    list_display = ["aquarium","date_change_eau","quantite_litre","osmose_pourcentage","robinet_pourcentage"]


@admin.register(Traitement)
class TraitementAdmin(admin.ModelAdmin):
    list_display = ["aquarium","nom_produit","quantite","date_traitement"]

@admin.register(Espece)
class EspeceAdmin(admin.ModelAdmin):
    list_display = ["aquarium","nom_espece","nombre_espece","paramettre_min_ph","paramettre_max_ph","paramettre_eau"]

@admin.register(Plante)
class PlanteAdmin(admin.ModelAdmin):
    list_display = ["aquarium","nom_plante","emplacement_aquarium","paramettre_min_ph","paramettre_max_ph","paramettre_min_co2","paramettre_max_co2"]