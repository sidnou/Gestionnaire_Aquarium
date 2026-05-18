# Aquarium Manager

Plateforme de gestion automatisée d’aquarium basée sur :

- Python
- Django
- PostgreSQL
- ESP32
- MQTT
- Bootstrap
- Home Assistant
- Proxmox

Projet personnel conçu avec une architecture professionnelle, modulaire et évolutive.

---

# Infrastructure

## Serveur principal

| Élément | Valeur |
|---|---|
| Serveur | Dell OptiPlex 3080 |
| CPU | Intel i5 |
| RAM | 32 Go |
| Hyperviseur | Proxmox VE |
| Sauvegarde | NAS externe |
| Réseau | LAN Gigabit |

---

# Architecture globale

```text
Proxmox
│
├── VM Home Assistant
│
├── VM PostgreSQL
│
├── VM Aquarium Application
│
├── VM Monitoring (optionnel)
│
└── ESP32
```

---

# Objectifs du projet

Créer une plateforme permettant :

- dosage automatique
- gestion des pompes
- supervision aquarium
- historique des actions
- alertes
- automatisations
- intégration Home Assistant
- dashboard Web moderne
- gestion MQTT
- architecture évolutive

---

# Répartition des rôles

## Home Assistant

Déjà installé sur VM.

Rôle :

- supervision
- dashboard domotique
- automatisations
- notifications
- intégration MQTT

---

## VM PostgreSQL

Rôle :

- stockage des données
- historique
- statistiques
- logs
- planning

---

## VM Application

Rôle :

- backend Django
- interface Bootstrap
- API REST
- WebSocket
- logique métier
- gestion MQTT

---

## ESP32

Rôle :

- contrôle relais
- gestion pompes
- sécurité locale
- exécution temps réel
- communication MQTT

---

# Technologies utilisées

| Fonction | Technologie |
|---|---|
| Backend | Python |
| Framework | Django |
| Frontend | Bootstrap 5 |
| Base de données | PostgreSQL |
| Temps réel | WebSocket |
| Broker MQTT | Mosquitto |
| Firmware ESP32 | MicroPython |
| Monitoring | Grafana |
| Virtualisation | Proxmox |

---

# Structure du projet

```text
aquarium-manager/
├── app/
│   ├── manage.py
│   ├── config/
│   ├── dashboard/
│   ├── dosing/
│   ├── devices/
│   ├── sensors/
│   ├── notifications/
│   ├── integrations/
│   └── templates/
│
├── static/
├── media/
├── docker/
├── scripts/
├── docs/
├── requirements.txt
├── docker-compose.yml
├── .env
└── README.md
```

---

# Modules applicatifs

# Dashboard

Gestion de l’interface principale.

Fonctionnalités :

- état général
- état des pompes
- alertes
- statistiques
- dashboard responsive

---

# Dosing

Gestion des dosages automatiques.

Fonctionnalités :

- dosage manuel
- dosage programmé
- planning journalier
- calibration ml/s
- sécurité anti-sur dosage

---

# Devices

Gestion des équipements.

Fonctionnalités :

- pompes
- relais
- disponibilité ESP32
- supervision réseau
- commandes MQTT

---

# Sensors

Gestion des capteurs.

Fonctionnalités :

- température
- pH
- niveau liquide
- conductivité
- monitoring système

---

# Notifications

Gestion des alertes.

Fonctionnalités :

- Home Assistant
- email
- Telegram
- alertes critiques

---

# Integrations

Communication externe.

Fonctionnalités :

- MQTT
- Home Assistant
- WebSocket
- API REST

---

# Plan de développement

# Phase 1 — Infrastructure

## Tâches

- [ ] Créer VM PostgreSQL
- [ ] Créer VM Application
- [ ] Configurer Docker
- [ ] Configurer Git
- [ ] Configurer réseau Proxmox
- [ ] Configurer sauvegardes

---

# Phase 2 — PostgreSQL

## Tâches

- [ ] Installer PostgreSQL
- [ ] Créer utilisateur aquarium
- [ ] Créer base aquarium_db
- [ ] Configurer accès réseau
- [ ] Configurer sauvegardes SQL
- [ ] Configurer logs PostgreSQL

---

# Phase 3 — Projet Django

## Tâches

- [ ] Créer environnement virtuel
- [ ] Installer Django
- [ ] Configurer .env
- [ ] Configurer PostgreSQL
- [ ] Configurer Git
- [ ] Configurer logs

---

# Phase 4 — Modèles Django

