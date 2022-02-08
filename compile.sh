#!/bin/sh
cd ./src/
echo -e "\033]2;P.O.S.I-SW - Package Online Service Installer Software (Complier mode)\x07"
pyinstaller -i icon.ico -n P.O.S.I-SW -c -F main.py
echo ""
read -s -n 1 -p "Press any key to continue . . ."