from unittest import result
import requests
def insta(link):
 url = "https://instagram-downloader-download-instagram-videos-stories.p.rapidapi.com/index"

 querystring = {"url":link}

 headers = {
	"X-RapidAPI-Key": "5d3341363bmsh632a8a894ade58fp174180jsncaece800ebeb",
	"X-RapidAPI-Host": "instagram-downloader-download-instagram-videos-stories.p.rapidapi.com"
 }

 response = requests.request("GET", url, headers=headers, params=querystring)
 respone=response.json()
 result=respone["media"]
 print(result)
 return str(result)

