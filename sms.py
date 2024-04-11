import requests

url = "https://sms77io.p.rapidapi.com/sms"

payload = "to=%2B97336982337&p=BIZ6bwnv9EOiAvPUDeiJwvGFxD3owYL4NbHQumW4Pb0Bru3x6TMCHNRoSona4Ykg&text=boyafa3 says maraq maraq&from=Boyaf3"

headers = {
	"content-type": "application/x-www-form-urlencoded",
	"X-RapidAPI-Key": "764905dd0cmshc891402bd00dd69p1570b7jsn7abdba66fb03",
	"X-RapidAPI-Host": "sms77io.p.rapidapi.com"
}

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)