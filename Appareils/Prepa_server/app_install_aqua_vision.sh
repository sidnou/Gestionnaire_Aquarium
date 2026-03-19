#!/usr/bin/env bash

#mise à jour Système
sudo apt update && sudo apt dist-upgrade -y

#installation des packages nécessaires
sudo apt install python3-pip
sudo apt install v4l-utils fswebcam
sudo apt install motion
sudo apt install glances # Optionnel , pour surveiller les ressources du système
#installation UV
curl -Ls https://astral.sh/uv/install.sh | sh
export PATH="$HOME/.local/bin:$PATH"

mkdir srv_surveillance
cd srv_surveillance
uv venv
source .venv/bin/activate
#uv pip install -r ../requirements.txt

#uv pip install opencv-python ultralytics  # A Testé, mais pas nécessaire pour le moment
