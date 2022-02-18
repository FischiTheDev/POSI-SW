@echo off
title O.P.P.I-SW - Package Online Server Installer Software
cd ./src/
echo [38;2;00;255;00mOnline Powerful Packages Installer Software (Running mode).[0m
echo [38;2;00;255;255mCreated by: yasserprogamer.[0m
echo[
echo [38;2;255;255;255mDo you want to run program in Python source code? ([38;2;00;255;00mY[38;2;255;255;255m/[38;2;255;00;00mN[38;2;255;255;255m) [0m
set /p RunSourceCodeAnswer=
goto python-sc-%RunSourceCodeAnswer%

echo [38;2;255;255;255mDo you want to run program in Compiled or executable file? ([38;2;00;255;00mY[38;2;255;255;255m/[38;2;255;00;00mN[38;2;255;255;255m) [0m
set /p RunSourceCodeAnswer=

:python-sc-yeah
:python-sc-yea
:python-sc-yup
:python-sc-yes
:python-sc-ye
:python-sc-y
if not exist main.py (
	set filename=main.py
	set type=file
	goto ErrorNoFileFound
)
:RunProgram
echo[
py main.py
:Crashed
cls
echo Program stopped or crashed at: %TIME% %DATE%
:AskIfUserSureAboutLeaving
echo [38;2;255;255;255mDo you really want to exit program? ([38;2;00;255;00mY[38;2;255;255;255m/[38;2;255;00;00mN[38;2;255;255;255m) [0m
set /p ExitProgramAnswer= 
goto %ExitProgramAnswer%

:y
:yes
exit 0

:n
:no
echo Restarting program....
goto RunProgram

:ErrorNoFileFound
echo [38;2;255;00;00mError: Could not find %type% (%filename%). Please try redownload this software.[0m
PAUSE

exit 0