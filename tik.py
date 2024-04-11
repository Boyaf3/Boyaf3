import requests


def download(url1):
 url = "https://tiktok-video-no-watermark2.p.rapidapi.com/"

 querystring = {"url":url1,"hd":"0"}

 headers = {
	"X-RapidAPI-Key": "5d3341363bmsh632a8a894ade58fp174180jsncaece800ebeb",
	"X-RapidAPI-Host": "tiktok-video-no-watermark2.p.rapidapi.com"
 }

 response = requests.request("GET", url, headers=headers, params=querystring)
 name=response.json()
 print(name)
 link=name["data"]
 name=link['wmplay']

        

 print(name)
 return name




