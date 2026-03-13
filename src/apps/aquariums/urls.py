"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from .views import ajout_equipement

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.accueil, name='accueil'),
    path('aquariums/',views.accueil,name="aquariums"),
    path("tableau-bord/", views.tableau_bord, name="tableau_bord"),
    path("analyses/", views.analyse, name="analyses"),
    path("analyses/<int:aquarium_id>/", views.analyse_detail_aquarium, name="analyse_detail_aquarium"),
    path("analyses/ajout/", views.ajout_analyse, name="ajout_analyse"),
    path("traitements/", views.traitement, name="traitements"),
    path("traitements/ajout/",views.ajout_traitement,name="ajout_traitement"),
    path("especes/", views.espece, name="especes"),
    path("especes/ajout/", views.ajout_espece, name="ajout_espece"),
    path("plantes/", views.plante, name="plantes"),
    path("plantes/ajout/",views.ajout_plante,name="ajout_plante"),
    path("equipements/", views.equipement, name="equipements"),
    path("equipements/ajout/",views.ajout_equipement,name="ajout_equipement"),
    path("aquariums/ajout/", views.ajout_aquarium, name="ajout_aquarium"),

]
