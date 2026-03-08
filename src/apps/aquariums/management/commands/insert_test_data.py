"""
Commande Django pour insérer des données de test dans l'application Gestionnaire d'Aquarium

Ce script crée des données d'exemple réalistes pour :
- Aquariums (3 types différents)
- Analyses d'eau avec paramètres chimiques
- Changements d'eau avec mélanges osmose/robinet
- Traitements avec produits courants
- Espèces de poissons et invertébrés
- Plantes aquatiques avec exigences
- Équipements (filtres, chauffage, éclairage, etc.)

Usage:
    python manage.py insert_test_data           # Ajoute les données de test
    python manage.py insert_test_data --clear   # Supprime d'abord les données existantes
"""

from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import datetime, date
from apps.aquariums.models import Aquarium, Analyse, ChangeEau, Traitement, Espece, Plante, Equipement


class Command(BaseCommand):
    help = 'Insère des données de test dans toutes les tables de l\'application aquarium'
    
    def add_arguments(self, parser):
        parser.add_argument(
            '--clear',
            action='store_true',
            help='Supprime les données existantes avant d\'insérer les nouvelles données de test',
        )

    def handle(self, *args, **options):
        """
        Insère des données de test réalistes pour le développement et les tests.
        Ces données incluent plusieurs aquariums avec leurs analyses, équipements,
        espèces, plantes, traitements et changements d'eau.
        """
        self.stdout.write(self.style.SUCCESS('Début de l\'insertion des données de test...'))
        
        # Supprimer les données de test existantes si l'option --clear est utilisée
        if options['clear']:
            self.stdout.write('Suppression des données de test existantes...')
            Equipement.objects.all().delete()
            Plante.objects.all().delete() 
            Espece.objects.all().delete()
            Traitement.objects.all().delete()
            ChangeEau.objects.all().delete()
            Analyse.objects.all().delete()
            Aquarium.objects.all().delete()
            self.stdout.write(self.style.WARNING('✅ Données existantes supprimées'))
        
        # Créer des aquariums
        self.stdout.write('Création des aquariums...')
        aquarium1 = Aquarium.objects.create(
            nom="Aquarium Communautaire",
            volume_eau=200,
            date_mise_en_service=date(2024, 1, 15),
            commentaire="Aquarium principal avec poissons tropicaux"
        )
        
        aquarium2 = Aquarium.objects.create(
            nom="Aquarium Cichlidés",
            volume_eau=300,
            date_mise_en_service=date(2024, 3, 10),
            commentaire="Aquarium spécialisé pour cichlidés africains"
        )
        
        aquarium3 = Aquarium.objects.create(
            nom="Nano Aquarium",
            volume_eau=60,
            date_mise_en_service=date(2024, 6, 5),
            commentaire="Petit aquarium pour crevettes et poissons nains"
        )
        
        # Créer des analyses d'eau
        self.stdout.write('Création des analyses d\'eau...')
        Analyse.objects.create(
            aquarium=aquarium1,
            date_analyse=date(2025, 4, 5),
            no2=0.1,
            no3=15.0,
            ph=7.2,
            nh4=0.0,
            kh=4.5,
            gh=8.0,
            sio2=2.1,
            po4=0.5,
            mg=12.5,
            fe=0.1,
            cu=0.02,
            tds=250,
            observation="Paramètres stables"
        )
        
        Analyse.objects.create(
            aquarium=aquarium2,
            date_analyse=date(2025,6,15),
            no2=0.0,
            no3=20.0,
            ph=8.1,
            nh4=0.0,
            kh=12.0,
            gh=15.0,
            sio2=1.5,
            po4=0.3,
            mg=25.0,
            fe=0.05,
            cu=0.01,
            tds=320,
            observation="Eau dure adaptée aux cichlidés"
        )
        
        Analyse.objects.create(
            aquarium=aquarium3,
            date_analyse=date(2025,7,25),
            no2=0.05,
            no3=10.0,
            ph=6.8,
            nh4=0.1,
            kh=2.0,
            gh=5.0,
            sio2=3.0,
            po4=0.8,
            mg=8.0,
            fe=0.2,
            cu=0.03,
            tds=180,
            observation="Eau douce pour plantes"
        )
        
        # Créer des changements d'eau
        self.stdout.write('Création des changements d\'eau...')
        ChangeEau.objects.create(
            aquarium=aquarium1,
            date_change_eau=date(2024, 11, 1),
            quantite_litre=50,
            osmose_pourcentage=70,
            robinet_pourcentage=30
        )
        
        ChangeEau.objects.create(
            aquarium=aquarium2,
            date_change_eau=date(2024, 11, 2),
            quantite_litre=75,
            osmose_pourcentage=30,
            robinet_pourcentage=70
        )
        
        ChangeEau.objects.create(
            aquarium=aquarium3,
            date_change_eau=date(2024, 11, 3),
            quantite_litre=20,
            osmose_pourcentage=90,
            robinet_pourcentage=10
        )
        
        # Créer des traitements
        self.stdout.write('Création des traitements...')
        Traitement.objects.create(
            aquarium=aquarium1,
            nom_produit="Easy-Life Fluid Filter Medium",
            quantite=10,
            date_traitement=date(2024, 10, 15)
        )
        
        Traitement.objects.create(
            aquarium=aquarium1,
            nom_produit="Seachem Flourish",
            quantite=5,
            date_traitement=date(2024, 10, 20)
        )
        
        Traitement.objects.create(
            aquarium=aquarium2,
            nom_produit="JBL pH-Plus",
            quantite=15,
            date_traitement=date(2024, 10, 18)
        )
        
        Traitement.objects.create(
            aquarium=aquarium3,
            nom_produit="Tetra CO2 Plus",
            quantite=3,
            date_traitement=date(2024, 10, 25)
        )
        
        # Créer des espèces
        self.stdout.write('Création des espèces...')
        Espece.objects.create(
            aquarium=aquarium1,
            nom_espece="Néon Bleu",
            type_espece="Characidé",
            nombre_espece=15,
            paramettre_min_ph=6.0,
            paramettre_max_ph=7.5,
            paramettre_eau="DOUCE"
        )
        
        Espece.objects.create(
            aquarium=aquarium1,
            nom_espece="Guppy",
            type_espece="Poeciliidae",
            nombre_espece=8,
            paramettre_min_ph=6.8,
            paramettre_max_ph=8.0,
            paramettre_eau="MOYENNEMENT_DURE"
        )
        
        Espece.objects.create(
            aquarium=aquarium2,
            nom_espece="Cichlidé Zèbre",
            type_espece="Cichlidae",
            nombre_espece=6,
            paramettre_min_ph=7.5,
            paramettre_max_ph=8.5,
            paramettre_eau="DURE"
        )
        
        Espece.objects.create(
            aquarium=aquarium3,
            nom_espece="Crevette Red Cherry",
            type_espece="Caridina",
            nombre_espece=20,
            paramettre_min_ph=6.2,
            paramettre_max_ph=7.2,
            paramettre_eau="DOUCE"
        )
        
        # Créer des plantes
        self.stdout.write('Création des plantes...')
        Plante.objects.create(
            aquarium=aquarium1,
            nom_plante="Echinodorus Amazon",
            emplacement_aquarium="ARRIERE PLAN",
            paramettre_min_ph=6.0,
            paramettre_max_ph=7.8,
            paramettre_min_co2=10.0,
            paramettre_max_co2=30.0
        )
        
        Plante.objects.create(
            aquarium=aquarium1,
            nom_plante="Anubias Nana",
            emplacement_aquarium="SUR OBJET",
            paramettre_min_ph=6.0,
            paramettre_max_ph=8.0,
            paramettre_min_co2=5.0,
            paramettre_max_co2=25.0
        )
        
        Plante.objects.create(
            aquarium=aquarium2,
            nom_plante="Vallisneria",
            emplacement_aquarium="ARRIERE PLAN",
            paramettre_min_ph=6.5,
            paramettre_max_ph=8.5,
            paramettre_min_co2=8.0,
            paramettre_max_co2=35.0
        )
        
        Plante.objects.create(
            aquarium=aquarium3,
            nom_plante="Mousse de Java",
            emplacement_aquarium="SUR OBJET",
            paramettre_min_ph=5.5,
            paramettre_max_ph=8.0,
            paramettre_min_co2=3.0,
            paramettre_max_co2=20.0
        )
        
        Plante.objects.create(
            aquarium=aquarium3,
            nom_plante="Riccia Fluitans",
            emplacement_aquarium="FLOTANTE",
            paramettre_min_ph=6.0,
            paramettre_max_ph=7.5,
            paramettre_min_co2=15.0,
            paramettre_max_co2=40.0
        )
        
        # Créer des équipements
        self.stdout.write('Création des équipements...')
        Equipement.objects.create(
            aquarium=aquarium1,
            type_equipement="Filtre",
            nom_equipement="Eheim Classic 250",
            date_installation=date(2024, 1, 15),
            carateristique="Débit: 440 L/h, Volume: jusqu'à 250L",
            commentaire="Filtre externe très silencieux"
        )
        
        Equipement.objects.create(
            aquarium=aquarium1,
            type_equipement="Chauffage",
            nom_equipement="Aquael Ultra Heater 100W",
            date_installation=date(2024, 1, 15),
            carateristique="Puissance: 100W, Réglable 20-33°C",
            commentaire="Chauffage électronique avec thermostat intégré"
        )
        
        Equipement.objects.create(
            aquarium=aquarium1,
            type_equipement="Éclairage",
            nom_equipement="Fluval Plant 3.0 LED",
            date_installation=date(2024, 2, 1),
            carateristique="46W, Spectre complet, Programmable",
            commentaire="Éclairage LED pour plantes avec contrôleur"
        )
        
        Equipement.objects.create(
            aquarium=aquarium2,
            type_equipement="Filtre",
            nom_equipement="Fluval FX4",
            date_installation=date(2024, 3, 10),
            carateristique="Débit: 2650 L/h, Volume: jusqu'à 1000L",
            commentaire="Filtre haute performance pour gros bac"
        )
        
        Equipement.objects.create(
            aquarium=aquarium2,
            type_equipement="Pompe à air",
            nom_equipement="Tetra APS 400",
            date_installation=date(2024, 3, 12),
            carateristique="Débit air: 400L/h, 2 sorties",
            commentaire="Pour oxygénation supplémentaire"
        )
        
        Equipement.objects.create(
            aquarium=aquarium3,
            type_equipement="Filtre",
            nom_equipement="Eden 501 Nano",
            date_installation=date(2024, 6, 5),
            carateristique="Débit: 150 L/h, Volume: 30-60L",
            commentaire="Parfait pour nano aquarium"
        )
        
        Equipement.objects.create(
            aquarium=aquarium3,
            type_equipement="CO2",
            nom_equipement="JBL ProFlora u95",
            date_installation=date(2024, 6, 10),
            carateristique="Kit CO2 jetable, régulateur intégré",
            commentaire="Système CO2 simple pour débuter"
        )
        
        # Messages de fin
        self.stdout.write(self.style.SUCCESS('✅ Données de test insérées avec succès !'))
        self.stdout.write(self.style.SUCCESS(f'   - {Aquarium.objects.count()} aquariums créés'))
        self.stdout.write(self.style.SUCCESS(f'   - {Analyse.objects.count()} analyses créées'))
        self.stdout.write(self.style.SUCCESS(f'   - {ChangeEau.objects.count()} changements d\'eau créés'))
        self.stdout.write(self.style.SUCCESS(f'   - {Traitement.objects.count()} traitements créés'))
        self.stdout.write(self.style.SUCCESS(f'   - {Espece.objects.count()} espèces créées'))
        self.stdout.write(self.style.SUCCESS(f'   - {Plante.objects.count()} plantes créées'))
        self.stdout.write(self.style.SUCCESS(f'   - {Equipement.objects.count()} équipements créés'))
        self.stdout.write('')
        self.stdout.write(self.style.SUCCESS('Pour lancer ce script :'))
        self.stdout.write(self.style.SUCCESS('  python manage.py insert_test_data           # Ajouter les données de test'))
        self.stdout.write(self.style.SUCCESS('  python manage.py insert_test_data --clear   # Supprimer puis ajouter'))