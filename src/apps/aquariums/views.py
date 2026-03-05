from django.shortcuts import render

# Create your views here.

def accueil(request):
    context = {
        "titre": "Bienvenue sur le gestionnaire d'aquarium",
        "version": "0.0.1dev",

    }

    return render(request, 'aquariums/index.html',context)

def tableau_bord(request):
    context = {
        "titre": "Tableau de bord",
        "version": "0.0.1dev",

    }

    return render(request, 'aquariums/dashboard.html',context)