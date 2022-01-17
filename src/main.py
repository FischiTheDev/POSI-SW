import urllib.request
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

OSplatformVersion = "Unknown!"

if(sys.platform.lower() == "win32"):
    OSplatformVersion = f"Windows {sys.getwindowsversion().major}"
elif(sys.platform.lower() in ["linux", "linux2"]):
    OSplatformVersion = "Linux"
elif(sys.platform.lower() == "darwin"):
    OSplatformVersion = "Mac OS"

CWD = os.getcwd()

try:
    os.system(f"title {version.name} ({version.version}) - {version.fullname}")
except:
    actlikenothinghappened = ""

print("".center(76, "="))
print("|"+"".center(74, " ")+"|")
print("|"+" ____   ___   ____   ___     ______        __".center(74, " ")+"|")
print("|"+"|  _ \ / _ \ / ___| |_ _|   / ___\ \      / /".center(74, " ")+"|")
print("|"+"| |_) | | | |\___ \  | |____\___ \\\\ \ /\ / / ".center(74, " ")+"|")
print("|"+"|  __/| |_| | ___) | | |_____|__) |\ V  V /  ".center(74, " ")+"|")
print("|"+"|_| (_)\___(_)____(_)___|   |____/  \_/\_/   ".center(74, " ")+"|")
print("|"+"".center(74, " ")+"|")
print("|"+f"{version.fullname} ({version.version})".center(74, " ")+"|")
print("|"+f"{OSplatformVersion}".center(74, " ")+"|")
print("|"+"".center(74, " ")+"|")
print("|"+f"{version.CopyrightText}".center(74, " ")+"|")
print("".center(76, "="))

running = True

print("")
try:
    UpdateNotificationStatusCode = requests.get("https://posi-sw.github.io/website/version/api/updates/latest.html").status_code
    if(UpdateNotificationStatusCode == 200):
        UpdateNotification = requests.get("https://posi-sw.github.io/website/version/api/updates/latest.html").text.replace(" ", "").replace("\n", "")  
        if(version.version != UpdateNotification):
            print(f"There is new {UpdateNotification} update for this software! You are still on {version.version} version.")
            print("We recommended you to update because we may fixed some of bugs and added new features that you will like! Updating is kinda important for some of outdated versions")
            print("")
