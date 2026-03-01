from django.contrib import admin
from .models import Aquarium,Analyse,ChangeEau,Traitement
# Register your models here.

@admin.register(Aquarium)
class AquariumAdmin(admin.ModelAdmin):
    pass
@admin.register(Analyse)
class AnalyseAdmin(admin.ModelAdmin):
    pass
@admin.register(ChangeEau)
class ChangeEauAdmin(admin.ModelAdmin):
    pass
@admin.register(Traitement)
class TraitementAdmin(admin.ModelAdmin):
    pass