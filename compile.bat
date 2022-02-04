@echo off
cd ./src/
pyinstaller -i icon.ico -n P.O.S.I-SW -c -F main.py
echo[
PAUSE