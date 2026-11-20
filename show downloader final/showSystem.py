import subprocess
import os

def showsystem(needsAudio, indexURL, audioIndexURL, ShowName, SeasonNum, EpisodeNum, EpisodeName, deleteVerify, Path):
    base = f"{Path}/{ShowName} - S{SeasonNum}E{EpisodeNum} - {EpisodeName}"
    if needsAudio == True:
        ShowCommand = f'yt-dlp -P "{Path}" --remux-video mkv "{indexURL}" -o "{ShowName} - S{SeasonNum}E{EpisodeNum} - {EpisodeName} - visual.%(ext)s"'
        audioCommand = f'yt-dlp -P "{Path}" --remux-video mkv "{audioIndexURL}" -o "{ShowName} - S{SeasonNum}E{EpisodeNum} - {EpisodeName} - audio.%(ext)s"'
        combineCommand = f'mkvmerge -o "{base}.mkv" "{base} - visual.mkv" "{base} - audio.mkv"'
    else:
        ShowCommand = f'yt-dlp -P "{Path}" --remux-video mkv "{indexURL}" -o "{ShowName} - S{SeasonNum}E{EpisodeNum} - {EpisodeName}.%(ext)s"'

    subprocess.run(ShowCommand, shell=True)
    print("")

    if needsAudio == True:
        subprocess.run(audioCommand, shell=True)
        print("")
        subprocess.run(combineCommand, shell=True)
        print("")
        if deleteVerify == True:
            os.remove(f"{base} - visual.mkv")
            os.remove(f"{base} - audio.mkv")

    if os.path.exists(f"{base}.mkv"):
        print("Download Complete!!!!")
    else:
        print("Something went wrong :(")