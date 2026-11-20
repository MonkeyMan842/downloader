import movieSystem
import showSystem

def start(isShow, needsAudio, indexURL, audioIndexURL, showName, SeasonNum, EpisodeNum, EpisodeName, deleteVerify, needsPath, Path):
    danthemanPath = "/media/jellyfin_media/unsorted downloads"
    if needsPath == True:
        filePath = danthemanPath
    else:
        filePath = Path

    if isShow == True:
        showSystem.showsystem(needsAudio, indexURL, audioIndexURL, showName, SeasonNum, EpisodeNum, EpisodeName, deleteVerify, filePath)
    elif isShow == False:
        movieSystem.moviesystem(needsAudio, indexURL, audioIndexURL, EpisodeName, deleteVerify, filePath)