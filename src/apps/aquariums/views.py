from django.shortcuts import render, redirect
from .models import Aquarium, Analyse, Traitement, Espece, Plante, Equipement, ChangeEau
from .forms import AquariumForm, AnalyseForm, EspeceForm, PlanteForm, TraitementForm, EquipementForm, ChangeEauForm
from pathlib import Path
from datetime import date

ANNEE = str(date.today().year)

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent  # dossier src

APP_VERSION = (BASE_DIR / "VERSION").read_text().strip()


# Create your views here.

def accueil(request):
    context = {
        "titre": "Bienvenue sur le gestionnaire d'aquarium",
        "version": APP_VERSION,
        "annee" : ANNEE,
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
                "analyses": Analyse.objects.filter(aquarium=aquarium),  # TODO: Afficher la dernière analyse
            }
        )

    context = {
        "titre": "Tableau de bord",
        "version": APP_VERSION,
        "annee": ANNEE,
        'liste_aquariums_detail': aquariums_detail,
    }
    return render(request, 'aquariums/tableau-bord.html', context)


def analyse(request):
    context = {
        "titre": "Analyses d'Aquarium",
        "version": APP_VERSION,
        "annee": ANNEE,
        "liste_analyses": Analyse.objects.all(),


    }

    return render(request, 'aquariums/analyses.html', context)


def analyse_detail_aquarium(request, aquarium_id):
    context = {
        "titre": "Analyses d'Aquarium",
        "version": APP_VERSION,
        "annee": ANNEE,
        "liste_analyses": Analyse.objects.filter(aquarium_id=aquarium_id),
        "liste_changements_eau": ChangeEau.objects.filter(aquarium=aquarium_id),
        "liste_traitements": Traitement.objects.filter(aquarium=aquarium_id),
        "liste_especes": Espece.objects.filter(aquarium=aquarium_id),
        "liste_plantes": Plante.objects.filter(aquarium=aquarium_id),
        "liste_equipements": Equipement.objects.filter(aquarium=aquarium_id)

    }
    return render(request, 'aquariums/analyse-detail-aquarium.html', context)


def traitement(request):
    context = {
        "titre": "Traitement",
        "version": APP_VERSION,
        "annee": ANNEE,
        "liste_traitements": Traitement.objects.all(),
    }

    return render(request, "aquariums/traitements.html", context)


def espece(request):
    context = {
        "titre": "Les Espèces",
        "version": APP_VERSION,
        "annee": ANNEE,
        "liste_especes": Espece.objects.all()
    }

    return render(request, "aquariums/especes.html", context)


def plante(request):
    context = {
        "titre": "Les Plantes",
        "version": APP_VERSION,
        "annee": ANNEE,
        "liste_plantes": Plante.objects.all(),

    }

    return render(request, "aquariums/plantes.html", context)


def equipement(request):
    context = {
        "titre": "Equipements",
        "version": APP_VERSION,
        "annee": ANNEE,
        "liste_equipements": Equipement.objects.all(),

    }

    return render(request, "aquariums/equipements.html", context)


def change_eau(request):
    context = {
        "titre": "Changement d'Eaux",
        "version": APP_VERSION,
        "annee": ANNEE,
        "change_eaux": ChangeEau.objects.all(),

    }

    return render(request, "aquariums/change-d-eaux.html", context)


def ajout_aquarium(request):
    context = {
        "titre": "Ajout Aquarium",
        "version": APP_VERSION,
        "annee": ANNEE,
        "liste_aquariums": Aquarium.objects.all(),
        "formulaire_aquarium": AquariumForm()
    }
    if request.method == "POST":
        form = AquariumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("aquariums")

    return render(request, "aquariums/ajout-aquarium.html", context)


def ajout_analyse(request):
    context = {
        "titre": "Ajout Analyse",
        "version": APP_VERSION,
        "annee": ANNEE,
        "liste_analyses": Analyse.objects.all(),
        'formulaire_analyse': AnalyseForm(),
        "url_name": 'ajout_analyse',
    }
    if request.method == "POST":
        form = AnalyseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("analyses")

    return render(request, "aquariums/ajout-analyse.html", context)


def ajout_espece(request):
    context = {
        "titre": "Ajout Espèce",
        "version": APP_VERSION,
        "annee": ANNEE,
        "liste_especes": Espece.objects.all(),
        'formulaire_espece': EspeceForm()
    }
    if request.method == "POST":
        form = EspeceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("especes")

    return render(request, "aquariums/ajout-espece.html", context)


def ajout_plante(request):
    context = {
        "titre": "Ajout Plante",
        "version": APP_VERSION,
        "annee": ANNEE,
        "liste_plantes": Plante.objects.all(),
        'formulaire_plante': PlanteForm()
    }

    if request.method == "POST":
        form = PlanteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("plantes")

    return render(request, "aquariums/ajout-plante.html", context)


def ajout_traitement(request):
    context = {
        "titre": "Ajout Traitement",
        "version": APP_VERSION,
        "annee": ANNEE,
        "liste_traitements": Traitement.objects.all(),
        "formulaire_traitement": TraitementForm(),
    }
    if request.method == "POST":
        form = TraitementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("traitements")

    return render(request, "aquariums/ajout-traitement.html", context)


def ajout_equipement(request):
    context = {
        "titre": "Ajout Équipement",
        "version": APP_VERSION,
        "annee": ANNEE,
        "liste_equipement": Equipement.objects.all(),
        "formulaire_equipement": EquipementForm()
    }

    if request.method == "POST":
        form = EquipementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("equipements")

    return render(request, "aquariums/ajout-equipement.html", context)


def ajout_change_eau(request):
    context = {
        "titre": "Ajout Changement d'eau",
        "version": APP_VERSION,
        "annee": ANNEE,
        "liste_change_eaux": ChangeEau.objects.all(),
        "formulaire_change_eau": ChangeEauForm(),
    }

    if request.method == "POST":
        form = ChangeEauForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("change_eaux")

    return render(request, 'aquariums/ajout-change-eau.html',context)

# TODO: Créer un fichier test pour test tous les vues
