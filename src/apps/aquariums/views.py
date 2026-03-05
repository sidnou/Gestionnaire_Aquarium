from django.shortcuts import render
from .models import Aquarium
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent # dossier src

APP_VERSION = (BASE_DIR / "VERSION").read_text().strip()

# Create your views here.

def accueil(request):
    context = {
        "titre": "Bienvenue sur le gestionnaire d'aquarium",
        "version": APP_VERSION,
        "liste_aquariums": Aquarium.objects.all()

    }

    return render(request, 'aquariums/index.html',context)

def tableau_bord(request):
    context = {
        "titre": "Tableau de bord",
        "version": APP_VERSION,

    }

    return render(request, 'aquariums/dashboard.html',context)