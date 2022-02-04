print("\rLoading....", end="\r")

import urllib.request
import webbrowser
import zipfile
import requests
import os
import json 
import YouTube_services
import version
import data
import ToS
import messages
import credit
import sys 
import colors
import time
import re
import glob
import datetime
import utils
import logging
import papermc

try:
    if not os.path.exists("./logs/"):
        os.makedirs("./logs/")
    logging.basicConfig(filename="./logs/latest.txt", filemode="w", encoding="UTF-8", level=1, format="[%(name)s:%(levelname)s]: %(message)s")
    Logger = True
    logging.info("Logger has successfully started!")
except PermissionError:
    print(f"Permission denied to create logger file and start logging.")
    print(f"If you want logging system work, please make your Anti-Virus or Windows Defender allow this application to create or access files.")
    logging.shutdown()
    Logger = False
    print("")

OSplatformVersion = "Unknown!"

logging.info("Checking user's OS platform.")
if(sys.platform.lower() == "win32"):
    logging.info("Successfully detected user's platform: Windows.")
    OSplatformVersion = f"Windows {sys.getwindowsversion().major}"
elif(sys.platform.lower() in ["linux", "linux2"]):
    logging.info("Successfully detected user's platform: Linux.")
    OSplatformVersion = "Linux"
elif(sys.platform.lower() == "darwin"):
    logging.info("Successfully detected user's platform: Mac OS.")
    OSplatformVersion = "Mac OS"
else:
    logging.info("Could not detect user's platform: Unknown or anonymous OS.")
    OSplatformVersion = "Unknown!"

CWD = os.getcwd()

ConsoleTitle = f"{version.name} ({version.version}) - {version.fullname}"

try:
    os.system(f"title {ConsoleTitle}")
    logging.info(f"Console title was successfully changed to \"{ConsoleTitle}\".")
except:
    actlikenothinghappened = ""

ColorOfTitle = colors.Color.RANDOM

print("\r", end="\r")

print(colors.Color.Yellow+"┌"+"".center(78, "─")+"┐"+colors.Color.reset)
print(colors.Color.Yellow+"│"+"".center(78, " ")+"│"+colors.Color.reset)
print(colors.Color.Yellow+"│"+ColorOfTitle+" ____   ___   ____   ___     ______        __".center(78, " ")+colors.Color.Yellow+"│")
print(colors.Color.Yellow+"│"+ColorOfTitle+"│  _ \ / _ \ / ___│ │_ _│   / ___\ \      / /".center(78, " ")+colors.Color.Yellow+"│")
print(colors.Color.Yellow+"│"+ColorOfTitle+"│ │_) │ │ │ │\___ \  │ │____\___ \\\\ \ /\ / / ".center(78, " ")+colors.Color.Yellow+"│")
print(colors.Color.Yellow+"│"+ColorOfTitle+"│  __/│ │_│ │ ___) │ │ │_____│__) │\ V  V /  ".center(78, " ")+colors.Color.Yellow+"│")
print(colors.Color.Yellow+"│"+ColorOfTitle+"│_│ (_)\___(_)____(_)___│   │____/  \_/\_/   ".center(78, " ")+colors.Color.Yellow+"│")
print(colors.Color.Yellow+"│"+"".center(78, " ")+"│"+colors.Color.reset)
print(colors.Color.Yellow+"│"+ColorOfTitle+f"{version.fullname} ({version.version})".center(78, " ").replace(f"{version.fullname} ({version.version})", f"{colors.Color.bold}{version.fullname} ({version.version}){colors.Color.nobold}")+colors.Color.Yellow+"│")
print(colors.Color.Yellow+"│"+colors.Color.Cyan+f"{OSplatformVersion}".center(78, " ")+colors.Color.Yellow+"│")
print(colors.Color.Yellow+"│"+"".center(78, " ")+"│"+colors.Color.reset)
print(colors.Color.Yellow+"│"+colors.Color.White+f"{version.CopyrightText}".center(78, " ")+colors.Color.Yellow+"│")
print(colors.Color.Yellow+"└"+"".center(78, "─")+"┘"+colors.Color.reset)

colors.window.setTitle(ConsoleTitle) #Trying to change terminal title in every OS' console

running = True
logging.warning("Status \"running\" changed from False to True.")

print("")
try:
    headers = {'user-agent': f'{version.name}-{version.version}'}
    Updatewebsite = requests.get("https://posi-sw.github.io/website/version/api/updates/manifest.json", headers=headers)
    UpdateNotificationStatusCode = Updatewebsite.status_code
    if(UpdateNotificationStatusCode == 200):
        POSISWManifestJson = Updatewebsite.json()
        UpdateNotification = POSISWManifestJson["latest"]["release"]
        DownloadPageLink = POSISWManifestJson["version"][UpdateNotification]["download_page"]
        DownloadUrlLink = POSISWManifestJson["version"][UpdateNotification]["download_url"]
        Updatewebsite.close()
        if(version.version != UpdateNotification):
            print(f"{colors.Color.Lime}There is new {UpdateNotification} update for this software! You are still on {version.version} version.{colors.Color.reset}")
            print(f"{colors.Color.gold}We recommended you to update because we may fixed some of bugs and added new features that you will like and it is kinda important for some of outdated and unprotected versions.{colors.Color.reset}")
            print("")
            print(f"{colors.Color.blue}Download update from: {colors.Color.white}{colors.Color.underline}{DownloadPageLink}{colors.Color.Nounderline}{colors.Color.reset}")
            print("")
            if (not os.path.exists("./autoupdate.txt") and not os.path.isfile("./autoupdate.txt")):
                AutoupdateFile = open("./autoupdate.txt", "w")
                AutoupdateFile.write("none")
                AutoupdateFile.close()
            AutoupdateFile = open("./autoupdate.txt", "r")
            AutoUpdateFileTexts = AutoupdateFile.read().lower()
            if(AutoUpdateFileTexts == "none"):
                print(f"Do you want to enable auto-update? (Y/N)\n")
                EnableAutoUpdate = input(f"")
                if(EnableAutoUpdate.lower() in ["y", "ye", "yes", "yea", "yeah", "yup", "true"]):
                    AcceptingInAutoupdateFile = open("./autoupdate.txt", "w")
                    AcceptingInAutoupdateFile.write("yes")
                    AcceptingInAutoupdateFile.close()
                    AutoUpdate = True
                elif(EnableAutoUpdate.lower() in ["n", "no", "nope", "nah", "false"]):
                    DenyingInAutoupdateFile = open("./autoupdate.txt", "w")
                    DenyingInAutoupdateFile.write("no")
                    DenyingInAutoupdateFile.close()
                    AutoUpdate = False
            elif(AutoUpdateFileTexts == "no"):
                print(f"{colors.Color.Red}{version.name} >{colors.Color.Yellow} You need to download update manually due auto-update is off! Please turn auto-update in settings if you want to automatically update it.{colors.Color.reset}")
                print("")
                AutoUpdate = False
            elif(AutoUpdateFileTexts == "yes"):
                AutoUpdate = True
            else:
                print("Something doesn't look great in autoupdate.txt or Auto-Update settings.... Make sure everything is right!")
                RepairingAutoupdateFile = open("./autoupdate.txt", "w")
                RepairingAutoupdateFile.write("none")
                RepairingAutoupdateFile.close()
                print(f"{colors.Color.Lime}Successfully repaired autoupdate.txt!{colors.Color.reset}")
                AutoUpdate = False
            if(AutoUpdate == True):
                RequestExecutableFile = requests.get(DownloadUrlLink, stream=True)
                DownloadSizeInB = int(RequestExecutableFile.headers.get("Content-length"))
                DownloadSize = (DownloadSizeInB/1024)/1024
                print(f"- Download size: {DownloadSize} MB")
                print("")
                ContinueDownloading = input(f"{colors.Color.White}Do you want to continue downloading this program? (Y/N){colors.Color.reset}\n")
                if(ContinueDownloading in ["yes", "ye", "y", "yup", "true"]):
                    print("")
                    print("Updating program.... (This may take a long time)")
                    print("Updating program.... 0%")
                    urllib.request.urlretrieve(DownloadUrlLink, "./P.O.S.I-SW.exe")
                    print("Updating program.... 100%")
                    print("")
                    print(f"{colors.Color.Lime}Successfully updated program.{colors.Color.reset}")
                    print(f"{colors.Color.Cyan}Your program is saved on:{colors.Color.reset} {colors.Color.White}{colors.Color.Underline}{CWD}\\P.O.S.I-SW.exe{colors.Color.Nounderline}{colors.Color.reset}")
                    print("")
                elif(ContinueDownloading in ["no", "n", "nope", "false"]):
                    print(f"{colors.Color.Lime}Successfully cancelled operation.{colors.Color.reset}")
                    print("")
                else:
                    print(f"{colors.Color.Red}Because of bad or incorrect answer, we are not going to update this program (Operation cancelled).{colors.Color.reset}")
                    print("")
                RequestExecutableFile.close()
