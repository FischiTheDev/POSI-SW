#!/bin/sh
echo -e "\033]2;O.P.P.I-SW - Online Powerful Packages Installer Software (Installer mode)\x07"
echo "O.P.P.I-SW Installer mode."
echo ""
echo "Downloading and installing python packages...."
pip install -r requirements.txt
echo "Successfully downloaded and installed required python packages!"
echo ""
read -s -n 1 -p "Press any key to continue . . ."
exit 0;