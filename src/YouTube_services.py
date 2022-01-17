import pytube
import os
from pytube.cli import on_progress

CWD = os.getcwd()

def GetInfoAboutVideo(url):
    Video = pytube.YouTube(url=url)
    print("")
    print("---------------------------------------------")
    print("Information about video:")
    print("")
    print(f"Title: {Video.title}")
    print(f"Views: {Video.views}")
    print("")
    print(f"Published by: {Video.author}")
    print(f"Published at: {Video.publish_date}")
    print("")
    print(f"Description:\n{Video.description}")
    print("---------------------------------------------")
    print("")


def Download(url, quality):
    Video = pytube.YouTube(url, on_progress_callback=on_progress)
    res = Video.streams.filter(progressive=True).get_by_itag(quality)
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
            print("")
            res.download(f"./YouTube/{Video.title}/")
            print("Downloading: |")
            print("")
            print("Successfully downloaded video.")
            print(f"Your video is saved on {CWD}\\YouTube\\{Video.title}\\{res.default_filename}")
            print("")
    except:
        print("Could not download video. Try another resolution! ")
