from pytube import YouTube
from sys import argv


def yt_download(link):
    # creating YouTube object from link
    yt = YouTube(link)
    # printing Title and Views for video as a checkpoint
    print("Title: ", yt.title)
    print("Views: ", yt.views)

    video = yt.streams.get_highest_resolution()

    # provide target directory location where YT video will be downloaded
    video.download('/Users/jenonefater/Downloads')


if __name__ == "__main__":
    if len(argv) != 2:
        raise Exception("You must pass in one YouTube link")
    else:
        link = argv[1]
        yt_download(link)
