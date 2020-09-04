from pytube import YouTube
link = input("Enter YouTube video link: ")
yt = YouTube(link)
ys = yt.streams.get_highest_resolution()
print("Downloading...")
ys.download('Downloads')
print("Download completed!!")
print("Your file is located in your 'downloads' folder")
readline()