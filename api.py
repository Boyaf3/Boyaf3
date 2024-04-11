

from urllib import response
import requests
def texttocode(input):
  print(input)
  a={'source':'webapp',
      "textInput": input,
        "userId":""}
  b=requests.post(url="https://www.useblackbox.io/autocomplete",data=a)
  print(b.text)
  b=b.json()
  response=b["response"]
  if 'python' in input:
   response=str(response)+"#boyaf3 build it for free"
  if 'javascript' in input:
   response=str(response)+"//boyaf3 build it for free"
  if 'java' in input:
   response=str(response)+"//boyaf3 build it for free "
  if 'c++' in input:
   response=str(response)+"//boyaf3 build it for free"
  if "html" in input:
    response=str(response)+"<!--boyaf3 build it for free-->"
  else: 
    response=str(response) + "'''boyaf3 build it for free'''"
  return response
 