from django.shortcuts import render
from pathlib import Path


# Create your views here.
BASE_DIR = Path(__file__).resolve().parent.parent.parent # dossier src

APP_VERSION = (BASE_DIR / "VERSION").read_text().strip()
def appareils(request):
    context = {
        "titre": "Appariels",
        'version': APP_VERSION
    }
    return render(request,"appareils/index.html",context)