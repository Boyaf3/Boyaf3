import replicate
import os
def text2image(text):
 text=text
 os.environ["REPLICATE_API_TOKEN"]="05e9f97fefc2df6f4592b7f6db759f7b4d66756c"
 a=os.environ.get("REPLICATE_API_TOKEN")
 print(a)
 list =[]
 model = replicate.models.get("pixray/text2image")
 for image in model.predict(prompts=text):
   print(image)
   list.append(image)

 return str(list[-1])



