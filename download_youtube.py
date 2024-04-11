
from pytube import YouTube
import string
import random
import os
import math

def youtube(url):
  url=url
  letters = string.ascii_lowercase
  letter = string.digits
  filename=''.join(random.choice(letters+letter) for i in range(5)) 


  if url.endswith("mp3"):
    url=url.replace("mp3","")
    link=YouTube(url)
    mp3=link.streams.filter(only_audio=True).first()
    out_file= mp3.download(output_path=os.getcwd())
    base, ext = os.path.splitext(out_file)
    new_file = filename + '.mp3'
    os.rename(out_file, new_file)
    filename=new_file
  else:
   link=YouTube(url)
   a=link.streams.get_highest_resolution().download(filename=filename+'.mp4',output_path=os.getcwd())
   e=os.path.abspath(filename+'.mp4')
   print(e)
   
   size=os.stat(str(os.getcwd())+"/"+filename+'.mp4')
   a=int(size.st_size / (1024 * 1024))
   if a > 16:
    os.remove(str(os.getcwd())+"/"+filename+'.mp4')
    a=link.streams.filter(res="360p").first().download(filename=filename+'.mp4',output_path=os.getcwd())
    e=os.path.abspath(filename+'.mp4')
  filename=filename+'.mp4'
   #get_by_resolution('720p')
   
  
  return filename

#youtube('https://youtu.be/P2-qYfzCgmU')