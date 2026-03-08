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


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.accueil,name='accueil'),
    path("tableau-bord/",views.tableau_bord,name="tableau_bord"),
    path("analyses/",views.analyse,name="analyses"),
    path("traitements/",views.traitement,name="traitements"),
    path("especes/",views.espece,name="especes"),
    path("plantes/",views.plante,name="plantes"),
    path("equipements/",views.equipement,name="equipements")
    
]
