@echo off
title P.O.S.I-SW - Package Online Server Installer Software
cd ./src/
echo [38;2;00;255;00mPackage Online Service Installer Software (Running mode).[0m
echo [38;2;00;255;255mCreated by: yasserprogamer.[0m
echo[
if not exist main.py (
	set filename=main.py
	set type=file
	goto ErrorNoFileFound
)
:RunProgram
py main.py
:Crashed
cls
echo Program stopped or crashed at: %TIME% %DATE%
:AskIfUserSureAboutLeaving
echo ^> Do you really want to exit program?
set /p ExitProgramAnswer= 
goto %ExitProgramAnswer%

:y
:yes
exit

:n
:no
echo Restarting program....
goto RunProgram

:ErrorNoFileFound
echo [38;2;255;00;00mError: Could not find %type% (%filename%). Please try redownload this software.[0m
PAUSE
exit