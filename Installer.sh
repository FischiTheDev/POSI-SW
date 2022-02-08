#!/bin/sh
echo -e "\033]2;P.O.S.I-SW - Package Online Service Installer Software (Installer mode)\x07"
echo "P.O.S.I-SW Installer mode."
echo ""
echo "Downloading and installing python packages...."
pip install -r requirements.txt
echo "Successfully downloaded and installed required python packages!"
echo ""
read -s -n 1 -p "Press any key to continue . . ."
exit 0;