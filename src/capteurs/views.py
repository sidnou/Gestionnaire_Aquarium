from django.shortcuts import render
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent.parent # dossier src

APP_VERSION = (BASE_DIR / "VERSION").read_text().strip()

# Create your views here.
def capteur(request):
    context = {
        "titre" : "Liste des Capteurs",
        'version': APP_VERSION,

    }

    return render(request,'capteurs/index.html',context)