## Tâches

- [ ] Créer modèle Aquarium
- [ ] Créer modèle Pompe
- [ ] Créer modèle Calibration
- [ ] Créer modèle Planning
- [ ] Créer modèle Historique
- [ ] Créer modèle Alerte
- [ ] Créer modèle Capteur

---

# Phase 5 — Frontend Bootstrap

## Dashboard

### Tâches

- [ ] Créer layout principal
- [ ] Créer navbar
- [ ] Créer sidebar
- [ ] Ajouter dark mode
- [ ] Créer dashboard responsive
- [ ] Créer cartes statistiques

---

# Gestion pompes

## Tâches

- [ ] Interface dosage manuel
- [ ] Interface calibration
- [ ] Interface planning
- [ ] Gestion erreurs
- [ ] État temps réel

---

# Graphiques

## Tâches

- [ ] Intégrer Chart.js
- [ ] Historique dosage
- [ ] Consommation
- [ ] Température
- [ ] Alertes

---

# Phase 6 — MQTT

## Tâches

- [ ] Installer Mosquitto
- [ ] Définir topics MQTT
- [ ] Configurer auto-discovery Home Assistant
- [ ] Gérer états ESP32
- [ ] Configurer heartbeat

---

# Topics MQTT

```text
doseur/pompe1/set
doseur/pompe1/state

doseur/pompe2/set
doseur/pompe2/state

doseur/system/status
```

---

# Phase 7 — ESP32

## Firmware MicroPython

### Tâches

- [ ] Installer MicroPython
- [ ] Configurer WiFi
- [ ] Configurer MQTT
- [ ] Configurer watchdog
- [ ] Configurer sécurité relais
- [ ] Configurer NTP
- [ ] Configurer mode autonome

---

# Gestion pompes

## Tâches

- [ ] Contrôle relais
- [ ] Calibration ml/s
- [ ] Timeout sécurité
- [ ] Journalisation locale
- [ ] Vérification disponibilité

---

# Phase 8 — Temps réel

## WebSocket

### Tâches

- [ ] Installer Django Channels
- [ ] Configurer WebSocket
- [ ] Mise à jour live dashboard
- [ ] Synchronisation état pompes

---

# Phase 9 — Sécurité

## Application

### Tâches

- [ ] HTTPS
- [ ] Reverse proxy Nginx
- [ ] Fail2ban
- [ ] JWT API
- [ ] Gestion permissions
- [ ] Protection CSRF

---

## Réseau

### Tâches

- [ ] VLAN IoT
- [ ] Isolation ESP32
- [ ] Firewall
- [ ] DNS local

---

# Phase 10 — Sauvegardes

## Sauvegardes Proxmox

Sauvegarde vers NAS externe.

### Tâches

- [ ] Snapshots VM
- [ ] Sauvegarde PostgreSQL
- [ ] Sauvegarde Docker
- [ ] Test restauration
- [ ] Rotation sauvegardes

---

# Monitoring

## Stack recommandée

| Service | Usage |
|---|---|
| Grafana | Dashboard |
| Prometheus | Metrics |
| Loki | Logs |

---

# Tâches monitoring

- [ ] Superviser VMs
- [ ] Superviser ESP32
- [ ] Superviser PostgreSQL
- [ ] Superviser MQTT
- [ ] Superviser application Django

---

# Fonctionnalités futures

## Extensions possibles

- [ ] IA prédictive
- [ ] Caméra aquarium
- [ ] PWA mobile
- [ ] Notifications avancées
- [ ] Maintenance prédictive
- [ ] Gestion multi-aquariums

---

# Tests finaux

## Validation

- [ ] Test dosage réel
- [ ] Test coupure réseau
- [ ] Test coupure courant
- [ ] Test reboot ESP32
- [ ] Test reboot VM
- [ ] Test sauvegardes
- [ ] Test restauration

---

# Recommandations importantes

## Architecture recommandée

Conserver :

- Home Assistant sur VM dédiée
- PostgreSQL sur VM dédiée
- Application Django sur VM dédiée
- ESP32 dédié au temps réel

---

## ESP32

L’ESP32 doit rester simple :

- relais
- pompes
- capteurs
- sécurité

---

## Application Django

Toute la logique métier doit rester côté serveur.

---

# Objectif final

Créer une plateforme :

- stable
- moderne
- maintenable
- évolutive
- sécurisée
- intégrée Home Assistant
- autonome

avec une architecture claire inspirée des environnements professionnels.
