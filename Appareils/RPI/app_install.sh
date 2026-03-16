#!/usr/bin/env bash

#mise à jour Système
sudo apt update && sudo apt dist-upgrade -y

#installation des packages nécessaires
sudo apt install python3-pip
sudo apt install v4l-utils fswebcam
sudo apt install motion
#installation UV
curl -Ls https://astral.sh/uv/install.sh | sh


