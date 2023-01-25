from pytube import YouTube
import ssl
ssl._create_default_https_context = ssl._create_stdlib_context

file = open('urls.txt', 'r')

def Download(link):
  youtubeObject = YouTube(link)
  youtubeObject = youtubeObject.streams.get_audio_only()
  try:
    print(youtubeObject.title)
    youtubeObject.download()
  except:
    print("Your video did not download - boo")
  print("The download finished")

for link in file:
  Download(link)
 
file.close()