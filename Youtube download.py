from pytube import YouTube
yt=input('Enter Link: ')
YouTube(yt).streams.first().download()