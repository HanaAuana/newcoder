#!/usr/bin/env bash
echo "Installing lib png and freetype"
sudo apt-get -y install libpng12-dev
sudo apt-get -y install libfreetype6-dev
echo "Installing numpy"
sudo pip install numpy
echo "Installing matplotlib"
sudo pip install matplotlib
echo "Installing geojson"
sudo pip install geojson