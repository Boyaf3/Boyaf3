 
 
 
 

#import requests

#def url(url,respone):
    ##    changing_url = url.split("/")
      ##  url_code = changing_url[4]
       ## url = f"https://instagram.com/p/{url_code}?__a=1"
       ## try:
       ##     global checking_video
       ##     visit = requests.get(url).json()
      ##      checking_video = visit['graphql']['shortcode_media']['is_video']
      ##  except:
     ##       print('a')
        
     ##   if checking_video==True:
    ##        try:
      ##          video_url = visit['graphql']['shortcode_media']['video_url']
     ##           print(video_url)
      ##          return video_url
     ##       except:
       ##         pass

      ####  elif checking_video==False:
       ##     try:
       ####         post_url = visit['graphql']['shortcode_media']['display_url']
         ####       print(post_url)
        ##        return post_url
       ##     except:
       ##         pass
       ## else:
       ##     return response.body()
    
##url(url='https://www.instagram.com/p/Cgw2wC8LqUJ/',respone=None)