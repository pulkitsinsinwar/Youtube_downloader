from pytube import YouTube
from pytube import Playlist
import ffmpeg
import subprocess
import os
import time
import re



def playlist_download():
    for video in pl.videos:
        video.streams.get_highest_resolution().download(path_to_save)


def audio_download():
    audio_stream = yt.streams.filter(only_audio=True)
    print(audio_stream)
    audio_stream[0].download(output_path=path_to_save, filename="1_audio")
    input_audio = path_to_save + "/" + "1_audio" + "." + "mp4"
    output_audio = path_to_save + "/" + "1_complete" + "." + "mp3"
    print(output_audio)
    audio_map = "a"
    subprocess.run(f"ffmpeg -i {input_audio} -g:a {0} -map {audio_map} {output_audio}")
    os.rename(output_audio,path_to_save+"/"+link_title + ".mp3")
    os.remove(input_audio)


def video_download():
    try:
        yt.streams.filter(res=link_resolution, mime_type=link_mime_type)[0].download(output_path=path_to_save,filename="1_video")
        print("video file downloaded")
        yt.streams.filter(mime_type=link_amime_type)[0].download(output_path=path_to_save, filename="1_audio")
        print("audio file downloaded")

        videofile = path_to_save + "/" + "1_video" + "." + format
        audiofile = path_to_save + "/" + "1_audio" + "." + format
        outputfile = path_to_save + "/" + "_complete" + "." + format

        map_v = "0:v"
        map_a = "1:a"
        codec = "copy"
        subprocess.run(f"ffmpeg -i {videofile} -i {audiofile} -c {codec} -map {map_v} -map {map_a} {outputfile}")
        print("running try clause")
    except IndexError:
        print(
            "Error: Either the requested video resolution or video format  is not available in link.Trying "
            "alternative !!")
    finally:
        print("finally clause")
        yt.streams.get_highest_resolution().download(path_to_save)  # downloading the 720p res with audio


link = input("please enter the youtube link :")
link_resolution = input("please enter the resolution :")
format = input("please enter the video format :")
user_input = input("do you want to download video or audio")
path_to_save = "C:/Users/amd/Downloads/ytd"

link_mime_type = "video/" + format
link_amime_type = "audio/" + format
print(link_mime_type)
print(link_amime_type)

yt = YouTube(link)
print(yt)
link_title = yt.title
#bad_chars = [';', ':', '!', "*","|","@""_","!","#","$","%","^","&","*","()","<",">","?","/","}","{","~","-"]

for i in bad_chars:
    link_title = link_title.replace(i, '')
print(link_title)

link_stream_all = yt.streams

for i in link_stream_all:
    print(i)



if user_input == "video":
    video_download()
elif user_input == "audio":
    audio_download()
else:
    pl = Playlist(link)
    playlist_download()
