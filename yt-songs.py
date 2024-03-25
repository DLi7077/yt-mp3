# importing packages
import eyed3
from eyed3.id3.frames import ImageFrame
from moviepy.editor import *
from pytube import YouTube
import os
import requests
from pathlib import Path


def saveImgFromUrl(thumbnailPath, url):
    img_data = requests.get(url)._content
    with open(thumbnailPath, 'wb') as handler:
        handler.write(img_data)


def MP4ToMP3(mp4Path, mp3Path):
    FILETOCONVERT = AudioFileClip(mp4Path)
    FILETOCONVERT.write_audiofile(mp3Path)
    FILETOCONVERT.close()
    os.remove(mp4Path)


def setThumbnail(mp3File, imgUrl):
    title = Path(mp3File).stem

    # save image first
    thumbnailPath = f'./THUMBNAIL-{title}.jpg' # will be deleted after use
    saveImgFromUrl(thumbnailPath, imgUrl)

    audiofile = eyed3.load(mp3File)
    if (audiofile.tag == None):
        audiofile.initTag()

    audiofile.tag.images.set(
        ImageFrame.MEDIA, open(thumbnailPath, 'rb').read(), 'image/jpeg'
    )

    audiofile.tag.save(version=eyed3.id3.ID3_V2_3)

    os.remove(thumbnailPath)


def downloadYtMp3(url, destination="."):
    yt = YouTube(url)
    # extract only audio
    video = yt.streams.filter(only_audio=True).first()
    thumbnailUrl = yt.thumbnail_url

    # download the file
    mp4File = video.download(output_path=destination)

    base, ext = os.path.splitext(mp4File)
    mp3File = base + '.mp3'
    # save the file
    MP4ToMP3(mp4File, mp3File)

    # set thumbnail
    setThumbnail(mp3File, thumbnailUrl)

    # result of success
    print(yt.title + " has been successfully downloaded.")


urls = [
    'https://www.youtube.com/watch?v=zDHSrV5Q89k'
]
location = "./songs"

for url in urls:
    downloadYtMp3(url, location)
