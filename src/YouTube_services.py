import pytube
import requests
import urllib.request
import os
import colors
import utils

CWD = os.getcwd()

def GetInfoAboutVideo(url):
    if url == None:
        return False
    elif url.replace(" ", "") == "":
        return "Error: Invalid YouTube video link."
    Video = pytube.YouTube(url=url)
    VideoTitle = Video.title
    print("")
    print(colors.Color.Gold+f" {VideoTitle} ".center(104, "─").replace(f"{VideoTitle}", f"{colors.Color.Cyan}{VideoTitle}{colors.Color.Gold}")+colors.Color.reset)
    print(f"{colors.Color.White}Information about video:")
    print("")
    print(f"{colors.Color.Blue}Title: {colors.Color.White}{VideoTitle}")
    print(f"{colors.Color.Blue}Views: {colors.Color.White}{Video.views}")
    print("")
    print(f"{colors.Color.Blue}Published by: {colors.Color.White}{Video.author}")
    print(f"{colors.Color.Blue}Published at: {colors.Color.White}{Video.publish_date}")
    print("")
    print(f"{colors.Color.Blue}Description:\n{colors.Color.White}{Video.description}")
    print(colors.Color.Gold+"".center(104, "─")+colors.Color.reset)
    print("")


def DownloadVideo(url, quality):
    Video = pytube.YouTube(url)
    res = Video.streams.get_by_itag(quality)
    try:
        FileSize = (res.filesize/1024)/1024
        print(f"Download size: {FileSize} MB")
        askcontinue = input("Do you want to continue? ")
        if askcontinue.lower() in ["yes", "y", "ye", "t", "true"]:
            continuedownloading = True
        elif askcontinue.lower() in ["no", "n", "f", "false"]:
            continuedownloading = False
        if(continuedownloading == True):
            print("")
            print(f"Video title: {Video.title}\nVideo filename: {res.default_filename}")
            print("")
            print("Downloading YouTube video....")
            print("Downloading YouTube video.... 0%")
            res.download(f"./YouTube/videos/{Video.title}/")
            print("Downloading YouTube video.... 100%")
            print("")
            print("Successfully downloaded video.")
            print(f"Your video is saved on {CWD}\\YouTube\\videos\\{Video.title}\\{res.default_filename}")
            print("")
    except:
        print("Could not download video. Try another resolution! ")

def DownloadThumbnail(url):
    Video = pytube.YouTube(url)
    VideoID = Video.video_id
    VideoTitle = Video.title
    ThumbnailLink = f"https://img.youtube.com/vi/{VideoID}/maxresdefault.jpg"
    try:
        RequestedImage = requests.get(url=ThumbnailLink, stream=True)
        if(RequestedImage.status_code == 200):
            DownloadSizeInBytes = int(RequestedImage.headers.get("Content-length"))
            DownloadSizeInMB = (DownloadSizeInBytes/1024)/1024
            print("")
            print(f"{colors.Color.PURPLE}• Download size: {colors.Color.Yellow}{DownloadSizeInMB} MB{colors.Color.reset}")
            print("")
            ContinueDownloading = input(f"{colors.Color.White}Do you want to continue download this thumbnail? (Y/N){colors.Color.reset}\n")
            print("")
            if not os.path.exists(f"./YouTube/thumbnails/{Video.title}/"):
                os.makedirs(f"./YouTube/thumbnails/{Video.title}/")
            i = 0
            DownloadingOperationStartedNow = True
            utils.printProgressBar(i, DownloadSizeInBytes, "Downloading:", "Complete", length=50, fill=f"{colors.Color.Lime}█{colors.Color.reset}")
            with open(f'./YouTube/thumbnails/{Video.title}/{VideoTitle}.jpg', 'wb') as file:
                for filedata in RequestedImage.iter_content(1024):
                    utils.printProgressBar(i + len(filedata), DownloadSizeInBytes, "Downloading:", "Complete", length=50, fill=f"{colors.Color.Lime}█{colors.Color.reset}")
                    if(DownloadingOperationStartedNow == False):
                        i = i + len(filedata)
                    elif(DownloadingOperationStartedNow == True):
                        i = len(filedata)
                        DownloadingOperationStartedNow = False
                    file.write(filedata)
            print("")
            print(f"{colors.Color.Lime}Successfully downloaded thumbnail.{colors.Color.reset}")
            print(f"{colors.Color.Cyan}Your video is saved on:{colors.Color.reset} {colors.Color.White}{colors.Color.Underline}{CWD}\\YouTube\\thumbnails\\{Video.title}\\{Video.title}.jpg{colors.Color.Nounderline}{colors.Color.reset}")
            print("")
            RequestedImage.close()
        elif(RequestedImage.status_code == 404):
            print(f"{colors.Color.Red}Error: Could not find thumbnail file. Status code: 404.{colors.Color.reset}")
    except:
        print(f"{colors.Color.Red}Failed to connect to YouTube services. Make sure you are connected with internet or website and APIs are down.{colors.Color.reset}")
        print("")