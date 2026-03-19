#!/usr/bin/env bash


#mise à jour Système
sudo apt update && sudo apt dist-upgrade -y

#installation des packages nécessaires
curl -Ls https://astral.sh/uv/install.sh | sh
export PATH="$HOME/.local/bin:$PATH"




# Crétation du dossier aqua_srv
mkdir aqua_srv
cd aqua_srv

