@echo off
title P.O.S.I-SW - Package Online Service Installer Software (Installer mode)
echo P.O.S.I-SW Installer mode.
echo[
echo Downloading and installing python packages....
pip install -r requirements.txt
echo Successfully downloaded and installed required python packages!
echo[
PAUSE
exit