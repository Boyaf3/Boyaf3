
import requests
import json

def result(url):
 api = "https://tiktok-video-no-watermark2.p.rapidapi.com/"
 url=url
 querystring = {"url":url}

 headers = {
	 "X-RapidAPI-Key": "764905dd0cmshc891402bd00dd69p1570b7jsn7abdba66fb03",
	"X-RapidAPI-Host": "tiktok-video-no-watermark2.p.rapidapi.com"
 }

 response1 = requests.request("GET", api, headers=headers, params=querystring)
 respone=response1.text
 
 #if "[{" in respone:
 end_result= json.loads(respone)

 end_result= end_result["data"]
 end_result= end_result["play"]
 #end_result= str(end_result)
 #else: 
 #result=str(respone["video"])
 #video=end_result.replace('[',"")
 #end_result=video.replace(']',"")
 #end_result=end_result.replace("'","")

 print(end_result)

 return str(end_result)

#result(url="https://www.tiktok.com/@adole974444/video/7146281753009720577")
 