except requests.exceptions.ConnectionError:
    logging.warning(f"Failed to connect {version.name} services. Some features will not be able to work!")
    print(f"{colors.Color.red}Failed to connect {version.name} services. Make sure you are connected with internet to make some features works!\033[39m")
    print("")

while(running):
    while(ToS.Tos == False or ToS.Privacy == False):
        print("\n")
        print("Before you start using our software. Please answer next questions!")
        print("To answer questions input: YES, NO, Y, N, T, F, TRUE or FALSE (Not case-sensitive)")
        print("")
        print("")
        if(ToS.Tos == False):
            AcceptTos = input(f"Do you agree {version.fullname} ({version.name}) Terms of Service?\n")
            if(AcceptTos.upper() == "YES" or AcceptTos.upper() == "Y" or AcceptTos.upper() == "T" or AcceptTos.upper() == "TRUE"):
                try:
                    ToS.Tos = True
                    TosFileData = open("./ToS.py", "w")
                    PrivacyBooleanForfile = False
                    TosFileData.write("Tos = True\n")
                    if(ToS.Privacy == True):PrivacyBooleanForfile = True
                    TosFileData.write(f"Privacy = {PrivacyBooleanForfile}")
                    TosFileData.close()
                    print("Successfully agreed Terms of Service!")
                except ValueError:
                    print("Value error")
            elif(AcceptTos.upper() == "NO" or AcceptTos.upper() == "N" or AcceptTos.upper() == "F" or AcceptTos.upper() == "FALSE"):
                print("Successfully refused Terms of Service!")
                print("Due you denied it you are not able to use this software! Restart this application to agree or refuse again!")
                Leave = input("Press any key to continue....")
                exit("*")
            else:
                print("Incorrect response. Answer with: YES, Y, T, TRUE or NO, N, F, FALSE")

        if(ToS.Privacy == False):
            AcceptPrivacy = input(f"Do you agree {version.fullname} ({version.name}) Privacy Policy?\n")
            if(AcceptPrivacy.upper() == "YES" or AcceptPrivacy.upper() == "Y" or AcceptPrivacy.upper() == "T" or AcceptPrivacy.upper() == "TRUE"):
                try:
                    ToS.Privacy = True
                    TosFileData = open("./ToS.py", "w")
                    TermsBooleanForfile = False
                    if(ToS.Privacy == True):TermsBooleanForfile = True
                    TosFileData.write(f"Tos = {TermsBooleanForfile}\nPrivacy = True")
                    TosFileData.close()
                    print("Successfully agreed Privacy Policy!")
                except ValueError:
                    print("Value error")
            elif(AcceptPrivacy.upper() == "NO" or AcceptPrivacy.upper() == "N" or AcceptPrivacy.upper() == "F" or AcceptPrivacy.upper() == "FALSE"):
                print("Successfully refused Privacy Policy!")
                print("Due you denied it you are not able to use this software! Restart this application to agree or refuse again!")
                Leave = input("Press any key to continue....")
                exit("*")
            else:
                print("Incorrect response. Answer with: YES, Y, T, TRUE or NO, N, F, FALSE")

    while(data.Menu == True):
        print(f"{colors.Color.White}Welcome to {version.name} Menu ({version.version}).{colors.Color.reset}")
        print(f"{colors.Color.White}What service do you want to use?{colors.Color.reset}")
        numbers = [1, 2, 3, 8, 10, 11, 0]
        Services = ["GitHub", "Minecraft", "YouTube", "Settings", "Social", "Credit", "Exit"]
        for number, service in zip(numbers, Services):
            print(f"[{number}] {service}")
        print("")
        SelectedService = input(f"{colors.Color.White}Choose a service:{colors.Color.reset} ")
        if(SelectedService.lower().replace(" ", "") in ["github", "1"]):
            data.GitHubService = True
            data.Menu = False
            GHServiceStartedNow = True
        elif(SelectedService.lower().replace(" ", "") in ["minecraft", "mc", "2"]):
            data.MinecraftMenu = True
            data.Menu = False
            MCServiceStartedNow = True
        elif(SelectedService.lower().replace(" ", "") in ["youtube", "yt", "3"]):
            data.YouTubeMenu = True
            data.Menu = False
            YTServiceStartedNow = True
        #elif(SelectedService.lower().replace(" ", "") in ["custom", "7"]):
        #    data.Custom = True
        #    data.Menu = False
        #    CUSTOMDOWNLOADINGSERVICESTARTEDNOW = True
        elif(SelectedService.lower().replace(" ", "") in ["settings", "8"]):
            print("Coming soon! This will be probably existed in 1.2!")
            print("")
        #elif(SelectedService.lower() == "repair" or SelectedService.replace(" ", "") == "9"):
        #    import repair
        elif(SelectedService.lower().replace(" ", "") in ["social", "socialmedia", "socials", "social_media", "social-media", "10"]):
            data.SocialMenu = True
            data.Menu = False
            SOCIALMENUSTARTEDNOW = True
        elif(SelectedService.lower().replace(" ", "") in ["credit", "credits", "11"]):
            credit.credit()
        elif(SelectedService.lower() == "exit" or SelectedService.replace(" ", "") == "0"):
            logging.info("Closing software....")
            print(messages.CLOSING_SOFTWARE)
            running = False
            logging.warning("Status \"running\" changed from True to False.")
            logging.warning("Stopping logger....")
            logging.shutdown()
            exit()
        else:
            print(messages.NOT_OPTION_MAINMENU)
            print("")

    while(data.GitHubService == True):
        if(GHServiceStartedNow == True):
            print("")
            print(colors.Color.purple+"┌"+"".center(104, "─")+"┐")
            print(colors.Color.purple+"│"+colors.Color.RANDOM+"GitHub Service".center(104, " ")+colors.Color.purple+"│")
            print(colors.Color.purple+"│"+"".center(104, " ")+"│")
            print(colors.Color.purple+"│"+colors.Color.white+"Here you can download GitHub repositories and get information about them".center(104, " ")+colors.Color.purple+"│")
            print(colors.Color.purple+"│"+colors.Color.white+"You must include a GitHub repository link such as: https://github.com/yasserprogamer/POSI-SW".center(104, " ").replace("https://github.com/yasserprogamer/POSI-SW", f"{colors.Color.Underline}https://github.com/yasserprogamer/POSI-SW{colors.Color.Nounderline}")+colors.Color.purple+"│")
            print(colors.Color.purple+"│"+colors.Color.white+"or you can directly input a short path like: yasserprogamer/repository".center(104, " ")+colors.Color.purple+"│")
            print(colors.Color.purple+"│"+"".center(104, " ")+"│")
            print(colors.Color.purple+"│"+colors.Color.cyan+"Type \"CANCEL\" to leave this service. If you got any bug please report it!".center(104, " ").replace("CANCEL", f"{colors.Color.red}CANCEL{colors.Color.cyan}")+colors.Color.purple+"│")
            print(colors.Color.purple+"└"+"".center(104, "─")+"┘"+colors.Color.reset)
            print("")
            colors.window.addToTitle("GitHub")
            GHServiceStartedNow = False
        github = input(f"{colors.Color.White}GitHub repository link or alias:{colors.Color.reset} ").replace("https://github.com/", "").replace("https://www.github.com/", "").replace("http://github.com/", "").replace("http://www.github.com/", "")
        if(github.lower() in ["cancel", "leave", "back", "quit"]):
            data.GitHubService = False
            data.Menu = True
            colors.window.restoreTitle()
            print("")
        elif(github.lower().replace(" ", "") == ""):
            print(end="")
        else:
            try:
                RepositoryZIPdownloadURL = f"https://codeload.github.com/{github}/zip/refs/heads/main"
                RepositoryRequest = requests.get(RepositoryZIPdownloadURL, stream=True)
                if(RepositoryRequest.status_code == 404):
                    RepositoryZIPdownloadURL = f"https://codeload.github.com/{github}/zip/refs/heads/master"
                    RepositoryRequest = requests.get(RepositoryZIPdownloadURL, stream=True)
                StatusCodeOfGitHubReq = RepositoryRequest.status_code
                if(StatusCodeOfGitHubReq == 200):
                    print("")
                    print(f"{colors.Color.Cyan}Successfully found package!{colors.Color.reset}")
                    print(f"{colors.Color.White}Status: {colors.Color.Lime}GOOD!   {colors.Color.White}Downloadable: {colors.Color.Lime}yes{colors.Color.reset}")
                    print("")
                    DownloadSizeInB = int(RepositoryRequest.headers.get("Content-length"))
                    DownloadSize = (DownloadSizeInB/1024)/1024
                    print(f"{colors.Color.Cyan}Download size: {colors.Color.White}{DownloadSize} MB{colors.Color.reset}")
                    print("")
                    EnableCommandFeature = True

                    while(EnableCommandFeature == True):
                        Command = input(f"{colors.Color.White}Type a command to run a feature:{colors.Color.reset} ")

                        if(Command.lower() == "help"):
                            commands = ["help", "download"]
                            DescOfCommands = ["Show you this list!", "Download this GitHub repository"]
                            print("")
                            print("")
                            print("Here is help list that you want:")
                            print("")
                            for command, DescOfCommand in zip(commands, DescOfCommands):
                                print(f'{command.upper()}: {DescOfCommand}')
                            print("")
                        elif(Command.lower() == "download"):
                            print("Downloading files...")
                            if not os.path.exists(f"./GitHub/{github}/"):
                                print("Creating new folders to save files on it...")
                                os.makedirs(f"./GitHub/{github}/")
                                print("Successfully created folders!")
                            i = 0
                            DownloadingOperationStartedNow = True
                            print("")
                            utils.printProgressBar(i, DownloadSizeInB, "Downloading:", "Complete", length=50, fill=f"{colors.Color.Lime}█{colors.Color.reset}")
                            with open(f'./GitHub/{github}/main.zip', 'wb') as file:
                                for filedata in RepositoryRequest.iter_content(1024):
                                    utils.printProgressBar(i + len(filedata), DownloadSizeInB, "Downloading:", "Complete", length=50, fill=f"{colors.Color.Lime}█{colors.Color.reset}")
                                    if(DownloadingOperationStartedNow == False):
                                        i = i + len(filedata)
                                    elif(DownloadingOperationStartedNow == True):
                                        i = len(filedata)
                                        DownloadingOperationStartedNow = False
                                    file.write(filedata)
                            #print("Downloading files.... 0%")
                            #urllib.request.urlretrieve(RepositoryZIPdownloadURL, f"./GitHub/{github}/main.zip")
                            #print("Downloading files.... 100%")
                            print("")
                            print(f"{colors.Color.Lime}Successfully downloaded files!{colors.Color.reset}")
                            print(f"{colors.Color.Cyan}Files are saved on: {colors.Color.White}{colors.Color.Underline}{CWD}\\GitHub\\{github}\\main.zip{colors.Color.Nounderline}".replace("/", "\\"))
                            print("")
                            EnableCommandFeature = False
                        elif(Command.lower().replace(" ", "") == "cancel"):
                            EnableCommandFeature = False
                        else:
                            print(f"{colors.Color.Red}Unknown command. Type \"help\" to get commands list{colors.Color.reset}")
                elif(StatusCodeOfGitHubReq == 404):
                    print(f"{colors.Color.Red}Error: Could not find that repository. It is probably not existed or private. Status code: 404.{colors.Color.reset}")
                    print("")
                elif(StatusCodeOfGitHubReq == 403):
                    print(f"{colors.Color.Red}Error: Bad Gateway. Please try later. Status code: 403.{colors.Color.reset}")
                    print("")
                else:
                    print(f"{colors.Color.Red}Error: Sorry, we can't find a reason for this error! GitHub APIs are probably down or it can be an unknown error. Status code: {StatusCodeOfGitHubReq}{colors.Color.reset}")
                    print("")
            except requests.exceptions.ConnectionError:
                logging.error("No internet connection.")
                errormsg = ""
                print(end=colors.Cursor.hidden)
                for letter in messages.ERR_NO_INTERNET:
                    errormsg = errormsg+letter
                    print("\r"+errormsg, end="\r")
                    time.sleep(0.02)
                print("")
                print(end=colors.Cursor.visible)
                print("")

    while(data.MinecraftMenu):
        if(MCServiceStartedNow == True):
            print("")
            print(colors.Color.Lime+"┌"+"".center(104, "─")+"┐")
            print(colors.Color.Lime+"│"+colors.Color.RANDOM+"Minecraft Services Menu".center(104, " ")+colors.Color.Lime+"│")
            print(colors.Color.Lime+"│"+"".center(104, " ")+"│")
            print(colors.Color.Lime+"│"+colors.Color.White+"Here you can download Minecraft servers with latest protections and safety features!".center(104, " ")+colors.Color.Lime+"│")
            print(colors.Color.Lime+"│"+colors.Color.White+"Log4J protections, automatically accepting EULA and BAT server starting file.".center(104, " ")+colors.Color.Lime+"│")
            print(colors.Color.Lime+"│"+colors.Color.White+"Everything is for free and no money needed!".center(104, " ")+colors.Color.Lime+"│")
            print(colors.Color.Lime+"└"+"".center(104, "─")+"┘"+colors.Color.reset)
            print("")
            MCServiceStartedNow = False
        print(f"{colors.Color.White}What do you want to download or use?{colors.Color.reset}")
        Services = ["Servers", "Back"]
        numbers = [1, 0]
        for number,service in zip(numbers,Services):
            print(f"[{number}] {service}")
        print("")
        SelectedOption = input(f"{colors.Color.White}Select an option or service:{colors.Color.reset} ")
        if(SelectedOption.lower().startswith("server") or SelectedOption.replace(" ", "") == "1"):
            data.MinecraftMenu = False
            data.MinecraftServersMenu = True
            MCServersSoftwareListStartedNow = True
        elif(SelectedOption.lower().startswith("client") or SelectedOption.replace(" ", "") == "2"):
            data.MinecraftMenu = False
            data.MinecraftClientsMenu = True
            MCClientsListStartedNow = True
        elif(SelectedOption.lower().replace(" ", "") in ["0", "back", "quit", "leave", "cancel"]):
            data.MinecraftMenu = False
            data.Menu = True
        else:
            print(messages.WRONG_OR_NOT_OPTION.replace("[option]", SelectedOption))
            print("")

    while (data.MinecraftServersMenu):
        if(MCServersSoftwareListStartedNow == True):
            print("")
            print(colors.Color.Lime+"┌"+"".center(104, "─")+"┐")
            print(colors.Color.Lime+"│"+colors.Color.RANDOM+"Minecraft servers software".center(104, " ")+colors.Color.Lime+"│")
            print(colors.Color.Lime+"│"+"".center(104, " ")+"│")
            print(colors.Color.Lime+"│"+colors.Color.White+"If you play in minecraft releases we recommend you to pick Vanilla as server software for your game.".center(104, " ")+colors.Color.Lime+"│")
            print(colors.Color.Lime+"│"+"".center(104, " ")+"│")
            print(colors.Color.Lime+"│"+colors.Color.White+"NOTE: To make everyone able to join your minecraft server you may need to port forward".center(104, " ")+colors.Color.Lime+"│")
            print(colors.Color.Lime+"│"+colors.Color.White+"your host port! Skipping or ignoring this step may make your server unjoinable by other players.".center(104, " ")+colors.Color.Lime+"│")
            print(colors.Color.Lime+"└"+"".center(104, "─")+"┘"+colors.Color.reset)
            print("")
            MCServersSoftwareListStartedNow = False
        print(f"{colors.Color.White}What software do you want for your server?{colors.Color.reset}")
        MCSoftwares = ["Vanilla", "Snapshot", "PaperMC", "Back"]
        numbers = [1, 2, 3, 0]
        for number,software in zip(numbers,MCSoftwares):
            print(f"[{number}] {software}")
        print("")
        SelectedMCSoftware = input(f"{colors.Color.White}Choose a minecraft server software:{colors.Color.reset} ")
        if(SelectedMCSoftware.lower().startswith("vanilla") or SelectedMCSoftware.replace(" ", "") == "1"):
            data.MinecraftServersMenu = False
            data.MinecraftVanillaServersService = True
        elif(SelectedMCSoftware.lower().startswith("snapshot") or SelectedMCSoftware.replace(" ", "") == "2"):
            data.MinecraftServersMenu = False
            data.MinecraftSnapshotServersService = True
        elif(SelectedMCSoftware.lower().startswith("papermc") or SelectedMCSoftware.replace(" ", "") == "3"):
            data.MinecraftServersMenu = False
            data.MinecraftPaperMCServersService = True
            PaperMCserversServiceStartedNow = True
        elif(SelectedMCSoftware.lower().replace(" ", "") in ["0", "back", "quit", "leave", "menu"]):
            data.MinecraftServersMenu = False
            data.MinecraftMenu = True
            MCServiceStartedNow = True
        else:
            print(f"{colors.Color.Red}Unknown Minecraft server software.{colors.Color.reset}")

    while (data.MinecraftClientsMenu):
        if(MCClientsListStartedNow == True):
            print("")
            print("----------------------------------------------------------------------------------------------------------")
            print("|"+"Minecraft clients software".center(104, " ")+"|")
            print("|"+"".center(104, " ")+"|")
            print("|"+"If you want to play in original minecraft releases, please pick Vanilla vlient.".center(104, " ")+"|")
            print("----------------------------------------------------------------------------------------------------------")
            print("")
            MCClientsListStartedNow = False
        print("What client do you want install?")
        MCSoftwares = ["Vanilla", "Snapshot", "Back"]
        numbers = [1, 0]
        for number,software in zip(numbers,MCSoftwares):
            print(f"[{number}] {software}")
        print("")
        SelectedMCSoftware = input("Choose a minecraft client type: ")
        if(SelectedMCSoftware.lower().startswith("vanilla") or SelectedMCSoftware.replace(" ", "") == "1"):
            data.MinecraftClientsMenu = False
            data.MinecraftVanillaClientsService = True
        else:
            print("Unknown Minecraft server software.")

    while(data.MinecraftVanillaServersService or data.MinecraftSnapshotServersService):
        ServiceType = "servers"
        if(data.MinecraftVanillaServersService == True and data.MinecraftSnapshotServersService == False):
            VersionType = "release"
            ServerType = "Vanilla"
        elif(data.MinecraftVanillaServersService == False and data.MinecraftSnapshotServersService == True):
            VersionType = "snapshot"
            ServerType = "Snapshot"
        print("")
        print(f"Welcome to Minecraft {ServerType} {ServiceType} service.")
        print("")
        print(f"{colors.Color.White}What do you want to do?{colors.Color.reset}")
        print("You have to pick a service by inputting their number")
        MCservices = ["Download a server", "Back"]
        numbers = [1, 0]
        for number, service in zip(numbers, MCservices):
            print(f"[{number}] {service}")
        SelectedOption = input("")
        if(SelectedOption.replace(" ", "") == "1"):
            MCServersDownloadingService = True
        if SelectedOption.lower().replace(" ","") in ["0", "menu", "leave", "quit", "back"]:
            data.MinecraftVanillaServersService = False
            data.MinecraftSnapshotServersService = False
            data.MinecraftServersMenu = True
            MCServersDownloadingService = False

        while (MCServersDownloadingService == True):
            print("")
            print(f"{colors.Color.White}What server version do you want to download?{colors.Color.reset}")
            print(f"{colors.Color.Cyan}Type {colors.Color.Red}CANCEL{colors.Color.Cyan} to back to the recently Menu.{colors.Color.reset}")
            print("")
            VERSION_MANIFEST_URL = "https://launchermeta.mojang.com/mc/game/version_manifest.json"
            AffectedLogForJ1 = ["1.7","1.8","1.9","1.10","1.11"]
            AffectedLogForJ2 = ["1.12","1.13","1.14","1.15","1.16"]
            try:
                ManifestJSON = requests.get(VERSION_MANIFEST_URL).json()
                LatestMCVersion = ManifestJSON["latest"][VersionType]
                print(f"{colors.Color.White}Latest minecraft server version release:{colors.Color.Lime} {LatestMCVersion}{colors.Color.reset}")
                print(f"{colors.Color.White}Available minecraft versions:{colors.Color.reset}")
                for mcserverversion in ManifestJSON["versions"]:
                    if(mcserverversion["type"] == VersionType):
                        print(mcserverversion["id"], end=", ")
                print("\n")
                SelectedMCserverVersion = str(input(f"{colors.Color.White}Pick a minecraft version:{colors.Color.reset} "))
                if(SelectedMCserverVersion.lower() == "cancel"):
                    MCServersDownloadingService = False
                print(SelectedMCserverVersion)
                for MCversion in ManifestJSON["versions"]:
                    if(SelectedMCserverVersion.lower().replace(" ", "") == MCversion["id"] and MCversion["type"] == VersionType):
                        VERSIONPackagesURL =  MCversion["url"]
                        ChoosenVersion = MCversion["id"]
                        ChoosenType = MCversion["type"]
                        VersionJson = requests.get(VERSIONPackagesURL).json()
                        MCServerVersionJarFileSizeInMB = (int(VersionJson["downloads"]["server"]["size"])/1024)/1024
                        print(f"Information about {ChoosenVersion} server version:")
                        print("")
                        print(f"- Version: {ChoosenVersion}")
                        print(f"- Type: {ChoosenType}")
                        print("")
                        print(f"- Download Size: {MCServerVersionJarFileSizeInMB} MB")
                        print("")
                        ContinueDownloadingQuestion = input("Do you want to continue? If your internet is data limited we recommend you to check your data before you start downloading! (Y/N)\n")
                        if(ContinueDownloadingQuestion.lower() in ["yes", "y", "ye", "t", "true"]):
                            START_DOWNLOADING_SERVER = True
                        elif(ContinueDownloadingQuestion.lower() in ["no", "n", "f", "false"]):
                            START_DOWNLOADING_SERVER = False
                            print(f"{colors.Color.Lime}Successfully cancelled operation")
                        else:
                            START_DOWNLOADING_SERVER = False
                            print("Automatically cancelled operation because of an incorrect answer.")
                        MinecraftServerDownloadLink = VersionJson["downloads"]["server"]["url"]
                        if(START_DOWNLOADING_SERVER == True):
                            try:
                                RequestOFMCServerJar = urllib.request.urlopen(MinecraftServerDownloadLink)
                                StatusCodeOfMCServerJarLink = RequestOFMCServerJar.status
                                if(StatusCodeOfMCServerJarLink == 200):
                                    print("STATUS: GOOD - STATUS CODE: 200")
                                    print("")
                                    LogForJProtection = input("Do you want add Log4j protection?\n")
                                    print("")
                                    MCServername = input("How do you want your minecraft server name be? (Leave it blank to skip)\n")
                                    if not MCServername: MCServername = "A Minecraft Server"
                                    print("")
                                    if not os.path.exists(f"./Minecraft/servers/{ChoosenVersion}/{MCServername}/"):
                                        print("Creating new folders for server....")
                                        os.makedirs(f"./Minecraft/servers/{ChoosenVersion}/{MCServername}/")
                                        print("Successfully created new folders for server!")
                                    print(f"Downloading {ChoosenVersion} server.jar 0%")
                                    urllib.request.urlretrieve(MinecraftServerDownloadLink, f"./Minecraft/servers/{ChoosenVersion}/{MCServername}/server.jar")
                                    print("Successfully downloaded server.jar!")
                                    if(LogForJProtection.upper() == "Y" or LogForJProtection.upper() == "YES" or LogForJProtection.upper() == "T" or LogForJProtection.upper() == "TRUE"):
                                        Log4Jprotection = True
                                        VersionNotAffected = True
                                        if(SelectedMCserverVersion.lower().replace(" ", "").startswith("1.17") or SelectedMCserverVersion.lower().replace(" ", "") == "1.18"):
                                            print("Please add the following JVM arguments to your startup command line:\n  -Dlog4j2.formatMsgNoLookups=true")
                                            VersionNotAffected = False
                                        for MCversion in AffectedLogForJ1:
                                            if(SelectedMCserverVersion.lower().replace(" ", "").startswith(MCversion)):
                                                urllib.request.urlretrieve("https://launcher.mojang.com/v1/objects/4bb89a97a66f350bc9f73b3ca8509632682aea2e/log4j2_17-111.xml", f"./Minecraft/servers/{ChoosenVersion}/{MCServername}/log4j2_17-111.xml")
                                                print("Please add the following JVM arguments to your startup command line:\n  -Dlog4j.configurationFile=log4j2_17-111.xml")
                                                VersionNotAffected = False
                                        for MCversion in AffectedLogForJ2:
                                            if(SelectedMCserverVersion.lower().replace(" ", "").startswith(MCversion)):
                                                urllib.request.urlretrieve("https://launcher.mojang.com/v1/objects/02937d122c86ce73319ef9975b58896fc1b491d1/log4j2_112-116.xml", f"./Minecraft/servers/{ChoosenVersion}/{MCServername}/log4j2_112-116.xml")
                                                print("Please add the following JVM arguments to your startup command line:\n  -Dlog4j.configurationFile=log4j2_112-116.xml")
                                                VersionNotAffected = False
                                        if(VersionType == "snapshot"):
                                            print("Log4J protections are not available for snapshots in this software.")
                                            Log4Jprotection = False
                                        elif(VersionNotAffected == True):
                                            print(f"Your server version is not affected by Log4J.")
                                            Log4Jprotection = False
                                    elif(LogForJProtection.upper() == "N" or LogForJProtection.upper() == "NO" or LogForJProtection.upper() == "F" or LogForJProtection.upper() == "FALSE"):
                                        Log4Jprotection = False
                                        print("You successfully denied adding Log4J protection which is very risky.")
                                        print("REMEMBER: Servers that don't have Log4J protection are unsecure or having bad protections. Hackers can easily run a command or code to hack other players computer.")
                                        print("")
                                    print("")
                                    AutoAcceptingEULAQuestion = input("Do you want to automatically accept EULA?\n")
                                    if(AutoAcceptingEULAQuestion.upper() == "Y" or AutoAcceptingEULAQuestion.upper() == "YES" or AutoAcceptingEULAQuestion.upper() == "T" or AutoAcceptingEULAQuestion.upper() == "TRUE"):
                                        print("")
                                        print("Accepting Minecraft EULA....")
                                        print("")
                                        print("NOTE: This feature is not going to start your server. It will directly create eula.txt file and agree EULA.")
                                        print("")
                                        EULAFile = open(f"./Minecraft/servers/{ChoosenVersion}/{MCServername}/eula.txt", "w")
                                        EULAFile.write("#By changing the setting below to TRUE you are indicating your agreement to our EULA (https://account.mojang.com/documents/minecraft_eula).\n")
                                        EULAFile.write(f"#No time provided!")
                                        EULAFile.write("eula=true")
                                        EULAFile.close()
                                        print("Successfully accepted EULA!")
                                        print("")
                                    elif(AutoAcceptingEULAQuestion.upper() == "N" or AutoAcceptingEULAQuestion.upper() == "NO" or AutoAcceptingEULAQuestion.upper() == "F" or AutoAcceptingEULAQuestion.upper() == "FALSE"):
                                        print("")
                                        print("User refused to automatically accept EULA.")
                                        print("")
                                        print("REMEMBER: To start your Minecraft server you are required to accept Mojang EULA! You have to do it with yourself from now.")
                                        print("")
                                    else:
                                        print(f"\"{AutoAcceptingEULAQuestion}\" is not an option! Answer with: YES, Y, TRUE, T or N, NO, F, FALSE or with their number.")
                                        print("")
                                    AddBat = input("Do you want to make a bat file that start server?\n")
                                    if(AddBat.upper() == "Y" or AddBat.upper() == "YES" or AddBat.upper() == "T" or AddBat.upper() == "TRUE"):
                                        if(Log4Jprotection == True):
                                            JVMArgument = ""
                                            if(SelectedMCserverVersion.lower().replace(" ", "").startswith("1.17") or SelectedMCserverVersion.lower().replace(" ", "") == "1.18"):
                                                JVMArgument = " -Dlog4j2.formatMsgNoLookups=true"
                                            for MCversion in AffectedLogForJ1:
                                                if(SelectedMCserverVersion.lower().replace(" ", "").startswith(MCversion)):
                                                    JVMArgument = " -Dlog4j.configurationFile=log4j2_17-111.xml"
                                            for MCversion in AffectedLogForJ2:
                                                if(SelectedMCserverVersion.lower().replace(" ", "").startswith(MCversion)):
                                                    JVMArgument = " -Dlog4j.configurationFile=log4j2_112-116.xml"
                                            shfile = open(f"./Minecraft/servers/{ChoosenVersion}/{MCServername}/start.bat", "w")
                                            print("Server rams set at: 1GB. You can change it anytime")
                                            shfile.write(f"java -Xmx1024M -Xms1024M{JVMArgument} -jar server.jar nogui\nPAUSE")
                                            print(f"Automatically added JVM arguments:{JVMArgument}")
                                            shfile.close()
                                        elif(Log4Jprotection == False):
                                            shfile = open(f"./Minecraft/servers/{ChoosenVersion}/{MCServername}/start.bat", "w")
                                            print("Server rams set at: 1GB. You can change it anytime")
                                            shfile.write("java -Xmx1024M -Xms1024M -jar server.jar nogui\nPAUSE")
                                            shfile.close()
                                        else:
                                            print("Unknown error.")
                                    print("Downloading server.jar 100%")
                                    print("")
                                    print("Successfully download file!")
                                    print(f"{colors.Color.Cyan}Your file is saved on: {colors.Color.White}{colors.Color.Underline}{CWD}\\Minecraft\\servers\\{ChoosenVersion}\\{MCServername}\\server.jar{colors.Color.Nounderline}{colors.Color.reset}")
                            except:
                                print("")
                                print("Failed to download server.jar due an internet connection issue or service is down.")
            except:
                print("Failed to connect to Minecraft services. Make sure you are connected with internet! If you believe this is a bug please report it!")
                MCServersDownloadingService = False

    while(data.MinecraftPaperMCServersService):
        if(PaperMCserversServiceStartedNow == True):
            print("")
            print(colors.Color.Lime+"┌"+"".center(104, "─")+"┐")
            print("│"+colors.Color.Bold+colors.Color.RANDOM+"PaperMC Minecraft server software".center(104," ")+colors.Color.NoBold+colors.Color.Lime+"│")
            print("│"+"".center(104," ")+"│")
            print(colors.Color.Lime+"│"+colors.Color.White+"PaperMC is a Minecraft server software which allow you to install plugins and addons on it!".center(104," ")+colors.Color.Lime+"│")
            print(colors.Color.Lime+"│"+colors.Color.White+"And using it you can make an advanced Minecraft server for free!".center(104," ")+colors.Color.Lime+"│")
            print(colors.Color.Lime+"└"+"".center(104, "─")+"┘"+colors.Color.reset)
            print("")
            PaperMCserversServiceStartedNow = False
        print(f"{colors.Color.White}What do you want to do?{colors.Color.reset}")
        numbers = [1, 0]
        options = ["Download a PaperMC server jar.", "Back to recent Menu."]
        for number, option in zip(numbers, options):
            print(f"[{number}] {option}")
        print()
        PickedOption = input(f"{colors.Color.White}Pick an option:{colors.Color.reset} ")

        DownloadingMCServer = False

        if(PickedOption.lower().replace(" ", "") == "1"):
            DownloadingMCServer = True
            print("")
        elif(PickedOption.lower().replace(" ", "") == "0"):
            data.MinecraftPaperMCServersService = False
            data.MinecraftServersMenu = True
            MCServersSoftwareListStartedNow = True
        else:
            print(messages.WRONG_OR_NOT_OPTION.replace("[option]", PickedOption))
            print("")

        while(DownloadingMCServer):
            try:
                print(f"{colors.Color.White}Latest PaperMC server version:{colors.Color.Lime} {papermc.Paper.GetLatestMinecraftVersion()}{colors.Color.reset}")
                print(f"{colors.Color.White}Available PaperMC versions:{colors.Color.reset}")
                PaperVersionsList = papermc.Paper.GetVersionsList()
                for MCversion in PaperVersionsList:
                    print(MCversion, end=", ")
                print()
                print()
                SelectedMCserverVersion = input(f"{colors.Color.White}Pick a PaperMC version:{colors.Color.reset} ")
                if(SelectedMCserverVersion.lower().replace(" ", "") in ["cancel", "leave", "quit"]):
                    DownloadingMCServer = False
                elif(SelectedMCserverVersion.lower().replace(" ", "") in PaperVersionsList):
                    SelectedMCserverVersion = SelectedMCserverVersion.replace(" ", "")
                    print()
                    LatestPaperBuild = papermc.Paper.GetLatestMCBuild(SelectedMCserverVersion)
                    PaperBuildsList = papermc.Paper.GetBuildsList(SelectedMCserverVersion)
                    print(f"{colors.Color.White}Latest PaperMC build:{colors.Color.Lime} {LatestPaperBuild}{colors.Color.reset}")
                    print(f"{colors.Color.White}Available PaperMC builds:{colors.Color.reset}")
                    for MCBuild in PaperBuildsList:
                        print(MCBuild, end=", ")
                    print()
                    print()
                    print("> Leave it blank to select latest build.")
                    SelectedMCserverBuild = input(f"{colors.Color.White}Select a PaperMC build:{colors.Color.reset} ")

                    if(SelectedMCserverBuild.lower().replace(" ", "") == "" or not SelectedMCserverBuild):
                        SelectedMCserverBuild = str(LatestPaperBuild)

                    if(SelectedMCserverBuild.lower().replace(" ", "") in ["cancel", "leave", "quit"]):
                        DownloadingMCServer = False
                    elif(int(SelectedMCserverBuild.lower().replace(" ", "")) in PaperBuildsList):
                        SelectedMCserverBuild = int(SelectedMCserverBuild)
                        PaperMCServerFilename = papermc.Paper.GetFilename(SelectedMCserverVersion, SelectedMCserverBuild)
                        DownloadSize = papermc.Paper.GetDownloadSize(SelectedMCserverVersion, SelectedMCserverBuild)
                        print()
                        print(f"Information about PaperMC {SelectedMCserverVersion}:")
                        print()
                        print("┌─────────────────────┬────────────────────────────────────┐")
                        print("│ Info                │ Version / Number / Text            │")
                        print("├─────────────────────┼────────────────────────────────────┤")
                        print("│ Minecraft version   │"+SelectedMCserverVersion.center(36, " ")+"│")
                        print("│ Build               │"+str(SelectedMCserverBuild).center(36, " ")+"│")
                        print("│ Download size       │"+DownloadSize.center(36, " ")+"│")
                        print("├─────────────────────┼────────────────────────────────────┤")
                        print("│ Log4J protection    │                Off                 │")
                        print("│ Auto EULA           │                Off                 │")
                        print("│ BAT or SH File      │                Off                 │")
                        print("├─────────────────────┼────────────────────────────────────┤")
                        print("│ Type                │              PaperMC               │")
                        print("│ Filename            │"+PaperMCServerFilename.center(36, " ")+"│")
                        print("└─────────────────────┴────────────────────────────────────┘")
                        print()
                        print("> If you leave it blank, empty or answered wrong it will cancel operation.")
                        ContinueDownloading = input(f"{colors.Color.White}Do you want to continue downloading this file? ({colors.Color.Lime}Y{colors.Color.White}/{colors.Color.Red}N{colors.Color.White}){colors.Color.reset}\n")
                        print()
                        if(ContinueDownloading.lower().replace(" ", "").replace(".", "") in ["yes", "y", "ye", "yeah", "yup", "true"]):
                            print("> Leave it blank to skip.")
                            MCservername = input(f"{colors.Color.White}How do you want your Minecraft server name be?{colors.Color.reset}\n")
                            print(f"Downloading PaperMC {SelectedMCserverVersion}....")
                            print(f"Downloading PaperMC {SelectedMCserverVersion} 0%")
                            PaperMCServerFilename = papermc.Paper.DownloadVersion(SelectedMCserverVersion, SelectedMCserverBuild, f"./Minecraft/servers/Paper-{SelectedMCserverVersion}/{MCservername}/")
                            print(f"Downloading PaperMC {SelectedMCserverVersion} 100%")
                            print()
                            print(f"{colors.Color.Lime}Successfully downloaded file!")
                            print(f"{colors.Color.Cyan}Your file is saved on: {colors.Color.White}{colors.Color.Underline}{CWD}\\Minecraft\\servers\\Paper-{SelectedMCserverVersion}\\{MCservername}\\{PaperMCServerFilename}{colors.Color.Nounderline}{colors.Color.reset}")
                            print()
                            DownloadingMCServer = False
                        else:
                            print(f"{colors.Color.Lime}Successfully cancelled operation!{colors.Color.reset}")
                            print()
                    else:
                        print("Error: Wrong answer. Try again!")
                else:
                    print("Error: Wrong answer. Try again!")
            except ConnectionError:
                print(messages.ERR_NO_INTERNET)
                print()
                DownloadingMCServer = False

    while(data.YouTubeMenu):
        if(YTServiceStartedNow == True):
            print("")
            YTServiceStartedNow = False
            print(colors.Color.Red+"┌"+"".center(104, "─")+"┐")
            print("│"+colors.Color.Bold+colors.Color.RANDOM+"YouTube Services Menu".center(104," ").replace("YouTube", f"{colors.Color.White}You{colors.Color.Red}Tube{colors.Color.RANDOM}")+colors.Color.NoBold+colors.Color.Red+"│")
            print("│"+"".center(104," ")+"│")
            print(colors.Color.Red+"│"+colors.Color.White+"Here where you can download and get info of YouTube videos that you want for free!".center(104," ")+colors.Color.Red+"│")
            print(colors.Color.Red+"│"+colors.Color.White+"And you can do same with Thumbnails.".center(104," ")+colors.Color.Red+"│")
            print("│"+"".center(104," ")+"│")
            print("│"+"REMEMBER: Downloading copyrighted YouTube videos is ILLEGAL! I'm NOT responsible for your downloads.".center(104," ")+"│")
            print("│"+"You must know how, why and where to use copyrighted items.".center(104," ")+"│")
            print(colors.Color.Red+"└"+"".center(104, "─")+"┘"+colors.Color.reset)
            print("")
            numbers = [1, 2, 3, 9, 0]
            Services = ["Download a YouTube video", "Download a YouTube Thumbnail of a video", "Download a YouTube playlist (Coming soon)", "Delete all YouTube videos and thumbnails", "Back to Main Menu"]
            for number,service in zip(numbers, Services):
                print(f"[{number}] {service}")
            print("")
        PickedOption = input(f"{colors.Color.White}Pick an option:{colors.Color.reset} ")
        if(PickedOption.replace(" ", "") == "0"):
            data.Menu = True
            data.YouTubeMenu = False
        elif(PickedOption.replace(" ", "") == "1"):
            data.YouTubeVideoDownloadService = True
            data.YouTubeMenu = False
            YTVideoDOWNLOADSERVICESTARTEDNOW = True
        elif(PickedOption.replace(" ", "") == "2"):
            data.YouTubeThumbnailDownloadService = True
            data.YouTubeMenu = False
            YTThumbnailDOWNLOADSERVICESTARTEDNOW = True
        elif(PickedOption.replace(" ", "") == "9"):
            os.system("cls")
            print("")
            print(f"{colors.Color.Gold}───────────────────────────────────────────────────────────────────────────{colors.Color.reset}")
            InAsk = "backup"
            while(InAsk == "backup"):
                AskCreateBackup = input(f"{colors.Color.White}Do you want to create a backup before starting operation? ({colors.Color.Lime}Y{colors.Color.White}/{colors.Color.Red}N{colors.Color.White}){colors.Color.reset}\n")
                if(AskCreateBackup.lower().replace(" ", "") in ["y", "ye", "yes", "true"]):
                    BACKUP = True
                    if(not os.path.exists("./backups/")):
                        os.makedirs("./backups/")
                    print("")
                    print(f"{colors.Color.Orange}NOTE:{colors.Color.Yellow} Backup may take long time to complete deleting operation. Closing window or console may cause problems to compressed file.{colors.Color.reset}")
                    print("")
                    InAsk = "delete_videos"
                elif(AskCreateBackup.lower().replace(" ", "") in ["n", "no", "false"]):
                    BACKUP = False
                    print("")
                    InAsk = "delete_videos"
                else:
                    print(f"")
                    print("")
            while(InAsk == "delete_videos"):
                ConfirmDeletingVideos = input(f"{colors.Color.White}Do you really want to DELETE all YouTube videos are saved in your device? ({colors.Color.Lime}Y{colors.Color.White}/{colors.Color.Red}N{colors.Color.White}){colors.Color.reset}\n")
                if(ConfirmDeletingVideos.lower() in ["y", "ye", "yes", "true"]):
                    print("")
                    print("\rCounting how many folders/videos are downloaded", end="\r")
                    time.sleep(0.8)
                    print("\rCounting how many folders/videos are downloaded.", end="\r")
                    time.sleep(0.8)
                    print("\rCounting how many folders/videos are downloaded..", end="\r")
                    time.sleep(0.8)
                    print("\rCounting how many folders/videos are downloaded...", end="\r")
                    time.sleep(0.8)
                    print("\rCounting how many folders/videos are downloaded....", end="\n")
                    if(not os.path.exists("./YouTube/videos/")):
                        print(f"{colors.Color.Yellow}Found 0 files or videos!{colors.Color.reset}")
                        print(f"{colors.Color.Lime}Great! There is nothing to delete now.{colors.Color.reset}")
                        BACKUP = False
                        InAsk = None
                    else:
                        VideosInArray = glob.glob(".\\YouTube\\videos\\*\\*.mp4")
                        LengthOfVideos = len(VideosInArray)
                        if(LengthOfVideos == 1):
                            FileOrFiles = "file"
                            VideoOrVideos = "video"
                        else:
                            FileOrFiles = "files"
                            VideoOrVideos = "videos"
                        print(f"{colors.Color.Yellow}Found {LengthOfVideos} {FileOrFiles} or {VideoOrVideos}!{colors.Color.reset}")
                        print(f"{colors.Color.Lime}Deleting logger is successfully activated!{colors.Color.reset}")
                        print("")
                        if(BACKUP == True):
                            if(not os.path.exists("./backups/")):
                                os.makedirs("./backups/")
                            BackupTime = datetime.date.today().strftime("%m-%d-%y-%H.%M.%S")
                            BackupZipFilename = f"YouTube-videos-Backup-{BackupTime}.zip"
                            BackupZipFile = zipfile.ZipFile(f"./backups/{BackupZipFilename}", "w", zipfile.ZIP_DEFLATED)
                        for video in VideosInArray:
                            if(BACKUP == True):
                                print(f"[%time%] {colors.Color.Yellow}Adding \"{video}\" video to backup....{colors.Color.reset}".replace("%time%", f"{datetime.datetime.today().hour}:{datetime.datetime.today().minute}:{datetime.datetime.today().second}"))
                                logging.debug(f"Adding \"{video}\" video to backup....")
                                BackupZipFile.write(video)
                                logging.debug(f"Successfully added \"{video}\" video to backup!")
                                print(f"[%time%] {colors.Color.Lime}Successfully made a backup for \"{video}\" video!{colors.Color.reset}".replace("%time%", f"{datetime.datetime.today().hour}:{datetime.datetime.today().minute}:{datetime.datetime.today().second}"))
                            print(f"[%time%] {colors.Color.Orange}Deleting \"{video}\" video....{colors.Color.reset}".replace("%time%", f"{datetime.datetime.today().hour}:{datetime.datetime.today().minute}:{datetime.datetime.today().second}"))
                            logging.warning(f"Deleting \"{video}\" video....")
                            os.remove(video)
                            logging.debug(f"Successfully deleted \"{video}\" video!")
                            print(f"[%time%] {colors.Color.Lime}Successfully deleted \"{video}\" video!{colors.Color.reset}".replace("%time%", f"{datetime.datetime.today().hour}:{datetime.datetime.today().minute}:{datetime.datetime.today().second}"))
                            print("")
                        if(BACKUP == True):
                            BackupZipFile.close()
                        print(f"{colors.Color.Red}Successfully disactivated Deleting Logger!{colors.Color.reset}")
                        print("")
                        print(f"{colors.Color.Lime}Successfully deleted all YouTube videos!{colors.Color.reset}")
                        if(BACKUP == True):
                            print(f"{colors.Color.Cyan}Your backup file saved on: {colors.Color.White}{colors.Color.Underline}{CWD}\\backups\\{BackupZipFilename}{colors.Color.Nounderline}{colors.Color.reset}")
                        InAsk = None
                YTServiceStartedNow = True
        else:
            print(messages.WRONG_OR_NOT_OPTION.replace("[option]", PickedOption))
            print("")
    
    while(data.YouTubeVideoDownloadService):
        if(YTVideoDOWNLOADSERVICESTARTEDNOW == True):
            print("")
            print(colors.Color.Red+"┌"+"".center(104, "─")+"┐")
            print(colors.Color.Red+"│"+colors.Color.White+"To download a YouTube video, you need to input your video link first, after".center(104," ")+colors.Color.Red+"│")
            print(colors.Color.Red+"│"+colors.Color.White+"choose the resolution you want (if your Internet is data limited please pick the lowest quality)".center(104," ")+colors.Color.Red+"│")
            print(colors.Color.Red+"│"+colors.Color.White+"then wait until your video be successfully downloaded.".center(104," ")+colors.Color.Red+"│")
            print(colors.Color.Red+"│"+"".center(104," ")+"│")
            print(colors.Color.Red+"│"+colors.Color.Cyan+"Type \"CANCEL\" to back to YouTube services Menu.".center(104," ").replace("CANCEL", f"{colors.Color.Red}CANCEL{colors.Color.Cyan}")+colors.Color.Red+"│")
            print(colors.Color.Red+"└"+"".center(104, "─")+"┘"+colors.Color.reset)
            print("")
            YTDOWNLOADSERVICESTARTEDNOW = False
        VideoLink = input(f"{colors.Color.White}Paste your video link here:{colors.Color.reset}\n")
        ContinueYTDownloadingService = False
        if(VideoLink.lower().replace(" ", "") == "cancel"):
            data.YouTubeVideoDownloadService = False
            data.YouTubeMenu = True
            YTServiceStartedNow = True
        else:
            YouTube_services.GetInfoAboutVideo(VideoLink)
            ContinueYTDownloadingService = True
        
        if(ContinueYTDownloadingService == True):
            print("Available resolutions:\nLow: 360p\nNormal: 720p (HD)\nHigh: 1080p (Full HD)\nVery high: 2160p (4K) (NO AUDIO)")
            VideoQuality = input(f"{colors.Color.White}Type resolution of video that you want:{colors.Color.reset} ")
            if VideoQuality.lower() in ["cancel", "exit", "leave"]:
                print("Do you want to leave this downloading operation or back to menu?")
            else:
                if VideoQuality.lower() in ["low", "360", "360p"]:
                    VideoQuality = 18
                elif VideoQuality.lower() in ["normal", "720", "720p", "hd"]:
                    VideoQuality = 22
                elif VideoQuality.lower() in ["high", "1080", "1080p", "fullhd", "full_hd", "full hd"]:
                    VideoQuality = 137
                elif VideoQuality.lower() in ["veryhigh", "very high", "very_high", "2160", "2160p", "4k"]:
                    VideoQuality = 313
                else:
                    print("Because of incorrect answer or usage, we are going to choose the lowest quality of video (144p) for you.")
                    VideoQuality = 18

                YouTube_services.DownloadVideo(VideoLink, VideoQuality)

    while(data.YouTubeThumbnailDownloadService):
        if(YTThumbnailDOWNLOADSERVICESTARTEDNOW == True):
            print("")
            print(colors.Color.Red+"┌"+"".center(104, "─")+"┐")
            print(colors.Color.Red+"│"+colors.Color.RANDOM+"YouTube Thumbnails".center(104," ").replace("YouTube", f"{colors.Color.White}You{colors.Color.Red}Tube{colors.Color.RANDOM}")+colors.Color.Red+"│")
            print("│"+"".center(104," ")+"│")
            print(colors.Color.Red+"│"+colors.Color.Cyan+"Type \"CANCEL\" to back to YouTube services Menu.".center(104," ").replace("CANCEL", f"{colors.Color.Red}CANCEL{colors.Color.Cyan}")+colors.Color.Red+"│")
            print(colors.Color.Red+"└"+"".center(104, "─")+"┘"+colors.Color.reset)
            print("")
            YTThumbnailDOWNLOADSERVICESTARTEDNOW = False
        VideoLink = input(f"{colors.Color.White}Paste your video link here:{colors.Color.reset}\n")
        if(VideoLink.lower().replace(" ", "") in ["cancel", "quit", "leave"]):
            data.YouTubeThumbnailDownloadService = False
            data.YouTubeMenu = True
            YTServiceStartedNow = True
        else:
            YouTube_services.DownloadThumbnail(VideoLink)

    while(data.SocialMenu):
        if(SOCIALMENUSTARTEDNOW == True):
            print("")
            print(colors.Color.Cyan+"┌"+"".center(104, "─")+"┐")
            print(colors.Color.Cyan+"│"+colors.Color.Bold+colors.Color.RANDOM+"Social Media".center(104, " ")+colors.Color.Cyan+"│")
            print(colors.Color.Cyan+"│"+"".center(104, " ")+"│")
            print(colors.Color.Cyan+"│"+colors.Color.White+"Here you can join us or follow our Social Media.".center(104, " ")+colors.Color.Cyan+"│")
            print(colors.Color.Cyan+"│"+colors.Color.White+"You are able to join our main and developers server in anytime you want!".center(104, " ")+colors.Color.Cyan+"│")
            print(colors.Color.Cyan+"└"+"".center(104, "─")+"┘"+colors.Color.reset)
            print("")
            SOCIALMENUSTARTEDNOW = False

        print(f"What do you want to join or follow?")
        SocialMedias = ["Discord", "Back"]
        numbers = [1, 0]
        for number,socialmedia in zip(numbers, SocialMedias):
            print(f"[{number}] {socialmedia}")
        print("")
        SelectedSocialMedia = input(f"{colors.Color.White}Choose a social media you want to follow or join:{colors.Color.reset} ")
        if(SelectedSocialMedia.lower().replace(" ", "") in ["1", "discord"]):
            JoinDiscord = True
            while (JoinDiscord):
                print("")
                print("====================================================================")
                print("")
                print("Main Discord server (Official): https://discord.gg/wJtBMnu")
                print("")
                print("Yasserprogamer's server (Founder): https://discord.gg/wJtBMnu")
                print("")
                print("====================================================================")
                print("")
                print("Opening browser and new tab to automatically join Discord server....")
                webbrowser.open_new_tab("https://discord.gg/wJtBMnu")
                print("")
                JoinDiscord = False
        elif(SelectedSocialMedia.lower().replace(" ", "") in ["0", "back", "leave", "mainmenu", "quit", "menu"]):
            data.SocialMenu = False
            data.Menu = True
        else:
            print(messages.WRONG_OR_NOT_OPTION.replace("[option]", SelectedSocialMedia))
            print("")