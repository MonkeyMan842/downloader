import subprocess
import os

def moviesystem(needsAudio, indexURL, audioIndexURL, movieName, deleteVerify, Path):
    base = f"{Path}/{movieName}"
    if needsAudio == True:
        movieCommand = f'yt-dlp -P "{Path}" --remux-video mkv "{indexURL}" -o "{movieName} - visual.%(ext)s"'
        audioCommand = f'yt-dlp -P "{Path}" --remux-video mkv "{audioIndexURL}" -o "{movieName} - audio.%(ext)s"'
        combineCommand = f'mkvmerge -o "{base}.mkv" "{base} - visual.mkv" "{base} - audio.mkv"'
    else:
        movieCommand = f'yt-dlp -P "{Path}" --remux-video mkv "{indexURL}" -o "{movieName}.%(ext)s"'

    subprocess.run(movieCommand, shell=True)
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