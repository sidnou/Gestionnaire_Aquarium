"""
Commande Django pour insérer des données de test dans l'application Gestionnaire d'Aquarium

Ce script crée des données d'exemple réalistes et cohérentes pour :
- Aquariums (10 aquariums de tailles et types variés)
- Analyses d'eau (12 analyses avec paramètres chimiques réalistes)
- Changements d'eau (12 changements avec différents mélanges osmose/robinet)
- Traitements (12 traitements avec des produits courants du marché)
- Espèces (12 espèces de poissons, invertébrés et crevettes)
- Plantes aquatiques (12 plantes avec exigences variées)
- Équipements (12 équipements : filtres, chauffages, éclairages, CO2, etc.)

Les données couvrent différents scénarios :
- Aquariums de 20L (nano) à 600L (grand bac)
- Eau douce, moyennement dure et dure
- Analyses normales et analyses avec des valeurs limites (NO2 élevé, pH extrême)
- Traitements préventifs et curatifs
- Espèces compatibles et espèces nécessitant des paramètres spécifiques
- Plantes de tous les emplacements (arrière-plan, premier plan, flottante, etc.)
- Équipements de différents types et marques

Usage:
    python manage.py insert_test_data           # Ajoute les données de test
    python manage.py insert_test_data --clear   # Supprime d'abord les données existantes
"""

