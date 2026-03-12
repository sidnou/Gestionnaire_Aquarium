from django.shortcuts import render
from .models import Aquarium, Analyse, Traitement, Espece, Plante, Equipement, ChangeEau
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent  # dossier src

APP_VERSION = (BASE_DIR / "VERSION").read_text().strip()


# Create your views here.

def accueil(request):
    context = {
        "titre": "Bienvenue sur le gestionnaire d'aquarium",
        "version": APP_VERSION,
        "liste_aquariums": Aquarium.objects.all()

    }

    return render(request, 'aquariums/index.html', context)


def tableau_bord(request):
    aquariums = Aquarium.objects.all()
    aquariums_detail = []
    for aquarium in aquariums:
        aquariums_detail.append(
            {
                "aquariums": aquarium,
                "especes": Espece.objects.filter(aquarium=aquarium),
                "plantes": Plante.objects.filter(aquarium=aquarium),
                "analyses":Analyse.objects.filter(aquarium=aquarium), # TODO: Afficher la dernière analyse
            }
        )

    context = {
        "titre": "Tableau de bord",
        "version": APP_VERSION,
        'liste_aquariums_detail': aquariums_detail,
    }
    return render(request, 'aquariums/tableau-bord.html', context)


def analyse(request):
    context = {
        "titre": "Analyses d'Aquarium",
        "version": APP_VERSION,
        "liste_analyses": Analyse.objects.all()

    }

    return render(request, 'aquariums/analyses.html', context)

def analyse_detail_aquarium(request,aquarium_id):
    context = {
        "titre": "Analyses d'Aquarium",
        "version": APP_VERSION,
        "liste_analyses": Analyse.objects.filter(aquarium_id=aquarium_id),
        "liste_changements_eau": ChangeEau.objects.filter(aquarium=aquarium_id),
        "liste_traitements": Traitement.objects.filter(aquarium=aquarium_id),
        "liste_especes": Espece.objects.filter(aquarium=aquarium_id),
        "liste_plantes": Plante.objects.filter(aquarium=aquarium_id),
        "liste_equipements": Equipement.objects.filter(aquarium=aquarium_id)


    }
    return render(request,'aquariums/analyse-detail-aquarium.html',context)

def traitement(request):
    context = {
        "titre": "Traitement",
        "version": APP_VERSION,
        "liste_traitements": Traitement.objects.all(),
    }

    return render(request, "aquariums/traitements.html", context)


def espece(request):
    context = {
        "titre": "Les Espèces",
        "version": APP_VERSION,
        "liste_especes": Espece.objects.all()
    }

    return render(request, "aquariums/especes.html", context)


def plante(request):
    context = {
        "titre": "Les Plantes",
        "version": APP_VERSION,
        "liste_plantes": Plante.objects.all(),

    }

    return render(request, "aquariums/plantes.html", context)


def equipement(request):
    context = {
        "titre": "Equipements",
        "version": APP_VERSION,
        "liste_equipements": Equipement.objects.all(),

    }

    return render(request, "aquariums/equipements.html", context)
