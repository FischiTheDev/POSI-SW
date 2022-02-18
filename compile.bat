@echo off
title O.P.P.I-SW - Online Powerful Packages Installer Software (Complier mode)
cd ./src/
pyinstaller -i icon.ico -n O.P.P.I-SW -c -F main.py
echo[
PAUSE