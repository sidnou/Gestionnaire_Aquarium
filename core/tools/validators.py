from django.core.validators import RegexValidator


LETTRE_ESPACE_TIRET_VALIDATEUR = RegexValidator(r"^[a-zA-ZÀ-ÖØ-öø-ÿ' -]+$")