except:
    print(f"Failed to connect {version.name} services. Make sure you are connected with internet to make some features works!")
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
        print("")
        print(f"Welcome to {version.name} ({version.version}).")
        print(f"What service do you want to use?")
        numbers = [1, 2, 3, 8, 10, 11, 0]
        Services = ["GitHub", "Minecraft", "YouTube", "Settings", "Social", "Credit", "Exit"]
        for number, service in zip(numbers, Services):
            print(f"[{number}] {service}")
        print("")
        SelectedService = input("Choose a service: ")
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
            running = False
            print("Closing software....")
            exit()
        else:
            print(messages.NOT_OPTION_MAINMENU)
            print("")

    while(data.GitHubService == True):
        if(GHServiceStartedNow == True):
            print("")
            print("----------------------------------------------------------------------------------------------------------")
            print("|"+"GitHub Service".center(104, " ")+"|")
            print("|"+"".center(104, " ")+"|")
            print("|"+"Here you can download GitHub repositories and get information about them".center(104, " ")+"|")
            print("|"+"You must include a GitHub repository link such: https://github.com/POSI-SW/POSI-SW".center(104, " ")+"|")
            print("|"+"or you can directly input a short path like: yasserprogamer/repository".center(104, " ")+"|")
            print("|"+"".center(104, " ")+"|")
            print("|"+"Type \"CANCEL\" to leave this service. If you got any bug please report it!".center(104, " ")+"|")
            print("----------------------------------------------------------------------------------------------------------")
            print("")
            GHServiceStartedNow = False
        github = input("GitHub repository link or alias: ").replace("https://github.com/", "").replace("https://www.github.com/", "").replace("http://github.com/", "").replace("http://www.github.com/", "")
        if(github.lower() in ["cancel", "leave", "back", "quit"]):
            data.GitHubService = False
            data.Menu = True
        else:
            RepositoryZIPdownloadURL = f"https://codeload.github.com/{github}/zip/refs/heads/main"
            RepositoryRequest = requests.get(RepositoryZIPdownloadURL)
            StatusCodeOfGitHubReq = RepositoryRequest.status_code
            if(StatusCodeOfGitHubReq == 200):
                print("Successfully found package!")
                print("Status: GOOD!   Downloadable: yes")
                print("")

                EnableCommandFeature = True

                while(EnableCommandFeature == True):
                    Command = input("Type a command to run a feature: ")

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
                        print("Downloading files.... 0%")
                        urllib.request.urlretrieve(RepositoryZIPdownloadURL, f"./GitHub/{github}/main.zip")
                        print("Downloading files.... 100%")
                        print("")
                        print("Successfully downloaded files!")
                        print(f"Files are saved on: {CWD}\\GitHub\\{github}\\main.zip")
                        EnableCommandFeature = False
                    else:
                        print("Unknown command. Type \"help\" to get commands list")

    while(data.MinecraftMenu):
        if(MCServiceStartedNow == True):
            print("")
            print("----------------------------------------------------------------------------------------------------------")
            print("|"+"Minecraft Services Menu".center(104, " ")+"|")
            print("|"+"".center(104, " ")+"|")
            print("|"+"Here you can download Minecraft servers with latest protections and safety features!".center(104, " ")+"|")
            print("|"+"Log4J protections, automatically accepting EULA and SH server starting file.".center(104, " ")+"|")
            print("|"+"Everything is for free and no money needed!".center(104, " ")+"|")
            print("----------------------------------------------------------------------------------------------------------")
            print("")
            MCServiceStartedNow = False
        print("What do you want to download or use?")
        Services = ["Servers", "Back"]
        numbers = [1, 0]
        for number,service in zip(numbers,Services):
            print(f"[{number}] {service}")
        print("")
        SelectedOption = input("Select an option or service: ")
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
            print("----------------------------------------------------------------------------------------------------------")
            print("|"+"Minecraft servers software".center(104, " ")+"|")
            print("|"+"".center(104, " ")+"|")
            print("|"+"If you play in minecraft releases we recommend you to pick Vanilla as server software for your game.".center(104, " ")+"|")
            print("|"+"".center(104, " ")+"|")
            print("|"+"NOTE: To make everyone able to join your minecraft server you may need to port forward".center(104, " ")+"|")
            print("|"+"your host port! Skipping or ignoring this step may make your server unjoinable by other players.".center(104, " ")+"|")
            print("----------------------------------------------------------------------------------------------------------")
            print("")
            MCServersSoftwareListStartedNow = False
        print("What software do you want for your server?")
        MCSoftwares = ["Vanilla", "Back"]
        numbers = [1, 0]
        for number,software in zip(numbers,MCSoftwares):
            print(f"[{number}] {software}")
        print("")
        SelectedMCSoftware = input("Choose a minecraft server software: ")
        if(SelectedMCSoftware.lower().startswith("vanilla") or SelectedMCSoftware.replace(" ", "") == "1"):
            data.MinecraftServersMenu = False
            data.MinecraftVanillaServersService = True
        elif(SelectedMCSoftware.lower().replace(" ", "") in ["0", "back", "quit", "leave", "menu"]):
            data.MinecraftServersMenu = False
            data.MinecraftMenu = True
        else:
            print("Unknown Minecraft server software.")

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
        MCSoftwares = ["Vanilla", "Back"]
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

    while(data.MinecraftVanillaServersService):
        ServiceType = "servers"
        print("")
        print(f"Welcome to Minecraft Vanilla {ServiceType} service.")
        print("")
        print("What do you want to do?")
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
            data.MinecraftServersMenu = True
            MCServersDownloadingService = False

        while (MCServersDownloadingService == True):
            print("")
            print("What server version do you want to download?")
            print("Type CANCEL to back to the recently Menu.")
            print("")
            VERSION_MANIFEST_URL = "https://launchermeta.mojang.com/mc/game/version_manifest.json"
            AffectedLogForJ1 = ["1.7","1.8","1.9","1.10","1.11"]
            AffectedLogForJ2 = ["1.12","1.13","1.14","1.15","1.16"]
            try:
                ManifestJSON = requests.get(VERSION_MANIFEST_URL).json()
                LatestMCVersion = ManifestJSON["latest"]["release"]
                print(f"Latest minecraft server version release: {LatestMCVersion}")
                print("Available minecraft versions:")
                for mcserverversion in ManifestJSON["versions"]:
                    if(mcserverversion["type"] == "release"):
                        print(mcserverversion["id"], end=", ")
                print("\n")
                SelectedMCserverVersion = str(input("Pick a minecraft version: "))
                if(SelectedMCserverVersion.lower() == "cancel"):
                    MCServersDownloadingService = False
                print(SelectedMCserverVersion)
                for MCversion in ManifestJSON["versions"]:
                    if(SelectedMCserverVersion.lower().replace(" ", "") == MCversion["id"]):
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
                            print("Successfully canceled operation")
                        else:
                            START_DOWNLOADING_SERVER = False
                            print("Automatically canceled operation because of an incorrect answer.")
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
                                        if(VersionNotAffected == True):
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
                                    print(f"Your file is saved on: {CWD}\\Minecraft\\servers\\{ChoosenVersion}\\{MCServername}\\server.jar")
                            except:
                                print("")
                                print("Failed to download server.jar due an internet connection issue or service is down.")
            except:
                print("Failed to connect to Minecraft services. Make sure you are connected with internet! If you believe this is a bug please report it!")
                MCServersDownloadingService = False

    while(data.YouTubeMenu):
        if(YTServiceStartedNow == True):
            print("")
            YTServiceStartedNow = False
            print("----------------------------------------------------------------------------------------------------------")
            print("|"+"YouTube Services Menu".center(104," ")+"|")
            print("|"+"".center(104," ")+"|")
            print("|"+"REMEMBER: Downloading copyrighted YouTube videos is ILLEGAL! I'm NOT responsible for your downloads.".center(104," ")+"|")
            print("|"+"You must know how, why and where to use copyrighted items.".center(104," ")+"|")
            print("----------------------------------------------------------------------------------------------------------")
            numbers = [1, 0]
            Services = ["Download a YouTube video", "Back to Main Menu"]
            for number,service in zip(numbers, Services):
                print(f"[{number}] {service}")
            print("")
        PickedOption = input("Pick an option: ")
        if(PickedOption.replace(" ", "") == "0"):
            data.Menu = True
            data.YouTubeMenu = False
        elif(PickedOption.replace(" ", "") == "1"):
            data.YouTubeVideoDownloadService = True
            data.YouTubeMenu = False
            YTDOWNLOADSERVICESTARTEDNOW = True
        else:
            print(messages.WRONG_OR_NOT_OPTION.replace("[option]", PickedOption))
            print("")
    
    while(data.YouTubeVideoDownloadService):
        if(YTDOWNLOADSERVICESTARTEDNOW == True):
            print("")
            print("----------------------------------------------------------------------------------------------------------")
            print("|"+"To download a YouTube video, you need to input your video link first, after".center(104," ")+"|")
            print("|"+"choose the resolution you want (if your Internet is data limited please pick the lowest quality)".center(104," ")+"|")
            print("|"+"then wait until your video be successfully downloaded.".center(104," ")+"|")
            print("|"+"".center(104," ")+"|")
            print("|"+"Type \"CANCEL\" to back to YouTube services Menu.".center(104," ")+"|")
            print("----------------------------------------------------------------------------------------------------------")
            print("")
            YTDOWNLOADSERVICESTARTEDNOW = False
        VideoLink = input("Paste your video link or search for it:\n")
        if(VideoLink.lower().replace(" ", "") == "cancel"):
            data.YouTubeVideoDownloadService = False
            data.YouTubeMenu = True
            ContinueYTDownloadingService = False
            YTServiceStartedNow = True
        else:
            YouTube_services.GetInfoAboutVideo(VideoLink)
            ContinueYTDownloadingService = True
        
        if(ContinueYTDownloadingService == True):
            print("Available resolutions:\nLowest: 144p (.3gp)\nLow: 360p\nNormal: 720p (HD)\nHigh: 1080p (Full HD)\nVery high: 2160p (4K) (NO AUDIO)")
            VideoQuality = input("Type resolution of video that you want: ")
            if VideoQuality.lower() in ["cancel", "exit", "leave"]:
                print("Do you want to leave this downloading operation or back to menu?")
            else:
                if VideoQuality.lower() in ["lowest", "144", "144p"]:
                    VideoQuality = 17
                elif VideoQuality.lower() in ["low", "360", "360p"]:
                    VideoQuality = 18
                elif VideoQuality.lower() in ["normal", "720", "720p", "hd"]:
                    VideoQuality = 22
                elif VideoQuality.lower() in ["high", "1080", "1080p", "fullhd", "full_hd", "full hd"]:
                    VideoQuality = 137
                elif VideoQuality.lower() in ["veryhigh", "very high", "very_high", "2160", "2160p", "4k"]:
                    VideoQuality = 313
                else:
                    print("Because of incorrect answer or usage, we are going to choose the lowest quality of video (144p) for you.")
                    VideoQuality = 17

                YouTube_services.Download(VideoLink, VideoQuality)

    while(data.SocialMenu):
        if(SOCIALMENUSTARTEDNOW == True):
            print("".center(106, "—"))
            print("|"+"Social Media".center(104, " ")+"|")
            print("|"+"".center(104, " ")+"|")
            print("|"+"Here you can join us or follow our Social Media.".center(104, " ")+"|")
            print("|"+"You are able to join our main and developers server in anytime you want!".center(104, " ")+"|")
            print("".center(106, "—"))
            SOCIALMENUSTARTEDNOW = False

        print("What do you want to join or follow?")
        SocialMedias = ["Discord", "Back"]
        numbers = [1, 0]
        for number,socialmedia in zip(numbers, SocialMedias):
            print(f"[{number}] {socialmedia}")
        print("")
        SelectedSocialMedia = input("Choose a social media you want to follow or join: ")
        if(SelectedSocialMedia.lower().replace(" ", "") in ["1", "discord"]):
            JoinDiscord = True
            while (JoinDiscord):
                print("")
                print("====================================================================")
                print("")
                print("Main Discord server (Official): Coming soon....")
                print("")
                print("Yasserprogamer's server (Founder): https://discord.gg/wJtBMnu")
                print("")
                print("====================================================================")
                print("")
                JoinDiscord = False
        elif(SelectedSocialMedia.lower().replace(" ", "") in ["0", "back", "leave", "mainmenu", "quit", "menu"]):
            data.SocialMenu = False
            data.Menu = True
        else:
            print(messages.WRONG_OR_NOT_OPTION.replace("[option]", SelectedSocialMedia))
            print("")
