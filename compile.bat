@echo off
title P.O.S.I-SW - Package Online Service Installer Software (Complier mode)
cd ./src/
pyinstaller -i icon.ico -n P.O.S.I-SW -c -F main.py
echo[
PAUSE