#!/bin/sh
cd ./src/
echo -e "\033]2;O.P.P.I-SW - Online Powerful Packages Installer Software (Complie mode)\x07"
echo "[38;2;00;255;00mOnline Powerful Packages Installer Software (Compile mode).[0m"
echo "[38;2;00;255;255mCreated by: yasserprogamer.[0m"
echo ""
pyinstaller -i icon.ico -n O.P.P.I-SW -c -F main.py
echo ""
read -s -n 0 -p "Press any key to continue . . ."
exit 0;