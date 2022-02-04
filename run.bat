@echo off
title P.O.S.I-SW - Package Online Server Installer Software
cd ./src/
:RunProgram
echo Loading....
py main.py
:Crashed
cls
echo Program stopped or crashed at: %TIME% %DATE%
:AskIfUserSureAboutLeaving
echo Do you really want to exit program?
set /p ExitProgramAnswer= 
goto %ExitProgramAnswer%

:y
:yes
exit

:n
:no
echo Restarting program....
goto RunProgram
