from pytube import YouTube

path = ""
url = input("enter youtube video's url:")
#pytube.YouTube(url).streams.get_highest_resolution().download(path)

yt = YouTube(url)
print(yt.title)
print(yt.length)
print(yt.views)
print(yt.publish_date)