#Codes are orignally made by: yasserprogamer.

import requests
import urllib.request

class Paper:
    VERSION_MANIFEST_URL = "https://papermc.io/api/v2/projects/paper/"
    VERSION_INFO_URL = "https://papermc.io/api/v2/projects/paper/versions/{0}/"
    BUILD_INFO_URL = "https://papermc.io/api/v2/projects/paper/versions/{0}/builds/{1}/"

    def GetVersionsList() -> (list | ConnectionError):
        try:
            PAPERMC_MAIN_API_JSON = requests.get(url=Paper.VERSION_MANIFEST_URL).json()
        except requests.exceptions.ConnectionError:
            raise ConnectionError("No Internet connection.")
        return PAPERMC_MAIN_API_JSON["versions"]

    def GetLatestMinecraftVersion() -> (str | ConnectionError):
        try:
            PaperMCAvailableVersions = Paper.GetVersionsList()
        except requests.exceptions.ConnectionError:
            raise ConnectionError("No Internet connection.")
        VersionsAmount = len(PaperMCAvailableVersions)
        return PaperMCAvailableVersions[VersionsAmount-1]

    def GetBuildsList(version: str) -> (list | ConnectionError):
        if version.replace(" ", "") == "":
            raise TypeError("Argument 'version' is empty! Required to fill it out.") 
        try:
            PAPERMC_VERSION_INFO_JSON = requests.get(url=Paper.VERSION_INFO_URL.format(version)).json()
        except requests.exceptions.ConnectionError:
            raise ConnectionError("No Internet connection.")
        return PAPERMC_VERSION_INFO_JSON["builds"]

    def GetLatestMCBuild(version: str) -> (int | ConnectionError):
        try:
            BUILDS_LIST = Paper.GetBuildsList(version=version)
        except requests.exceptions.ConnectionError:
            raise ConnectionError("No Internet connection.")
        BuildsAmount = len(BUILDS_LIST)
        return BUILDS_LIST[BuildsAmount-1]

    def GetFilename(version: str, build: int | str) -> (str | ConnectionError):
        try:
            BUILD_INFO_JSON = requests.get(Paper.BUILD_INFO_URL.format(version, build)).json()
        except requests.exceptions.ConnectionError:
            raise ConnectionError("No Internet connection.")
        JarFilename = BUILD_INFO_JSON["downloads"]["application"]["name"]
        return JarFilename

    def GetDownloadSize(version: str, build: int | str) -> str:
        try:
            JarFilename = Paper.GetFilename(version, build)
            DOWNLOAD_LINK = requests.get(f"https://papermc.io/api/v2/projects/paper/versions/{version}/builds/{str(build)}/downloads/{JarFilename}", stream=True)
        except requests.exceptions.ConnectionError:
            raise ConnectionError("No Internet connection.")
        DownloadSizeInBytes = int(DOWNLOAD_LINK.headers.get("Content-length"))
        DownloadSizeInMB = round((DownloadSizeInBytes/1024)/1024)
        return f"{DownloadSizeInMB} MB"

    def DownloadVersion(version: str, build: int | str, path:str = "./") -> str:
        try:
            JarFilename = Paper.GetFilename(version, build)
            SERVER_DOWNLOAD_LINK = f"https://papermc.io/api/v2/projects/paper/versions/{version}/builds/{str(build)}/downloads/{JarFilename}"
        except requests.exceptions.ConnectionError:
            raise ConnectionError("No Internet connection.")
        if(not path.endswith("/")):
            path = f"{path}/"
        urllib.request.urlretrieve(SERVER_DOWNLOAD_LINK, f"{path}{JarFilename}")
        return JarFilename
