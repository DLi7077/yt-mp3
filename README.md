```
Context: I want to download youtube mp3s
Old solution - Replace youtube with youmagictube
replace: https://www.youtube.com/watch?v={videoId}
with:    https://www.youmagictube.com/watch?v={videoId}
This redirects you to another website that lets you download the video either as 360p or mp3.
I just want the mp3 and the process is tedious
```
This script lets you download videos as mp3s from youtube
Includes thumbnail as album cover

1. Install python3 https://www.python.org/downloads/
2. Clone this repo, open in terminal, and install the required libraries
`pip3 install eyed3 moviepy pytube`
3. Modify line 65: `urls = [...]` with the video urls you want to download
4. Modify line 68: `location = "./songs"` with where you want the mp3s to be downloaded to
5. Run the scripts to download your mp3s `python -u "./yt-songs.py"`