from django.core.management.base import BaseCommand
from datetime import date
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

        # ──────────────────────────────────────────────────────────────
        # Supprimer les données existantes si l'option --clear est utilisée
        # ──────────────────────────────────────────────────────────────
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

        # ══════════════════════════════════════════════════════════════
        # AQUARIUMS (10)
        # Couvre : nano (20-60L), moyen (100-250L), grand (300-600L)
        # Différentes dates de mise en service et usages
        # ══════════════════════════════════════════════════════════════
        self.stdout.write('Création des aquariums...')

        # 1 - Grand bac communautaire tropical classique
        aq1 = Aquarium.objects.create(
            nom="Communautaire Tropical",
            volume_eau=200,
            date_mise_en_service=date(2023, 1, 15),
            commentaire="Aquarium principal avec poissons tropicaux d'eau douce"
        )
        # 2 - Bac spécialisé cichlidés africains (eau dure, pH élevé)
        aq2 = Aquarium.objects.create(
            nom="Cichlidés Malawi",
            volume_eau=350,
            date_mise_en_service=date(2023, 6, 10),
            commentaire="Bac Malawi avec décor rocheux, eau dure"
        )
        # 3 - Nano aquarium pour crevettes (petit volume, eau douce)
        aq3 = Aquarium.objects.create(
            nom="Nano Crevettes",
            volume_eau=30,
            date_mise_en_service=date(2024, 2, 1),
            commentaire="Nano aquarium dédié aux crevettes Red Cherry"
        )
        # 4 - Aquascaping planté haute technologie
        aq4 = Aquarium.objects.create(
            nom="Aquascape Iwagumi",
            volume_eau=120,
            date_mise_en_service=date(2024, 4, 20),
            commentaire="Bac planté style Iwagumi avec injection CO2"
        )
        # 5 - Bac d'élevage / quarantaine (cas limite : très petit)
        aq5 = Aquarium.objects.create(
            nom="Bac Quarantaine",
            volume_eau=20,
            date_mise_en_service=date(2024, 8, 5),
            commentaire="Petit bac sans décor pour quarantaine et traitements"
        )
        # 6 - Grand bac amazonien (eau très douce, pH acide)
        aq6 = Aquarium.objects.create(
            nom="Biotope Amazonien",
            volume_eau=400,
            date_mise_en_service=date(2022, 11, 1),
            commentaire="Biotope Amazonie avec bois, feuilles de catappa"
        )
        # 7 - Bac Tanganyika (eau très dure)
        aq7 = Aquarium.objects.create(
            nom="Cichlidés Tanganyika",
            volume_eau=250,
            date_mise_en_service=date(2023, 9, 15),
            commentaire="Bac Tanganyika avec coquillages et roches calcaires"
        )
        # 8 - Paludarium (cas particulier : aquarium + partie émergée)
        aq8 = Aquarium.objects.create(
            nom="Paludarium Tropical",
            volume_eau=150,
            date_mise_en_service=date(2024, 1, 10),
            commentaire="Paludarium avec partie aquatique et partie terrestre"
        )
        # 9 - Bac eau froide pour poissons locaux
        aq9 = Aquarium.objects.create(
            nom="Bac Eau Froide",
            volume_eau=100,
            date_mise_en_service=date(2024, 5, 15),
            commentaire="Aquarium eau froide pour poissons de nos rivières"
        )
        # 10 - Très grand bac show-room (cas limite : volume max)
        aq10 = Aquarium.objects.create(
            nom="Showroom 600L",
            volume_eau=600,
            date_mise_en_service=date(2022, 3, 1),
            commentaire="Bac d'exposition, mélange de poissons et plantes spectaculaires"
        )

        # ══════════════════════════════════════════════════════════════
        # ANALYSES D'EAU (12)
        # Scénarios : paramètres normaux, pic de nitrites (cyclage),
        # pH élevé (cichlidés), eau très douce (crevettes),
        # températures variées (18-28°C), cas limite TDS élevé
        # ══════════════════════════════════════════════════════════════
        self.stdout.write('Création des analyses d\'eau...')

        analyses_data = [
            # 1 - Communautaire : paramètres stables et normaux
            {
                "aquarium": aq1, "date_analyse": date(2025, 1, 10),
                "no2": 0.0, "no3": 15.0, "ph": 7.0, "nh4": 0.0,
                "kh": 5.0, "gh": 8.0, "sio2": 2.0, "po4": 0.5,
                "mg": 12.0, "fe": 0.1, "cu": 0.02, "tds": 250,
                "temperature": 25.0,
                "observation": "Paramètres stables, bac bien cyclé"
            },
            # 2 - Communautaire : légère montée de NO3 après fertilisation
            {
                "aquarium": aq1, "date_analyse": date(2025, 2, 15),
                "no2": 0.0, "no3": 30.0, "ph": 7.1, "nh4": 0.0,
                "kh": 5.0, "gh": 8.0, "sio2": 2.5, "po4": 1.0,
                "mg": 13.0, "fe": 0.15, "cu": 0.02, "tds": 270,
                "temperature": 25.5,
                "observation": "NO3 élevé après fertilisation, changement d'eau recommandé"
            },
            # 3 - Cichlidés Malawi : eau dure, pH alcalin (normal pour ce bac)
            {
                "aquarium": aq2, "date_analyse": date(2025, 1, 20),
                "no2": 0.0, "no3": 20.0, "ph": 8.2, "nh4": 0.0,
                "kh": 12.0, "gh": 16.0, "sio2": 1.5, "po4": 0.3,
                "mg": 28.0, "fe": 0.05, "cu": 0.01, "tds": 350,
                "temperature": 26.0,
                "observation": "Eau dure adaptée Malawi, paramètres conformes"
            },
            # 4 - Nano crevettes : eau douce, pH légèrement acide
            {
                "aquarium": aq3, "date_analyse": date(2025, 2, 1),
                "no2": 0.0, "no3": 5.0, "ph": 6.5, "nh4": 0.0,
                "kh": 2.0, "gh": 4.0, "sio2": 3.0, "po4": 0.2,
                "mg": 6.0, "fe": 0.05, "cu": 0.0, "tds": 140,
                "temperature": 24.0,
                "observation": "Eau douce parfaite pour crevettes Neocaridina"
            },
            # 5 - Aquascape Iwagumi : CO2 actif, pH bas
            {
                "aquarium": aq4, "date_analyse": date(2025, 2, 10),
                "no2": 0.0, "no3": 10.0, "ph": 6.4, "nh4": 0.0,
                "kh": 3.0, "gh": 6.0, "sio2": 1.0, "po4": 0.8,
                "mg": 10.0, "fe": 0.2, "cu": 0.01, "tds": 180,
                "temperature": 25.0,
                "observation": "pH bas dû au CO2, plantes en pleine croissance"
            },
            # 6 - Quarantaine : pic de nitrites (cas limite - cyclage en cours)
            {
                "aquarium": aq5, "date_analyse": date(2025, 1, 5),
                "no2": 1.5, "no3": 5.0, "ph": 7.5, "nh4": 0.5,
                "kh": 4.0, "gh": 7.0, "sio2": 1.0, "po4": 0.3,
                "mg": 8.0, "fe": 0.0, "cu": 0.0, "tds": 200,
                "temperature": 26.0,
                "observation": "⚠️ Pic de NO2 et NH4 - bac en cours de cyclage"
            },
            # 7 - Biotope Amazonien : eau très douce et acide
            {
                "aquarium": aq6, "date_analyse": date(2025, 1, 25),
                "no2": 0.0, "no3": 8.0, "ph": 5.8, "nh4": 0.0,
                "kh": 1.0, "gh": 3.0, "sio2": 4.0, "po4": 0.4,
                "mg": 4.0, "fe": 0.3, "cu": 0.01, "tds": 90,
                "temperature": 27.0,
                "observation": "Eau très douce et acide, idéale pour discus et cardinalis"
            },
            # 8 - Tanganyika : eau très dure, pH très élevé
            {
                "aquarium": aq7, "date_analyse": date(2025, 2, 5),
                "no2": 0.0, "no3": 25.0, "ph": 8.8, "nh4": 0.0,
                "kh": 14.0, "gh": 20.0, "sio2": 0.5, "po4": 0.2,
                "mg": 35.0, "fe": 0.02, "cu": 0.01, "tds": 420,
                "temperature": 26.5,
                "observation": "Eau très dure, pH élevé conforme Tanganyika"
            },
            # 9 - Paludarium : paramètres modérés
            {
                "aquarium": aq8, "date_analyse": date(2025, 2, 20),
                "no2": 0.05, "no3": 12.0, "ph": 7.0, "nh4": 0.0,
                "kh": 4.0, "gh": 7.0, "sio2": 2.0, "po4": 0.6,
                "mg": 10.0, "fe": 0.1, "cu": 0.02, "tds": 220,
                "temperature": 25.0,
                "observation": "Paramètres corrects, partie aquatique en bon état"
            },
            # 10 - Eau Froide : température basse (cas limite)
            {
                "aquarium": aq9, "date_analyse": date(2025, 3, 1),
                "no2": 0.0, "no3": 18.0, "ph": 7.5, "nh4": 0.0,
                "kh": 6.0, "gh": 10.0, "sio2": 3.0, "po4": 0.4,
                "mg": 14.0, "fe": 0.08, "cu": 0.02, "tds": 280,
                "temperature": 18.0,
                "observation": "Eau froide 18°C, pas de chauffage, poissons locaux"
            },
            # 11 - Showroom : grand volume, paramètres stables
            {
                "aquarium": aq10, "date_analyse": date(2025, 1, 15),
                "no2": 0.0, "no3": 12.0, "ph": 7.2, "nh4": 0.0,
                "kh": 5.0, "gh": 9.0, "sio2": 1.5, "po4": 0.5,
                "mg": 15.0, "fe": 0.12, "cu": 0.02, "tds": 260,
                "temperature": 26.0,
                "observation": "Grand bac stable, entretien régulier"
            },
            # 12 - Showroom : 2e analyse après traitement anti-algues
            {
                "aquarium": aq10, "date_analyse": date(2025, 3, 5),
                "no2": 0.0, "no3": 8.0, "ph": 7.0, "nh4": 0.0,
                "kh": 5.0, "gh": 9.0, "sio2": 0.5, "po4": 0.2,
                "mg": 14.0, "fe": 0.1, "cu": 0.03, "tds": 240,
                "temperature": 25.5,
                "observation": "Post-traitement anti-algues, SiO2 et PO4 en baisse"
            },
        ]

        for data in analyses_data:
            Analyse.objects.create(**data)

        # ══════════════════════════════════════════════════════════════
        # CHANGEMENTS D'EAU (12)
        # Scénarios : changements réguliers (20-30%), gros changements (50%),
        # 100% osmose (crevettes), 100% robinet (eau froide), mélanges variés
        # ══════════════════════════════════════════════════════════════
        self.stdout.write('Création des changements d\'eau...')

        changements_data = [
            # 1 - Communautaire : changement hebdo classique 25%
            {"aquarium": aq1, "date_change_eau": date(2025, 1, 12), "quantite_litre": 50, "osmose_pourcentage": 60, "robinet_pourcentage": 40},
            # 2 - Communautaire : changement après pic NO3
            {"aquarium": aq1, "date_change_eau": date(2025, 2, 16), "quantite_litre": 80, "osmose_pourcentage": 70, "robinet_pourcentage": 30},
            # 3 - Cichlidés Malawi : peu d'osmose (eau dure souhaitée)
            {"aquarium": aq2, "date_change_eau": date(2025, 1, 22), "quantite_litre": 90, "osmose_pourcentage": 20, "robinet_pourcentage": 80},
            # 4 - Nano crevettes : 100% osmose (eau très douce)
            {"aquarium": aq3, "date_change_eau": date(2025, 2, 3), "quantite_litre": 8, "osmose_pourcentage": 100, "robinet_pourcentage": 0},
            # 5 - Aquascape : changement régulier 30%
            {"aquarium": aq4, "date_change_eau": date(2025, 2, 12), "quantite_litre": 36, "osmose_pourcentage": 80, "robinet_pourcentage": 20},
            # 6 - Quarantaine : gros changement 50% après traitement
            {"aquarium": aq5, "date_change_eau": date(2025, 1, 7), "quantite_litre": 10, "osmose_pourcentage": 50, "robinet_pourcentage": 50},
            # 7 - Biotope Amazonien : 100% osmose reminéralisée
            {"aquarium": aq6, "date_change_eau": date(2025, 1, 27), "quantite_litre": 100, "osmose_pourcentage": 100, "robinet_pourcentage": 0},
            # 8 - Tanganyika : 100% robinet (eau dure du réseau)
            {"aquarium": aq7, "date_change_eau": date(2025, 2, 7), "quantite_litre": 60, "osmose_pourcentage": 0, "robinet_pourcentage": 100},
            # 9 - Paludarium : petit changement
            {"aquarium": aq8, "date_change_eau": date(2025, 2, 22), "quantite_litre": 30, "osmose_pourcentage": 50, "robinet_pourcentage": 50},
            # 10 - Eau Froide : changement avec eau du robinet
            {"aquarium": aq9, "date_change_eau": date(2025, 3, 3), "quantite_litre": 25, "osmose_pourcentage": 0, "robinet_pourcentage": 100},
            # 11 - Showroom : gros changement régulier
            {"aquarium": aq10, "date_change_eau": date(2025, 1, 18), "quantite_litre": 150, "osmose_pourcentage": 50, "robinet_pourcentage": 50},
            # 12 - Showroom : changement après traitement anti-algues
            {"aquarium": aq10, "date_change_eau": date(2025, 3, 7), "quantite_litre": 200, "osmose_pourcentage": 60, "robinet_pourcentage": 40},
        ]

        for data in changements_data:
            ChangeEau.objects.create(**data)

        # ══════════════════════════════════════════════════════════════
        # TRAITEMENTS (12)
        # Scénarios : fertilisation plantes, anti-algues, conditionneur,
        # traitement médical, reminéralisation, anti-parasitaire
        # ══════════════════════════════════════════════════════════════
        self.stdout.write('Création des traitements...')

        traitements_data = [
            # 1 - Engrais liquide complet pour plantes
            {"aquarium": aq1, "nom_produit": "Seachem Flourish", "quantite": 10, "date_traitement": date(2025, 1, 10)},
            # 2 - Conditionneur d'eau (élimine chlore)
            {"aquarium": aq1, "nom_produit": "Seachem Prime", "quantite": 4, "date_traitement": date(2025, 1, 12)},
            # 3 - Anti-algues pour bac cichlidés
            {"aquarium": aq2, "nom_produit": "Easy-Life AlgExit", "quantite": 35, "date_traitement": date(2025, 1, 20)},
            # 4 - Conditionneur eau pour cichlidés
            {"aquarium": aq2, "nom_produit": "JBL Biotopol C", "quantite": 15, "date_traitement": date(2025, 1, 22)},
            # 5 - Reminéralisation eau osmose pour crevettes
            {"aquarium": aq3, "nom_produit": "SaltyShrimp GH+", "quantite": 2, "date_traitement": date(2025, 2, 3)},
            # 6 - Engrais fer pour plantes rouges
            {"aquarium": aq4, "nom_produit": "Seachem Flourish Iron", "quantite": 5, "date_traitement": date(2025, 2, 10)},
            # 7 - Traitement médical anti-parasitaire (quarantaine)
            {"aquarium": aq5, "nom_produit": "eSHa 2000", "quantite": 3, "date_traitement": date(2025, 1, 5)},
            # 8 - Catappa extrait (tanins) pour biotope amazonien
            {"aquarium": aq6, "nom_produit": "Tantora Catappa", "quantite": 20, "date_traitement": date(2025, 1, 25)},
            # 9 - Tampon pH pour Tanganyika
            {"aquarium": aq7, "nom_produit": "Seachem Tang. Buffer", "quantite": 8, "date_traitement": date(2025, 2, 5)},
            # 10 - Bactéries vivantes pour paludarium
            {"aquarium": aq8, "nom_produit": "Prodibio BioDigest", "quantite": 1, "date_traitement": date(2025, 2, 20)},
            # 11 - Anti-algues pour showroom
            {"aquarium": aq10, "nom_produit": "JBL Algol", "quantite": 60, "date_traitement": date(2025, 3, 1)},
            # 12 - Engrais macro NPK pour showroom planté
            {"aquarium": aq10, "nom_produit": "Tropica Specialised", "quantite": 12, "date_traitement": date(2025, 1, 15)},
        ]

        for data in traitements_data:
            Traitement.objects.create(**data)

        # ══════════════════════════════════════════════════════════════
        # ESPÈCES (12)
        # Scénarios : poissons tropicaux, cichlidés, crevettes,
        # poissons de fond, labyrinthidés, eau froide
        # Dureté d'eau cohérente avec l'aquarium associé
        # ══════════════════════════════════════════════════════════════
        self.stdout.write('Création des espèces...')

        especes_data = [
            # 1 - Néon bleu : banc classique, eau douce
            {"aquarium": aq1, "nom_espece": "Néon Bleu", "type_espece": "Characidé", "nombre_espece": 15, "paramettre_min_ph": 6.0, "paramettre_max_ph": 7.5, "paramettre_eau": "DOUCE"},
            # 2 - Corydoras : poisson de fond, grégaire
            {"aquarium": aq1, "nom_espece": "Corydoras Panda", "type_espece": "Callichthyidae", "nombre_espece": 6, "paramettre_min_ph": 6.0, "paramettre_max_ph": 7.5, "paramettre_eau": "DOUCE"},
            # 3 - Guppy : vivipare résistant
            {"aquarium": aq1, "nom_espece": "Guppy Endler", "type_espece": "Poeciliidae", "nombre_espece": 8, "paramettre_min_ph": 6.8, "paramettre_max_ph": 8.0, "paramettre_eau": "MOYENNEMENT_DURE"},
            # 4 - Cichlidé Malawi agressif
            {"aquarium": aq2, "nom_espece": "Pseudotropheus Demason", "type_espece": "Cichlidae", "nombre_espece": 12, "paramettre_min_ph": 7.5, "paramettre_max_ph": 8.8, "paramettre_eau": "DURE"},
            # 5 - Cichlidé Malawi paisible
            {"aquarium": aq2, "nom_espece": "Labidochromis Yellow", "type_espece": "Cichlidae", "nombre_espece": 8, "paramettre_min_ph": 7.5, "paramettre_max_ph": 8.5, "paramettre_eau": "DURE"},
            # 6 - Crevette Red Cherry : invertébré, eau douce
            {"aquarium": aq3, "nom_espece": "Crevette Red Cherry", "type_espece": "Neocaridina", "nombre_espece": 25, "paramettre_min_ph": 6.2, "paramettre_max_ph": 7.5, "paramettre_eau": "DOUCE"},
            # 7 - Rasbora Galaxy : petit poisson compatible crevettes
            {"aquarium": aq4, "nom_espece": "Rasbora Galaxy", "type_espece": "Cyprinidae", "nombre_espece": 10, "paramettre_min_ph": 6.0, "paramettre_max_ph": 7.5, "paramettre_eau": "DOUCE"},
            # 8 - Discus : poisson exigeant eau très douce (biotope amazonien)
            {"aquarium": aq6, "nom_espece": "Discus Bleu", "type_espece": "Cichlidae", "nombre_espece": 5, "paramettre_min_ph": 5.5, "paramettre_max_ph": 6.8, "paramettre_eau": "TRES_DOUCE"},
            # 9 - Cardinalis : classique amazonien
            {"aquarium": aq6, "nom_espece": "Cardinalis", "type_espece": "Characidé", "nombre_espece": 20, "paramettre_min_ph": 5.5, "paramettre_max_ph": 7.0, "paramettre_eau": "TRES_DOUCE"},
            # 10 - Neolamprologus : cichlidé Tanganyika coquillier
            {"aquarium": aq7, "nom_espece": "Neolamprologus Brevis", "type_espece": "Cichlidae", "nombre_espece": 6, "paramettre_min_ph": 7.8, "paramettre_max_ph": 9.0, "paramettre_eau": "TRES_DURE"},
            # 11 - Vairon : poisson d'eau froide local
            {"aquarium": aq9, "nom_espece": "Vairon", "type_espece": "Cyprinidae", "nombre_espece": 10, "paramettre_min_ph": 6.5, "paramettre_max_ph": 8.0, "paramettre_eau": "MOYENNEMENT_DURE"},
            # 12 - Scalaire : grand poisson majestueux pour showroom
            {"aquarium": aq10, "nom_espece": "Scalaire", "type_espece": "Cichlidae", "nombre_espece": 4, "paramettre_min_ph": 6.0, "paramettre_max_ph": 7.5, "paramettre_eau": "DOUCE"},
        ]

        for data in especes_data:
            Espece.objects.create(**data)

        # ══════════════════════════════════════════════════════════════
        # PLANTES (12)
        # Scénarios : arrière-plan, milieu, premier plan, flottante,
        # sur objet (mousse), exigences CO2 variées
        # ══════════════════════════════════════════════════════════════
        self.stdout.write('Création des plantes...')

        plantes_data = [
            # 1 - Grande plante d'arrière-plan, facile
            {"aquarium": aq1, "nom_plante": "Vallisneria Gigantea", "emplacement_aquarium": "ARRIERE PLAN", "paramettre_min_ph": 6.0, "paramettre_max_ph": 8.5, "paramettre_min_co2": 5.0, "paramettre_max_co2": 30.0},
            # 2 - Plante robuste sur racine / pierre
            {"aquarium": aq1, "nom_plante": "Anubias Barteri", "emplacement_aquarium": "SUR OBJET", "paramettre_min_ph": 6.0, "paramettre_max_ph": 8.0, "paramettre_min_co2": 3.0, "paramettre_max_co2": 25.0},
            # 3 - Plante de milieu, couleur rouge
            {"aquarium": aq1, "nom_plante": "Ludwigia Palustris", "emplacement_aquarium": "MILIEU PLAN", "paramettre_min_ph": 5.5, "paramettre_max_ph": 7.5, "paramettre_min_co2": 15.0, "paramettre_max_co2": 35.0},
            # 4 - Mousse pour nano crevettes
            {"aquarium": aq3, "nom_plante": "Mousse de Java", "emplacement_aquarium": "SUR OBJET", "paramettre_min_ph": 5.5, "paramettre_max_ph": 8.0, "paramettre_min_co2": 3.0, "paramettre_max_co2": 20.0},
            # 5 - Plante flottante pour crevettes (protection)
            {"aquarium": aq3, "nom_plante": "Salvinia Natans", "emplacement_aquarium": "FLOTANTE", "paramettre_min_ph": 6.0, "paramettre_max_ph": 7.5, "paramettre_min_co2": 0.0, "paramettre_max_co2": 15.0},
            # 6 - Gazon premier plan (Iwagumi)
            {"aquarium": aq4, "nom_plante": "Eleocharis Mini", "emplacement_aquarium": "PREMIER PLAN", "paramettre_min_ph": 5.5, "paramettre_max_ph": 7.5, "paramettre_min_co2": 20.0, "paramettre_max_co2": 40.0},
            # 7 - Plante d'arrière-plan Iwagumi
            {"aquarium": aq4, "nom_plante": "Rotala Rotundifolia", "emplacement_aquarium": "ARRIERE PLAN", "paramettre_min_ph": 5.5, "paramettre_max_ph": 7.5, "paramettre_min_co2": 15.0, "paramettre_max_co2": 35.0},
            # 8 - Echinodorus amazonien
            {"aquarium": aq6, "nom_plante": "Echinodorus Bleheri", "emplacement_aquarium": "ARRIERE PLAN", "paramettre_min_ph": 5.5, "paramettre_max_ph": 7.5, "paramettre_min_co2": 8.0, "paramettre_max_co2": 30.0},
            # 9 - Plante flottante amazonienne
            {"aquarium": aq6, "nom_plante": "Pistia Stratiotes", "emplacement_aquarium": "FLOTANTE", "paramettre_min_ph": 5.5, "paramettre_max_ph": 7.5, "paramettre_min_co2": 0.0, "paramettre_max_co2": 10.0},
            # 10 - Cryptocoryne adaptable pour paludarium
            {"aquarium": aq8, "nom_plante": "Cryptocoryne Wendtii", "emplacement_aquarium": "MILIEU PLAN", "paramettre_min_ph": 6.0, "paramettre_max_ph": 8.0, "paramettre_min_co2": 5.0, "paramettre_max_co2": 25.0},
            # 11 - Bucephalandra sur objet pour showroom
            {"aquarium": aq10, "nom_plante": "Bucephalandra Brownie", "emplacement_aquarium": "SUR OBJET", "paramettre_min_ph": 5.5, "paramettre_max_ph": 7.5, "paramettre_min_co2": 10.0, "paramettre_max_co2": 30.0},
            # 12 - Plante de premier plan pour showroom
            {"aquarium": aq10, "nom_plante": "Hemianthus Callitrich.", "emplacement_aquarium": "PREMIER PLAN", "paramettre_min_ph": 5.0, "paramettre_max_ph": 7.5, "paramettre_min_co2": 20.0, "paramettre_max_co2": 40.0},
        ]

        for data in plantes_data:
            Plante.objects.create(**data)

        # ══════════════════════════════════════════════════════════════
        # ÉQUIPEMENTS (12)
        # Scénarios : filtres internes/externes, chauffages, éclairages LED,
        # systèmes CO2, pompes à air, osmoseurs, etc.
        # ══════════════════════════════════════════════════════════════
        self.stdout.write('Création des équipements...')

        equipements_data = [
            # 1 - Filtre externe classique pour communautaire
            {"aquarium": aq1, "type_equipement": "Filtre externe", "nom_equipement": "Eheim Classic 350", "date_installation": date(2023, 1, 15), "carateristique": "Débit: 620 L/h, pour bacs jusqu'à 350L", "commentaire": "Filtre silencieux et fiable, nettoyage tous les 3 mois"},
            # 2 - Chauffage pour communautaire
            {"aquarium": aq1, "type_equipement": "Chauffage", "nom_equipement": "Eheim ThermoControl 150W", "date_installation": date(2023, 1, 15), "carateristique": "150W, réglable 18-34°C", "commentaire": "Thermostat précis à ±0.5°C"},
            # 3 - Éclairage LED pour communautaire planté
            {"aquarium": aq1, "type_equipement": "Éclairage", "nom_equipement": "Chihiros WRGB II 60", "date_installation": date(2023, 2, 1), "carateristique": "60W, spectre WRGB, Bluetooth", "commentaire": "Éclairage haut de gamme pour plantes exigeantes"},
            # 4 - Filtre surpuissant pour cichlidés
            {"aquarium": aq2, "type_equipement": "Filtre externe", "nom_equipement": "Fluval FX4", "date_installation": date(2023, 6, 10), "carateristique": "Débit: 2650 L/h, 1700L volume", "commentaire": "Filtre haute performance pour forte charge organique"},
            # 5 - Filtre nano pour crevettes
            {"aquarium": aq3, "type_equipement": "Filtre interne", "nom_equipement": "Dennerle Corner Filter", "date_installation": date(2024, 2, 1), "carateristique": "Débit 40-150 L/h, mousse fine", "commentaire": "Mousse fine pour protéger les bébés crevettes"},
            # 6 - Système CO2 complet pour aquascape
            {"aquarium": aq4, "type_equipement": "Système CO2", "nom_equipement": "JBL ProFlora CO2 m502", "date_installation": date(2024, 4, 20), "carateristique": "Bouteille 500g, régulateur", "commentaire": "Injection CO2 avec électrovanne et minuterie"},
            # 7 - Éclairage puissant pour aquascape
            {"aquarium": aq4, "type_equipement": "Éclairage", "nom_equipement": "Twinstar S Series 600", "date_installation": date(2024, 4, 20), "carateristique": "48W, 6500K, spectre plantes", "commentaire": "LED haut de gamme spécial aquascaping"},
            # 8 - Petit chauffage quarantaine
            {"aquarium": aq5, "type_equipement": "Chauffage", "nom_equipement": "Aquael Ultra Heater 25W", "date_installation": date(2024, 8, 5), "carateristique": "25W, pour bacs 10-25L", "commentaire": "Chauffage compact pour bac de quarantaine"},
            # 9 - Filtre externe pour biotope amazonien
            {"aquarium": aq6, "type_equipement": "Filtre externe", "nom_equipement": "Oase BioMaster 600", "date_installation": date(2022, 11, 1), "carateristique": "Débit: 1250 L/h, pré-filtre", "commentaire": "Filtre avec module de chauffe intégré"},
            # 10 - Pompe à air pour Tanganyika (oxygénation)
            {"aquarium": aq7, "type_equipement": "Pompe à air", "nom_equipement": "Eheim Air Pump 400", "date_installation": date(2023, 9, 15), "carateristique": "Débit air: 400 L/h, 2 sorties", "commentaire": "Pour rampe à bulles, oxygénation forte nécessaire"},
            # 11 - Osmoseur pour préparer l'eau osmosée
            {"aquarium": aq6, "type_equipement": "Osmoseur", "nom_equipement": "Dennerle Osmose 130", "date_installation": date(2022, 11, 1), "carateristique": "130 L/jour, 3 étapes filtration", "commentaire": "Produit de l'eau pure pour reminéralisation"},
            # 12 - Éclairage LED showroom
            {"aquarium": aq10, "type_equipement": "Éclairage", "nom_equipement": "Fluval Plant 3.0 120cm", "date_installation": date(2022, 3, 1), "carateristique": "59W, spectre complet, WiFi", "commentaire": "Double rampe LED pour bac 600L"},
        ]

        for data in equipements_data:
            Equipement.objects.create(**data)

        # ══════════════════════════════════════════════════════════════
        # RÉSUMÉ FINAL
        # ══════════════════════════════════════════════════════════════
        self.stdout.write('')
        self.stdout.write(self.style.SUCCESS('✅ Données de test insérées avec succès !'))
        self.stdout.write(self.style.SUCCESS(f'   - {Aquarium.objects.count()} aquariums créés'))
        self.stdout.write(self.style.SUCCESS(f'   - {Analyse.objects.count()} analyses créées'))
        self.stdout.write(self.style.SUCCESS(f'   - {ChangeEau.objects.count()} changements d\'eau créés'))
        self.stdout.write(self.style.SUCCESS(f'   - {Traitement.objects.count()} traitements créés'))
        self.stdout.write(self.style.SUCCESS(f'   - {Espece.objects.count()} espèces créées'))
        self.stdout.write(self.style.SUCCESS(f'   - {Plante.objects.count()} plantes créées'))
        self.stdout.write(self.style.SUCCESS(f'   - {Equipement.objects.count()} équipements créés'))
        self.stdout.write('')
        self.stdout.write(self.style.SUCCESS('Pour relancer : python manage.py insert_test_data --clear'))
