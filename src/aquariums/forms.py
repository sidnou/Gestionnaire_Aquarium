from django import forms
from .models import Aquarium, Analyse, Plante, Espece, ChangeEau, Equipement, Traitement


class AquariumForm(forms.ModelForm):
    class Meta:
        model = Aquarium
        fields = "__all__"


class AnalyseForm(forms.ModelForm):
    class Meta:
        model = Analyse
        fields = "__all__"


class TraitementForm(forms.ModelForm):
    class Meta:
        model = Traitement
        fields = "__all__"


class EspeceForm(forms.ModelForm):
    class Meta:
        model = Espece
        fields = "__all__"


class PlanteForm(forms.ModelForm):
    class Meta:
        model = Plante
        fields = "__all__"


class ChangeEauForm(forms.ModelForm):
    class Meta:
        model = ChangeEau
        fields = "__all__"


class EquipementForm(forms.ModelForm):
    class Meta:
        model = Equipement
        fields = "__all__"
